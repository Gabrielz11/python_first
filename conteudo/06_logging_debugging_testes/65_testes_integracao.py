"""
65_testes_integracao.py - Testes de Integração e Pirâmide de Testes

Objetivos:
1. Compreender a diferença entre testes unitários (unidade isolada com mocks) e testes de integração (módulos integrados).
"""

def test_fluxo_integrado_simplificado() -> None:
    carrinho = ["ItemA", "ItemB"]
    total = len(carrinho) * 50.0
    assert total == 100.0


def main() -> None:
    print("==========================================================")
    print("  AULA 65: TESTES DE INTEGRAÇÃO")
    print("==========================================================")
    test_fluxo_integrado_simplificado()
    print("[OK] Teste de integração simplificado aprovado!")
    print("\n[Concluido] Arquivo 65 executado com sucesso.")


if __name__ == "__main__":
    main()
