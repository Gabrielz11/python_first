"""
76_linked_list.py - Lista Simplesmente Encadeada (Singly Linked List) e Inversão em O(n)

Objetivos:
1. Implementar nós (`Node`) e a estrutura de dados Lista Encadeada.
2. Inverter uma lista encadeada in-place em O(n) tempo e O(1) espaço.
"""

class Node:
    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.proximo: "Node | None" = None


def inverter_linked_list(head: Node | None) -> Node | None:
    anterior: Node | None = None
    atual = head
    while atual is not None:
        proximo_no = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo_no
    return anterior


def main() -> None:
    print("==========================================================")
    print("  AULA 76: LISTA ENCADEADA E INVERSÃO DE PONTEIROS")
    print("==========================================================")
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n1.proximo = n2
    n2.proximo = n3

    nova_cabeca = inverter_linked_list(n1)
    print(f"Nova cabeça da lista invertida: {nova_cabeca.valor if nova_cabeca else None}")
    print("\n[Concluido] Arquivo 76 executado com sucesso.")


if __name__ == "__main__":
    main()
