"""
65_testes_integracao.py - Testes de Integração, Banco de Dados em Memória e Pytest Assíncrono

Objetivos:
1. Compreender a diferença fundamental entre Testes Unitários (isolados) e Testes de Integração (componentes integrados).
2. Utilizar bancos de dados em memória (como SQLite `:memory:`) para cenários de integração rápidos e isolados.
3. Testar código assíncrono utilizando decoradores do `pytest-asyncio` (`@pytest.mark.asyncio`).
4. Aplicar o padrão Pirâmide de Testes (Test Pyramid) em arquiteturas de backend.
5. Garantir o encerramento e rollback de transações de banco após a execução de cada teste de integração.
"""

import sqlite3
import pytest
from typing import Generator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Testes de Integração?
Diferente dos testes unitários (que isolam a unidade de código mockando todas as dependências externas),
os Testes de Integração comprovam que múltiplos módulos reais (ex: Repositório + Banco de Dados + SQL)
funcionam corretamente quando conectados entre si.

A Pirâmide de Testes (Test Pyramid):
1. Topo: Testes End-to-End (E2E) -> Poucos, lentos e caros.
2. Meio: Testes de Integração -> Quantidade moderada, testam integração entre camadas reais (DB/HTTP).
3. Base: Testes Unitários -> Centenas/Milhares, ultra-rápidos e isolados com Mocks.

Estratégia de Banco de Dados para Integração:
Em vez de conectar ao banco de dados PostgreSQL/MySQL de produção, utiliza-se um Banco de Dados SQLite em Memória (`:memory:`)
que é criado do zero antes do teste e destruído imediatamente após o término do teste.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: BANCO SQLITE EM MEMÓRIA COMO FIXTURE
# ==========================================================
@pytest.fixture(scope="function")
def db_connection() -> Generator[sqlite3.Connection, None, None]:
    """Fixture de Integração: Cria banco SQLite em memória limpo para cada teste."""
    # Setup
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")
    conn.commit()

    yield conn

    # Teardown
    conn.close()


class UsuarioRepositorySQL:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def salvar(self, nome: str, email: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        self.conn.commit()
        return cursor.lastrowid  # type: ignore

    def buscar_por_id(self, user_id: int) -> tuple[int, str, str] | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (user_id,))
        return cursor.fetchone()


def test_integracao_salvar_e_buscar_usuario(db_connection: sqlite3.Connection) -> None:
    # Teste de Integração Real: Repositório executando SQL de verdade contra o SQLite em memória!
    repo = UsuarioRepositorySQL(db_connection)

    user_id = repo.salvar("Gabriel", "gabriel@empresa.com")
    usuario_recuperado = repo.buscar_por_id(user_id)

    assert usuario_recuperado is not None
    assert usuario_recuperado[0] == user_id
    assert usuario_recuperado[1] == "Gabriel"
    assert usuario_recuperado[2] == "gabriel@empresa.com"


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: TESTES ASSÍNCRONOS
# ==========================================================
async def servico_calculo_assincrono(a: int, b: int) -> int:
    """Função assíncrona simulada."""
    return a + b


# Marcador do pytest-asyncio para executar testes async
@pytest.mark.asyncio
async def test_servico_assincrono() -> None:
    resultado = await servico_calculo_assincrono(10, 20)
    assert resultado == 30


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_execucao_integracao() -> None:
    print("\n--- 1. APLICAÇÃO BACKEND: Execução do Teste de Integração SQL ---")

    # Criando conexao sqlite temporaria para simular execucao do pytest
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")
    conn.commit()

    test_integracao_salvar_e_buscar_usuario(conn)
    print("  [PASS] test_integracao_salvar_e_buscar_usuario (SQL executado com sucesso no SQLite em memória!)")

    conn.close()


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ISOLAMENTO DE BANCO DE DADOS
# ==========================================================
"""
Como garantir o isolamento em Testes de Integração:
1. SQLite `:memory:`: Cada chamada a `sqlite3.connect(':memory:')` aloca um espaço de memória único e isolado.
2. Transações e Rollback: Em bancos de dados de contêiner (como PostgreSQL em Docker), a fixture inicia uma transação `BEGIN` antes do teste
   e executa `ROLLBACK` incondicionalmente no Teardown do teste, desfazendo qualquer modificação gravada sem precisar recriar as tabelas.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Teste de Integração com SQLite em memória: Tempo O(1) de criação da tabela (< 5ms), Espaço O(K) de memória RAM.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 2. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Conectar o teste de integração diretamente no banco de dados de desenvolvimento ou staging
    print("[X] Nao-Pythonic (Testes rodando em banco de dados real compartilhado):")
    print("  connect('postgres://prod_db')  # PERIGO! Suja o banco e causa falhas por conflitos entre testes!")

    # [OK] PYTHONIC: Utilizar SQLite em memória ou fixtures de transação com Rollback
    print("\n[OK] Pythonic:")
    print("  @pytest.fixture\n  def db(): conn = connect(':memory:'); yield conn; conn.close()  # Isolamento 100% limpo!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Separe os testes unitários dos testes de integração em diretórios distintos (`tests/unit/` e `tests/integration/`).
2. Utilize o marcador `@pytest.mark.integration` para poder rodar apenas os testes unitários rápidos durante o desenvolvimento local.
3. Garanta que cada teste de integração limpe seus dados no Teardown (via Rollback de transação ou recriação do SQLite em memória).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 3. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Escrever poucos testes unitários e confiar apenas em testes de integração lentos
    print("[!] Armadilha 1: Uma suíte com 500 testes de integração lentos pode demorar 10 minutos para rodar, desestimulando a execução de testes no dia a dia!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença de propósito entre um Teste Unitário e um Teste de Integração e como você os organiza em uma API backend?"
A: "1. Teste Unitário: Testa uma única função ou classe de forma isolada, mockando todas as dependências externas. Executa em milissegundos.
    2. Teste de Integração: Testa a comunicação e integração real entre duas ou mais camadas (ex: Repositório Python + Banco de Dados SQLite executando SQL real).
    Na arquitetura, organizamos a suíte seguindo a Pirâmide de Testes: mantemos uma base massiva de testes unitários super rápidos no CI/CD e uma camada complementar de testes de integração para validar queries SQL e endpoints."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma fixture SQLite `:memory:` que crie uma tabela `produtos` e teste a inserção e listagem de produtos.
# Exercício 2: Escreva um teste de integração assíncrono usando `@pytest.mark.asyncio` que teste uma função que consulte um repositório assíncrono.
# Exercício 3: Implemente um teste de integração que valide o lançamento de erro ao tentar inserir um email duplicado em uma coluna `UNIQUE`.


def main() -> None:
    print("==========================================================")
    print("  AULA 65: TESTES DE INTEGRAÇÃO E BANCO DE DADOS EM MEMÓRIA")
    print("==========================================================")
    demonstrar_execucao_integracao()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 65 executado com sucesso.")


if __name__ == "__main__":
    main()
