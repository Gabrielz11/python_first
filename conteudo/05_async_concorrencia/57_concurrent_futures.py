"""
57_concurrent_futures.py - `ThreadPoolExecutor` e `ProcessPoolExecutor`

Objetivos:
1. Utilizar a abstração de alto nível `concurrent.futures`.
2. Executar tarefas em pools de threads ou processos com `executor.map()` ou `submit()`.
"""

from concurrent.futures import ThreadPoolExecutor


def calcular_quadrado(n: int) -> int:
    return n * n


def main() -> None:
    print("==========================================================")
    print("  AULA 57: CONCURRENT.FUTURES THREADPOOLEXECUTOR")
    print("==========================================================")
    numeros = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers=3) as executor:
        resultados = list(executor.map(calcular_quadrado, numeros))
    print(f"Quadrados calculados em pool de workers: {resultados}")
    print("\n[Concluido] Arquivo 57 executado com sucesso.")


if __name__ == "__main__":
    main()
