"""
62_pytest_fixtures.py - Fixtures no Pytest para Preparação de Estado

Objetivos:
1. Utilizar fixtures para injeção de dependências e estado inicial reutilizável em suítes de teste.
"""

def preparar_banco_dados_ficticio() -> dict[str, str]:
    return {"status": "conectado", "env": "test"}


def test_conexao_banco() -> None:
    db = preparar_banco_dados_ficticio()
    assert db["status"] == "conectado"


def main() -> None:
    print("==========================================================")
    print("  AULA 62: FIXTURES DE TESTE REUTILIZÁVEIS")
    print("==========================================================")
    test_conexao_banco()
    print("[OK] Teste com fixture manual passou com sucesso!")
    print("\n[Concluido] Arquivo 62 executado com sucesso.")


if __name__ == "__main__":
    main()
