"""
22_itertools.py - Ferramentas de Iteração de Alta Performance (`itertools`)

Objetivos:
1. Dominar o módulo `itertools` para manipulação de iteradores em CPython com O(1) de memória espacial.
2. Explorar combinatória: `product`, `permutations`, `combinations`.
3. Explorar iteradores infinitos e agrupamentos: `count`, `cycle`, `repeat`, `chain`, `groupby`.
"""

import itertools


def demonstrar_itertools() -> None:
    print("\n--- 1. COMBINATÓRIA: product, permutations, combinations ---")

    opcoes = ["A", "B", "C"]

    # Combinações (sem repetição de ordem)
    combs = list(itertools.combinations(opcoes, 2))
    print(f"Combinations (n=2): {combs}")

    # Permutações (ordem importa)
    perms = list(itertools.permutations(opcoes, 2))
    print(f"Permutations (n=2): {perms}")

    # Produto Cartesiano (equivalente a loops aninhados)
    prod = list(itertools.product([1, 2], ["x", "y"]))
    print(f"Product: {prod}")

    print("\n--- 2. AGRUPAMENTO E ENCADEAMENTO: chain e groupby ---")

    l1 = [1, 2, 3]
    l2 = [4, 5]
    # chain evita concatenar listas fisicamente na memória!
    encadeado = list(itertools.chain(l1, l2))
    print(f"Chain: {encadeado}")

    dados = [("dev", "Ana"), ("dev", "Bia"), ("ops", "Carlos")]
    # groupby exige que os dados estejam ORDENADOS pela chave de agrupamento!
    for k, g in itertools.groupby(dados, key=lambda x: x[0]):
        print(f"Grupo {k}: {list(g)}")


def main() -> None:
    print("==========================================================")
    print("  AULA 22: MÓDULO ITERTOOLS E ITERADORES DE ALTA PERFORMANCE")
    print("==========================================================")
    demonstrar_itertools()
    print("\n[Concluido] Arquivo 22 executado com sucesso.")


if __name__ == "__main__":
    main()
