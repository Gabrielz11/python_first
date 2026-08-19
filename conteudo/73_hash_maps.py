"""
73_hash_maps.py - Algoritmos com Hash Maps (Padrão Two Sum e Frequência em O(n))

Objetivos:
1. Resolver o clássico algoritmo Two Sum em O(n) utilizando Hash Table.
"""

def two_sum_hashmap(numeros: list[int], alvo: int) -> tuple[int, int] | None:
    """Encontra os índices dos dois números que somam o alvo em O(n) temporal."""
    mapa_visitados: dict[int, int] = {}  # valor -> índice
    for i, num in enumerate(numeros):
        complemento = alvo - num
        if complemento in mapa_visitados:
            return (mapa_visitados[complemento], i)
        mapa_visitados[num] = i
    return None


def main() -> None:
    print("==========================================================")
    print("  AULA 73: ALGORITMO TWO SUM COM HASH MAP O(n)")
    print("==========================================================")
    nums = [2, 7, 11, 15]
    res = two_sum_hashmap(nums, 9)
    print(f"Dois números que somam 9 em {nums}: índices {res}")
    print("\n[Concluido] Arquivo 73 executado com sucesso.")


if __name__ == "__main__":
    main()
