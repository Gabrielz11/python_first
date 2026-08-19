"""
72_arrays_lists.py - Algoritmos em Arrays: Two Pointers e Sliding Window

Objetivos:
1. Resolver problemas de arrays usando o padrão Two Pointers (Dois Ponteiros).
2. Resolver problemas de subsequências usando Sliding Window (Janela Deslizante).
"""

def dois_ponteiros_soma_alvo(numeros_ordenados: list[int], alvo: int) -> tuple[int, int] | None:
    """Retorna os índices de dois números que somam o alvo em O(n) tempo e O(1) espaço."""
    esquerda = 0
    direita = len(numeros_ordenados) - 1

    while esquerda < direita:
        soma = numeros_ordenados[esquerda] + numeros_ordenados[direita]
        if soma == alvo:
            return (esquerda, direita)
        elif soma < alvo:
            esquerda += 1
        else:
            direita -= 1
    return None


def main() -> None:
    print("==========================================================")
    print("  AULA 72: TÉCNICA TWO POINTERS EM ARRAYS/LISTAS")
    print("==========================================================")
    nums = [1, 3, 5, 7, 10, 11]
    resultado = dois_ponteiros_soma_alvo(nums, 12)
    if resultado is not None:
        print(f"Índices que somam 12 em {nums}: {resultado} (Valores: {nums[resultado[0]]} + {nums[resultado[1]]})")
    print("\n[Concluido] Arquivo 72 executado com sucesso.")


if __name__ == "__main__":
    main()
