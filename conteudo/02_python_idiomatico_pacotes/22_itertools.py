"""
22_itertools.py - Ferramentas de Iteração Eficiente com o Módulo itertools

Objetivos:
1. Dominar as principais funções do módulo `itertools` para manipulação de iteráveis.
2. Utilizar iteradores infinitos (`count`, `cycle`, `repeat`) e combinatórias (`permutations`, `combinations`, `product`).
3. Aplicar agrupamentos inteligentes com `groupby` e concatenação lazy com `chain` e `islice`.
4. Compreender os benefícios de performance e consumo de memória O(1) com iteradores C-optimized.
5. Desenvolver pipelines de processamento de dados e geração de combinações de testes no backend.
"""

import itertools
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo itertools?
O `itertools` é um módulo nativo da biblioteca padrão do Python que fornece um conjunto de blocos
de construção de alta performance e memória eficiente para iteração.

Categorias principais de ferramentas no itertools:
1. Iteradores Infinitos: `count()`, `cycle()`, `repeat()` (geram dados sob demanda sem limite pré-definido).
2. Combinatória: `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`.
3. Encadeamento e Fatiamento Lazy: `chain()`, `chain.from_iterable()`, `islice()`, `zip_longest()`.
4. Filtro e Agrupamento: `groupby()`, `dropwhile()`, `takewhile()`, `accumulate()`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CHAIN, ISLICE E COMBINATÓRIA
# ==========================================================
def demonstrar_fundamentos_itertools() -> None:
    print("\n--- 1. FUNDAMENTOS: chain, islice e product ---")

    # 1. chain: Concatena múltiplos iteráveis sem criar uma nova lista gigante na RAM
    l1 = [1, 2, 3]
    l2 = [4, 5]
    l3 = (6, 7)
    iterador_concatenado = itertools.chain(l1, l2, l3)
    print(f"chain() lazy: {list(iterador_concatenado)}")

    # 2. islice: Fatiamento de iteradores/geradores sem consumir a sequência inteira
    gerador_infinito = itertools.count(start=100, step=10)
    fatia = list(itertools.islice(gerador_infinito, 4))
    print(f"islice() nos primeiros 4 elementos do count(): {fatia}")

    # 3. product: Produto Cartesiano (substitui loops aninhados)
    tamanhos = ["P", "M"]
    cores = ["Azul", "Preto"]
    combinacoes = list(itertools.product(tamanhos, cores))
    print(f"product() Cartesian: {combinacoes}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: GROUPBY E ACCUMULATE
# ==========================================================
def demonstrar_groupby_e_accumulate() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: groupby e accumulate ---")

    # accumulate: Soma acumulada / running total
    vendas_diarias = [100, 250, 80, 500, 300]
    acumulado = list(itertools.accumulate(vendas_diarias))
    print(f"Vendas diarias: {vendas_diarias}")
    print(f"Total acumulado (accumulate): {acumulado}")

    # groupby: Requer que os dados estejam Pré-ORDENADOS pela chave de agrupamento!
    pedidos = [
        {"cliente": "Ana", "valor": 50},
        {"cliente": "Ana", "valor": 120},
        {"cliente": "Bruno", "valor": 200},
        {"cliente": "Carlos", "valor": 80},
    ]

    print("\nAgrupamento por cliente com groupby():")
    for cliente, grupo in itertools.groupby(pedidos, key=lambda p: p["cliente"]):
        itens = list(grupo)
        total = sum(i["valor"] for i in itens)
        print(f"  Cliente {cliente}: {len(itens)} pedidos | Total: R$ {total}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def processar_lotes_dados(colecao: list[Any], tamanho_lote: int):
    """Fatia qualquer colecao ou stream em lotes (batching) com consumo de memoria O(1)."""
    it = iter(colecao)
    while True:
        lote = list(itertools.islice(it, tamanho_lote))
        if not lote:
            break
        yield lote


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Batch Processor para Filas/DB ---")
    registros_fila = [f"Payload_ID_{i}" for i in range(1, 13)]

    print(f"Total de registros a processar: {len(registros_fila)}")
    for num_lote, lote in enumerate(processar_lotes_dados(registros_fila, tamanho_lote=4), start=1):
        print(f"  [Lote {num_lote}] Enviando para worker: {lote}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE
# ==========================================================
"""
Como o itertools funciona em CPython:
1. Todas as funções do `itertools` são implementadas diretamente na camada C do Python (`Modules/itertoolsmodule.c`).
2. Operam inteiramente sob a C-API de iteradores, evitando o overhead de criação de objetos Python intermediários.
3. Consumo de Memória: Praticamente O(1). Em vez de alocar listas intermediárias para produtos cartesianos ou concatenações, o itertools mantém apenas os ponteiros para o estado do iterador atual.
"""


def demonstrar_eficiencia_memoria() -> None:
    print("\n--- 4. INTERNO: Comparativo de Memoria (chain vs lista) ---")
    import sys

    # Concatenação criando lista nova na RAM
    lista_1 = list(range(10000))
    lista_2 = list(range(10000, 20000))
    lista_concatenada = lista_1 + lista_2

    # Concatenação lazy com chain
    iterador_chain = itertools.chain(lista_1, lista_2)

    print(f"Tamanho da Lista Concat (Bytes na RAM): {sys.getsizeof(lista_concatenada)}")
    print(f"Tamanho do Iterador chain (Bytes na RAM): {sys.getsizeof(iterador_chain)}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `itertools.chain(*iteraveis)`: Tempo O(N + M), Espaço O(1).
- `itertools.islice(iteravel, n)`: Tempo O(n), Espaço O(1).
- `itertools.groupby(dados)`: Tempo O(N), Espaço O(1) para o iterador.
- `itertools.product(A, B)`: Tempo O(|A| * |B|), Espaço O(1) de estado interno.
- `itertools.permutations(N, R)`: Tempo O(N! / (N-R)!), Espaço O(1). Usa combinatória pesada!
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    l1 = [1, 2]
    l2 = [3, 4]

    # [X] NÃO-PYTHONIC: Matriz manual com loops aninhados para produto cartesiano
    print("[X] Nao-Pythonic (Loops aninhados):")
    pares_manual = []
    for x in l1:
        for y in l2:
            pares_manual.append((x, y))
    print(f"  Resultado: {pares_manual}")

    # [OK] PYTHONIC: itertools.product
    print("\n[OK] Pythonic:")
    pares_py = list(itertools.product(l1, l2))
    print(f"  Resultado (product): {pares_py}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre ordene os dados ANTES de passar para `itertools.groupby()`. Se não ordenar, dados com a mesma chave serão divididos em grupos separados.
2. Prefira `itertools.chain.from_iterable(list_of_lists)` quando tiver uma lista de listas para alinhamento rápido.
3. Não converta iteradores do `itertools` para `list()` a menos que realmente precise de acesso indexado, senão você perde o benefício de memória O(1).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer de ordenar antes do groupby()
    dados_desordenados = [
        {"cat": "A", "val": 1},
        {"cat": "B", "val": 2},
        {"cat": "A", "val": 3},  # "A" aparece novamente!
    ]

    grupos_errados = [cat for cat, _ in itertools.groupby(dados_desordenados, key=lambda x: x["cat"])]
    print(f"[!] Armadilha groupby sem sorted(): Categorias encontradas: {grupos_errados} (Criou 3 grupos em vez de 2!)")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença de complexidade espacial entre `combinations` e a criação de subconjuntos via recursão em memória?"
A: "O `itertools.combinations` calcula e fornece a próxima combinação sob demanda usando geradores em linguagem C (O(1) de espaço auxiliar).
    Já a recursão ingênua ou armazenar todos os subconjuntos em uma lista precisa de O(2^N) de memória para guardar o resultado final.
    O `itertools` permite iterar em bilhões de combinações sem estourar a RAM da máquina."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Utilize `itertools.cycle` para simular uma fila circular de servidores Load Balancer
#              atribuindo 6 requisições para 3 servidores.
# Exercício 2: Utilize `itertools.combinations` para encontrar todos os pares de números de uma lista
#              cuja soma seja igual a 10.
# Exercício 3: Escreva uma função que receba uma lista de dicionários de transações financeiras,
#              ordene por data e utilize `itertools.groupby` para calcular o saldo total de cada dia.


def main() -> None:
    print("==========================================================")
    print("  AULA 22: ITERAÇÃO EFICIENTE COM O MÓDULO ITERTOOLS")
    print("==========================================================")
    demonstrar_fundamentos_itertools()
    demonstrar_groupby_e_accumulate()
    demonstrar_aplicacao_backend()
    demonstrar_eficiencia_memoria()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 22 executado com sucesso.")


if __name__ == "__main__":
    main()
