"""
78_recursao.py - Recursão, Caso Base, Call Stack e Limites do CPython

Objetivos:
1. Dominar o paradigma da Recursão e sua mecânica de execução.
2. Identificar os dois pilares obrigatórios: Caso Base (Base Case) e Passo Recursivo (Recursive Case).
3. Inspecionar o impacto da Pilha de Chamadas (Call Stack) no consumo de memória RAM O(N).
4. Compreender a exceção `RecursionError` e a função `sys.setrecursionlimit()`.
5. Entender por que o CPython NÃO implementa Otimização de Chamada de Cauda (Tail Call Optimization - TCO).
"""

import sys
import time
from typing import Any


# ==========================================================
# 1. CONCEITO E ESTRUTURA DE UMA FUNÇÃO RECURSIVA
# ==========================================================
"""
O que é Recursão?
Recursão é a técnica onde uma função resolve um problema chamando A SI MESMA sobre sub-problemas menores.

Estrutura Obrigatória de Toda Função Recursiva:
1. Caso Base (Base Case):
   Condição de parada explicita que NÂO faz chamada recursiva. Evita o loop infinito.
2. Passo Recursivo (Recursive Case):
   A chamada da própria função aproximando o parâmetro da condição do Caso Base.

Por que o Python NÃO possui Tail Call Optimization (TCO)?
Linguagens funcionais (como Haskell, Scheme, Elixir) otimizam chamadas recursivas no final da função para não empilhar novos frames.
Guido van Rossum (criador do Python) optou intencionalmente por NÃO implementar TCO no CPython para:
1. Preservar o Stack Trace completo e legível durante a depuração de erros.
2. Manter a simplicidade da máquina virtual de bytecode.
"""


# ==========================================================
# 2. SINTAXE E EXEMPLOS PROGRESSIVOS
# ==========================================================
# Exemplo 1: Fatorial Recursivo vs Iterativo
def fatorial_recursivo(n: int) -> int:
    """Fatorial: O(n) Tempo, O(n) Espaço da Call Stack."""
    if n <= 1:  # Caso Base
        return 1
    return n * fatorial_recursivo(n - 1)  # Passo Recursivo


def fatorial_iterativo(n: int) -> int:
    """Fatorial Iterativo: O(n) Tempo, O(1) Espaço."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Exemplo 2: Fibonacci com Memoization (DP) vs Recursivo Puro
def fibonacci_puro(n: int) -> int:
    """Fibonacci Recursivo Puro: O(2^n) Tempo (PÉSSIMO), O(n) Espaço."""
    if n <= 1:
        return n
    return fibonacci_puro(n - 1) + fibonacci_puro(n - 2)


def fibonacci_memoizado(n: int, memo: dict[int, int] | None = None) -> int:
    """Fibonacci Recursivo com Memoization: O(n) Tempo, O(n) Espaço."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)
    return memo[n]


def demonstrar_fundamentos_recursao() -> None:
    print("\n--- 1. FUNDAMENTOS: Fatorial e Fibonacci Recursivo ---")

    print(f"Fatorial de 5 (Recursivo): {fatorial_recursivo(5)}")
    print(f"Fatorial de 5 (Iterativo): {fatorial_iterativo(5)}")

    t0 = time.perf_counter()
    fib_puro = fibonacci_puro(30)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    fib_memo = fibonacci_memoizado(30)
    t3 = time.perf_counter()

    print(f"Fibonacci(30) Puro [O(2^n)] : {fib_puro} em {(t1 - t0)*1000:.2f} ms")
    print(f"Fibonacci(30) Memo [O(n)]   : {fib_memo} em {(t3 - t2)*1000:.4f} ms (Milhares de vezes mais rápido!)")


# ==========================================================
# 3. LIMITES DO CPYTHON E RECURSIONERROR
# ==========================================================
def demonstrar_limite_recursao() -> None:
    print("\n--- 2. INTERNO: Limite de Profundidade do CPython ---")

    limite_atual = sys.getrecursionlimit()
    print(f"Limite padrao de profundidade da Call Stack em CPython: {limite_atual} frames")

    def recursao_infinita(contador: int) -> None:
        recursao_infinita(contador + 1)

    try:
        recursao_infinita(1)
    except RecursionError as e:
        print(f"[!] Capturado RecursionError esperado: {e}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: NAVEGAÇÃO EM JSON ANINHADO
# ==========================================================
def buscar_chave_em_json_aninhado(dados: Any, chave_alvo: str) -> Any | None:
    """Navegação recursiva em dicionários e listas aninhadas (ex: payloads JSON flexíveis)."""
    if isinstance(dados, dict):
        if chave_alvo in dados:
            return dados[chave_alvo]
        for valor in dados.values():
            res = buscar_chave_em_json_aninhado(valor, chave_alvo)
            if res is not None:
                return res

    elif isinstance(dados, list):
        for item in dados:
            res = buscar_chave_em_json_aninhado(item, chave_alvo)
            if res is not None:
                return res

    return None


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Parser Recursivo de JSON Aninhado ---")
    payload_complexo = {
        "status": 200,
        "data": {
            "usuario": {
                "perfil": {
                    "permissoes": ["READ", "WRITE"],
                    "configuracoes": {"tema": "escuro", "lang": "pt-BR"},
                }
            }
        },
    }

    lang = buscar_chave_em_json_aninhado(payload_complexo, "lang")
    print(f"Chave 'lang' encontrada no JSON aninhado: '{lang}'")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades em Algoritmos Recursivos:
- Fatorial / Busca Recursiva: Tempo O(N), Espaço O(N) da Call Stack.
- Fibonacci Puro: Tempo O(2^N) [Árvore binária de chamadas], Espaço O(N).
- Fibonacci Memoizado: Tempo O(N), Espaço O(N).
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Quais são as vantagens e desvantagens de usar Recursão em vez de Iteração (Loops) em Python?"
A: "1. Vantagens: Torna o código extremamente limpo, elegante e autodocumentável para problemas de natureza indutiva ou hierárquica (como árvores, grafos, parsing de JSON e divisão e conquista).
    2. Desvantagens: Em CPython, cada chamada recursiva aloca um novo Frame de Execução na Call Stack da memória RAM (Espaço O(N)), correndo o risco de causar `RecursionError` para valores grandes de N.
       Já a iteração (loops `for/while`) reutiliza o mesmo frame em tempo O(1) de espaço."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função recursiva `soma_array(nums: list[int]) -> int` que retorne a soma dos elementos de uma lista.
# Exercício 2 (Intermediário): Escreva uma função recursiva `inverter_string_recursiva(s: str) -> str`.
# Exercício 3 (Desafio / Entrevista): Implemente a função `flatten_list(lista_aninhada)` que transforme uma lista de listas arbitrária (ex: `[1, [2, [3, 4]], 5]`) em uma lista plana `[1, 2, 3, 4, 5]`.


def main() -> None:
    print("==========================================================")
    print("  AULA 78: RECURSÃO, CASO BASE E LIMITES DO CPYTHON")
    print("==========================================================")
    demonstrar_fundamentos_recursao()
    demonstrar_limite_recursao()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 78 executado com sucesso.")


if __name__ == "__main__":
    main()
