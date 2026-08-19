"""
49_decoradores_com_argumentos.py - Decoradores Parametrizados (Fábricas de Decoradores)

Objetivos:
1. Criar decoradores que aceitam parâmetros (ex: `@repeat(vezes=3)`).
2. Compreender os 3 níveis de funções aninhadas requeridos.
"""

from functools import wraps
from typing import Any, Callable


def repetir(vezes: int) -> Callable[..., Any]:
    def decorador(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            resultado = None
            for i in range(vezes):
                print(f" Execução {i + 1}/{vezes} de {func.__name__}")
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador


@repetir(vezes=2)
def enviar_notificacao(mensagem: str) -> None:
    print(f"  [Notificação] {mensagem}")


def main() -> None:
    print("==========================================================")
    print("  AULA 49: DECORADORES PARAMETRIZADOS")
    print("==========================================================")
    enviar_notificacao("Servidor online!")
    print("\n[Concluido] Arquivo 49 executado com sucesso.")


if __name__ == "__main__":
    main()
