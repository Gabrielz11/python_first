"""
64_mocking.py - Isolamento de Dependências com unittest.mock, MagicMock e @patch

Objetivos:
1. Dominar o isolamento de dependências externas em testes unitários utilizando `unittest.mock` (`Mock`, `MagicMock`).
2. Utilizar os gerenciadores de contexto e decoradores `@patch` e `patch.object`.
3. Configurar comportamentos simulados utilizando `return_value` e `side_effect`.
4. Verificar invocações com asserções de mock (`assert_called_once`, `assert_called_with`).
5. Compreender a regra de ouro da depuração: "Patch no local onde o objeto é IMPORTADO, não onde é definido".
"""

from unittest.mock import MagicMock, Mock, patch
import pytest
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Mocking?
Mocking é a técnica de substituir componentes reais (como APIs externas, bancos de dados, chamadas de rede ou arquivos no disco)
por objetos simulados (Mocks) durante a execução de testes unitários.

Diferença entre Mock e MagicMock:
1. `Mock`: Objeto base de simulação que registra chamadas, acessos a atributos e argumentos passados.
2. `MagicMock`: Subclasse de `Mock` que pré-implementa todos os métodos dunder mágicos do Python
   (como `__len__`, `__getitem__`, `__iter__`, `__enter__`, `__exit__`). É o tipo padrão retornado pelo `@patch`.

