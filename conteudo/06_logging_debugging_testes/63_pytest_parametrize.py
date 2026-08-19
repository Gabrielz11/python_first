"""
63_pytest_parametrize.py - Testes Parametrizados com @pytest.mark.parametrize e Testes Baseados em Tabela

Objetivos:
1. Dominar o uso do decorador `@pytest.mark.parametrize` para implementar Testes Baseados em Tabela (Table-Driven Tests).
2. Eliminar duplicação de funções de teste ao rodar a mesma lógica sobre múltiplos conjuntos de dados.
3. Personalizar a identificação de cada caso de teste no terminal utilizando o argumento `ids`.
4. Compreender a técnica de aninhamento de múltiplos decoradores `@pytest.mark.parametrize` (Produto Cartesiano).
5. Prevenir o antipadrão de utilizar loops `for` dentro de um único teste unitário.
"""

import pytest
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Testes Parametrizados?
Testes Parametrizados permitem executar a MESMA função de teste repetidamente passando diferentes
entradas e comparando com as saídas esperadas.

Por que NÃO usar um loop for dentro de um teste?
Se você colocar um `for entrada, esperado in tabela:` dentro de uma única função de teste:
1. Primeira Falha Aborta Tudo: Se o primeiro item do loop falhar, o teste é interrompido IMEDIATAMENTE e todos os outros 99 itens da tabela NUNCA serão testados!
2. Falta de Granularidade: O relatório do Pytest contabilizará apenas 1 único teste executado.

Com `@pytest.mark.parametrize`:
O Pytest gera um NÓ DE TESTE INDEPENDENTE para cada linha da tabela.
Se um caso falhar, os outros continuam rodando e aparecem individualmente no relatório final do terminal!
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: PARAMETRIZE BÁSICO
# ==========================================================
def e_email_valido(email: str) -> bool:
    """Validador simples de formato de email."""
    if not isinstance(email, str):
        return False
    return "@" in email and "." in email and not email.startswith("@")


# Tabela de testes parametrizados (Entrada -> Resultado Esperado)
CASOS_TESTE_EMAIL = [
    ("gabriel@empresa.com", True),
    ("usuario.sobrenome@dominio.br", True),
    ("email_sem_arroba.com", False),
    ("email@sem_ponto", False),
    ("@sem_usuario.com", False),
    ("", False),
]


@pytest.mark.parametrize("email_input, resultado_esperado", CASOS_TESTE_EMAIL)
def test_validar_email_tabela(email_input: str, resultado_esperado: bool) -> None:
    resultado = e_email_valido(email_input)
    assert resultado == resultado_esperado


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: IDS PERSONALIZADOS E PRODUTO CARTESIANO
# ==========================================================
# Personalizando descrições de cada caso com ids=
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ("  python  ", "python"),
        ("PRODUÇÃO", "produção"),
    ],
    ids=["Remover espaços pontas", "Converter para minúsculas"],
)
def test_sanitizar_string(entrada: str, esperado: str) -> None:
    assert entrada.strip().lower() == esperado


# Aninhamento de Parametrize (Produto Cartesiano: 2x2 = 4 testes gerados!)
@pytest.mark.parametrize("role", ["ADMIN", "USER"])
@pytest.mark.parametrize("status", ["ATIVO", "INATIVO"])
def test_matriz_permissoes(role: str, status: str) -> None:
    assert len(role) > 0
    assert len(status) > 0


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def calcular_frete(peso_kg: float, regiao: str) -> float:
    """Calculador de frete para e-commerce backend."""
    if peso_kg <= 0:
        raise ValueError("Peso deve ser positivo.")

    tabelas = {"SUDESTE": 10.0, "SUL": 15.0, "NORDESTE": 25.0}
    taxa_base = tabelas.get(regiao.upper(), 30.0)
    return taxa_base + (peso_kg * 2.0)


