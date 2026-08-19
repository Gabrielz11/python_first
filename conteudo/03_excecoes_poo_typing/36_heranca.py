"""
36_heranca.py - Herança Simples, Sobrescrita de Métodos, super() e Princípio de Liskov

Objetivos:
1. Dominar o conceito de Herança em POO Python e o reaproveitamento de código em subclasses.
2. Utilizar o método nativo `super()` para chamadas cooperativas aos construtores e métodos da classe pai.
3. Compreender a Sobrescrita de Métodos (Method Overriding) e o Princípio de Substituição de Liskov (LSP).
4. Utilizar `isinstance()` e `issubclass()` para checagem segura de tipos na hierarquia.
5. Desenvolver arquiteturas limpas de backend utilizando classes base e repositórios genéricos.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Herança em POO?
Herança é um mecanismo onde uma classe filha (subclasse) herda atributos e comportamentos
(métodos) de uma classe pai (superclasse/base).

Conceitos-Chave:
1. Reutilização de Código: Evita duplicação de atributos e métodos comuns.
2. Relação "É um" (Is-A): Uma subclasse deve ser uma especialização válida da classe pai.
   Exemplo: `FuncionarioCLT` É UM `Funcionario`.
3. super(): Função que retorna um objeto proxy delegado para invocar métodos da superclasse.
4. Princípio de Substituição de Liskov (LSP - SOLID):
   Uma subclasse deve poder ser usada no lugar de sua classe pai sem quebrar o comportamento correto da aplicação.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: HERANÇA E SUPER()
# ==========================================================
class FuncionarioBase:
    """Superclasse Base."""

    def __init__(self, nome: str, email: str, salario_base: float) -> None:
        self.nome = nome
        self.email = email
        self.salario_base = salario_base

    def calcular_remuneracao(self) -> float:
        """Método padrão que será sobrescrito se necessário."""
        return self.salario_base


class Desenvolvedor(FuncionarioBase):
    """Subclasse que herda de FuncionarioBase."""

    def __init__(self, nome: str, email: str, salario_base: float, linguagem_principal: str) -> None:
        # Invoca o construtor da superclasse pai via super()
        super().__init__(nome, email, salario_base)
        self.linguagem_principal = linguagem_principal

    def calcular_remuneracao(self) -> float:
        # Sobrescrita de Método (Method Overriding) com bônus de tecnologia
        return super().calcular_remuneracao() + 1000.00


def demonstrar_fundamentos_heranca() -> None:
    print("\n--- 1. FUNDAMENTOS: Herança e super() ---")

    dev = Desenvolvedor("Gabriel", "gabriel@empresa.com", 8000.0, "Python")

    print(f"Desenvolvedor: {dev.nome} | Linguagem: {dev.linguagem_principal}")
    print(f"Salario Base: R$ {dev.salario_base:.2f}")
    print(f"Remuneração Calculada (com bonus dev): R$ {dev.calcular_remuneracao():.2f}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ISINSTANCE E ISSUBCLASS
# ==========================================================
class Gerente(FuncionarioBase):
    def __init__(self, nome: str, email: str, salario_base: float, tamanho_equipe: int) -> None:
        super().__init__(nome, email, salario_base)
        self.tamanho_equipe = tamanho_equipe


def demonstrar_checagem_tipos() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: isinstance() e issubclass() ---")

    dev = Desenvolvedor("Ana", "ana@empresa.com", 7000.0, "Go")

    print(f"dev é instancia de Desenvolvedor? {isinstance(dev, Desenvolvedor)}")
    print(f"dev é instancia de FuncionarioBase? {isinstance(dev, FuncionarioBase)}")
    print(f"Desenvolvedor é subclasse de FuncionarioBase? {issubclass(Desenvolvedor, FuncionarioBase)}")
    print(f"Gerente é subclasse de Desenvolvedor? {issubclass(Gerente, Desenvolvedor)}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class BaseRepository:
    """Repositório Base genérico em memória."""

    def __init__(self) -> None:
        self._dados: dict[int, Any] = {}

    def salvar(self, id_entidade: int, objeto: Any) -> None:
        self._dados[id_entidade] = objeto
        print(f"  [BaseRepository] Entidade ID {id_entidade} salva com sucesso.")

    def buscar_por_id(self, id_entidade: int) -> Any | None:
        return self._dados.get(id_entidade)


class UserRepository(BaseRepository):
    """Repositório de Usuários especializado."""

    def buscar_por_email(self, email: str) -> Any | None:
        for obj in self._dados.values():
            if getattr(obj, "email", None) == email:
                return obj
        return None


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Repositórios Herdados ---")
    user_repo = UserRepository()

    dev = Desenvolvedor("Carlos", "carlos@empresa.com", 6000.0, "Python")
    user_repo.salvar(101, dev)

    usuario_encontrado = user_repo.buscar_por_email("carlos@empresa.com")
    print(f"Usuario encontrado via repositório: {getattr(usuario_encontrado, 'nome', None)}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: __BASES__ E CPYTON LOOKUP
# ==========================================================
"""
Como a Herança funciona no CPython:
1. Toda classe em Python possui uma tupla interna de classes pai armazenada em `Classe.__bases__`.
2. Em Python 3, todas as classes que não declaram superclasse herdam implicitamente da classe `object`.
3. Quando você invoca um método `obj.metodo()`, o CPython busca o método na classe do objeto;
   se não encontrar, busca sequencialmente nas classes listadas em `__bases__`.
