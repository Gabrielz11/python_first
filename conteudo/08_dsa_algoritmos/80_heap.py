r"""
80_heap.py - Fila de Prioridades com Min-Heap (`heapq`) e Algoritmo Top-K

Objetivos:
1. Utilizar o módulo `heapq` para min-heaps em Python.
2. Resolver o problema dos Top-K elementos maiores/menores em $O(n \log k)$.
"""

import heapq


def obter_top_k_maiores(numeros: list[int], k: int) -> list[int]:
    return heapq.nlargest(k, numeros)


def main() -> None:
    print("==========================================================")
    print("  AULA 80: HEAP E TOP-K ELEMENTOS COM HEAPQ")
    print("==========================================================")
    dados = [42, 10, 99, 3, 55, 88, 23]
    top3 = obter_top_k_maiores(dados, 3)
    print(f"Os 3 maiores elementos de {dados}: {top3}")
    print("\n[Concluido] Arquivo 80 executado com sucesso.")


if __name__ == "__main__":
    main()
