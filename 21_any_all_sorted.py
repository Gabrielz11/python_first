"""
21_any_all_sorted.py - Built-ins `any()`, `all()`, `sorted()`, `min()` e `max()`

Objetivos:
1. Avaliação de curto-circuito com `any()` e `all()`.
2. Ordenação Timsort com `sorted()`.
"""

def demonstrar_builtins() -> None:
    print("\n--- 1. ANY E ALL ---")
    status = [True, True, False]
    print(f"Any: {any(status)} | All: {all(status)}")


def main() -> None:
    print("==========================================================")
    print("  AULA 21: ANY, ALL E SORTED")
    print("==========================================================")
    demonstrar_builtins()
    print("\n[Concluido] Arquivo 21 executado com sucesso.")


if __name__ == "__main__":
    main()
