"""
72_arrays_lists.py - Arrays Dinâmicos, Operações em Listas, Two Pointers e Sliding Window

Objetivos:
1. Compreender a estrutura interna de `list` em Python (Arrays Dinâmicos baseados em vetores contíguos de ponteiros em C).
2. Analisar os custos assintóticos de operações em listas (`append`, `insert`, `pop`, `remove`, `indexing`).
3. Dominar a técnica de Algoritmos com Dois Ponteiros (Two Pointers) para resolução de problemas lineares.
4. Dominar a técnica de Janela Deslizante (Sliding Window) para busca de sub-intervalos em O(N).
5. Resolver problemas clássicos de entrevista (Inversão in-place, Maior Soma de Subarray Fixo).
"""

import time
from typing import Any


# ==========================================================
# 1. CONCEITO E ESTRUTURA INTERNA DA LIST PYTHON
# ==========================================================
"""
O que é uma list em Python?
Em Python, o tipo `list` e implementado internamente no CPython como um Array Dinâmico (Dynamic Array) de ponteiros.

Estrutura de Memória (CPython `PyListObject`):
- Os elementos são armazenados em um bloco contíguo de memória RAM que guarda os endereços (ponteiros) para os objetos.
- Como é contíguo, o acesso por índice (`lista[i]`) é instantâneo: O(1) de tempo.
- Re-alocação de Tamanho (Over-allocation):
  Quando a lista fica cheia, o CPython aloca um novo bloco maior de memória com folga (crescimento ~1.125x)
  e copia os ponteiros anteriores. Por isso, a inserção no final (`.append()`) é O(1) AMORTIZADO.

Custos Assintóticos de Operações em list:
- Acesso por Índice `lista[i]`: O(1)
- Alterar valor `lista[i] = x`: O(1)
- Inserir no final `lista.append(x)`: O(1) amortizado
- Remover do final `lista.pop()`: O(1)
- Inserir no início `lista.insert(0, x)`: O(n) (precisa deslocar N ponteiros para a direita na RAM!)
- Remover do início `lista.pop(0)`: O(n) (precisa deslocar N ponteiros para a esquerda na RAM!)
- Busca de elemento `x in lista`: O(n)
"""


# ==========================================================
# 2. TÉCNICA 1: TWO POINTERS (PONTEIROS DUPLOS)
# ==========================================================
"""
O que é a técnica Two Pointers?
Utiliza dois índices (ponteiros) navegando pela mesma sequência.
Aplicações Típicas:
- Um ponteiro no início (`left = 0`) e outro no fim (`right = len - 1`) convergindo ao centro.
- Usado para inverter arrays in-place, buscar pares em coleções ordenadas, verificar palíndromos.
"""


def inverter_array_inplace(nums: list[int]) -> None:
    """Inverte um array in-place usando Two Pointers em O(n) tempo e O(1) espaço."""
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def demonstrar_two_pointers() -> None:
    print("\n--- 1. TÉCNICA: Two Pointers (Inversão In-Place) ---")
    dados = [1, 2, 3, 4, 5]
    print(f"Original: {dados}")
    inverter_array_inplace(dados)
    print(f"Invertido in-place: {dados}")


# ==========================================================
# 3. TÉCNICA 2: SLIDING WINDOW (JANELA DESLIZANTE)
# ==========================================================
"""
O que é a técnica Sliding Window?
Transforma dois loops aninhados O(n²) em um único loop O(n) ao deslizar um intervalo (janela) sobre o array.

Problema Clássico: Encontrar a MAIOR SOMA de um sub-array contínuo de tamanho fixo K.
- Solução Naive: Para cada elemento i, calcula a soma dos K elementos seguintes -> O(N * K).
- Solução Sliding Window: Calcula a soma dos primeiros K elementos. Ao deslizar a janela para a direita,
  SUBTRAI o elemento que saiu e SOMA o novo elemento que entrou -> O(N) tempo e O(1) espaço!
"""


