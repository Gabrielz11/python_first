"""
62_pytest_fixtures.py - Pytest Fixtures, Escopos (function, module, session) e Setup/Teardown com yield

Objetivos:
1. Dominar a criação e injeção de dependências em testes utilizando Pytest Fixtures (`@pytest.fixture`).
2. Compreender os diferentes escopos de fixtures (`function`, `class`, `module`, `session`).
3. Implementar a fase de limpeza (Teardown) utilizando a instrução `yield` em fixtures.
4. Conhecer as Built-in Fixtures nativas do Pytest (`tmp_path`, `monkeypatch`, `capsys`).
5. Compartilhar fixtures globais entre múltiplos arquivos de teste utilizando a convenção `conftest.py`.
"""

import os
from pathlib import Path
import pytest
from typing import Generator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma Pytest Fixture?
Uma Fixture é uma função decorada com `@pytest.fixture` que fornece dados, estados, conexões ou objetos
preparados para as funções de teste.

Vantagens das Fixtures:
1. Injeção de Dependências Automática: O Pytest injeta o retorno da fixture bastando declarar seu nome nos parâmetros do teste (`def test_algo(minha_fixture):`).
2. Reutilização e Modularidade: Elimina a duplicação de códigos de inicialização (Setup) em múltiplos testes.
3. Setup e Teardown via `yield`:
   - Código ANTES do `yield`: Executado durante a fase de Setup (preparação).
   - O valor do `yield`: Entregue à função de teste.
   - Código DEPOIS do `yield`: Executado obrigatoriamente na fase de Teardown (limpeza/cleanup).

Escopos das Fixtures (scope=):
- `"function"` (padrão): Executada uma nova vez para cada função de teste individual.
- `"class"`: Executada uma única vez por classe de teste.
- `"module"`: Executada uma única vez por arquivo `.py` de teste.
- `"session"`: Executada uma única vez para toda a suíte de testes do projeto.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: FIXTURE COM SETUP E TEARDOWN
# ==========================================================
class BancoEmMemoria:
    def __init__(self) -> None:
        self.registros: list[str] = []
        self.conectado = True

    def fechar(self) -> None:
        self.conectado = False


@pytest.fixture(scope="function")
def db_session() -> Generator[BancoEmMemoria, None, None]:
    """Fixture de banco de dados simulado com Setup e Teardown."""
    # --- SETUP ---
    banco = BancoEmMemoria()
    banco.registros.append("Usuario_Root")

    # Entrega o objeto para o teste
    yield banco

    # --- TEARDOWN (Cleanup) ---
    banco.fechar()


def test_banco_inicializado_com_root(db_session: BancoEmMemoria) -> None:
    assert len(db_session.registros) == 1
    assert db_session.registros[0] == "Usuario_Root"
    assert db_session.conectado is True


def test_adicionar_novo_registro(db_session: BancoEmMemoria) -> None:
    db_session.registros.append("Usuario_Comum")
    assert len(db_session.registros) == 2


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: BUILT-IN FIXTURE TMP_PATH
# ==========================================================
def test_escrita_arquivo_com_tmp_path(tmp_path: Path) -> None:
    """Utiliza a built-in fixture tmp_path do Pytest (cria pasta temp isolada)."""
    arquivo_temp = tmp_path / "config.json"
    arquivo_temp.write_text('{"env": "test"}', encoding="utf-8")

    assert arquivo_temp.exists()
    assert "env" in arquivo_temp.read_text(encoding="utf-8")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ServicoNotificacaoEmail:
    def __init__(self, smtp_host: str) -> None:
        self.smtp_host = smtp_host

    def enviar(self, destinatario: str) -> bool:
        return True


@pytest.fixture
def servico_email() -> ServicoNotificacaoEmail:
    return ServicoNotificacaoEmail(smtp_host="smtp.empresa.com")


def test_envio_email_sucesso(servico_email: ServicoNotificacaoEmail) -> None:
    sucesso = servico_email.enviar("cliente@empresa.com")
    assert sucesso is True
    assert servico_email.smtp_host == "smtp.empresa.com"


