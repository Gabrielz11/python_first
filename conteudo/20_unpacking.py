"""
20_unpacking.py - Desempacotamento de Sequências e Operadores * e **

Objetivos:
1. Dominar o desempacotamento com `*` e `**`.
"""

def demonstrar_unpacking() -> None:
    print("\n--- 1. EXTENDED UNPACKING ---")
    primeiro, *meio, ultimo = [1, 2, 3, 4, 5]
    print(f"Primeiro: {primeiro}, Meio: {meio}, Último: {ultimo}")


def main() -> None:
    print("==========================================================")
    print("  AULA 20: UNPACKING AVANÇADO")
    print("==========================================================")
    demonstrar_unpacking()
    print("\n[Concluido] Arquivo 20 executado com sucesso.")


if __name__ == "__main__":
    main()
