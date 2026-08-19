"""
61_pytest_basico.py - Fundamentos de Testes Unitários com Pytest

Objetivos:
1. Estruturar funções de teste com o padrão `test_*()`.
2. Utilizar asserções nativas com a instrução `assert`.
"""

def somar(a: int, b: int) -> int:
    return a + b


def test_somar_sucesso() -> None:
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def main() -> None:
    print("==========================================================")
    print("  AULA 61: FUNDAMENTOS DE TESTES UNITÁRIOS COM PYTEST")
    print("==========================================================")
    test_somar_sucesso()
    print("[OK] Teste unitário manual passou com sucesso!")
    print("\n[Concluido] Arquivo 61 executado com sucesso.")


if __name__ == "__main__":
    main()
