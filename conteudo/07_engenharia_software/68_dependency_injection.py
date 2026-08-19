"""
68_dependency_injection.py - Injeção de Dependência (DI) e Inversão de Controle (IoC)

Objetivos:
1. Compreender o padrão de Injeção de Dependência (Dependency Injection - DI) e Inversão de Controle (IoC).
2. Eliminar o acoplamento rígido causado pela instanciação de dependências diretas dentro do `__init__`.
3. Dominar as modalidades de injeção: Injeção por Construtor (Constructor Injection) e por Propriedade/Setter.
4. Construir um Container de Injeção de Dependência (DI Container) simples para microsserviços.
5. Facilitar a substituição de dependências reais por Mocks durante a execução de testes unitários.
"""

from abc import ABC, abstractmethod
from typing import Any, Type


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Injeção de Dependência (DI)?
Injeção de Dependência é uma técnica de design onde um objeto recebe suas dependências de uma fonte externa
em vez de criá-las internamente utilizando `new` / `ClasseConcreta()`.

Problema do Acoplamento Rígido:
Se a classe `ServicoPedido` instanciar diretamente `self.banco = PostgresDatabase()` no seu construtor:
1. Impossível de Testar: Você não consegue testar `ServicoPedido` em isolamento sem conectar ao Postgres real.
2. Impossível de Alterar: Se quiser mudar para MySQL ou MongoDB, terá que alterar o código interno de `ServicoPedido`.

Solução com Injeção de Dependência:
`ServicoPedido` declara que precisa de um objeto que satisfaça a abstração `DatabaseInterface`
e recebe a instância pronta através do seu parâmetro `__init__(self, db: DatabaseInterface)`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: INJEÇÃO VIA CONSTRUTOR
# ==========================================================
class MessageSenderInterface(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass


class EmailSenderImpl(MessageSenderInterface):
    def send(self, recipient: str, message: str) -> bool:
        print(f"  [EmailSender] Enviado para {recipient}: {message}")
        return True


class MockSenderImpl(MessageSenderInterface):
    def send(self, recipient: str, message: str) -> bool:
        print(f"  [MockSender] Registrado para teste: {recipient}")
        return True


class UserRegistrationService:
    """Classe que recebe suas dependências por Injeção de Construtor."""

    def __init__(self, sender: MessageSenderInterface) -> None:
        # Dependência Injetada!
        self.sender = sender

    def register_user(self, email: str) -> None:
        print(f"  [UserRegistrationService] Usuário {email} cadastrado.")
        self.sender.send(email, "Bem-vindo à nossa plataforma!")


def demonstrar_fundamentos_di() -> None:
    print("\n--- 1. FUNDAMENTOS: Injeção por Construtor ---")

    # Injetando serviço real de Email
    servico_prod = UserRegistrationService(sender=EmailSenderImpl())
    servico_prod.register_user("cliente@empresa.com")

    # Injetando Mock para testes (Zero alteração na classe UserRegistrationService!)
    servico_teste = UserRegistrationService(sender=MockSenderImpl())
    servico_teste.register_user("teste@empresa.com")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: CONTAINER DE DI SIMPLES
# ==========================================================
class DIContainer:
    """Container de Injeção de Dependência dinâmico para registro e resolução."""

    def __init__(self) -> None:
        self._registry: dict[Type[Any], Any] = {}

    def register(self, interface: Type[Any], implementation: Any) -> None:
        self._registry[interface] = implementation

    def resolve(self, interface: Type[Any]) -> Any:
        if interface not in self._registry:
            raise KeyError(f"Dependência não registrada no container: {interface.__name__}")
        return self._registry[interface]


def demonstrar_container_di() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: DI Container ---")
    container = DIContainer()

    # Registra as implementações no container central
    container.register(MessageSenderInterface, EmailSenderImpl())

    # Resolve e injeta
    sender_instancia = container.resolve(MessageSenderInterface)
    servico = UserRegistrationService(sender=sender_instancia)
    servico.register_user("user_container@empresa.com")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Injeção em Arquitetura Limpa ---")
    # Frameworks modernos como FastAPI executam essa injeção automaticamente via Depends()
    print("  Exemplo FastAPI: def endpoint(service: UserService = Depends()): ...")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: INVERSÃO DE CONTROLE
# ==========================================================
"""
Inversão de Controle (IoC - Inversion of Control):
1. No fluxo tradicional, a sua classe de aplicação tem o controle de criar e instanciar os objetos dos quais depende.
2. Na Inversão de Controle, o controle é INVERTIDO: um framework ou container externo fica responsável por instanciar
   as dependências e passá-las prontas para o seu componente.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Injeção de Dependência via `__init__`: Tempo O(1), Espaço O(1).
- Resolução em DI Container: Busca em dicionário CPython -> Tempo O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Instanciar dependências concretas no __init__
    print("[X] Nao-Pythonic (Acoplamento rígido):")
    print("  class Service: def __init__(self): self.db = PostgresDB()  # Impossível de mockar!")

    # [OK] PYTHONIC: Passar dependências anotadas no __init__
    print("\n[OK] Pythonic:")
    print("  class Service: def __init__(self, db: DatabaseInterface): self.db = db")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize Injeção por Construtor (`__init__`) como método primário de injeção de dependências em Python.
2. Anote os parâmetros do construtor utilizando Abstrações (`ABC` ou `Protocol`), nunca classes concretas.
3. Evite o antipadrão Service Locator (onde o objeto busca dependências em um container global dentro de seus métodos).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Criar parâmetros com instâncias mutáveis padrão no construtor
    # def __init__(self, db=PostgresDB()): ... # [!] PERIGO: Executado uma única vez na definição da classe!
    print("[!] Armadilha 1: NUNCA coloque `db=PostgresDB()` como valor padrão de parâmetro no `__init__`! Use `db: DatabaseInterface | None = None`.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a relação entre Inversão de Controle (IoC), Injeção de Dependência (DI) e o princípio DIP do SOLID?"
A: "1. DIP (Dependency Inversion Principle): É a REGRA ARQUITETURAL do SOLID que estabelece que módulos de alto nível devem depender de abstrações, não de classes concretas.
    2. IoC (Inversion of Control): É o CONCEITO amplo de inverter a responsabilidade de criação e gerenciamento do ciclo de vida dos objetos.
    3. DI (Dependency Injection): É a TÉCNICA PRÁTICA usada para implementar o IoC e o DIP, onde as dependências são passadas para o objeto (via construtor ou setter) por um agente externo."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma interface abstrata `CacheInterface` e duas implementações (`RedisCache`, `MemoryCache`).
# Exercício 2: Escreva uma classe `ProdutoService` que receba `CacheInterface` por Injeção de Construtor.
# Exercício 3: Escreva um teste unitário para `ProdutoService` passando o `MemoryCache`.


def main() -> None:
    print("==========================================================")
    print("  AULA 68: INJEÇÃO DE DEPENDÊNCIA (DI) E IOC")
    print("==========================================================")
    demonstrar_fundamentos_di()
    demonstrar_container_di()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 68 executado com sucesso.")


if __name__ == "__main__":
    main()
