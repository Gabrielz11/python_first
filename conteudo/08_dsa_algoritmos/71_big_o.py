"""
71_big_o.py - Guia Definitivo de Análise de Complexidade de Algoritmos (Notação Big O)

Objetivos:
1. Dominar os fundamentos teóricos e práticos de Análise de Complexidade de Algoritmos (Tempo e Espaço).
2. Compreender a notação Big O para expressar a taxa de Crescimento Assintótico no Pior Caso (Worst-Case).
3. Entender o porquê constantes e termos de menor ordem são descartados na análise assintótica.
4. Analisar as principais classes de complexidade: O(1), O(log n), O(n), O(n log n), O(n²), O(2^n) e O(n!).
5. Comparar estruturas nativas de Python (list vs dict vs set) e algoritmos clássicos (Busca Linear vs Busca Binária).
"""

import math
import time
from typing import Any


# ==========================================================
# 1. CONCEITO E FUNDAMENTOS DE ANÁLISE DE COMPLEXIDADE
# ==========================================================
"""
1. O que é Análise de Complexidade?
Análise de complexidade é o estudo teórico de quanto tempo de CPU e quanta memória RAM um algoritmo consome
à medida que o tamanho dos dados de entrada (representado pela letra 'N') cresce tendendo ao infinito.

2. Por que usamos a Notação Big O?
Não medimos a eficiência de um algoritmo apenas em segundos com um cronômetro, pois o tempo em segundos varia conforme o hardware, SO e carga de CPU.
A notação Big O mede a TAXA DE CRESCIMENTO do trabalho de forma independente da máquina.

3. Crescimento Assintótico:
Mede o comportamento do algoritmo para valores gigantescos de N (limite assintótico).

4. Por que constantes e termos de menor ordem são descartados?
- No Big O, 2N + 100 se reduz a O(N), pois para N = 1.000.000, o termo N domina completamente o comportamento e a constante 2 ou 100 se torna irrelevante.
- O(N² + 5N + 1000) se reduz a O(N²).

Hierarquia de Crescimento Assintótico (Do mais rápido ao mais lento):
    O(1) [Constante]
      ↓
    O(log n) [Logarítmico]
      ↓
    O(n) [Linear]
      ↓
    O(n log n) [Linearítmico / Quasilinear]
      ↓
    O(n²) [Quadrático]
      ↓
    O(2^n) [Exponencial]
      ↓
    O(n!) [Fatorial]

Diferença entre Pior Caso, Caso Médio e Melhor Caso:
- Big O (O): Pior Caso (Upper Bound - Limite Superior de tempo). É o que nos dá garantias de engenharia.
- Big Theta (Θ): Caso Médio (Tight Bound).
- Big Omega (Ω): Melhor Caso (Lower Bound - Limite Inferior).
"""


# ==========================================================
# 2. AS CLASSES DE COMPLEXIDADE COM CÓDIGO E EXPLICAÇÃO
# ==========================================================
# 1. O(1) - Complexidade Constante
def exemplo_o_1(lista: list[int]) -> int:
    """Acesso direto por índice em uma lista: O(1) Tempo, O(1) Espaço."""
    return lista[0] if lista else 0


# 2. O(log n) - Complexidade Logarítmica (Divisão pela metade a cada passo)
def exemplo_o_log_n(lista_ordenada: list[int], alvo: int) -> int:
    """Busca Binária: A cada iteração o espaço de busca e reduzido pela metade. O(log n) Tempo, O(1) Espaço."""
    inicio = 0
    fim = len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


# 3. O(n) - Complexidade Linear
def exemplo_o_n(lista: list[int]) -> int:
    """Busca Linear / Soma acumulada: Percorre N elementos 1 vez. O(n) Tempo, O(1) Espaço."""
    soma = 0
    for num in lista:  # Loop de 1 ate N
        soma += num
    return soma