def maior_soma_subarray_k_naive(nums: list[int], k: int) -> int:
    """Solução Naive: O(N * K) Tempo."""
    max_soma = -float("inf")
    n = len(nums)
    for i in range(n - k + 1):
        soma_atual = sum(nums[i : i + k])
        if soma_atual > max_soma:
            max_soma = soma_atual
    return int(max_soma)


def maior_soma_subarray_k_sliding_window(nums: list[int], k: int) -> int:
    """Solução Otimizada Sliding Window: O(N) Tempo, O(1) Espaço."""
    n = len(nums)
    if n < k:
        return 0

    # 1. Calcula a soma da primeira janela
    soma_janela = sum(nums[:k])
    max_soma = soma_janela

    # 2. Desliza a janela do índice k até n
    for i in range(k, n):
        # Subtrai o elemento que saiu à esquerda (i - k) e adiciona o novo (i)
        soma_janela += nums[i] - nums[i - k]
        if soma_janela > max_soma:
            max_soma = soma_janela

    return max_soma


def demonstrar_sliding_window() -> None:
    print("\n--- 2. TÉCNICA: Sliding Window (Maior Soma de Subarray K) ---")
    array_teste = [2, 1, 5, 1, 3, 2, 9, 1]
    k = 3

    res_naive = maior_soma_subarray_k_naive(array_teste, k)
    res_window = maior_soma_subarray_k_sliding_window(array_teste, k)

    print(f"Array: {array_teste} | K={k}")
    print(f"Maior Soma Naive   O(N*K): {res_naive}")
    print(f"Maior Soma Window O(N)   : {res_window}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class BufferMovelMetricasBackend:
    """Processador de métricas de tráfego usando Sliding Window."""

    def __init__(self, tamanho_janela_segundos: int) -> None:
        self.k = tamanho_janela_segundos

    def calcular_pico_trafego(self, requisicoes_por_segundo: list[int]) -> int:
        return maior_soma_subarray_k_sliding_window(requisicoes_por_segundo, self.k)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Detector de Pico de Tráfego ---")
    reqs_seg = [10, 20, 15, 100, 250, 300, 40, 50]  # reqs por seg
    processor = BufferMovelMetricasBackend(tamanho_janela_segundos=3)
    pico = processor.calcular_pico_trafego(reqs_seg)
    print(f"Pico maximo de reqs em janela de 3 segundos: {pico} requisições")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades:
- Inversão de Array com Two Pointers: Tempo O(N), Espaço O(1) in-place.
- Busca de Subarray com Sliding Window: Tempo O(N), Espaço O(1).
- Operação `.pop(0)` em lista tradicional: Tempo O(N) (Evite! Use `collections.deque` para O(1)).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que a operação `lista.insert(0, valor)` ou `lista.pop(0)` e O(N) enquanto `lista.append(valor)` e O(1) amortizado em Python?"
A: "Em CPython, o tipo `list` e alocado contiguamente na memória RAM.
    Ao inserir ou remover um elemento no índice 0 (início do array), todos os N elementos restantes precisam ser fisicamente deslocados uma posição para a direita ou esquerda no bloco de memória do SO, resultando em O(N).
    Já o `.append()` insere no final do bloco reservado, utilizando a margem de over-allocation pré-alocada pelo CPython, garantindo custo O(1) amortizado."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função `is_palindromo_array(texto: str) -> bool` usando a técnica Two Pointers (left e right).
# Exercício 2 (Intermediário): Implemente a função `mover_zeros_para_o_final(nums: list[int]) -> None` que move todos os zeros de um array para o final mantendo a ordem dos não-zeros in-place em O(N).
# Exercício 3 (Desafio / Entrevista): Dada uma lista de inteiros positivos e um valor S, encontre o comprimento mínimo de um subarray contínuo cuja soma seja maior ou igual a S utilizando Sliding Window de tamanho dinâmico.


def main() -> None:
    print("==========================================================")
    print("  AULA 72: ARRAYS DINÂMICOS, TWO POINTERS E SLIDING WINDOW")
    print("==========================================================")
    demonstrar_two_pointers()
    demonstrar_sliding_window()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 72 executado com sucesso.")


if __name__ == "__main__":
    main()
