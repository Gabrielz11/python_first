"""
45_typing_avancado.py - Typing Avançado: Protocol, TypeVar, Generic e Structural Subtyping

Objetivos:
1. Dominar o uso de `typing.Protocol` para Subtipagem Estrutural (Static Duck Typing - PEP 544).
2. Criar classes e repositórios genéricos utilizando `TypeVar` e `Generic[T]`.
3. Utilizar o decorador `@runtime_checkable` para permitir o uso de `isinstance()` com `Protocol`.
4. Utilizar `Callable`, `ParamSpec`, `TypeGuard` e `Literal` para tipagem precisa em middlewares e decoradores.
5. Desenvolver arquiteturas limpas desacopladas com Type Checking estático avançado em Python.
"""

from typing import Any, Callable, Generic, Literal, Protocol, TypeVar, runtime_checkable


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Structural Subtyping e Protocol (PEP 544)?
Em tipagem estática tradicional (Subtipagem Nominal), para que a classe B seja aceita no lugar de A,
ela DEVE herdar explicitamente de A (`class B(A)`).

Em Python com `typing.Protocol` (Subtipagem Estrutural / Static Duck Typing):
Se a classe B implementa os mesmos métodos e atributos declarados no `Protocol`, o Mypy a considera
uma subclasse válida SEM EXIGIR HERANÇA EXPLICITA!

Genéricos (`TypeVar` e `Generic[T]`):
Permite criar estruturas reutilizáveis (como Repositórios ou Filas) mantendo o tipo dos elementos
preservado pela análise estática (ex: `Repository[Usuario]` vs `Repository[Produto]`).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: PROTOCOL E STATIC DUCK TYPING
# ==========================================================
@runtime_checkable
class ImprimivelProtocol(Protocol):
    """Protocolo que exige apenas o método formatar_para_impressao()."""

    def formatar_para_impressao(self) -> str:
        ...


class RelatorioPDF:
    """Classe que NÃO herda de ImprimivelProtocol, mas satisfaz a estrutura!"""

    def __init__(self, titulo: str) -> None:
        self.titulo = titulo

    def formatar_para_impressao(self) -> str:
        return f"[PDF] Relatório: {self.titulo}"


class CupomFiscal:
    """Outra classe sem herança explícita."""

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def formatar_para_impressao(self) -> str:
        return f"[CUPOM] Valor: R$ {self.valor:.2f}"


def imprimir_documento(doc: ImprimivelProtocol) -> None:
    """Função que aceita qualquer objeto que satisfaça o ImprimivelProtocol."""
    print(f"  Imprimindo: {doc.formatar_para_impressao()}")


