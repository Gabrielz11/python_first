"""
70_repository_pattern.py - Repository Pattern e Desacoplamento da Camada de Persistência

Objetivos:
1. Dominar a implementação do Repository Pattern em arquiteturas corporativas de backend (DDD / Clean Architecture).
2. Abstrair completamente o mecanismo de acesso a dados (SQL, NoSQL, ORM, API externa) da lógica de domínio.
3. Definir a interface abstrata `AbstractRepository` utilizando o módulo `abc`.
4. Implementar repositórios concretos para produção (`SQLRepository`) e para testes unitários (`InMemoryRepository`).
5. Impedir o vazamento de vazamentos de abstração (Abstraction Leak) de ORMs para a camada de serviço.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o Repository Pattern?
O Repository Pattern é um padrão de arquitetura de software (popularizado por Eric Evans no Domain-Driven Design - DDD)
que funciona como uma coleção em memória contendo as Entidades do Domínio.

Vantagens Principais:
1. Desacoplamento do Banco de Dados: A camada de regras de negócio (Serviços/Domínio) NUNCA executa comandos SQL diretamente e nem conhece detalhes do ORM (SQLAlchemy, Django ORM).
2. Testabilidade Extrema: Permite substituir o banco de dados de produção por um `InMemoryRepository` de altíssima velocidade em testes unitários.
3. Troca de Persistência Simplificada: Migrar de PostgreSQL para MongoDB ou DynamoDB exige apenas criar uma nova classe de Repositório sem alterar nenhuma linha da lógica de negócio!
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ENTIDADE E REPOSITÓRIO ABSTRATO
# ==========================================================
@dataclass
class ClienteEntity:
    """Entidade de Domínio Pura (desacoplada de ORM)."""

    id: int | None
    nome: str
    email: str


class AbstractClienteRepository(ABC):
    """Interface Abstrata do Repositório de Clientes."""

    @abstractmethod
    def add(self, cliente: ClienteEntity) -> None:
        pass

    @abstractmethod
    def get_by_id(self, cliente_id: int) -> ClienteEntity | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> ClienteEntity | None:
        pass


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: REPOSITÓRIO EM MEMÓRIA (TESTES)
# ==========================================================
class InMemoryClienteRepository(AbstractClienteRepository):
    """Implementação concreta de Repositório em Memória para Testes Unitários."""

    def __init__(self) -> None:
        self._clientes: dict[int, ClienteEntity] = {}
        self._next_id = 1

    def add(self, cliente: ClienteEntity) -> None:
        if cliente.id is None:
            cliente.id = self._next_id
            self._next_id += 1
        self._clientes[cliente.id] = cliente

    def get_by_id(self, cliente_id: int) -> ClienteEntity | None:
        return self._clientes.get(cliente_id)

    def get_by_email(self, email: str) -> ClienteEntity | None:
        for c in self._clientes.values():
            if c.email == email:
                return c
        return None


def demonstrar_in_memory_repository() -> None:
    print("\n--- 1. FUNDAMENTOS: InMemoryClienteRepository ---")

    repo = InMemoryClienteRepository()

    c1 = ClienteEntity(id=None, nome="Gabriel", email="gabriel@empresa.com")
    repo.add(c1)

    recuperado = repo.get_by_id(1)
    print(f"Cliente Adicionado e Recuperado pelo ID 1: {recuperado}")

    por_email = repo.get_by_email("gabriel@empresa.com")
    print(f"Cliente Recuperado por Email: {por_email}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ClienteService:
    """Camada de Serviço de Aplicação (Use Case) que consome o Repository desacoplado."""

    def __init__(self, repo: AbstractClienteRepository) -> None:
        self.repo = repo

    def cadastrar_novo_cliente(self, nome: str, email: str) -> ClienteEntity:
        # Validação de regra de negócio
        if self.repo.get_by_email(email):
            raise ValueError(f"Email '{email}' já cadastrado na base.")

        novo_cliente = ClienteEntity(id=None, nome=nome, email=email)
        self.repo.add(novo_cliente)
        return novo_cliente


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 2. APLICAÇÃO BACKEND: ClienteService e Repository ---")

    # Injeta a implementação em memória (poderia ser SQLRepository sem alterar o ClienteService!)
    repo = InMemoryClienteRepository()
    servico = ClienteService(repo)

    c = servico.cadastrar_novo_cliente("Ana Silva", "ana@empresa.com")
    print(f"  [Service] Cliente cadastrado com sucesso: ID {c.id}")

    try:
        servico.cadastrar_novo_cliente("Ana Repetida", "ana@empresa.com")
    except ValueError as e:
        print(f"  [Service Erro Negócio]: {e}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ISOLAMENTO DO DOMÍNIO
# ==========================================================
"""
Como o Repository Pattern previne o Leaking de Abstração:
1. O Repositório converte modelos específicos do ORM (como `SQLAlchemyModel`) em Entidades Puras do Domínio (`ClienteEntity`).
2. A camada de negócio lida EXCLUSIVAMENTE com Entidades Puras do Python (dataclasses/POPOs), imunes a mudanças na biblioteca de banco de dados.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Inserção/Busca em Repositório em Memória: Tempo O(1) com Dicionário.
- Inserção/Busca em Repositório SQL: Tempo O(log N) com Índices B-Tree de banco de dados.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 3. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Misturar queries SQL/ORM direto nas regras de negócio da API
    print("[X] Nao-Pythonic (Query SQL direto no Controller):")
    print("  def endpoint(): db.execute('SELECT * FROM users...')  # Totalmente acoplado!")

    # [OK] PYTHONIC: Isolar o acesso a dados no Repository Pattern
    print("\n[OK] Pythonic:")
    print("  def endpoint(repo: AbstractRepository): user = repo.get_by_id(1)  # Limpo e testável!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Retorne sempre Entidades Puras de Domínio (ou DTOs) dos seus métodos de repositório, nunca objetos ORM acoplados.
2. Defina os métodos de consulta pelo propósito do negócio (ex: `get_by_email()`), e não pela instrução técnica SQL.
3. Implemente sempre um `InMemoryRepository` correspondente para acelerar a execução de suítes de testes unitários.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Fazer o Repositório retornar objetos ORM do SQLAlchemy diretamente para o Controller
    print("[!] Armadilha 1: Retornar modelos de ORM vazados do Repositório quebra o desacoplamento da camada de serviço!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre o Repository Pattern e o Active Record Pattern (usado pelo Django ORM)?"
A: "1. Active Record (ex: Django ORM `user.save()`): A própria classe do modelo contém os dados E a lógica de persistência SQL acoplados no mesmo objeto. É mais rápido de desenvolver em projetos simples, mas dificulta a separação de arquitetura limpa.
    2. Repository Pattern (DDD): Separa completamente a classe de dados/negócio (`ClienteEntity`) da classe responsável pela persistência (`ClienteRepository`). Proporciona altíssima testabilidade e desacoplamento em aplicações empresariais."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma entidade `ProdutoEntity(id, nome, preco)` e uma interface abstrata `AbstractProdutoRepository`.
# Exercício 2: Implemente a classe `InMemoryProdutoRepository` com métodos para adicionar, buscar e listar produtos com preço > 100.
# Exercício 3: Escreva um teste unitário para um `ProdutoService` consumindo o repositório em memória.


def main() -> None:
    print("==========================================================")
    print("  AULA 70: REPOSITORY PATTERN E DESACOPLAMENTO DE DADOS")
    print("==========================================================")
    demonstrar_in_memory_repository()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 70 executado com sucesso.")


if __name__ == "__main__":
    main()
