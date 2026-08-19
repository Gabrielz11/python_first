"""
17_collections.py - Módulo `collections` (Counter, defaultdict, deque, NamedTuple, ChainMap)

Objetivos:
1. Dominar as estruturas especializadas do módulo nativo `collections` em Python 3.12+.
2. Compreender `collections.deque` e sua complexidade O(1) para inserção/remoção em ambas as pontas.
3. Utilizar `Counter` para análise estatística e contagem de frequências em O(n).
4. Evitar a repetição de código com `defaultdict` e estruturar dados leves com `NamedTuple`.
"""

import time
from collections import ChainMap, Counter, defaultdict, deque
from typing import NamedTuple

# ==========================================================
# 1. DEQUE: DOUBLE-ENDED QUEUE (O(1) popleft vs O(n) list.pop(0))
# ==========================================================
"""
Em CPython, o `deque` é implementado como uma LISTA DUPLAMENTE ENCADEADA DE BLOCOS (Blocks of Pointers).

Tabela Comparativa de Desempenho: `deque` vs `list`
-----------------------------------------------------------------------------
Operação                      `collections.deque`     `list`
-----------------------------------------------------------------------------
Adicionar ao Final (`append`) O(1)                    O(1) Amortizado
Remover do Final (`pop`)      O(1)                    O(1)
Adicionar no Início (`appendleft`) O(1)              O(n) [Realoca todos!]
Remover do Início (`popleft`) O(1)                    O(n) [Realoca todos!]
Acesso por Índice Central     O(n)                    O(1)
-----------------------------------------------------------------------------
"""


def demonstrar_deque() -> None:
    print("\n--- 1. CONCEITO: Performance de collections.deque ---")

    fila: deque[str] = deque(["pedido_1", "pedido_2", "pedido_3"])

    # Inserção e remoção O(1) no início e no final
    fila.append("pedido_4")  # Adiciona no final -> O(1)
    fila.appendleft("pedido_urgente")  # Adiciona no início -> O(1)

    print(f"Fila após append e appendleft: {fila}")

    atendido = fila.popleft()  # Remove do início -> O(1)
    print(f"Pedido atendido com popleft() O(1): '{atendido}'")
    print(f"Fila restante: {fila}")

    # Benchmark: Popleft em Deque vs Pop(0) em List
    TAMANHO = 50_000
    lista_teste = list(range(TAMANHO))
    deque_teste = deque(range(TAMANHO))

    inicio = time.perf_counter()
    while lista_teste:
        lista_teste.pop(0)
    tempo_lista = (time.perf_counter() - inicio) * 1000

    inicio = time.perf_counter()
    while deque_teste:
        deque_teste.popleft()
    tempo_deque = (time.perf_counter() - inicio) * 1000

    print(f"Tempo para processar {TAMANHO} itens com list.pop(0) [O(n²)]: {tempo_lista:.2f} ms")
    print(f"Tempo para processar {TAMANHO} itens com deque.popleft() [O(n)]: {tempo_deque:.2f} ms")
    if tempo_deque > 0:
        print(f"[*] `deque` foi aproximadamente {tempo_lista / max(tempo_deque, 0.001):.0f}x mais rápido!")


# ==========================================================
# 2. COUNTER: CONTAGEM DE FREQUÊNCIAS E MULTISETS
# ==========================================================
def demonstrar_counter() -> None:
    print("\n--- 2. CONCEITO: collections.Counter ---")

    votos = ["Python", "Python", "Rust", "Python", "Go", "Rust", "Python", "Go"]
    contador = Counter(votos)

    print(f"Frequência de votos: {contador}")
    print(f"As 2 linguagens mais votadas (.most_common(2)): {contador.most_common(2)}")

    # Operações de multiset com Counter
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    print(f"Soma de Counters (c1 + c2): {c1 + c2}")


# ==========================================================
# 3. DEFAULTDICT: AGRUPAMENTO SEM KEYERROR
# ==========================================================
def demonstrar_defaultdict() -> None:
    print("\n--- 3. CONCEITO: collections.defaultdict ---")

    transacoes = [
        ("Ana", 150.0),
        ("Carlos", 200.0),
        ("Ana", 50.0),
        ("Bia", 300.0),
        ("Carlos", 100.0),
    ]

    # `defaultdict(list)` inicializa automaticamente uma lista vazia se a chave não existir
    historico_clientes: defaultdict[str, list[float]] = defaultdict(list)

    for cliente, valor in transacoes:
        historico_clientes[cliente].append(valor)

    print("Histórico agrupado com defaultdict(list):")
    for cliente, valores in historico_clientes.items():
        print(f"  - {cliente}: {valores} (Total: R$ {sum(valores):.2f})")


# ==========================================================
# 4. TYPING.NAMEDTUPLE E CHAINMAP
# ==========================================================
class ServidorConfig(NamedTuple):
    host: str
    porta: int
    ssl: bool = True


def demonstrar_namedtuple_e_chainmap() -> None:
    print("\n--- 4. CONCEITO: NamedTuple e ChainMap ---")

    # 1. NamedTuple: Tupla imutável com campos nomeados e tipagem estática (acesso via `.host` ou por índice `[0]`)
    server = ServidorConfig(host="localhost", porta=8080)
    print(f"Servidor: {server.host}:{server.porta} (SSL: {server.ssl})")

    # 2. ChainMap: Pesquisa em cascata sobre múltiplos dicionários sem fundi-los fisicamente!
    config_padrao = {"tema": "claro", "fonte": 12, "debug": False}
    config_usuario = {"tema": "escuro"}  # Sobrescreve apenas o tema

    config_final = ChainMap(config_usuario, config_padrao)
    print(f"Configuração final (ChainMap): tema='{config_final['tema']}', fonte={config_final['fonte']}")


# ==========================================================
# 5. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Por que devemos utilizar `collections.deque` em vez de `list` quando implementamos uma Fila (FIFO) ou um Buffer Circular?"
A: "Em uma `list`, a remoção do primeiro elemento (`pop(0)`) exige o deslocamento de todos os `n-1` elementos
    restantes na memória contígua, tornando a operação O(n) e o algoritmo total O(n²).
    O `deque` armazena os elementos em blocos duplamente encadeados. As operações `popleft()` e `appendleft()`
    apenas alteram os ponteiros das extremidades, executando estritamente em O(1)."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `top_3_palavras(texto: str) -> list[tuple[str, int]]` que limpe um texto e use
#              `Counter` para retornar as 3 palavras mais frequentes.
# Exercício 2: Crie um buffer circular de tamanho 3 utilizando `deque(maxlen=3)` e demonstre como novos appends
#              descartam automaticamente os elementos mais antigos.


def main() -> None:
    print("==========================================================")
    print("  AULA 17: MÓDULO COLLECTIONS (DEQUE, COUNTER, DEFAULTDICT)")
    print("==========================================================")
    demonstrar_deque()
    demonstrar_counter()
    demonstrar_defaultdict()
    demonstrar_namedtuple_e_chainmap()
    print("\n[Concluido] Arquivo 17 executado com sucesso.")


if __name__ == "__main__":
    main()
