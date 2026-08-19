"""
76_linked_list.py - Listas Encadeadas (Singly Linked List), Nós, Operações e Comparação com Arrays

Objetivos:
1. Dominar a Estrutura de Dados Lista Encadeada Simples (Singly Linked List).
2. Compreender a anatomia de um Nó (`Node`) contendo valor e ponteiro `next`.
3. Implementar operações fundamentais: inserção no início/fim, remoção por valor e busca.
4. Comparar a eficiência assintótica entre Arrays Dinâmicos (`list`) e Listas Encadeadas (`LinkedList`).
5. Compreender o uso de Listas Encadeadas em estruturas avançadas (como LRU Cache e alocação de memória).
"""

from typing import Any


# ==========================================================
# 1. CONCEITO DE LISTA ENCADEADA (LINKED LIST)
# ==========================================================
"""
O que é uma Lista Encadeada (Linked List)?
Diferente de um Array Dinâmico (onde os elementos estão em posições de memória RAM contíguas),
uma Lista Encadeada e uma coleção de nós alocados de forma DISPERSA na memória RAM.

Componentes:
1. `Node` (Nó): Objeto contendo dois campos:
   - `data`: O valor armazenado.
   - `next`: Um ponteiro/referência para o próximo nó da lista (ou `None` se for o último).
2. `Head` (Cabeça): Ponteiro que marca o primeiro nó da lista encadeada.

Diferenças entre Array (`list`) e Linked List:
+------------------------+----------------+----------------+
| Operação               | Array (list)   | Linked List    |
+------------------------+----------------+----------------+
| Acesso por Índice [i]  | O(1)           | O(n)           |
| Inserção no Início     | O(n)           | O(1)           |
| Remoção no Início      | O(n)           | O(1)           |
| Inserção no Meio (no)  | O(n)           | O(1)           |
| Busca de Elemento      | O(n)           | O(n)           |
+------------------------+----------------+----------------+
"""


# ==========================================================
# 2. IMPLEMENTAÇÃO DO NÓ E DA LISTA ENCADEADA
# ==========================================================
class Node:
    """Nó individual da Lista Encadeada."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class SinglyLinkedList:
    """Implementação completa de Lista Encadeada Simples."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self._tamanho = 0

    def inserir_no_inicio(self, valor: Any) -> None:
        """Insere um novo elemento no início da lista (Head) em tempo O(1)."""
        novo_no = Node(valor)
        novo_no.next = self.head
        self.head = novo_no
        self._tamanho += 1

    def inserir_no_fim(self, valor: Any) -> None:
        """Insere um novo elemento no final da lista em tempo O(n)."""
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novo_no
        self._tamanho += 1

    def remover_por_valor(self, valor: Any) -> bool:
        """Remove o primeiro nó encontrado com o valor informado em tempo O(n)."""
        if self.head is None:
            return False

        # Se o nó a remover for o Head
        if self.head.data == valor:
            self.head = self.head.next
            self._tamanho -= 1
            return True

        atual = self.head
        while atual.next is not None and atual.next.data != valor:
            atual = atual.next

        if atual.next is not None:
            atual.next = atual.next.next
            self._tamanho -= 1
            return True

        return False

    def buscar(self, valor: Any) -> bool:
        """Busca se o valor está presente na lista em tempo O(n)."""
        atual = self.head
        while atual is not None:
            if atual.data == valor:
                return True
            atual = atual.next
        return False

    def to_list(self) -> list[Any]:
        """Converte a lista encadeada em uma lista Python para exibição."""
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(atual.data)
            atual = atual.next
        return elementos

    def __len__(self) -> int:
        return self._tamanho


def demonstrar_linked_list() -> None:
    print("\n--- 1. FUNDAMENTOS: Operações em SinglyLinkedList ---")

    lista = SinglyLinkedList()
    lista.inserir_no_inicio(20)
    lista.inserir_no_inicio(10)
    lista.inserir_no_fim(30)

    print(f"Lista atual: {lista.to_list()} (Tamanho: {len(lista)})")
    print(f"Buscar valor 20: {lista.buscar(20)}")

    lista.remover_por_valor(20)
    print(f"Lista após remover 20: {lista.to_list()}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: INVERSÃO DE LINKED LIST IN-PLACE
# ==========================================================
def inverter_linked_list(head: Node | None) -> Node | None:
    """Inverte os ponteiros de uma LinkedList in-place em O(n) tempo e O(1) espaço."""
    anterior: Node | None = None
    atual = head

    while atual is not None:
        proximo_no = atual.next  # Salva referência do próximo
        atual.next = anterior   # Inverte o ponteiro
        anterior = atual        # Avanca o anterior
        atual = proximo_no      # Avança o atual

    return anterior  # Novo Head


def demonstrar_inversao() -> None:
    print("\n--- 2. ALGORITMO CLÁSSICO: Inverter LinkedList In-Place ---")

    l = SinglyLinkedList()
    for v in [1, 2, 3, 4]:
        l.inserir_no_fim(v)

    print(f"Original : {l.to_list()}")
    l.head = inverter_linked_list(l.head)
    print(f"Invertida: {l.to_list()}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: LRU Cache e Listas Duplamente Encadeadas ---")
    print("  Listas Duplamente Encadeadas (Doubly LinkedList) com ponteiros prev e next")
    print("  são a base de implementação de LRU Caches (Least Recently Used) de altíssima performance!")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Singly LinkedList:
- Inserção / Remoção no Início (`Head`): Tempo O(1), Espaço O(1).
- Inserção / Remoção no Fim (sem ponteiro Tail): Tempo O(n), Espaço O(1).
- Busca por Valor ou Índice: Tempo O(n).
- Espaço Total da Estrutura: O(n) (com overhead de armazenar ponteiros adicionais em CPython).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como você detecta se existe um Ciclo/Loop em uma Lista Encadeada (Floyd's Cycle-Finding Algorithm / Tortoise and Hare)?"
A: "Utilizando dois ponteiros percorrendo a lista em velocidades diferentes:
    - Ponteiro Lento (Tartaruga): Avança 1 nó por passo (`lento = lento.next`).
    - Ponteiro Rápido (Lebre): Avança 2 nós por passo (`rapido = rapido.next.next`).
    Se houver um ciclo na lista, em algum momento o ponteiro rápido irá 'alcançar' o ponteiro lento e eles apontarão para o mesmo nó (`lento == rapido`), provando a existência do ciclo em O(N) tempo e O(1) espaço."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Implemente o método `inserir_no_indice(indice, valor)` na classe `SinglyLinkedList`.
# Exercício 2 (Intermediário): Escreva uma função que encontre o Nó do MEIO de uma Lista Encadeada em apenas UMA passagem (One Pass) usando dois ponteiros.
# Exercício 3 (Desafio / Entrevista): Implemente a função `mesclar_duas_listas_ordenadas(head1, head2)` que combine duas LinkedLists ordenadas em uma terceira ordenada.


def main() -> None:
    print("==========================================================")
    print("  AULA 76: LISTAS ENCADEADAS (LINKED LIST), NÓS E OPERAÇÕES")
    print("==========================================================")
    demonstrar_linked_list()
    demonstrar_inversao()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 76 executado com sucesso.")


if __name__ == "__main__":
    main()
