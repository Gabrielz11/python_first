"""
64_mocking.py - Isolamento de Dependências com Mocks (`unittest.mock`)

Objetivos:
1. Utilizar `unittest.mock.MagicMock` para simular chamadas de API externas ou banco de dados.
"""

from unittest.mock import MagicMock


class ClienteHTTP:
    def buscar_usuario(self, id: int) -> dict[str, str]:
        raise NotImplementedError("Requer conexão de rede real")


def obter_nome_usuario(cliente: ClienteHTTP, id: int) -> str:
    dados = cliente.buscar_usuario(id)
    return dados["nome"]


def test_obter_nome_usuario_com_mock() -> None:
    cliente_mock = MagicMock(spec=ClienteHTTP)
    cliente_mock.buscar_usuario.return_value = {"nome": "Maria Sônia"}

    nome = obter_nome_usuario(cliente_mock, 101)
    assert nome == "Maria Sônia"
    cliente_mock.buscar_usuario.assert_called_once_with(101)


def main() -> None:
    print("==========================================================")
    print("  AULA 64: ISOLAMENTO E MOCKING COM UNITCHK.MOCK")
    print("==========================================================")
    test_obter_nome_usuario_com_mock()
    print("[OK] Teste com MagicMock passou com sucesso!")
    print("\n[Concluido] Arquivo 64 executado com sucesso.")


if __name__ == "__main__":
    main()