def demonstrar_execucao_fixtures() -> None:
    print("\n--- 1. DEMONSTRAÇÃO: Executando lógica de Fixtures em testes ---")

    # Simulação do comportamento da Fixture em tempo de execução
    banco = BancoEmMemoria()
    banco.registros.append("Usuario_Root")

    test_banco_inicializado_com_root(banco)
    print("  [PASS] test_banco_inicializado_com_root")

    test_adicionar_novo_registro(banco)
    print("  [PASS] test_adicionar_novo_registro")

    banco.fechar()
    print("  [Teardown] Banco fechado com sucesso.")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ARQUIVO CONFTEST.PY
# ==========================================================
"""
Como o Pytest descobre e compartilha Fixtures (`conftest.py`):
1. Quando uma função de teste declara um parâmetro (ex: `db_session`), o Pytest busca a definição da fixture no próprio arquivo de teste.
2. Se não encontrar no próprio arquivo, o Pytest busca sequencialmente nos arquivos especiais nomeados `conftest.py`
   localizados na pasta do teste ou nas pastas superiores.
3. Não é necessário importar o `conftest.py`! O Pytest carrega todas as fixtures do `conftest.py` automaticamente.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Fixture `scope="function"`: Executa N vezes para N testes -> Isolamento perfeito, mas maior tempo se o Setup for pesado.
- Fixture `scope="session"`: Executa 1 única vez para todos os testes -> Baixíssimo tempo, mas exige cuidado para não vazar estado mutável entre os testes.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 2. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Duplicar código de inicialização de objeto no topo de cada função de teste
    print("[X] Nao-Pythonic (Setup duplicado manual):")
    print("  def test_a(): b = Banco(); ... \n  def test_b(): b = Banco(); ...  # Redundante!")

    # [OK] PYTHONIC: Utilizar @pytest.fixture com injeção de dependências
    print("\n[OK] Pythonic:")
    print("  @pytest.fixture\n  def b(): return Banco()\n  def test_a(b): ...  # Limpo e modular!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Mantenha as fixtures focadas em uma única responsabilidade. Uma fixture pode solicitar outra fixture por injeção!
2. Utilize `yield` para garantir a fase de Teardown/Cleanup de recursos (bancos, conexões, arquivos).
3. Coloque fixtures comuns e reutilizáveis por toda a aplicação dentro do arquivo `conftest.py`.
4. Evite alterar estados globais em fixtures com `scope="session"` sem restaurá-los ao final.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 3. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Reutilizar objetos mutáveis em fixtures com scope="module" ou "session"
    print("[!] Armadilha 1: Usar scope='session' em um banco em memória mutável faz o Teste A afetar o resultado do Teste B!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como funciona o arquivo `conftest.py` no Pytest e como ele implementa a Injeção de Dependências?"
A: "O `conftest.py` é um arquivo especial do Pytest usado para definir fixtures, hooks e configurações globais que são compartilhadas automaticamente por todos os arquivos de teste contidos naquele diretório (e subdiretórios).
    O Pytest utiliza o mecanismo de Injeção de Dependências: quando uma função de teste declara um argumento com o mesmo nome de uma fixture registrada em um `conftest.py`, o Pytest localiza e executa aquela fixture, entregando seu retorno diretamente para o parâmetro do teste."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma fixture `cliente_http_mock` que retorne um dicionário com `base_url` e `token_auth`.
# Exercício 2: Crie uma fixture com `yield` que crie uma pasta temporária, entregue a pasta para o teste e delete a pasta no Teardown.
# Exercício 3: Escreva uma fixture composta que consuma outra fixture existente e adicione um registro padrão.


def main() -> None:
    print("==========================================================")
    print("  AULA 62: PYTEST FIXTURES, ESCOPOS E SETUP/TEARDOWN")
    print("==========================================================")
    demonstrar_execucao_fixtures()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 62 executado com sucesso.")


if __name__ == "__main__":
    main()
