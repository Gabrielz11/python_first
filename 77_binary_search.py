"""
77_binary_search.py - Busca Binária (Binary Search O(log n))

Objetivos:
1. Implementar o algoritmo de Busca Binária em arrays ordenados.
2. Demonstrar a redução logarítmica do espaço de busca.
"""

def busca_binaria(arr: list[int], alvo: int) -> int:
    esquerda = 0
    direita = len(arr) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def main() -> None:
    print("==========================================================")
    print("  AULA 77: BUSCA BINÁRIA O(LOG N)")
    print("==========================================================")
    lista_ordenada = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    idx = busca_binaria(lista_ordenada, 70)
    print(f"Índice do elemento 70 em {lista_ordenada}: {idx}")
    print("\n[Concluido] Arquivo 77 executado com sucesso.")


if __name__ == "__main__":
    main()
