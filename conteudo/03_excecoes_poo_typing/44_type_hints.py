"""
44_type_hints.py - Sistema de Type Hints, PEP 484, PEP 585 e Análise Estática de Tipos

Objetivos:
1. Dominar a sintaxe de Anotações de Tipo (Type Hints - PEP 484 e PEP 526).
2. Utilizar a sintaxe moderna de coleções genéricas (PEP 585 - `list[int]`, `dict[str, Any]` em Python 3.9+).
3. Utilizar o operador de união `|` (PEP 604 - Python 3.10+) em substituição a `Union` e `Optional`.
4. Compreender que Type Hints NÃO alteram a execução dinâmica em runtime do CPython (desempenho Zero Overhead).
5. Inspecionar o dicionário `__annotations__` de funções e classes.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Type Hints em Python?
Type Hints são anotações opcionais adicionadas a variáveis, parâmetros de função e retornos
para indicar os tipos esperados de dados.

Regra de Ouro do Python:
O Python CONTINUA SENDO UMA LINGUAGEM DINÂMICA.
O interpretador CPython IGNORA as anotações de tipo em tempo de execução (Runtime).
Passar uma `str` para uma função anotada como `def f(x: int)` NÃO lança exceção em runtime!

Para que servem os Type Hints então?
1. Análise Estática de Código: Ferramentas como Mypy, Pyright e Linters detectam bugs ANTES da execução.
2. Autocompletar e Produtividade em IDEs: VS Code / PyCharm oferecem autocompletar inteligente.
3. Autodocumentação: Torna as assinaturas de funções e APIs autoexplicativas.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ANOTAÇÕES BÁSICAS E PEP 604
# ==========================================================
def calcular_desconto(
    preco_original: float,
    taxa_desconto: float,
    cupom: str | None = None,  # Sintaxe PEP 604 (substitui Optional[str])
) -> float:
    """Calcula o valor com desconto aplicando taxa opcional de cupom."""
    desconto_total = preco_original * taxa_desconto
    if cupom == "PROMO10":
        desconto_total += 10.0
    return max(0.0, preco_original - desconto_total)


def demonstrar_sintaxe_type_hints() -> None:
    print("\n--- 1. FUNDAMENTOS: Type Hints com PEP 604 (str | None) ---")

    # Anotações de Variáveis
    total_pedidos: int = 150
    cliente_ativo: bool = True
    itens_carrinho: list[str] = ["Notebook", "Mouse"]
    configuracao: dict[str, Any] = {"timeout": 30, "ssl": True}

    val1 = calcular_desconto(100.0, 0.10)
    val2 = calcular_desconto(100.0, 0.10, cupom="PROMO10")

    print(f"Desconto sem cupom: R$ {val1:.2f}")
    print(f"Desconto com cupom PROMO10: R$ {val2:.2f}")
    print(f"Itens anotados (list[str]): {itens_carrinho}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: COLEÇÕES GENÉRICAS E TUPLES
# ==========================================================
def processar_coordenadas(ponto: tuple[int, int]) -> dict[str, int]:
    x, y = ponto
    return {"eixo_x": x, "eixo_y": y}


def demonstrar_colecoes_genericas() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Tuplas e Dicionários Tipados ---")

    ponto_2d: tuple[int, int] = (10, 20)
    resultado = processar_coordenadas(ponto_2d)
    print(f"Coordenadas processadas: {resultado}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def buscar_usuario_por_id(user_id: int) -> dict[str, str | int] | None:
    """Simula consulta de repositório anotada com union (dict | None)."""
    if user_id == 101:
        return {"id": 101, "nome": "Gabriel Zilmar", "email": "gabriel@empresa.com"}
    return None


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Retornos Opcionais Tipados ---")
    u1 = buscar_usuario_por_id(101)
    u2 = buscar_usuario_por_id(999)

    print(f"Usuario 101: {u1}")
    print(f"Usuario 999: {u2}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: __ANNOTATIONS__
# ==========================================================
"""
Como o CPython armazena Type Hints:
1. Quando uma função ou classe é definida, o CPython avalia as expressões de tipo e as guarda
   no dicionário especial `__annotations__`.
2. O CPython NÃO valida esses valores em runtime; apenas os expõe para bibliotecas terceiras
   como Pydantic, FastAPI e Mypy.
"""


def demonstrar_internamente_annotations() -> None:
    print("\n--- 4. INTERNO: O Dicionário __annotations__ ---")
    print("Atributo __annotations__ da função calcular_desconto:")
    for k, v in calcular_desconto.__annotations__.items():
        print(f"  - {k}: {v}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Custo em Runtime de Type Hints: O(1) de tempo, O(1) de espaço (Zero-Cost Runtime Overhead em funções).
  As anotações são salvas em `__annotations__` no momento do import do módulo.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar sintaxe legada do módulo typing em Python 3.10+ (typing.Union, typing.Optional)
    print("[X] Nao-Pythonic (Sintaxe legada typing.Optional/Union):")
    print("  from typing import Optional, Union\n  def f(x: Optional[str]) -> Union[int, float]: ...")

    # [OK] PYTHONIC: Utilizar a sintaxe moderna PEP 604 com o operador |
    print("\n[OK] Pythonic (PEP 604 - Python 3.10+):")
    print("  def f(x: str | None) -> int | float: ...  # Muito mais limpo e conciso!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Adicione Type Hints em TODAS as assinaturas de funções e métodos públicos em projetos corporativos.
2. Utilize `str | None` em vez de `Optional[str]` em projetos desenvolvidos para Python 3.10+.
3. Utilize `list[int]` e `dict[str, Any]` em vez de `typing.List` e `typing.Dict` (PEP 585).
4. Utilize a ferramenta `mypy` no seu pipeline de CI/CD (`mypy .`) para garantir a integridade dos tipos.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Achar que Type Hints impedem a passagem de tipos incorretos em runtime!
    def funcao_tipada(numero: int) -> int:
        return numero * 2

    # [!] O CPython EXECUTA SEM ERROS mesmo passando uma string! (O Mypy pegaria em análise estática)
    resultado_sem_erro_runtime = funcao_tipada("10")  # type: ignore # Retorna '1010'
    print(f"[!] Armadilha 1 (Runtime não valida tipos!): '10' * 2 = {resultado_sem_erro_runtime!r}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O Python se tornou uma linguagem de tipagem estática após a introdução dos Type Hints (PEP 484)?"
A: "NÃO. O Python continua sendo uma linguagem de Tipagem Dinâmica e Forte.
    Os Type Hints são apenas anotações armazenadas no dicionário `__annotations__` e ignoradas pelo CPython em runtime.
    A checagem de tipos ocorre EXCLUSIVAMENTE fora do ciclo de execução através de ferramentas de análise estática como o Mypy,
    ou por bibliotecas de runtime como o Pydantic."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Anote uma função `calcular_media(notas: list[float]) -> float` com Type Hints completos.
# Exercício 2: Escreva uma função `obter_configuracao(chave: str) -> str | int | None` usando a sintaxe PEP 604.
# Exercício 3: Inspecione o dicionário `__annotations__` de uma classe com atributos anotados.


def main() -> None:
    print("==========================================================")
    print("  AULA 44: TYPE HINTS, PEP 484, PEP 585 E ANÁLISE ESTÁTICA")
    print("==========================================================")
    demonstrar_sintaxe_type_hints()
    demonstrar_colecoes_genericas()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_annotations()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 44 executado com sucesso.")


if __name__ == "__main__":
    main()
