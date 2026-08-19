"""
77_binary_search.py - Busca Binária (Binary Search), Divisão e Conquista e o Módulo bisect

Objetivos:
1. Dominar o Algoritmo de Busca Binária (Binary Search) baseado no paradigma de Divisão e Conquista.
2. Reconhecer a Pré-Condição Fundamental: A coleção DEVE estar pré-ordenada.
3. Prevenir a armadilha clássica de Integer Overflow ao calcular o ponto médio (`mid`).
4. Comparar as implementações Iterativa (O(1) espaço) e Recursiva (O(log n) espaço).
5. Utilizar o módulo nativo `bisect` em Python para inserções e buscas em listas ordenadas.
"""

import bisect
import time
from typing import Any


# ==========================================================
# 1. CONCEITO E FUNCIONAMENTO DA BUSCA BINÁRIA
# ==========================================================
"""
O que é Busca Binária (Binary Search)?
É um algoritmo de busca altamente eficiente que reduz pela METADE o espaço de busca a cada iteração.

Pré-condição Obrigatória:
A lista de entrada DEVE estar estritamente OPORTUNAMENTE ORDENADA.

Como funciona a mecânica de ponteiros:
1. Mantém dois ponteiros: `left = 0` (início) e `right = len - 1` (fim).
2. Calcula o elemento do meio: `mid = left + (right - left) // 2`.
3. Se `array[mid] == alvo`, elemento encontrado!
4. Se `array[mid] < alvo`, descarta toda a metade esquerda fazendo `left = mid + 1`.
5. Se `array[mid] > alvo`, descarta toda a metade direita fazendo `right = mid - 1`.

Prevenção de Integer Overflow (Gotcha de Entrevistas):
Em linguagens como C/C++/Java, escrever `mid = (left + right) // 2` pode estourar o limite de inteiros de 32 bits se `left + right > 2.147.483.647`.
A fórmula segura e: `mid = left + (right - left) // 2`.
(Em Python os inteiros têm precisão arbitrária, mas a fórmula é exigida em entrevistas).
"""


# ==========================================================
# 2. IMPLEMENTAÇÃO ITERATIVA E RECURSIVA
# ==========================================================
def busca_binaria_iterativa(nums: list[int], alvo: int) -> int:
    """Busca Binária Iterativa: Tempo O(log n), Espaço O(1)."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == alvo:
            return mid
        elif nums[mid] < alvo:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def busca_binaria_recursiva(nums: list[int], alvo: int, left: int, right: int) -> int:
    """Busca Binária Recursiva: Tempo O(log n), Espaço O(log n) de Call Stack."""
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if nums[mid] == alvo:
        return mid
    elif nums[mid] < alvo:
        return busca_binaria_recursiva(nums, alvo, mid + 1, right)
    else:
        return busca_binaria_recursiva(nums, alvo, left, mid - 1)


def demonstrar_fundamentos_busca_binaria() -> None:
    print("\n--- 1. FUNDAMENTOS: Busca Binária Iterativa vs Recursiva ---")
    dados_ordenados = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    alvo = 70

    idx_it = busca_binaria_iterativa(dados_ordenados, alvo)
    idx_rec = busca_binaria_recursiva(dados_ordenados, alvo, 0, len(dados_ordenados) - 1)

    print(f"Lista Ordenada: {dados_ordenados}")
    print(f"Alvo {alvo} encontrado na posição (Iterativo): {idx_it}")
    print(f"Alvo {alvo} encontrado na posição (Recursivo): {idx_rec}")


# ==========================================================
# 3. COMPARATIVO DE PERFORMANCE: BUSCA LINEAR VS BINÁRIA
# ==========================================================
def demonstrar_benchmark() -> None:
    print("\n--- 2. BENCHMARK: Busca Linear O(n) vs Busca Binária O(log n) ---")
    tamanho = 10_000_000
    grande_lista = list(range(tamanho))
    alvo = 9_999_999

    # Busca Linear O(n)
    t0 = time.perf_counter()
    _ = alvo in grande_lista
    t1 = time.perf_counter()
    tempo_linear = (t1 - t0) * 1000

    # Busca Binária O(log n)
    t0 = time.perf_counter()
    _ = busca_binaria_iterativa(grande_lista, alvo)
    t1 = time.perf_counter()
    tempo_binaria = (t1 - t0) * 1000

    print(f"Busca Linear  (10 milhões itens) [O(n)]    : {tempo_linear:.2f} ms")
    print(f"Busca Binária (10 milhões itens) [O(log n)]: {tempo_binaria:.4f} ms (Milhares de vezes mais rápido!)")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: MÓDULO BISECT
# ==========================================================
def demonstrar_modulo_bisect() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Módulo bisect em Python ---")

    # Módulo nativo bisect para manter listas ordenadas eficientemente
    precos_ordenados = [10.0, 25.0, 50.0, 100.0]

    # Encontra o ponto de inserção para manter a ordem
    pos = bisect.bisect_left(precos_ordenados, 30.0)
    print(f"Preço R$ 30.0 deve ser inserido na posição {pos} da lista {precos_ordenados}")

    bisect.insort(precos_ordenados, 30.0)
    print(f"Lista após insort(): {precos_ordenados}")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades na Busca Binária:
- Tempo (Pior Caso e Caso Médio): O(log n). Para 1.000.000 de elementos, exige apenas ~20 comparações!
- Tempo (Melhor Caso): O(1) quando o elemento está no exato meio.
- Espaço Iterativo: O(1) de variáveis locais.
- Espaço Recursivo: O(log n) de pilha de chamadas (Call Stack).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é 'Busca Binária no Espaço de Respostas' (Binary Search on Answer Range)?"
A: "É uma técnica avançada de solução de problemas de otimização onde o domínio da solução é contínuo e ordenado.
    Em vez de buscar um elemento em uma lista de dados, fazemos a busca binária sobre o intervalo de posssíveis RESPOSTAS numéricas (ex: 'Qual o menor tempo necessário para processar N tarefas?').
    Testa-se a viabilidade do valor `mid`: se for possível processar, tenta-se um valor menor (`right = mid - 1`); se não for possível, aumenta-se a busca (`left = mid + 1`). Reduz a complexidade de O(N) para O(log N)."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função que encontre a primeira e a última ocorrência de um número em uma lista ordenada com duplicatas usando Busca Binária.
# Exercício 2 (Intermediário): Implemente a função `raiz_quadrada_inteira(n: int) -> int` que calcula a raiz quadrada inteira de N usando Busca Binária sem usar `math.sqrt`.
# Exercício 3 (Desafio / Entrevista): Dada uma lista de inteiros que foi rotacionada em um ponto desconhecido (ex: `[4, 5, 6, 7, 0, 1, 2]`), encontre o menor elemento em O(log n).


def main() -> None:
    print("==========================================================")
    print("  AULA 77: BUSCA BINÁRIA (BINARY SEARCH) E DIVISÃO E CONQUISTA")
    print("==========================================================")
    demonstrar_fundamentos_busca_binaria()
    demonstrar_benchmark()
    demonstrar_modulo_bisect()
    print("\n[Concluido] Arquivo 77 executado com sucesso.")


if __name__ == "__main__":
    main()