"""


def demonstrar_internamente_bases() -> None:
    print("\n--- 4. INTERNO: Tupla __bases__ no CPython ---")
    print(f"Superclasses de Desenvolvedor: {Desenvolvedor.__bases__}")
    print(f"Superclasses de FuncionarioBase: {FuncionarioBase.__bases__}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Resolução de Métodos Herdados: Busca na árvore de herança -> Tempo O(D), onde D é a profundidade do caminho na árvore.
- Instanciação de Subclasse: Chama os construtores encadeados via `super()` -> Tempo O(D).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Chamada explícita rígida ao pai nomeando a classe pai diretamente
    print("[X] Nao-Pythonic (Chamar NomeDaClassePai.__init__ sem super):")
    print("  FuncionarioBase.__init__(self, nome, email, salario)")

    # [OK] PYTHONIC: Utilizar super() cooperativo
    print("\n[OK] Pythonic:")
    print("  super().__init__(nome, email, salario)  # Suporta MRO e Herança Múltipla!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Prefira Composição sobre Herança ("Favor Composition over Inheritance"): Use herança apenas para relacionamentos estritos de "É UM".
2. Mantenha as árvores de herança rasas (máximo 2 a 3 níveis de profundidade). Árvores profundas tornam o código frágil e difícil de manter.
3. Respeite o Princípio de Substituição de Liskov (LSP): Subclasses nunca devem alterar a assinatura nem enfraquecer as pré-condições da classe pai.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer de chamar super().__init__() na subclasse
    class SubClasseSemSuper(FuncionarioBase):
        def __init__(self, nome: str) -> None:
            # [!] Esqueceu super().__init__() -> Atributos da classe pai não foram inicializados!
            self.nome = nome

    s = SubClasseSemSuper("Teste")
    try:
        _ = s.salario_base
    except AttributeError as e:
        print(f"[!] Armadilha 1 (AttributeError por falta de super().__init__): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que devemos utilizar `super().__init__()` em vez de chamar diretamente `ClassePai.__init__(self)`?"
A: "1. Desacoplamento: O `super()` não exige que você nomeie explicitamente a classe pai, facilitando refatorações de renomeação.
    2. Herança Múltipla Cooperativa: O `super()` em Python não chama apenas a classe pai direta; ele segue a ordem
       definida pela C3 Linearization (Method Resolution Order - MRO), garantindo que cada classe na hierarquia
       seja inicializada exatamente uma única vez."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Veiculo` (marca, modelo) e uma subclasse `Carro` (quantidade_portas).
# Exercício 2: Escreva um método `exibir_informacoes()` na classe pai e sobrescreva-o na subclasse utilizando `super().exibir_informacoes()`.
# Exercício 3: Crie uma lista de objetos contendo instâncias de pai e subclasses e percorra a lista executando um método sobrescrito polimorficamente.


def main() -> None:
    print("==========================================================")
    print("  AULA 36: HERANÇA SIMPLES, SUPER() E LISKOV")
    print("==========================================================")
    demonstrar_fundamentos_heranca()
    demonstrar_checagem_tipos()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_bases()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 36 executado com sucesso.")


if __name__ == "__main__":
    main()
