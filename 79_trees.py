"""
79_trees.py - Árvore Binária de Busca (Binary Search Tree - BST) e Percursos

Objetivos:
1. Implementar o nó de uma Árvore Binária (`TreeNode`).
2. Realizar percurso em ordem (In-Order Traversal) para obter valores ordenados.
"""

class TreeNode:
    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.esquerda: "TreeNode | None" = None
        self.direita: "TreeNode | None" = None


def percurso_em_ordem(raiz: TreeNode | None, resultado: list[int]) -> None:
    if raiz is not None:
        percurso_em_ordem(raiz.esquerda, resultado)
        resultado.append(raiz.valor)
        percurso_em_ordem(raiz.direita, resultado)


def main() -> None:
    print("==========================================================")
    print("  AULA 79: ÁRVORE BINÁRIA DE BUSCA (BST)")
    print("==========================================================")
    raiz = TreeNode(10)
    raiz.esquerda = TreeNode(5)
    raiz.direita = TreeNode(15)

    valores: list[int] = []
    percurso_em_ordem(raiz, valores)
    print(f"Valores da BST em ordem ascendente: {valores}")
    print("\n[Concluido] Arquivo 79 executado com sucesso.")


if __name__ == "__main__":
    main()
