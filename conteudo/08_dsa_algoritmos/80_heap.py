"""
80_heap.py - Min-Heap, Fila de Prioridade (Priority Queue) e o Módulo heapq

Objetivos:
1. Dominar a Estrutura de Dados Heap (Min-Heap e Max-Heap) e Filas de Prioridade (Priority Queue).
2. Compreender a representação vetorial (Array) de uma Árvore Binária Completa.
3. Utilizar as funções do módulo nativo `heapq`: `heappush`, `heappop`, `heapify`, `nlargest`, `nsmallest`.
4. Analisar por que `heapq.heapify()` constrói um Heap em tempo O(n) linear (e não O(n log n)).
5. Resolver o problema clássico de entrevista: Encontrar os K maiores elementos (Top K).
"""

import heapq
import random
from typing import Any


# ==========================================================
# 1. CONCEITO DE HEAP E FILA DE PRIORIDADE
# ==========================================================
"""
O que é um Heap?
Um Heap e uma Árvore Binária Completa especial que satisfaz a Propriedade de Heap (Heap Property):
- Min-Heap: O valor de qualquer nó pai e SEMPRE menor ou igual ao valor de seus filhos. A RAIZ e o MENOR elemento de todos (`heap[0]`).
- Max-Heap: O valor de qualquer nó pai e SEMPRE maior ou igual ao valor de seus filhos. A RAIZ e o MAIOR elemento de todos.

Representação em Array de um Heap (Mapeamento de Índices):
Em vez de usar nós e ponteiros, o Heap e armazenado em uma simples lista contígua `list`:
- Para um nó no índice `i`:
  - Filho Esquerdo: `2 * i + 1`
  - Filho Direito: `2 * i + 2`
  - Nó Pai: `(i - 1) // 2`

Módulo `heapq` em Python:
O módulo `heapq` implementa um Min-Heap nativo operando sobre listas normais em Python.
Para simular um Max-Heap com `heapq`, multiplica-se os valores por `-1` ao inserir e retirar!
"""


# ==========================================================
# 2. SINTAXE E OPERAÇÕES COM HEAPQ
# ==========================================================
def demonstrar_operacoes_heapq() -> None:
    print("\n--- 1. FUNDAMENTOS: Operações básicas com heapq ---")

    # 1. Criando um heap do zero
    heap_min: list[int] = []
    heapq.heappush(heap_min, 40)
    heapq.heappush(heap_min, 10)
    heapq.heappush(heap_min, 30)
    heapq.heappush(heap_min, 5)

    print(f"Heap Min interno em lista: {heap_min}")
    print(f"Menor elemento no topo (O(1)): {heap_min[0]}")

    # Retirando elementos em ordem crescente (Priority Queue)
    menor = heapq.heappop(heap_min)  # O(log n)
    print(f"Elemento removido (heappop): {menor}")
    print(f"Novo menor no topo: {heap_min[0]}")

    # 2. Convertendo uma lista desordenada em Heap em O(n) via heapify()
    dados_desordenados = [90, 20, 50, 10, 80, 5]
    heapq.heapify(dados_desordenados)  # Transforma in-place em O(n)
    print(f"Lista transformada com heapify() O(n): {dados_desordenados}")


# ==========================================================
# 3. PROBLEMA CLÁSSICO DE ENTREVISTA: TOP K ELEMENTOS
# ==========================================================
"""
Problema: Encontrar os K maiores elementos de uma lista desordenada contendo N itens.

Abordagens:
1. Ordenar a lista toda com `sorted(nums)` e pegar os últimos K elementos -> Tempo O(N log N).
2. Manter um Min-Heap de tamanho fixo K contendo os maiores elementos -> Tempo O(N log K), Espaço O(K).
   (Quando N e de 1.000.000 e K e 10, O(N log K) e infinitamente mais eficiente!).
"""


