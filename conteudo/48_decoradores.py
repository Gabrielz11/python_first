"""
48_decoradores.py - Metaprogramação Leve com Decoradores de Funções

Objetivos:
1. Compreender o padrão Decorator (@decorador).
2. Manter a assinatura e metadados das funções originais com `functools.wraps`.
3. Medir tempo de execução de funções usando decoradores.
"""

import time
from functools import wraps
from typing import Any, Callable


def medidor_tempo(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        duracao = (time.perf_counter() - inicio) * 1000
        print(f"[METRICA] {func.__name__} executou em {duracao:.4f} ms")
        return resultado
    return wrapper


@medidor_tempo
def processar_dados() -> None:
    time.sleep(0.05)


def main() -> None:
    print("==========================================================")
    print("  AULA 48: DECORADORES DE FUNÇÕES E WRAPS")
    print("==========================================================")
    processar_dados()
    print("\n[Concluido] Arquivo 48 executado com sucesso.")


if __name__ == "__main__":
    main()
