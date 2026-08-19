"""
23_functools.py - Programação Funcional e Otimizações (`functools`)

Objetivos:
1. Dominar `functools.lru_cache` e `cache` para Memoization de funções puras.
2. Utilizar `functools.partial` para fixar argumentos e criar funções especializadas.
3. Utilizar `functools.wraps` para preservar metadados ao criar decoradores.
4. Aplicar `functools.reduce` para acumulação.
"""

import time
from functools import cache, partial, reduce


# 1. Memoization com @cache (O(1) busca em respostas já calculadas)
@cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def demonstrar_functools() -> None:
    print("\n--- 1. MEMOIZATION: @cache ---")
    inicio = time.perf_counter()
    res = fibonacci(35)
    tempo = (time.perf_counter() - inicio) * 1000
    print(f"Fibonacci(35) = {res} calculado em {tempo:.4f} ms (graças ao @cache!)")

    print("\n--- 2. PARTIAL: Fixando Parâmetros ---")
    def multiplicar(a: int, b: int) -> int:
        return a * b

    dobrar = partial(multiplicar, 2)
    print(f"Dobrar 15 (usando partial(multiplicar, 2)): {dobrar(15)}")

    print("\n--- 3. REDUCE: Acumulação ---")
    numeros = [1, 2, 3, 4, 5]
    produto_total = reduce(lambda acc, x: acc * x, numeros, 1)
    print(f"Produto total com reduce(): {produto_total}")


def main() -> None:
    print("==========================================================")
    print("  AULA 23: MÓDULO FUNCTOOLS, CACHING E PARTIAL APPL")
    print("==========================================================")
    demonstrar_functools()
    print("\n[Concluido] Arquivo 23 executado com sucesso.")


if __name__ == "__main__":
    main()
