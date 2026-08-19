"""
79_trees.py - Árvores Binárias de Busca (BST) e Percursos (In-Order, Pre-Order, Post-Order, Level-Order)

Objetivos:
1. Dominar os conceitos de Árvores Binárias (Binary Trees) e Árvores Binárias de Busca (BST).
2. Compreender os componentes: Nó Raiz (Root), Filhos (Children), Folhas (Leaves), Altura e Profundidade.
3. Implementar a Árvore Binária de Busca com métodos de Inserção e Busca em O(log n) médio.
4. Dominar os 4 Percursos em Árvore: In-Order, Pre-Order, Post-Order e Level-Order (BFS).
5. Analisar a degradação de performance de uma BST desbalanceada para O(n).
"""

from collections import deque
from typing import Any


# ==========================================================
# 1. CONCEITO DE ÁRVORES E BINARY SEARCH TREES (BST)
# ==========================================================
"""
O que é uma Árvore Binária de Busca (BST)?
Uma Árvore e uma estrutura de dados hierárquica não-linear formada por Nós conectados por Arestas.

Invariante da BST (Binary Search Tree Property):
Para qualquer nó X na árvore:
- Todos os valores na sub-árvore ESQUERDA de X são estritamente MENORES que X.val.
- Todos os valores na sub-árvore DIREITA de X são estritamente MAIORES que X.val.

Terminologia:
- Raiz (Root): O nó no topo da árvore (sem pai).
- Folha (Leaf): Nó que não possui nenhum filho (`left is None and right is None`).
- Altura (Height): O número máximo de arestas da raiz até a folha mais distante.
"""


# ==========================================================
# 2. IMPLEMENTAÇÃO DO NÓ E DA ÁRVORE BINÁRIA DE BUSCA (BST)
# ==========================================================
class TreeNode:
    """Nó de uma Árvore Binária."""

    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class BinarySearchTree:
    """Implementação didática de Árvore Binária de Busca."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def inserir(self, valor: int) -> None:
        """Insere um novo valor respeitando a propriedade de BST."""
        if self.root is None:
            self.root = TreeNode(valor)
        else:
            self._inserir_recursivo(self.root, valor)

    def _inserir_recursivo(self, no_atual: TreeNode, valor: int) -> None:
        if valor < no_atual.val:
            if no_atual.left is None:
                no_atual.left = TreeNode(valor)
            else:
                self._inserir_recursivo(no_atual.left, valor)
        elif valor > no_atual.val:
            if no_atual.right is None:
                no_atual.right = TreeNode(valor)
            else:
                self._inserir_recursivo(no_atual.right, valor)

    def buscar(self, valor: int) -> bool:
        """Busca um valor na BST em O(log n) médio."""
        return self._buscar_recursivo(self.root, valor)

    def _buscar_recursivo(self, no_atual: TreeNode | None, valor: int) -> bool:
        if no_atual is None:
            return False
        if no_atual.val == valor:
            return True
        elif valor < no_atual.val:
            return self._buscar_recursivo(no_atual.left, valor)
        else:
            return self._buscar_recursivo(no_atual.right, valor)


# ==========================================================
# 3. OS 4 PERCURSOS EM ÁRVORES (TREE TRAVERSALS)
# ==========================================================
"""
1. In-Order (Em-Ordem): Esquerda -> Raiz -> Direita
   - Propriedade Especial: Retorna os elementos da BST em ORDEM CRESCENTE perfeita!
2. Pre-Order (Pré-Ordem): Raiz -> Esquerda -> Direita
   - Útil para clonar/copiar uma árvore ou serializar a estrutura.
3. Post-Order (Pós-Ordem): Esquerda -> Direita -> Raiz
   - Útil para deletar nós da árvore ou calcular tamanho de diretórios.
