"""
81_graphs.py - Grafos, Lista de Adjacência, BFS (Busca em Largura) e DFS (Busca em Profundidade)

Objetivos:
1. Dominar a Estrutura de Dados Grafo (Vertices/Nós e Arestas/Conexões).
2. Compreender a diferença entre Grafos Direcionados/Não-Direcionados e Ponderados/Não-Ponderados.
3. Representar Grafos em Python utilizando Lista de Adjacência (`dict[Any, list[Any]]`).
4. Implementar a Busca em Largura (BFS - Breadth-First Search) para encontrar o Menor Caminho em grafos não-ponderados.
5. Implementar a Busca em Profundidade (DFS - Depth-First Search) usando Recursão ou Pilha.
"""

from collections import deque
from typing import Any


# ==========================================================
# 1. CONCEITO DE GRAFOS E REPRESENTAÇÃO
# ==========================================================
"""
O que é um Grafo (Graph)?
Um Grafo e uma estrutura de dados não-linear composta por um conjunto de Vértices (Nodes/Pontos)
conectados por Arestas (Edges/Linhas).

Classificação:
1. Direcionado (Digraph): As arestas possuem sentido (A -> B não implica B -> A). Ex: Seguidores no Instagram.
2. Não-Direcionado: As arestas são bidirecionais (A <-> B). Ex: Amigos no Facebook.
3. Ponderado (Weighted): As arestas possuem pesos/custos (ex: distância em km entre cidades).

Representação em Código:
- Lista de Adjacência (Adjacency List): A forma mais eficiente em Python. Um dicionário onde cada chave é um Vértice e seu valor é uma lista dos Vértices vizinhos.
  - Espaço: O(V + E)
- Matriz de Adjacência (Adjacency Matrix): Uma matriz V x V contendo 1 se há aresta e 0 se não há.
  - Espaço: O(V²)
"""


# ==========================================================
# 2. REPRESENTAÇÃO E BUSCA EM LARGURA (BFS)
# ==========================================================
"""
Busca em Largura (BFS - Breadth-First Search):
- Explora o grafo NÍVEL POR NÍVEL (em camadas a partir da origem).
- Utiliza uma FILA (Queue - `collections.deque`) e um conjunto de visitados (`visited = set()`).
- Propriedade Fundamental: Encontra o MENOR CAMINHO (menor número de arestas) entre a origem e qualquer outro nó em grafos não-ponderados!
"""


class GrafoAdjacencia:
    """Representação de Grafo Não-Direcionado via Lista de Adjacência."""

    def __init__(self) -> None:
        self.adj: dict[str, list[str]] = {}

    def adicionar_aresta(self, u: str, v: str) -> None:
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_menor_caminho(self, inicio: str, destino: str) -> list[str] | None:
        """Encontra o menor caminho entre 'inicio' e 'destino' usando BFS em O(V + E)."""
        if inicio not in self.adj or destino not in self.adj:
            return None

        fila = deque([[inicio]])  # Guarda o caminho percorrido
        visitados = {inicio}

        while fila:
            caminho = fila.popleft()
            vertice_atual = caminho[-1]

            if vertice_atual == destino:
                return caminho

            for vizinho in self.adj.get(vertice_atual, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)

        return None


def demonstrar_bfs() -> None:
    print("\n--- 1. FUNDAMENTOS: BFS (Menor Caminho em Grafo) ---")
    g = GrafoAdjacencia()
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("C", "E")
    g.adicionar_aresta("D", "E")
    g.adicionar_aresta("E", "F")

    caminho = g.bfs_menor_caminho("A", "F")
    print(f"Menor caminho de A até F via BFS: {caminho}")


# ==========================================================
# 3. BUSCA EM PROFUNDIDADE (DFS)
# ==========================================================
"""
Busca em Profundidade (DFS - Depth-First Search):
- Explora o grafo "MERGULHANDO" o mais fundo possível ao longo de cada ramo antes de retroceder (Backtracking).
- Utiliza RECURSÃO ou uma PILHA (Stack).
- Útil para: Detecção de ciclos, ordenação topológica (DAGs), componentes conexos.
"""


def dfs_recursivo(grafo: dict[str, list[str]], vertice_atual: str, visitados: set[str], resultado: list[str]) -> None:
    """Busca em Profundidade Recursiva em O(V + E)."""
    visitados.add(vertice_atual)
    resultado.append(vertice_atual)

    for vizinho in grafo.get(vertice_atual, []):
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados, resultado)


def demonstrar_dfs() -> None:
    print("\n--- 2. FUNDAMENTOS: DFS (Busca em Profundidade) ---")
    grafo = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": ["E"],
        "E": ["F"],
        "F": [],
    }

    visitados: set[str] = set()
    ordem_dfs: list[str] = []
    dfs_recursivo(grafo, "A", visitados, ordem_dfs)

    print(f"Ordem de visitação DFS a partir de A: {ordem_dfs}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Grafos na Vida Real ---")
    print("  1. Redes Sociais: Conexões de amizade e recomendações de pessoas (BFS).")
    print("  2. Sistemas de Recomendação: Grafos bipartidos de Usuários x Produtos.")
    print("  3. Resolução de Dependências (NPM / Pip / Package Managers): DAG (Directed Acyclic Graph) e Ordenação Topológica.")
    print("  4. GPS e Roteamento (Google Maps): Algoritmo de Dijkstra e A* em Grafos Ponderados.")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Algoritmos de Grafos:
- BFS e DFS (Lista de Adjacência):
  - Tempo: O(V + E), onde V e o número de Vértices e E e o número de Arestas.
  - Espaço: O(V) para armazenar a lista de visitados e a fila/pilha.
- BFS e DFS (Matriz de Adjacência):
  - Tempo: O(V²).
  - Espaço: O(V²).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Quando você deve utilizar BFS (Busca em Largura) e quando deve utilizar DFS (Busca em Profundidade)?"
A: "1. Utilizar BFS: Quando você precisa encontrar o MENOR CAMINHO (ou o menor número de passos/arestas) entre dois nós em um grafo não-ponderado, ou explorar nós que estão próximos da origem.
    2. Utilizar DFS: Quando você precisa explorar TODAS as rotas possíveis, verificar a existência de caminhos, detectar ciclos, resolver labirintos (backtracking) ou realizar Ordenação Topológica em Grafos Direcionados Acíclicos (DAGs)."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função `contar_componentes_conexos(grafo)` que retorne o número de ilhas/componentes desconexos em um grafo.
# Exercício 2 (Intermediário): Implemente a detecção de ciclo em um grafo não-direcionado utilizando DFS.
# Exercício 3 (Desafio / Entrevista): Implemente o Algoritmo de Dijkstra para encontrar o caminho mínimo em um grafo com pesos positivos utilizando `heapq`.


def main() -> None:
    print("==========================================================")
    print("  AULA 81: GRAFOS, LISTA DE ADJACÊNCIA, BFS E DFS")
    print("==========================================================")
    demonstrar_bfs()
    demonstrar_dfs()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 81 executado com sucesso.")


if __name__ == "__main__":
    main()
