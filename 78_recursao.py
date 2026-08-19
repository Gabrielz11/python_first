"""
78_recursao.py - Recursão, Call Stack e Condições de Parada (Caso Base)

Objetivos:
1. Compreender a pilha de execução (Call Stack) em chamadas recursivas.
2. Definir caso base e caso recursivo corretamente para evitar `RecursionError`.
"""

def fatorial(n: int) -> int:
    # Caso Base
    if n <= 1:
        return 1
    # Passo Recursivo
    return n * fatorial(n - 1)


def main() -> None:
    print("==========================================================")
    print("  AULA 78: RECURSÃO E PILHA DE CHAMADAS")
    print("==========================================================")
    res = fatorial(5)
    print(f"Fatorial de 5! = {res}")
    print("\n[Concluido] Arquivo 78 executado com sucesso.")


if __name__ == "__main__":
    main()
