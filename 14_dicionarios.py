"""
14_dicionarios.py - Estrutura de Dados Dict (Tabela Hash Compacta e Busca O(1))

Objetivos:
1. Dominar `dict` em Python 3.12+: criação, ordenação por inserção (Python 3.7+), métodos `.get()`, `.setdefault()`, `.update()` e o operador de união `|`.
2. Compreender a arquitetura interna do CPython (Compact Hash Table).
3. Analisar a complexidade Big O temporal e espacial de operações em dicionários.
4. Diferenciar objetos de visualização dinâmicos (`dict_keys`, `dict_values`, `dict_items`).
"""

import time
from typing import Any

# ==========================================================
# 1. CONCEITO: Como o `dict` Funciona Internamente no CPython?
# ==========================================================
"""
Em CPython 3.6+, o `dict` foi reescrito para utilizar uma TABELA HASH COMPACTA.

Arquitetura da Tabela Hash Compacta:
- `indices`: Um array pequeno de inteiros representando os buckets da tabela hash.
- `entries`: Um array denso contendo as entradas na ordem exata em que foram inseridas `[hash, key_ptr, value_ptr]`.
- Benefício: Economia de 20% a 25% de memória e preservação NATAL da ORDEM DE INSERÇÃO!

Tabela de Complexidade Temporal (Big O) do Dict:
-----------------------------------------------------------------------------
Operação                      Sintaxe                  Complexidade Média (Big O)
-----------------------------------------------------------------------------
Busca por Chave               `d[key]` ou `d.get(k)`   O(1) [Constante]
Inserção / Atualização        `d[key] = val`           O(1) [Constante]
Remoção por Chave             `del d[key]` ou `.pop()` O(1) [Constante]
Teste de Existência           `key in d`               O(1) [Constante]
Iteração sobre Chaves         `for k in d:`            O(n) [Linear]
-----------------------------------------------------------------------------
* Pior caso teórico: O(n) quando ocorrem colisões extremas de hash (muito raro em Python moderno).
"""


def demonstrar_operacoes_metodos() -> None:
    print("\n--- 1. CONCEITO: Métodos Fundamentais do Dict ---")

    usuario: dict[str, Any] = {
        "id": 101,
        "nome": "Ana Silva",
        "email": "ana@empresa.com",
        "ativo": True,
    }

    # Access seguro com `.get(chave, valor_default)` (Evita KeyError)
    telefone = usuario.get("telefone", "Não informado")
    print(f"Telefone (usando .get()): {telefone}")

    # `.setdefault(chave, default)`: Retorna o valor se existir; se não, insere a chave com o default
    usuario.setdefault("permissoes", ["leitura"])
    usuario.setdefault("permissoes", ["admin"])  # Não sobrescreve, pois já existe!
    print(f"Permissões (usando .setdefault()): {usuario['permissoes']}")

    # Operador de União `|` e Atualização `|=` (Python 3.9+)
    dados_complementares = {"departamento": "Engenharia", "ativo": True}
    usuario_completo = usuario | dados_complementares
    print(f"Dict Mesclado com `|`: {usuario_completo}")


# ==========================================================
# 2. VIEWS DINÂMICAS: dict_keys, dict_values e dict_items
# ==========================================================
def demonstrar_views_dinamicas() -> None:
    print("\n--- 2. EXEMPLO: Objetos View Dinâmicos ---")

    estoque = {"maca": 10, "banana": 20}

    # As views refletem alterações no dicionário em tempo real sem criar cópias em memória!
    chaves_view = estoque.keys()
    itens_view = estoque.items()

    print(f"Chaves iniciais: {list(chaves_view)}")

    # Inserindo novo item no estoque
    estoque["laranja"] = 15

    # A view foi atualizada AUTOMATICAMENTE!
    print(f"Chaves após inserção (refletido na View): {list(chaves_view)}")


# ==========================================================
# 3. BENCHMARK DE DESEMPENHO: Dict O(1) vs List O(n)
# ==========================================================
def demonstrar_comparativo_busca() -> None:
    print("\n--- 3. COMPARATIVO DE PERFORMANCE: Dict O(1) vs List O(n) ---")

    TAMANHO = 100_000
    lista_chaves = [f"id_{i}" for i in range(TAMANHO)]
    dict_chaves = {f"id_{i}": i for i in range(TAMANHO)}

    alvo = f"id_{TAMANHO - 1}"

    # Busca em Lista - O(n)
    inicio = time.perf_counter()
    _ = alvo in lista_chaves
    tempo_lista = (time.perf_counter() - inicio) * 1000

    # Busca em Dict - O(1)
    inicio = time.perf_counter()
    _ = alvo in dict_chaves
    tempo_dict = (time.perf_counter() - inicio) * 1000

    print(f"Tempo de busca em Lista (O(n) - {TAMANHO} itens): {tempo_lista:.4f} ms")
    print(f"Tempo de busca em Dict  (O(1) - {TAMANHO} itens): {tempo_dict:.4f} ms")
    if tempo_dict > 0:
        print(f"[*] O Dict foi aproximadamente {tempo_lista / max(tempo_dict, 0.0001):.1f}x mais rápido!")


# ==========================================================
# 4. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Modificar o tamanho do dict enquanto itera sobre ele
    configuracoes = {"env": "prod", "debug": "false", "cache": "true"}

    try:
        for chave in configuracoes:
            if chave == "debug":
                del configuracoes[chave]  # Modificação durante iteração!
    except RuntimeError as e:
        print(f"[X] RuntimeError capturado ao alterar dict em iteração: {e}")

    # SOLUÇÃO PYTHONIC: Iterar sobre list(dict.keys()) ou criar novo dict
    for chave in list(configuracoes.keys()):
        if chave == "debug":
            del configuracoes[chave]
    print(f"[OK] Dict corrigido com remoção segura: {configuracoes}")

    # Armadilha 2: Chave mutável (unhashable)
    try:
        dict_invalido = {[1, 2]: "valor"}  # list não pode ser chave!
    except TypeError as e:
        print(f"[X] TypeError com chave mutável: {e}")


# ==========================================================
# 5. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Como a mudança do `dict` no Python 3.6+ otimizou a memória e como funciona o lookup em uma Hash Table?"
A: "No Python 3.6+, a estrutura mudou de uma tabela esparsa (onde chaves/valores ficavam direto no bucket hash com 66% de espaço vago)
    para duas tabelas: um array denso contendo os pares na ordem de inserção e um array compacto de índices.
    O lookup calcula `hash(key) % tamanho_indices`. Se houver correspondência, acessa a posição no array denso de entradas
    e compara a chave com `__eq__` para resolver possíveis colisões."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função `contar_frequencia_palavras(texto: str) -> dict[str, int]`
#              que receba uma string e retorne a contagem de cada palavra (ignorando pontuações e maiúsculas).
# Exercício 2: Escreva uma função `inverter_dicionario(d: dict[str, int]) -> dict[int, list[str]]`
#              que inverta as chaves e valores, agrupando em listas as chaves que possuem valores duplicados.


def main() -> None:
    print("==========================================================")
    print("  AULA 14: ESTRUTURA DE DADOS DICT E HASH TABLES")
    print("==========================================================")
    demonstrar_operacoes_metodos()
    demonstrar_views_dinamicas()
    demonstrar_comparativo_busca()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 14 executado com sucesso.")


if __name__ == "__main__":
    main()