@pytest.mark.parametrize(
    "peso, regiao, valor_esperado",
    [
        (2.0, "SUDESTE", 14.0),   # 10 + 4
        (2.0, "SUL", 19.0),       # 15 + 4
        (5.0, "NORDESTE", 35.0),  # 25 + 10
    ],
)
def test_calcular_frete_sucesso(peso: float, regiao: str, valor_esperado: float) -> None:
    assert calcular_frete(peso, regiao) == valor_esperado


def demonstrar_execucao_parametrize() -> None:
    print("\n--- 1. DEMONSTRAÇÃO: Execução de casos parametrizados ---")

    for email_in, exp in CASOS_TESTE_EMAIL:
        res = e_email_valido(email_in)
        status = "PASS" if res == exp else "FAIL"
        print(f"  [{status}] Email: {email_in!r} -> Retornou {res} (Esperado: {exp})")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: TEST GENERATOR NO PYTEST
# ==========================================================
"""
Como o `@pytest.mark.parametrize` funciona por baixo dos panos:
1. Durante a fase de Coleta de Testes (Test Collection Phase), o Pytest inspeciona os atributos de marcação (`pytestmark`) da função.
2. O Pytest invoca o seu gerador interno de testes (`pytest_generate_tests`), criando uma cópia do nó da função de teste para cada tupla de parâmetros.
3. Cada nó gerado recebe um ID único (ex: `test_validar_email_tabela[gabriel@empresa.com-True]`).
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Geração dos Nós de Teste: Tempo O(N), onde N é o número de linhas da tabela de parâmetros.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 2. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Loop for manual dentro da função de teste
    print("[X] Nao-Pythonic (Loop for manual dentro do teste):")
    print("  def test_tudo():\n      for item in lista:\n          assert f(item) == ok  # Se 1 falhar, paralisa o teste todo!")

    # [OK] PYTHONIC: Utilizar @pytest.mark.parametrize
    print("\n[OK] Pythonic:")
    print("  @pytest.mark.parametrize('item, ok', tabela)\n  def test_indiv(item, ok):\n      assert f(item) == ok  # Testes independentes!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Defina listas de parametrização limpas e organizadas fora da função de teste para manter o código legível.
2. Utilize o parâmetro `ids=[...]` para nomear casos complexos ou testes de borda (Edge Cases).
3. Combine `@pytest.mark.parametrize` com `pytest.raises` para testar múltiplas entradas inválidas que devem lançar exceção.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 3. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Multiplicar parametrizes inadvertidamente criando centenas de testes desnecessários
    print("[!] Armadilha 1: Stacking de 3 decoradores @pytest.mark.parametrize de 10 itens cria 10x10x10 = 1000 testes! Cuidado com o Produto Cartesiano exagerado.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que devemos preferir `@pytest.mark.parametrize` a colocar um loop `for` dentro de uma função de teste unitário?"
A: "1. Isolamento de Falhas: No loop `for`, a primeira falha dispara um `AssertionError` que aborta o teste inteiro, impedindo a verificação dos casos subsequentes. No `parametrize`, cada linha da tabela gera um teste independente no Pytest.
    2. Visibilidade no Relatório: O Pytest gera relatórios detalhados com status INDIVIDUAL de PASS/FAIL para cada parâmetro, facilitando a identificação exata do caso de borda que quebrou."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `fatorial(n: int) -> int` e parametrize os testes com entradas `[0, 1, 5]` e saídas `[1, 1, 120]`.
# Exercício 2: Escreva um teste parametrizado com `ids` personalizados testando a conversão de strings de datas em objetos `date`.
# Exercício 3: Parametrize a validação de 4 senhas fracas diferentes que devem disparar `SenhaFracaError`.


def main() -> None:
    print("==========================================================")
    print("  AULA 63: TESTES PARAMETRIZADOS E TABLE-DRIVEN TESTS")
    print("==========================================================")
    demonstrar_execucao_parametrize()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 63 executado com sucesso.")


if __name__ == "__main__":
    main()
