"""
73_hash_maps.py - Tabelas Hash (Hash Maps), Dicionários, Hashing e o Problema Two Sum

Objetivos:
1. Dominar o funcionamento interno de Tabelas Hash (Hash Tables / Hash Maps) em Python (`dict` e `set`).
2. Entender o papel das Funções Hash (`hash()`) e a resolução conceitual de Colisões.
3. Compreender a complexidade de tempo O(1) médio para busca, inserção e remoção.
4. Resolver o problema clássico de entrevista Two Sum comparando a abordagem Naive O(n²) com Hash Map O(n).
5. Analisar o Trade-Off fundamental de Engenharia: Consumir mais Memória (Espaço) para obter Velocidade (Tempo).
"""

import time
from typing import Any


# ==========================================================
# 1. CONCEITO E FUNCIONAMENTO DAS TABELAS HASH
# ==========================================================
"""
O que é uma Tabela Hash (Hash Table / Hash Map)?
Uma Tabela Hash é uma estrutura de dados que mapeia chaves a valores permitindo acesso direto em tempo O(1) médio.

Como funciona a Função Hash:
1. Quando executamos `dicionario[chave] = valor`, o CPython chama a função interna `hash(chave)`.
2. A função hash converte a chave em um número inteiro único (Hash Code).
3. Esse inteiro é convertido via módulo (`hash_code % tamanho_tabela`) em um índice numérico de um array interno.
4. O valor é armazenado diretamente no slot daquele índice na memória RAM.

Conceito de Colisão Hash (Collision):
- Ocorre quando duas chaves diferentes geram exatamente o mesmo índice interno.
- Métodos de Resolução de Colisão:
  1. Open Addressing (Endereçamento Aberto): Usado pelo CPython. Se o slot estiver ocupado, ele calcula uma nova posição derivada (probing).
  2. Separate Chaining (Encadeamento): Cada slot do array contém uma lista encadeada guardando todas as chaves colididas.
"""


# ==========================================================
# 2. IMPLEMENTAÇÃO CONCEITUAL DE HASH MAP SIMPLES
# ==========================================================
class HashMapSimples:
    """Implementação didática de um Hash Map com resolução de colisão por Chaining."""

    def __init__(self, capacidade: int = 8) -> None:
        self.capacidade = capacidade
        self.tabela: list[list[tuple[Any, Any]]] = [[] for _ in range(capacidade)]

    def _gerar_indice(self, chave: Any) -> int:
        return abs(hash(chave)) % self.capacidade

    def put(self, chave: Any, valor: Any) -> None:
        idx = self._gerar_indice(chave)
        bucket = self.tabela[idx]
        for i, (k, _) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)  # Atualiza
                return
        bucket.append((chave, valor))  # Insere novo

    def get(self, chave: Any) -> Any | None:
        idx = self._gerar_indice(chave)
        bucket = self.tabela[idx]
        for k, v in bucket:
            if k == chave:
                return v
        return None


def demonstrar_hash_map_conceitual() -> None:
    print("\n--- 1. FUNDAMENTOS: HashMapSimples (Chaining) ---")
    mapa = HashMapSimples(capacidade=4)
    mapa.put("user_101", "Gabriel")
    mapa.put("user_102", "Ana")

    print(f"Busca user_101: {mapa.get('user_101')}")
    print(f"Busca user_102: {mapa.get('user_102')}")


# ==========================================================
# 3. PROBLEMA CLÁSSICO DE ENTREVISTA: TWO SUM
# ==========================================================
"""
Problema Two Sum:
Dada uma lista de números inteiros e um número Alvo (target), retorne os índices dos dois números cuja soma seja igual ao Alvo.

Solução Naive:
- Testar todos os pares possíveis com dois loops aninhados.
- Complexidade: Tempo O(n²), Espaço O(1).

Solução Otimizada com Hash Map (Trade-off Memória vs Tempo):
- Iterar sobre a lista armazenando cada número e seu índice em um Hash Map (`vistos[num] = indice`).
- Para cada número `x`, calcula-se o complemento necessário `c = target - x`.
- Se o complemento já estiver no Hash Map, encontramos o par em O(1) tempo de busca!
- Complexidade: Tempo O(n), Espaço O(n).
"""


