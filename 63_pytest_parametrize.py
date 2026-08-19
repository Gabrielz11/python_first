"""
63_pytest_parametrize.py - Testes Parametrizados (Evitando Duplicação)

Objetivos:
1. Executar o mesmo teste com diferentes combinações de entradas e saídas esperadas.
"""

def eh_par(numero: int) -> bool:
    return numero % 2 == 0


def test_eh_par_casos() -> None:
    casos_teste = [(2, True), (3, False), (0, True), (-4, True)]
    for num, esperado in casos_teste:
        assert eh_par(num) == esperado


def main() -> None:
    print("==========================================================")
    print("  AULA 63: TESTES PARAMETRIZADOS")
    print("==========================================================")
    test_eh_par_casos()
    print("[OK] Todos os casos parametrizados passaram com sucesso!")
    print("\n[Concluido] Arquivo 63 executado com sucesso.")


if __name__ == "__main__":
    main()
