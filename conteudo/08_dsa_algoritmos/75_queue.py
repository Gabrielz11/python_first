"""
75_queue.py - Fila (Queue), FIFO, Ineficiência de list.pop(0) e Otimização com collections.deque

Objetivos:
1. Dominar o funcionamento da Estrutura de Dados Fila (Queue) fundamentada no princípio FIFO (First-In, First-Out).
2. Compreender por que `list.pop(0)` e ineficiente em Python (O(n) de complexidade temporal).
3. Utilizar a estrutura nativa otimizada `collections.deque` para operações de Fila em O(1) constante (`append` e `popleft`).
4. Implementar um Worker de Fila de Tarefas (Task Queue Processor) assíncrono simulado no backend.
5. Inspecionar as complexidades de tempo e espaço de filas de alta performance.
"""

from collections import deque
import time
from typing import Any


# ==========================================================
# 1. CONCEITO DA ESTRUTURA FILA (QUEUE)
# ==========================================================
"""
O que é uma Fila (Queue)?
Uma Fila é uma estrutura de dados linear baseada no princípio FIFO (First-In, First-Out):
O PRIMEIRA elemento a ser inserido na fila e o PRIMEIRO elemento a ser removido (como uma fila de banco).

Operações Fundamentais da Fila:
- `enqueue(item)`: Adiciona um elemento ao final da fila (Tail/Rear).
- `dequeue()`: Remove e retorna o elemento do início da fila (Head/Front).
- `peek()`: Consulta o elemento do início sem removê-lo.
- `is_empty()`: Verifica se a fila está vazia.

Por que `list.pop(0)` e um ANTIPADRÃO em Python?
- Em listas nativas (`list`), remover o primeiro elemento (`lista.pop(0)`) obriga o CPython a deslocar TODOS os N-1 elementos restantes
  uma posição para a esquerda na memória RAM.
- Complexidade de `list.pop(0)`: O(n) TEMPO! Em loops de milhares de itens, a aplicação trava.
- Solução: Utilizar `collections.deque` (Doubly Ended Queue), implementada em C como uma lista duplamente encadeada de blocos de memória,
  garantindo `append()` e `popleft()` em O(1) TEMPO CONSTANTE!
"""


# ==========================================================
# 2. SINTAXE E COMPARATIVO: LIST VS COLLECTIONS.DEQUE
# ==========================================================
def demonstrar_ineficiencia_list_vs_deque() -> None:
    print("\n--- 1. FUNDAMENTOS: Benchmark list.pop(0) vs deque.popleft() ---")

    tamanho = 100_000

    # 1. Fila ineficiente com list (O(n) por pop)
    fila_lista = list(range(tamanho))
    t0 = time.perf_counter()
    while fila_lista:
        _ = fila_lista.pop(0)  # O(n) cada pop!
    t1 = time.perf_counter()
    tempo_list = (t1 - t0) * 1000

    # 2. Fila eficiente com collections.deque (O(1) por popleft)
    fila_deque = deque(range(tamanho))
    t0 = time.perf_counter()
    while fila_deque:
        _ = fila_deque.popleft()  # O(1) constante!
    t1 = time.perf_counter()
    tempo_deque = (t1 - t0) * 1000

    print(f"Desempilhar {tamanho} itens com list.pop(0)    [O(n)]: {tempo_list:.2f} ms")
    print(f"Desempilhar {tamanho} itens com deque.popleft() [O(1)]: {tempo_deque:.2f} ms (Centenas de vezes mais rápido!)")


# ==========================================================
# 3. IMPLEMENTAÇÃO CONCEITUAL DE UMA FILA COM DEQUE
# ==========================================================
class FilaOtimizada:
    """Fila FIFO de alta performance envelopando collections.deque."""

    def __init__(self) -> None:
        self._elementos: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Enfileirar elemento no final O(1)."""
        self._elementos.append(item)

    def dequeue(self) -> Any:
        """Desenfileirar elemento do início O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._elementos.popleft()

    def peek(self) -> Any:
        """Consultar início O(1)."""
        if self.is_empty():
            return None
        return self._elementos[0]

    def is_empty(self) -> bool:
        return len(self._elementos) == 0

    def __len__(self) -> int:
        return len(self._elementos)


def demonstrar_fila_otimizada() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: FilaOtimizada com deque ---")

    fila = FilaOtimizada()
    fila.enqueue("Cliente A")
    fila.enqueue("Cliente B")
    fila.enqueue("Cliente C")

    print(f"Primeiro da fila (peek): {fila.peek()}")
    print(f"Atendendo (dequeue): {fila.dequeue()}")
    print(f"Próximo a ser atendido (peek): {fila.peek()}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class TaskQueueWorkerBackend:
    """Fila de tarefas de segundo plano (Job Queue) para serviços web."""

    def __init__(self) -> None:
        self.queue = FilaOtimizada()

    def agendar_job(self, job_id: str, payload: dict[str, Any]) -> None:
        print(f"  [Enqueue Job] Agendando job '{job_id}' na fila...")
        self.queue.enqueue({"id": job_id, "payload": payload})

    def processar_proximo_job(self) -> bool:
        if self.queue.is_empty():
            print("  [Worker] Fila vazia. Nenhum job pendente.")
            return False

        job = self.queue.dequeue()
        print(f"  [Worker Processing] Executando Job ID '{job['id']}'...")
        return True


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Task Queue Worker ---")
    worker_queue = TaskQueueWorkerBackend()

    worker_queue.agendar_job("JOB-EMAIL-101", {"to": "user1@empresa.com"})
    worker_queue.agendar_job("JOB-PDF-102", {"report_id": 50})

    worker_queue.processar_proximo_job()
    worker_queue.processar_proximo_job()


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Fila (collections.deque):
- Enqueue (`deque.append()`): Tempo O(1), Espaço O(1).
- Dequeue (`deque.popleft()`): Tempo O(1), Espaço O(1).
- Peek (`deque[0]`): Tempo O(1), Espaço O(1).
- Busca de Elemento em Deque (`x in deque`): Tempo O(N).
- Espaço Total da Estrutura: O(N).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que você deve usar `collections.deque` em vez de `list` quando precisa de uma estrutura do tipo Fila em Python?"
A: "Em Python, o tipo nativo `list` e alocado como um array contíguo de memória.
    Remover o primeiro elemento de uma lista (`lista.pop(0)`) possui complexidade de tempo O(N), pois exige o deslocamento de todos os N-1 elementos restantes no bloco de memória.
    Já o `collections.deque` e uma estrutura de lista duplamente encadeada em C, permitindo que a adição ou remoção de elementos em ambas as pontas (`append` e `popleft`) seja executada em tempo O(1) constante."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Crie uma fila usando `collections.deque`, enfileire 5 nomes de processos e desmesfileire 2 deles imprimindo o estado atual.
# Exercício 2 (Intermediário): Implemente um buffer circular fixo usando `collections.deque(maxlen=3)` e observe o que acontece ao adicionar um 4º elemento.
# Exercício 3 (Desafio / Entrevista): Implemente a estrutura de dados Fila utilizando APENAS duas Pilhas (`list.append` e `list.pop`).


def main() -> None:
    print("==========================================================")
    print("  AULA 75: ESTRUTURA DE DADOS FILA (QUEUE) E COLLECTIONS.DEQUE")
    print("==========================================================")
    demonstrar_ineficiencia_list_vs_deque()
    demonstrar_fila_otimizada()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 75 executado com sucesso.")


if __name__ == "__main__":
    main()
