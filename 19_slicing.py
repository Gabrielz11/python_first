"""
19_slicing.py - Manipulação Avançada de Sequências via Slicing [start:stop:step]

Objetivos:
1. Dominar fatiamento (slicing) em strings, listas e tuplas.
2. Entender o objeto `slice(start, stop, step)` do CPython.
"""

def demonstrar_slicing() -> None:
    print("\n--- 1. SLICING E PASSO NEGATIVO ---")
    numeros = [0, 10, 20, 30, 40, 50]
    print(f"Original: {numeros}")
    print(f"Invertido [::-1]: {numeros[::-1]}")


def main() -> None:
    print("==========================================================")
    print("  AULA 19: SLICING AVANÇADO")
    print("==========================================================")
    demonstrar_slicing()
    print("\n[Concluido] Arquivo 19 executado com sucesso.")


if __name__ == "__main__":
    main()
