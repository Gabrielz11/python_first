"""
71_big_o.py - Análise de Complexidade de Algoritmos (Big O Notation)

Objetivos:
1. Compreender as classes de complexidade: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ).
2. Analisar complexidade temporal e espacial.
"""

def exemplo_constante_o1(lista: list[int]) -> int:
    return lista[0]  # O(1)


def exemplo_linear_on(lista: list[int]) -> int:
    soma = 0
    for x in lista:  # O(n)
        soma += x
    return soma


def exemplo_quadratico_on2(lista: list[int]) -> int:
    pares = 0
    for i in lista:
        for j in lista:  # O(n²)
            if i == j:
                pares += 1
    return pares


def main() -> None:
    print("==========================================================")
    print("  AULA 71: ANÁLISE BIG O TEMPORAL E ESPACIAL")
    print("==========================================================")
    dados = list(range(100))
    print(f"Acesso O(1): {exemplo_constante_o1(dados)}")
    print(f"Soma O(n): {exemplo_linear_on(dados)}")
    print("\n[Concluido] Arquivo 71 executado com sucesso.")


if __name__ == "__main__":
    main()
