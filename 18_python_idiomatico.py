"""
18_python_idiomatico.py - Python Idiomático (Pythonic Code, EAFP vs LBYL, Truthiness)

Objetivos:
1. Entender a filosofia "Pythonic" (Zen do Python - PEP 20).
2. Compreender a diferença entre EAFP (Easier to Ask for Forgiveness than Permission) e LBYL (Look Before You Leap).
3. Utilizar Truthiness e Falsiness de forma limpa e performática.
"""

from typing import Any


def demonstrar_eafp_vs_lbyl() -> None:
    print("\n--- 1. CONCEITO: EAFP vs LBYL ---")
    dados: dict[str, Any] = {"nome": "Gabriel", "idade": 28}

    # LBYL
    if "email" in dados:
        email_lbyl = dados["email"]
    else:
        email_lbyl = "nao_informado@email.com"
    print(f"LBYL Result: {email_lbyl}")

    # EAFP
    try:
        email_eafp = dados["email"]
    except KeyError:
        email_eafp = "nao_informado@email.com"
    print(f"EAFP Result: {email_eafp}")


def main() -> None:
    print("==========================================================")
    print("  AULA 18: PYTHON IDIOMÁTICO")
    print("==========================================================")
    demonstrar_eafp_vs_lbyl()
    print("\n[Concluido] Arquivo 18 executado com sucesso.")


if __name__ == "__main__":
    main()