def two_sum_naive(nums: list[int], target: int) -> tuple[int, int] | None:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_hash_map(nums: list[int], target: int) -> tuple[int, int] | None:
    vistos: dict[int, int] = {}
    for indice, num in enumerate(nums):
        complemento = target - num
        if complemento in vistos:
            return (vistos[complemento], indice)
        vistos[num] = indice
    return None


def demonstrar_two_sum() -> None:
    print("\n--- 2. PROBLEMA CLÁSSICO: Two Sum (Naive vs Hash Map) ---")
    nums = [2, 7, 11, 15, 3, 6, 8, 12, 14, 19, 21, 25, 30]
    target = 27

    t0 = time.perf_counter()
    res1 = two_sum_naive(nums, target)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    res2 = two_sum_hash_map(nums, target)
    t3 = time.perf_counter()

    print(f"Naive O(n²)   : Índices {res1} em {(t1 - t0)*1000:.4f} ms")
    print(f"Hash Map O(n) : Índices {res2} em {(t3 - t2)*1000:.4f} ms")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class CacheEmMemoriaBackend:
    """Simulador de Cache de alta velocidade usando dict em Python."""

    def __init__(self) -> None:
        self._cache: dict[str, Any] = {}

    def obter_usuario(self, user_id: int) -> dict[str, Any]:
        chave = f"user:{user_id}"
        if chave not in self._cache:
            print(f"  [Cache Miss] Buscando usuário {user_id} no banco de dados...")
            # Simula resultado do DB e grava no cache
            self._cache[chave] = {"id": user_id, "nome": f"Usuario_{user_id}"}
        else:
            print(f"  [Cache Hit] Retornando usuário {user_id} diretamente do Hash Map!")
        return self._cache[chave]


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: In-Memory Cache ---")
    cache = CacheEmMemoriaBackend()

    # 1ª Chamada: Miss
    u1 = cache.obter_usuario(101)
    # 2ª Chamada: Hit (O(1) instantâneo)
    u2 = cache.obter_usuario(101)


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Hash Maps (dict/set):
- Inserção / Busca / Remoção (Caso Médio): Tempo O(1), Espaço O(1).
- Pior Caso (Múltiplas Colisões extremas): Tempo O(n).
- Trade-off: Gasta O(n) de espaço de memória RAM para obter buscas instantâneas O(1).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o Python lida com colisões de hash nos dicionários e por que as chaves de um dict precisam ser imutáveis (hashable)?"
A: "1. Resolução de Colisão: O CPython utiliza a técnica de Open Addressing (Endereçamento Aberto) com sondagem pseudo-aleatória. Se um slot estiver ocupado, ele deriva um novo índice no array de slots.
    2. Exigência de Imutabilidade (Hashable): Para que um objeto seja chave de um dicionário, seu Hash Code NUNCA pode alterar durante o ciclo de vida do programa.
       Se objetos mutáveis (como listas ou dicionários) pudessem ser chaves, alterar o conteúdo da lista mudaria seu índice interno, tornando impossível encontrar o valor novamente na tabela Hash."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função `contar_frequencia_palavras(texto: str) -> dict[str, int]` usando um Hash Map.
# Exercício 2 (Intermediário): Resolva o problema de verificar se duas strings são Anagramas uma da outra usando Hash Map em O(N).
# Exercício 3 (Desafio / Entrevista): Encontre o primeiro caractere não-repetido em uma string em O(N) tempo e O(1) espaço de alfabeto.


def main() -> None:
    print("==========================================================")
    print("  AULA 73: TABELAS HASH, HASHING E DOIS PONTEIROS / TWO SUM")
    print("==========================================================")
    demonstrar_hash_map_conceitual()
    demonstrar_two_sum()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 73 executado com sucesso.")


if __name__ == "__main__":
    main()
