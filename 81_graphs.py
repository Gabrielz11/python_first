"""
81_graphs.py - Grafos: Representação com Lista de Adjacência e Algoritmo BFS

Objetivos:
1. Representar grafos usando dicionários de adjacência.
2. Implementar a Busca em Largura (BFS - Breadth-First Search) usando fila.
"""

from collections import deque


def bfs_caminho_grafo(grafo: dict[str, list[str]], inicio: str) -> list[str]:
    visitados: set[str] = {inicio}
    fila: deque[str] = deque([inicio])
    ordem_visita: list[str] = []

    while fila:
        vertice = fila.popleft()
        ordem_visita.append(vertice)
        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    return ordem_visita


def main() -> None:
    print("==========================================================")
    print("  AULA 81: GRAFOS E ALGORITMO BFS (BUSCA EM LARGURA)")
    print("==========================================================")
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"]
    }
    ordem = bfs_caminho_grafo(grafo, "A")
    print(f"Ordem de visitação BFS a partir de 'A': {ordem}")
    print("\n[Concluido] Arquivo 81 executado com sucesso.")


if __name__ == "__main__":
    main()
