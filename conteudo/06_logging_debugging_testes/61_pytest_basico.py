"""
61_pytest_basico.py - Testes Unitários com Pytest, Assertions Expressivos e Validação de Exceções

Objetivos:
1. Dominar a criação de suítes de testes unitários com a ferramenta Pytest.
2. Utilizar a instrução nativa `assert` do Python com inspecção de expressões expressivas do Pytest.
3. Validar o lançamento de exceções esperadas utilizando o gerenciador de contexto `pytest.raises()`.
4. Organizar testes utilizando o padrão AAA (Arrange, Act, Assert).
5. Entender a convenção de nomenclatura do Pytest (`test_*.py`, funções `test_*`).
"""

import pytest
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o Pytest e por que ele é o padrão da indústria?
Pytest é a ferramenta de testes mais popular do ecossistema Python.

Vantagens do Pytest sobre o unittest tradicional:
1. Assertions Nativos: Não exige métodos verbosos como `self.assertEqual(a, b)`. Utiliza o simples e poderoso `assert a == b`.
2. AST Rewriting: Reescreve a Árvore Sintática Abstrata (AST) em tempo de execução para fornecer relatórios detalhados quando um `assert` falha.
3. Menos Boilerplate: Não exige criação de classes derivadas de `unittest.TestCase` (basta criar funções que comecem com `test_`).
4. Autodescoberta (Test Discovery): Localiza automaticamente todos os arquivos nomeados `test_*.py` ou `*_test.py` e funções `test_*()`.

Padrão AAA (Arrange, Act, Assert):
- Arrange (Preparar): Configura as variáveis, objetos e dados necessários.
- Act (Agir): Invoca a função ou método que está sendo testado.
- Assert (Verificar): Comprova que o resultado obtido é igual ao esperado.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CÓDIGO A SER TESTADO E TESTES
# ==========================================================
def calcular_desconto_compra(valor_total: float, cupom: str | None = None) -> float:
    """Função de domínio a ser testada."""
    if valor_total < 0:
        raise ValueError("Valor total não pode ser negativo.")

    desconto = 0.0
    if cupom == "PROMO10":
        desconto = 0.10
    elif cupom == "VIP20":
        desconto = 0.20

    return valor_total * (1.0 - desconto)


# --- SUÍTE DE TESTES PYTEST ---

def test_calcular_desconto_sem_cupom() -> None:
    # 1. Arrange
    valor = 100.0

    # 2. Act
    resultado = calcular_desconto_compra(valor)

    # 3. Assert
    assert resultado == 100.0


def test_calcular_desconto_cupom_valido() -> None:
    # Arrange & Act
    resultado = calcular_desconto_compra(100.0, cupom="PROMO10")

    # Assert
    assert resultado == 90.0


def test_calcular_desconto_valor_negativo_lança_excecao() -> None:
    # Validando que a função dispara ValueError ao receber valor negativo
    with pytest.raises(ValueError) as exc_info:
        calcular_desconto_compra(-50.0)

    # Comprovando o texto da mensagem de exceção
    assert "Valor total não pode ser negativo" in str(exc_info.value)


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: EXECUÇÃO AUTÔNOMA
# ==========================================================
def demonstrar_execucao_simulada_testes() -> None:
    print("\n--- 1. FUNDAMENTOS: Executando funções de teste diretamente ---")

    # Simula a execução do Pytest no terminal
    test_calcular_desconto_sem_cupom()
    print("  [PASS] test_calcular_desconto_sem_cupom")

    test_calcular_desconto_cupom_valido()
    print("  [PASS] test_calcular_desconto_cupom_valido")

    test_calcular_desconto_valor_negativo_lança_excecao()
    print("  [PASS] test_calcular_desconto_valor_negativo_lança_excecao")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ServicoAutenticacao:
    @staticmethod
    def autenticar(usuario: str, senha: str) -> str:
        if not usuario or not senha:
            raise ValueError("Usuário e senha são obrigatórios.")
        if usuario == "admin" and senha == "secret123":
            return "TOKEN_JWT_VALIDO_123"
        raise PermissionError("Credenciais inválidas.")


