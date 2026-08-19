"""
75_queue.py - Estrutura de Dados Fila (Queue - FIFO)

Objetivos:
1. Implementar a estrutura de dados Fila (FIFO - First In, First Out) usando `collections.deque`.
"""

from collections import deque


class FilaAtendimento:
    def __init__(self) -> None:
        self._itens: deque[str] = deque()

    def enfileirar(self, item: str) -> None:
        self._itens.append(item)

    def desenfileirar(self) -> str:
        if not self._itens:
            raise IndexError("Fila vazia!")
        return self._itens.popleft()


def main() -> None:
    print("==========================================================")
    print("  AULA 75: FILA (QUEUE FIFO) COM COLLECTIONS.DEQUE")
    print("==========================================================")
    f = FilaAtendimento()
    f.enfileirar("Cliente 1")
    f.enfileirar("Cliente 2")
    print(f"Atendido com FIFO: {f.desenfileirar()}")
    print("\n[Concluido] Arquivo 75 executado com sucesso.")


if __name__ == "__main__":
    main()