# 4. O(n log n) - Complexidade Linearítmica
def exemplo_o_n_log_n(lista: list[int]) -> list[int]:
    """Ordenação Timsort / MergeSort em Python: O(n log n) Tempo, O(n) Espaço."""
    return sorted(lista)


# 5. O(n²) - Complexidade Quadrática (Loops Aninhados)
def exemplo_o_n_quadrado(lista: list[int]) -> list[tuple[int, int]]:
    """Pares de elementos (Loops Aninhados N x N): O(n²) Tempo, O(n²) Espaço."""
    pares = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            pares.append((lista[i], lista[j]))
    return pares


# 6. O(2^n) - Complexidade Exponencial
def exemplo_o_2_n(n: int) -> int:
    """Fibonacci Recursivo Ingênuo: Duplica as chamadas a cada nivel. O(2^n) Tempo, O(n) Espaço (Call Stack)."""
    if n <= 1:
        return n
    return exemplo_o_2_n(n - 1) + exemplo_o_2_n(n - 2)


# 7. O(n!) - Complexidade Fatorial
def exemplo_o_n_fatorial(lista: list[str]) -> list[tuple[str, ...]]:
    """Permutações de todos os elementos: O(n!) Tempo, O(n!) Espaço."""
    import itertools
    return list(itertools.permutations(lista))


def demonstrar_classes_complexidade() -> None:
    print("\n--- 1. FUNDAMENTOS: Classes de Complexidade Big O ---")
    dados = list(range(100))
    print(f"O(1) - Acesso direto: {exemplo_o_1(dados)}")
    print(f"O(log n) - Busca binaria do 75: indice {exemplo_o_log_n(dados, 75)}")
    print(f"O(n) - Soma linear: {exemplo_o_n(dados[:10])}")


# ==========================================================
# 3. REGRAS DE ANÁLISE DE CÓDIGO (COMO ANALISAR LOOPS)
# ==========================================================
"""
Regras Práticas para Calcular o Big O do seu Código:
1. Operações Consecutivas (Soma): Somam-se as complexidades -> O(A + B).
   Exemplo: Loop N seguido de Loop M = O(N + M). Se N == M, O(2N) = O(N).
2. Loops Aninhados (Multiplicação): Multiplicam-se as complexidades -> O(A * B).
   Exemplo: Loop de N contendo Loop de M = O(N * M). Se N == M, O(N²).
3. Divisão do Problema: Qualquer algoritmo que divide o problema pela metade a cada passo tem fator logarítmico O(log N).
"""


# ==========================================================
# 4. TABELA DE COMPLEXIDADE DAS ESTRUTURAS NATIVAS EM PYTHON
# ==========================================================
"""
Complexidade das Operações nas Estruturas de Dados Nativas em Python (CPython):

+-------------------+----------------+----------------+----------------+
| Operação          | list           | dict           | set            |
+-------------------+----------------+----------------+----------------+
| Indexação [i]     | O(1)           | O(1)           | N/A            |
| Busca (x in C)    | O(n)           | O(1) médio     | O(1) médio     |
| Inserção          | O(1) amort.    | O(1) médio     | O(1) médio     |
| Inserção no Meio  | O(n)           | N/A            | N/A            |
| Remoção           | O(n)           | O(1) médio     | O(1) médio     |
| Tamanho len()     | O(1)           | O(1)           | O(1)           |
+-------------------+----------------+----------------+----------------+
"""


def demonstrar_comparativo_estruturas() -> None:
    print("\n--- 2. COMPARATIVO PRÁTICO: Busca em list vs set (O(n) vs O(1)) ---")

    tamanho = 100_000
    lista_grande = list(range(tamanho))
    set_grande = set(range(tamanho))
    alvo = 99_999  # Pior caso de busca

    # Busca em list: O(n)
    t0 = time.perf_counter()
    _ = alvo in lista_grande
    t1 = time.perf_counter()
    tempo_lista = (t1 - t0) * 1000

    # Busca em set: O(1)
    t0 = time.perf_counter()
    _ = alvo in set_grande
    t1 = time.perf_counter()
    tempo_set = (t1 - t0) * 1000

    print(f"Busca de {alvo} em list (O(n)): {tempo_lista:.4f} ms")
    print(f"Busca de {alvo} em set  (O(1)): {tempo_set:.4f} ms (Centenas de vezes mais rápido!)")