4. Level-Order (Ordem por Nível / BFS): Visita nível a nível usando uma Fila (Queue).
"""


def percurso_in_order(no: TreeNode | None, resultado: list[int]) -> None:
    if no is not None:
        percurso_in_order(no.left, resultado)
        resultado.append(no.val)
        percurso_in_order(no.right, resultado)


def percurso_pre_order(no: TreeNode | None, resultado: list[int]) -> None:
    if no is not None:
        resultado.append(no.val)
        percurso_pre_order(no.left, resultado)
        percurso_pre_order(no.right, resultado)


def percurso_post_order(no: TreeNode | None, resultado: list[int]) -> None:
    if no is not None:
        percurso_post_order(no.left, resultado)
        percurso_post_order(no.right, resultado)
        resultado.append(no.val)


def percurso_level_order(raiz: TreeNode | None) -> list[int]:
    """Level-Order Traversal (BFS) usando Fila."""
    resultado = []
    if raiz is None:
        return resultado

    fila = deque([raiz])
    while fila:
        no_atual = fila.popleft()
        resultado.append(no_atual.val)
        if no_atual.left:
            fila.append(no_atual.left)
        if no_atual.right:
            fila.append(no_atual.right)

    return resultado


def demonstrar_percursos() -> None:
    print("\n--- 1. FUNDAMENTOS: Percursos em BST ---")
    bst = BinarySearchTree()
    # Construindo a árvore: 50, 30, 70, 20, 40
    for v in [50, 30, 70, 20, 40]:
        bst.inserir(v)

    in_order_res: list[int] = []
    percurso_in_order(bst.root, in_order_res)

    pre_order_res: list[int] = []
    percurso_pre_order(bst.root, pre_order_res)

    post_order_res: list[int] = []
    percurso_post_order(bst.root, post_order_res)

    level_order_res = percurso_level_order(bst.root)

    print(f"In-Order   (Crescente): {in_order_res}")
    print(f"Pre-Order  (Estrutura): {pre_order_res}")
    print(f"Post-Order (Bottom-up): {post_order_res}")
    print(f"Level-Order      (BFS): {level_order_res}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 2. APLICAÇÃO BACKEND: Árvores no Mundo Real ---")
    print("  1. Sistemas de Arquivos (File Systems): Diretórios e subdiretórios.")
    print("  2. Índices B-Tree / B+Tree em Bancos de Dados Relacionais (PostgreSQL, MySQL).")
    print("  3. Árvore Sintática Abstrata (AST) em Compiladores e Interpretadores Python.")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em BST:
- Busca / Inserção (Caso Médio - Árvore Balanceada): Tempo O(log n), Espaço O(log n) da Call Stack.
- Busca / Inserção (Pior Caso - Árvore Desbalanceada Degenerada em Lista): Tempo O(n).
- Solução para o Pior Caso: Árvores Auto-Balanceadas (AVL Trees, Red-Black Trees).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como verificar se uma Árvore Binária é uma Árvore Binária de Busca VÁLIDA (Validate Binary Search Tree)?"
A: "Não basta verificar apenas se `filho_esquerdo < pai < filho_direito` para cada nó isolado!
    É necessário passar um intervalo de validade (limite mínimo `min_val` e limite máximo `max_val`) para cada chamada recursiva:
    - Para o filho esquerdo: o valor máximo permitido se torna o valor do pai.
    - Para o filho direito: o valor mínimo permitido se torna o valor do pai.
    Se qualquer nó violar `min_val < node.val < max_val`, a árvore é inválida. Complexidade: Tempo O(N), Espaço O(N)."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função `calcular_altura_arvore(raiz: TreeNode | None) -> int` que retorne a altura máxima da árvore.
# Exercício 2 (Intermediário): Escreva uma função `inverter_arvore_binaria(raiz: TreeNode | None) -> TreeNode | None` que inverta a árvore (espelhamento) em O(N).
# Exercício 3 (Desafio / Entrevista): Implemente a validação `is_valid_bst(raiz: TreeNode | None) -> bool` utilizando a estratégia de limites min/max.


def main() -> None:
    print("==========================================================")
    print("  AULA 79: ÁRVORES BINÁRIAS DE BUSCA (BST) E PERCURSOS")
    print("==========================================================")
    demonstrar_percursos()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 79 executado com sucesso.")


if __name__ == "__main__":
    main()