def test_autenticar_sucesso() -> None:
    token = ServicoAutenticacao.autenticar("admin", "secret123")
    assert token == "TOKEN_JWT_VALIDO_123"


def test_autenticar_credenciais_invalidas() -> None:
    with pytest.raises(PermissionError):
        ServicoAutenticacao.autenticar("admin", "senha_errada")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 2. APLICAÇÃO BACKEND: Testes de Serviço de Autenticação ---")
    test_autenticar_sucesso()
    print("  [PASS] test_autenticar_sucesso")

    test_autenticar_credenciais_invalidas()
    print("  [PASS] test_autenticar_credenciais_invalidas")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: AST REWRITING NO PYTEST
# ==========================================================
"""
Como o Pytest inspeciona as instruções `assert`:
1. Quando você executa `pytest`, ele carrega o módulo Python e inspeciona o código usando a Árvore Sintática Abstrata (AST).
2. O Pytest REESCREVE as instruções `assert` no bytecode para capturar o valor individual de cada sub-expressão.
3. Se `assert a == b` falhar, o Pytest imprime o valor exato de `a` e o valor exato de `b` no relatório de erro do terminal (Assertion Introspection).
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Execução de Teste Unitário: Deve ser da ordem de milissegundos (< 10 ms por teste) para manter a suíte rápida.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 3. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar métodos legados da classe unittest.TestCase
    print("[X] Nao-Pythonic (Verborragia de unittest):")
    print("  self.assertEqual(resultado, 100)  # Exige herdar de TestCase!")

    # [OK] PYTHONIC: Utilizar assert nativo com Pytest
    print("\n[OK] Pythonic:")
    print("  assert resultado == 100  # Limpo, simples e idiomático!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Siga a convenção de nomes: arquivos `test_*.py`, funções `test_*()`.
2. Siga o padrão AAA (Arrange, Act, Assert) para organizar o corpo de cada função de teste.
3. Mantenha os testes unitários ISOLADOS e RÁPIDOS. Um teste não deve depender do resultado de outro teste.
4. Utilize `pytest.raises(MinhaExcecao)` para testar o caminho triste (erros e validações).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Escrever uma função de teste sem o prefixo test_
    # O Pytest simplesmente IGNORA a função e não executa o teste!
    print("[!] Armadilha 1: Nomear a função como `checar_desconto()` em vez de `test_checar_desconto()` faz o Pytest ignorá-la!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o Pytest consegue fornecer relatórios de erro tão detalhados em falhas de `assert` sem exigir o uso de métodos `self.assertEqual()`?"
A: "Através da técnica de AST Rewriting (Reescrita da Árvore Sintática Abstrata).
    Antes de compilar o arquivo de teste para bytecode, o Pytest intercepta o código e substitui as instruções `assert` nativas por um código CPython enriquecido.
    Esse código modificado captura e inspeciona os valores intermediários de cada variável da comparação, exibindo uma visão detalhada do lado esquerdo e direito da igualdade na saída do terminal."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `is_par(n: int) -> bool` e escreva dois testes unitários usando `assert`.
# Exercício 2: Crie uma função `dividir(a: float, b: float) -> float` e escreva um teste que valide o lançamento de `ZeroDivisionError` via `pytest.raises`.
# Exercício 3: Escreva um teste no padrão AAA que valide se um email sem `@` lança `ValueError`.


def main() -> None:
    print("==========================================================")
    print("  AULA 61: TESTES UNITÁRIOS COM PYTEST E ASSERTIONS")
    print("==========================================================")
    demonstrar_execucao_simulada_testes()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 61 executado com sucesso.")


if __name__ == "__main__":
    main()
