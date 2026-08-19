"""
03_tipos_dados.py - Tipos Primitivos, Coerção (Casting), Truthiness e Mutabilidade

Objetivos:
1. Conhecer profundamente os tipos nativos primitivos em Python: int, float, complex, bool, str, NoneType.
2. Compreender a conversão explícita de tipos (Casting) e coerções seguras.
3. Dominar as regras universais de Truthy e Falsy em Python.
4. Diferenciar Objetos Mutáveis de Objetos Imutáveis e o impacto disso no projeto de sistemas.
"""

from typing import Any

# ==========================================================
# 1. CONCEITO: Tipos Primitivos e Imutabilidade Fundamental
# ==========================================================
"""
Em Python, os tipos de dados fundamentais (primitivos) são todos OBJETOS na Heap.

Tabela de Mutabilidade dos Tipos Nativo-Base:
--------------------------------------------------------------
Tipo          Exemplo                   Mutável?
--------------------------------------------------------------
int           42, -7                    Não (Imutável)
float         3.14159                   Não (Imutável)
complex       3 + 4j                    Não (Imutável)
bool          True, False               Não (Imutável)
str           "Engenharia"              Não (Imutável)
NoneType      None                      Não (Imutável)
bytes         b"dados"                  Não (Imutável)
--------------------------------------------------------------
list          [1, 2, 3]                 SIM (Mutável)
dict          {"a": 1}                  SIM (Mutável)
set           {1, 2, 3}                 SIM (Mutável)
--------------------------------------------------------------

Por que a Imutabilidade é Crucial?
Objetos imutáveis garantem segurança em ambientes concorrentes/multi-thread
e permitem o cálculo de HASH seguro (podem ser usados como chaves em dicionários e elementos de conjuntos).
"""


def demonstrar_tipos_primitivos() -> None:
    print("\n--- 1. CONCEITO: Tipos Primitivos e Suas Propriedades ---")

    inteiro: int = 1_000_000  # Python 3.6+ permite sublinhado para legibilidade numérica
    ponto_flutuante: float = 0.1 + 0.2
    numero_complexo: complex = 2 + 5j
    booleano: bool = True
    texto: str = "Python Sênior"
    nulo: None = None

    print(f"int (com sublinha legível): {inteiro} | Tipo: {type(inteiro).__name__}")
    print(f"float (precisão IEEE 754): {ponto_flutuante} | Tipo: {type(ponto_flutuante).__name__}")
    print(f"complex: parte real={numero_complexo.real}, imag={numero_complexo.imag}")
    print(f"bool: {booleano} | Subclasse de int? {issubclass(bool, int)} (True == 1)")
    print(f"str: '{texto}' | Tamanho={len(texto)}")
    print(f"NoneType: {nulo} | Representa ausencia de valor")