def top_k_maiores_elementos(nums: list[int], k: int) -> list[int]:
    """Retorna os K maiores elementos mantendo um Min-Heap de tamanho K."""
    min_heap: list[int] = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Descarta o menor elemento do grupo Top K

    return sorted(min_heap, reverse=True)


def demonstrar_top_k() -> None:
    print("\n--- 2. PROBLEMA CLÁSSICO: Top K Maiores Elementos ---")
    nums = [3, 2, 1, 5, 6, 4, 10, 8, 7, 9]
    k = 3

    top_k = top_k_maiores_elementos(nums, k)
    top_k_nativo = heapq.nlargest(k, nums)

    print(f"Lista Original: {nums}")
    print(f"Os {k} maiores via Min-Heap O(N log K): {top_k}")
    print(f"Os {k} maiores via heapq.nlargest(): {top_k_nativo}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: SCHEDULER DE TAREFAS
# ==========================================================
class TaskPriorityScheduler:
    """Escalonador de tarefas por prioridade utilizando Fila de Prioridade."""

    def __init__(self) -> None:
        self.heap: list[tuple[int, str]] = []

    def agendar_tarefa(self, prioridade: int, nome_tarefa: str) -> None:
        # Menor número = Maior prioridade (ex: 1 e Alta Prioridade, 10 e Baixa)
        heapq.heappush(self.heap, (prioridade, nome_tarefa))

    def executar_proxima_tarefa(self) -> tuple[int, str] | None:
        if not self.heap:
            return None
        return heapq.heappop(self.heap)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Task Priority Scheduler ---")
    scheduler = TaskPriorityScheduler()

    scheduler.agendar_tarefa(3, "Enviar Email Batch")
    scheduler.agendar_tarefa(1, "Processar Pagamento Urgente (VIP)")
    scheduler.agendar_tarefa(2, "Gerar Relatório em PDF")

    exec1 = scheduler.executar_proxima_tarefa()
    exec2 = scheduler.executar_proxima_tarefa()

    print(f"  1ª Tarefa executada (Maior prioridade): {exec1}")
    print(f"  2ª Tarefa executada (Segunda prioridade): {exec2}")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Heaps:
- `heappush(heap, item)`: Tempo O(log n), Espaço O(1).
- `heappop(heap)`: Tempo O(log n), Espaço O(1).
- `heapify(lista)`: Tempo O(n) [Matematicamente O(n) através de Sift-Down], Espaço O(1) in-place.
- Obter Menor Elemento (`heap[0]`): Tempo O(1).
- Espaço Total: O(N).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que o algoritmo `heapify()` possui complexidade de tempo O(N) e não O(N log N)?"
A: "Porque o `heapify()` utiliza a abordagem bottom-up chamando a operação `sift-down` nos nós de baixo para cima.
    Os nós nas folhas (que representam N/2 da árvore) exigem 0 trocas. Os nós um nível acima exigem no máximo 1 troca, e apenas o nó raiz no topo exige log N trocas.
    A soma das séries geométricas de trocas resulta em um limite superior de exatamente 2N operações, provando matematicamente que o custo de construção e O(N) linear."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva um código que receba uma lista de inteiros e use `heapq` para ordená-la em ordem crescente (Heapsort).
# Exercício 2 (Intermediário): Implemente a simulação de um Max-Heap em Python invertendo os sinais numéricos dos elementos.
# Exercício 3 (Desafio / Entrevista): Escreva uma função que mescle K listas encadeadas ordenadas (Merge K Sorted Lists) em uma única lista ordenada usando um Min-Heap em O(N log K).


def main() -> None:
    print("==========================================================")
    print("  AULA 80: MIN-HEAP, FILA DE PRIORIDADE E O MÓDULO HEAPQ")
    print("==========================================================")
    demonstrar_operacoes_heapq()
    demonstrar_top_k()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 80 executado com sucesso.")


if __name__ == "__main__":
    main()
