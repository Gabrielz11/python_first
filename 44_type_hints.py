"""
44_type_hints.py - Tipagem Estática e Anotações de Tipos (PEP 484 / Python 3.12+)

Objetivos:
1. Utilizar type hints nativos em parâmetros e retornos de funções.
2. Utilizar sintaxe moderna de Union `A | B` e `Callable`.
3. Entender a utilidade das type hints para autocompletion na IDE e verificação com Mypy.
"""

from typing import Callable


def aplicar_operacao(a: float, b: float, operacao: Callable[[float, float], float]) -> float:
    return operacao(a, b)


def somar(x: float, y: float) -> float:
    return x + y


def main() -> None:
    print("==========================================================")
    print("  AULA 44: TYPE HINTS NATIVOS E CALLABLE")
    print("==========================================================")
    res = aplicar_operacao(10.0, 5.0, somar)
    print(f"Resultado de aplicar_operacao: {res}")
    print("\n[Concluido] Arquivo 44 executado com sucesso.")


if __name__ == "__main__":
    main()
