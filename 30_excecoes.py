"""
30_excecoes.py - Tratamento de Exceções, Hierarquia e Chaining (try/except/else/finally)

Objetivos:
1. Dominar o controle de fluxo com `try`, `except`, `else`, `finally`.
2. Compreender a hierarquia nativa de exceções em Python (`BaseException` -> `Exception`).
3. Entender Exception Chaining (`raise ... from err`) para preservação de tracebacks.
"""

def dividir_numeros(a: float, b: float) -> float:
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print(f"[X] ZeroDivisionError capturado: {e}")
        raise ValueError("Divisor não pode ser zero") from e
    else:
        print("[OK] Divisão realizada com sucesso.")
        return resultado
    finally:
        print("  [Finally] Bloco de finalização executado.")


def main() -> None:
    print("==========================================================")
    print("  AULA 30: TRATAMENTO DE EXCEÇÕES E EXCEPTION CHAINING")
    print("==========================================================")
    try:
        dividir_numeros(10, 2)
        dividir_numeros(10, 0)
    except ValueError as e:
        print(f"[!] Capturado na camada superior: {e} (Causa: {e.__cause__})")
    print("\n[Concluido] Arquivo 30 executado com sucesso.")


if __name__ == "__main__":
    main()
