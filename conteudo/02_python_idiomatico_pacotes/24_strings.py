"""
24_strings.py - Manipulação Eficiente de Strings e Formatação (f-strings, str methods)

Objetivos:
1. Entender a imutabilidade de strings no CPython e por que concatenar com `+` em loops é O(n²).
2. Utilizar `str.join()` para concatenação performática em O(n).
3. Dominar f-strings avançadas (alinhamento, numeração, especificadores de tipo, debug `=`).
"""

def demonstrar_strings() -> None:
    print("\n--- 1. CONCATENAÇÃO PERFORMATICA: str.join vs += ---")

    palavras = ["Python", "é", "uma", "linguagem", "poderosa"]

    # ✅ PYTHONIC (O(n)): str.join aloca a memória exata de uma só vez
    frase = " ".join(palavras)
    print(f"String unida com ' '.join(): {frase}")

    print("\n--- 2. F-STRINGS AVANÇADAS ---")
    preco = 1234.5678
    percentual = 0.854
    print(f"Preço formatado: R$ {preco:,.2f}")
    print(f"Percentual: {percentual:.1%}")
    print(f"Alinhamento à direita [>15]: '{preco:>15.2f}'")

    # F-string Debug (Python 3.8+)
    x = 42
    print(f"Debug com `=`: {x=}")


def main() -> None:
    print("==========================================================")
    print("  AULA 24: MANIPULAÇÃO DE STRINGS E F-STRINGS AVANÇADAS")
    print("==========================================================")
    demonstrar_strings()
    print("\n[Concluido] Arquivo 24 executado com sucesso.")


if __name__ == "__main__":
    main()