Regra de Ouro do Patching ("Where to Patch"):
Sempre aplique o `@patch` no caminho onde o módulo/classe É IMPORTADO E USADO pelo código sob teste,
e NÃO no local original onde ele foi definido!
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: RETURN_VALUE E SIDE_EFFECT
# ==========================================================
def demonstrar_fundamentos_mock() -> None:
    print("\n--- 1. FUNDAMENTOS: Mock, return_value e side_effect ---")

    # 1. Configurando return_value simples
    mock_cliente_http = Mock()
    mock_cliente_http.get.return_value = {"status": 200, "json": {"usuario": "Gabriel"}}

    resposta = mock_cliente_http.get("https://api.empresa.com/users/1")
    print(f"Resposta simulada do Mock: {resposta}")

    # Asserção de chamada
    mock_cliente_http.get.assert_called_once_with("https://api.empresa.com/users/1")
    print("  [PASS] mock_cliente_http.get foi chamado exatamente 1 vez com a URL correta.")

    # 2. Configurando side_effect (Disparar Exceção ou Múltiplos Retornos)
    mock_banco = Mock()
    mock_banco.query.side_effect = TimeoutError("Banco de dados indisponível.")

    try:
        mock_banco.query("SELECT * FROM users")
    except TimeoutError as e:
        print(f"  [PASS] side_effect disparou exceção esperada: {e}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ISOLAMENTO COM @PATCH
# ==========================================================
class GatewayPagamentoStripe:
    def processar_cartao(self, cartao_token: str, valor: float) -> dict[str, Any]:
        # Simula chamada real HTTP externa (que NUNCA deve rodar em teste unitário!)
        raise RuntimeError("Conexao real de rede com a Stripe realizada! (NUNCA DEVE OCORRER EM TESTE)")


class CheckoutService:
    def __init__(self) -> None:
        self.gateway = GatewayPagamentoStripe()

    def finalizar_pedido(self, cartao_token: str, valor: float) -> bool:
        res = self.gateway.processar_cartao(cartao_token, valor)
        return res.get("status") == "APPROVED"


def test_finalizar_pedido_com_mock() -> None:
    service = CheckoutService()

    # Substitui a instância real do gateway por um MagicMock
    service.gateway = MagicMock()
    service.gateway.processar_cartao.return_value = {"status": "APPROVED", "charge_id": "ch_123"}

    sucesso = service.finalizar_pedido("tok_visa", 150.0)

    assert sucesso is True
    service.gateway.processar_cartao.assert_called_once_with("tok_visa", 150.0)


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: PATCH DE CONTEXTO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 2. APLICAÇÃO BACKEND: Teste de Checkout com Patch de Gateway ---")

    test_finalizar_pedido_com_mock()
    print("  [PASS] test_finalizar_pedido_com_mock executado com sucesso e isolado da rede!")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: DYNAMIC ATTRIBUTE SWAPPING
# ==========================================================
"""
Como o `patch()` funciona por baixo dos panos:
1. Quando o bloco `with patch('modulo.Alvo') as mock_alvo:` inicia:
   - O Pytest/unittest salva o atributo original em uma variável temporária.
   - Substitui a chave no dicionário `modulo.__dict__['Alvo']` pelo objeto `MagicMock`.
2. Durante o bloco `with`, qualquer código que acesse `modulo.Alvo` estará acessando o `MagicMock`.
3. Ao sair do bloco `with` (ou no Teardown do decorador), o `patch()` RESTAURA incondicionalmente o atributo original no `__dict__` do módulo.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Substituição de Atributo via `patch()`: Tempo O(1) de alteração em dicionário de módulo CPython.
- Invocação de método de Mock: Tempo O(1) [Gravação dos argumentos na lista interna `mock.call_args_list`].
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 3. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Fazer chamadas reais de rede ou banco de dados durante testes unitários
    print("[X] Nao-Pythonic (Testes com chamadas HTTP reais):")
    print("  def test_api(): requests.get('https://api.com')  # Lento, frágil e falha sem internet!")

    # [OK] PYTHONIC: Utilizar Mocks para isolar chamadas I/O externas
    print("\n[OK] Pythonic:")
    print("  with patch('meu_modulo.requests.get') as mock_get: ...  # Teste ultra-rápido (< 1ms) e determinístico!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Regra de Ouro do Caminho ("Where to Patch"): Se o arquivo `servico.py` faz `from cliente import APIClient`, o patch DEVE ser `@patch('servico.APIClient')`, e NÃO `@patch('cliente.APIClient')`.
2. Utilize `assert_called_once_with(...)` para garantir que o serviço chamou a dependência externa com os parâmetros corretos.
3. Não exagere no Mocking (Over-Mocking). Se você mockar absolutamente todas as funções de um teste, estará testando os mocks e não a sua aplicação real.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Errar o caminho do import no patch ("Patch where used, not where defined")
    print("[!] Armadilha 1: Fazer patch no módulo de origem onde a classe foi declarada em vez de onde ela foi importada causa falhas sutis onde a chamada real continua sendo executada!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que significa a regra 'Patch onde o objeto é usado, não onde é definido' em testes unitários em Python?"
A: "Significa que o `unittest.mock.patch` altera a referência do objeto no namespace do MÓDULO QUE ESTÁ SENDO TESTADO.
    Se o módulo `pedidos.py` faz `from gateway import StripeClient`, a classe `StripeClient` é importada e guardada no namespace de `pedidos`.
    Se você fizer o patch em `'gateway.StripeClient'`, o módulo `pedidos` continuará segurando a referência original que já havia sido importada previamente!
    Por isso, o patch correto é `@patch('pedidos.StripeClient')`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um `Mock` para uma função de envio de SMS e verifique com `assert_called_once_with` se a mensagem correta foi enviada.
# Exercício 2: Utilize `@patch('urllib.request.urlopen')` para simular o retorno de uma chamada HTTP externa.
# Exercício 3: Configure um `side_effect` em um Mock que lance `ConnectionError` na primeira chamada e retorne um dicionário na segunda chamada.


def main() -> None:
    print("==========================================================")
    print("  AULA 64: ISOLAMENTO DE DEPENDÊNCIAS COM UNITTEST.MOCK")
    print("==========================================================")
    demonstrar_fundamentos_mock()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 64 executado com sucesso.")


if __name__ == "__main__":
    main()