# ==========================================================
# 5. EXEMPLO PRÁTICO: SOLUÇÃO NAIVE O(N²) VS OTIMIZADA O(N)
# ==========================================================
# Problema: Verificar se existem dois números em uma lista cuja soma seja igual a um Alvo (Two Sum).

# Solução Naive / Ingênua: Loops Aninhados -> O(n²) Tempo, O(1) Espaço
def two_sum_naive(nums: list[int], target: int) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


# Solução Otimizada: Hash Map -> O(n) Tempo, O(n) Espaço
def two_sum_otimizado(nums: list[int], target: int) -> tuple[int, int] | None:
    vistos: dict[int, int] = {}  # valor -> indice
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in vistos:
            return (vistos[complemento], i)
        vistos[num] = i
    return None


def demonstrar_two_sum_benchmark() -> None:
    print("\n--- 3. EXEMPLO PRÁTICO: Naive O(n²) vs Otimizado O(n) ---")
    nums = list(range(1, 2000))
    target = 3997

    t0 = time.perf_counter()
    res1 = two_sum_naive(nums, target)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    res2 = two_sum_otimizado(nums, target)
    t3 = time.perf_counter()

    print(f"Solução Naive O(n²): Resultado {res1} em {(t1 - t0)*1000:.2f} ms")
    print(f"Solução Otimizada O(n): Resultado {res2} em {(t3 - t2)*1000:.4f} ms")


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTA TÉCNICA
# ==========================================================
"""
Perguntas Comuns de Entrevista Técnica:

Q1: "Por que a notação Big O descarta constantes como em O(2N) -> O(N)?"
A1: "Porque o Big O mede a TAXA DE CRESCIMENTO assintótica quando N tende ao infinito.
     Para N imensamente grande, o crescimento proporcional é linear N em ambos os casos.
     Constantes dependem do hardware e do interpretador, enquanto Big O foca no comportamento do algoritmo."

Q2: "Qual a diferença entre complexidade de tempo e complexidade de espaço?"
A2: "Complexidade de tempo mede o número de operações computacionais executadas.
     Complexidade de espaço mede a quantidade de memória RAM adicional alocada pelo algoritmo (excluindo a entrada original)."

Q3: "O que é o Trade-off Tempo vs Memória (Time-Memory Tradeoff)?"
A3: "É a estratégia de gastar mais memória RAM (alocando Hash Maps/Sets adicionais) para reduzir drasticamente o tempo de execução de um algoritmo de O(N²) para O(N), como demonstrado no problema Two Sum."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Calcule a complexidade de tempo e espaço de um código que percorre uma matriz N x N imprimindo seus elementos.
# Exercício 2 (Intermediário): Escreva uma função que encontre se há elementos duplicados em uma lista comparando a solução O(N²) (loops aninhados) com a solução O(N) usando `set`.
# Exercício 3 (Desafio / Entrevista): Implemente a Busca Binária iterativa e explique por que a sua complexidade espacial é O(1), enquanto na versão recursiva é O(log N) devido à Call Stack.


def main() -> None:
    print("==========================================================")
    print("  AULA 71: GUIA DEFINITIVO DE ANÁLISE DE COMPLEXIDADE BIG O")
    print("==========================================================")
    demonstrar_classes_complexidade()
    demonstrar_comparativo_estruturas()
    demonstrar_two_sum_benchmark()
    print("\n[Concluido] Arquivo 71 executado com sucesso.")


if __name__ == "__main__":
    main()