# ==========================================================
# 2. EXEMPLOS: Conversão de Tipos (Casting) e Truthiness
# ==========================================================
def demonstrar_casting_e_truthiness() -> None:
    print("\n--- 2. EXEMPLOS: Casting e Regras de Truthy/Falsy ---")

    # 1. Casting Seguro
    str_numero = "450"
    num_convertido = int(str_numero)
    float_convertido = float("19.99")

    print(f"String '{str_numero}' convertida para int: {num_convertido + 50}")
    print(f"String '19.99' convertida para float: {float_convertido}")

    # 2. Regras de Truthy / Falsy em Python:
    # O que é FALSY em Python?
    # - None
    # - False
    # - Zero de qualquer tipo numérico (0, 0.0, 0j)
    # - Coleções e sequências vazias ('', [], (), {}, set(), range(0))
    # TUDO O MAIS é considerado TRUTHY!

    valores_para_testar: list[Any] = [
        0,
        1,
        "",
        "Texto",
        [],
        [1, 2],
        {},
        {"key": "val"},
        None,
    ]

    print("\nTabela de Avaliação Booleana (bool(x)):")
    for val in valores_para_testar:
        print(f"  Objeto: {repr(val):<15} -> bool: {bool(val)}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Processamento de Dados de Formulário/API
# ==========================================================
def processar_payload_api(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Higieniza e converte tipos recebidos em um payload de requisição HTTP.
    """
    print("\n--- 3. EXEMPLO PRÁTICO: Sanitização de Payload HTTP ---")

    raw_age = payload.get("age")
    raw_status = payload.get("active")
    raw_tags = payload.get("tags")

    # Converter idade para int com fallback seguro
    try:
        clean_age = int(raw_age) if raw_age is not None else 0
    except (ValueError, TypeError):
        clean_age = 0

    # Avaliação idiomática de Truthiness para verificar se a lista de tags possui elementos
    has_tags = bool(raw_tags)

    return {
        "user_age": clean_age,
        "is_active": bool(raw_status),
        "has_tags": has_tags,
        "total_tags": len(raw_tags) if isinstance(raw_tags, list) else 0,
    }


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Análise de Imutabilidade e Reatribuição de Strings e Números:
- Modificar uma String em um laço de repetição (`s += "a"`):
  - Complexidade Temporal: O(n²) se nova string for alocada em cada passo!
  - Alternativa Pythonic: Coletar partes em uma lista e usar `"".join(lista)` -> O(n) Temporal.
"""


def demonstrar_performance_strings() -> None:
    print("\n--- 4. COMPLEXIDADE: Acúmulo de Strings Imutáveis ---")

    # Forma lenta: reatribuição de string imutável O(n²)
    partes = ["parte_1", "parte_2", "parte_3", "parte_4"]

    # Forma Pythonic O(n):
    resultado_pythonic = ", ".join(partes)
    print(f"Join de lista em string O(n): {resultado_pythonic}")


# ==========================================================
# 5. COMPARATIVO: NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    itens: list[str] = []

    # [X] NÃO-PYTHONIC (Verificar se coleção está vazia comparando len(itens) == 0):
    print("[X] Nao-Pythonic:")
    if len(itens) == 0:
        print("  A lista esta vazia (via len(itens) == 0)")

    # [OK] PYTHONIC (Aproveitar a regra nativa de Falsy de coleções vazias):
    print("[OK] Pythonic:")
    if not itens:
        print("  A lista esta vazia (via 'if not itens')")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Imprecisão de Ponto Flutuante (IEEE 754)
    soma_float = 0.1 + 0.2
    print(f"0.1 + 0.2 == 0.3? {soma_float == 0.3} (Resultado real: {soma_float})")
    print("  -> Solução para finanças/precisão: use o módulo 'decimal.Decimal' ou math.isclose()")

    # Armadilha 2: Tentar alterar um caractere de uma string (TypeError)
    texto = "Python"
    try:
        # texto[0] = "J" # Lança TypeError porque str é imutável!
        pass
    except TypeError as e:
        print(f"[!] Armadilha de Imutabilidade: {e}")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como lidar com imprecisão de valores monetários e decimais em Python?"
A: "Nunca utilize o tipo primitivo `float` para cálculos financeiros devido à representação em ponto flutuante binário IEEE 754.
    Utilize o módulo nativo `decimal.Decimal`, que trabalha em base 10 e permite controle de precisão exato."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um script que receba uma string contendo um número float (ex: "1250.75")
#              e converta com segurança para int truncado e Decimal.
# Exercício 2: Escreva uma função que receba um argumento genérico e retorne uma string descrevendo
#              se o valor é Truthy ou Falsy e qual o seu tipo nativo.


def main() -> None:
    print("==========================================================")
    print("  AULA 03: TIPOS PRIMITIVOS, CASTING E MUTABILIDADE")
    print("==========================================================")
    demonstrar_tipos_primitivos()
    demonstrar_casting_e_truthiness()

    payload_teste = {"age": "28", "active": 1, "tags": ["python", "backend"]}
    res = processar_payload_api(payload_teste)
    print(f"Resultado Sanitizado: {res}")

    demonstrar_performance_strings()
    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 03 executado com sucesso.")


if __name__ == "__main__":
    main()