def demonstrar_fundamentos_protocol() -> None:
    print("\n--- 1. FUNDAMENTOS: Protocol (Static Duck Typing) ---")

    pdf = RelatorioPDF("Balanço Anual 2026")
    cupom = CupomFiscal(150.75)

    imprimir_documento(pdf)
    imprimir_documento(cupom)

    # Graças ao @runtime_checkable, o isinstance() funciona com Protocol!
    print(f"pdf é isinstance(ImprimivelProtocol)? {isinstance(pdf, ImprimivelProtocol)}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: GENERIC[T] E TYPEVAR
# ==========================================================
T = TypeVar("T")  # Tipo Genérico


class RepositorioGenerico(Generic[T]):
    """Repositório Genérico Tipado com Generic[T]."""

    def __init__(self) -> None:
        self._itens: list[T] = []

    def adicionar(self, item: T) -> None:
        self._itens.append(item)

    def obter_todos(self) -> list[T]:
        return self._itens


def demonstrar_genericos() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Generic[T] e TypeVar ---")

    repo_str: RepositorioGenerico[str] = RepositorioGenerico()
    repo_str.adicionar("Token_A")
    repo_str.adicionar("Token_B")

    repo_int: RepositorioGenerico[int] = RepositorioGenerico()
    repo_int.adicionar(100)
    repo_int.adicionar(200)

    print(f"Repositório de Strings: {repo_str.obter_todos()}")
    print(f"Repositório de Inteiros: {repo_int.obter_todos()}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
# Uso de Literal para limitar opções válidas de entrada
NivelLogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]


class LoggerAvancadoService:
    @staticmethod
    def registrar_log(mensagem: str, nivel: NivelLogLevel = "INFO") -> None:
        print(f"  [{nivel}] {mensagem}")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Literal e Typing Avançado ---")
    LoggerAvancadoService.registrar_log("Serviço iniciado com sucesso", nivel="INFO")
    LoggerAvancadoService.registrar_log("Falha de conexão com cache Redis", nivel="ERROR")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: PROTOCOL VS ABC
# ==========================================================
"""
Diferença entre `abc.ABC` e `typing.Protocol`:
1. `abc.ABC`: Exige Herança Nominal explícita (`class Sub(BaseABC)`). Falha na INSTANCIAÇÃO se esquecer um método.
2. `typing.Protocol`: NÃO exige herança (`class Sub`). A verificação é feita pelo LINTER/MYPY em tempo de checagem estática.
3. Se utilizar `@runtime_checkable`, o CPython inspeciona os métodos da classe no momento do `isinstance()`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Protocol e TypeVar em Runtime: Zero overhead de execução (ignorado pelo CPython em tempo de execução).
- `isinstance(obj, ProtocolRuntimeCheckable)`: Tempo O(M), onde M é o número de métodos a inspecionar no protocolo.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar Any em todo lugar perdendo a segurança de tipos
    print("[X] Nao-Pythonic (Uso descontrolado de Any):")
    print("  def salvar(item: Any) -> Any: ...  # O Mypy não consegue ajudar!")

    # [OK] PYTHONIC: Utilizar Generic[T] e Protocol
    print("\n[OK] Pythonic:")
    print("  def salvar[T](item: T) -> T: ...  # Preserva o tipo exato do objeto!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize `typing.Protocol` para definir contratos de interface sem forçar acoplamento de herança entre módulos.
2. Adicione `@runtime_checkable` aos seus Protocols se pretender utilizar `isinstance()` em blocos condicionais de runtime.
3. Utilize `Generic[T]` em classes contêineres e repositórios para garantir autocomplete e type safety no Mypy.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    class ProtocoloSemDecorator(Protocol):
        def acao(self) -> None: ...

    class ObjetoQualquer:
        def acao(self) -> None: pass

    # Armadilha 1: Tentar usar isinstance() em Protocol sem @runtime_checkable
    try:
        isinstance(ObjetoQualquer(), ProtocoloSemDecorator)  # type: ignore # Lança TypeError
    except TypeError as e:
        print(f"[!] Armadilha 1 (TypeError em Protocol sem @runtime_checkable): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre Subtipagem Nominal (`ABC`) e Subtipagem Estrutural (`Protocol`) em Python?"
A: "1. Subtipagem Nominal (`ABC`): A relação de tipo é baseada na HIERARQUIA DE HERANÇA declarada (`class B(A)`).
       É verificada em tempo de instanciação pelo CPython.
    2. Subtipagem Estrutural (`Protocol`): A relação de tipo é baseada na ESTRUTURA DOS MÉTODOS e atributos.
       Se a classe B possui os mesmos métodos do Protocol P, o Mypy a aceita como válida sem necessidade de herdar de P.
       É a formalização estática do famoso 'Duck Typing' do Python."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um `Protocol` chamado `Serializavel` com o método `to_dict(self) -> dict[str, Any]` e teste com duas classes independentes.
# Exercício 2: Escreva uma classe `FilaGenerica(Generic[T])` com métodos `enfileirar(item: T)` e `desenfileirar() -> T`.
# Exercício 3: Crie um parâmetro anotado com `Literal["GET", "POST", "PUT", "DELETE"]` para limitar os métodos HTTP em uma função de cliente web.


def main() -> None:
    print("==========================================================")
    print("  AULA 45: TYPING AVANÇADO, PROTOCOL E GENERIC[T]")
    print("==========================================================")
    demonstrar_fundamentos_protocol()
    demonstrar_genericos()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 45 executado com sucesso.")


if __name__ == "__main__":
    main()
