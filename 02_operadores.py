"""
02_operadores.py - Operadores e Expressões em Python

Objetivos:
1. Dominar operadores aritméticos, de comparação, lógicos, de atribuição, identidade e pertencimento.
2. Entender profundamente a diferença entre igualdade de valor (==) e igualdade de identidade (is).
3. Compreender a avaliação de curto-circuito (Short-Circuit Evaluation) em operadores lógicos.
4. Aplicar regras de precedência de operadores.
"""

from typing import Any

# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Operadores em Python são símbolos especiais que executam computações sobre um ou mais operandos.

Categorias Principais:
1. Aritméticos: +, -, *, /, // (divisão inteira), % (módulo/resto), ** (exponenciação).
2. Comparação (Relacionais): ==, !=, >, <, >=, <=.
3. Lógicos: and, or, not (utilizam avaliação em curto-circuito).
4. Atribuição: =, +=, -=, *=, /=, //=, %=, **=.
5. Identidade: is, is not (compara endereços de memória id()).
6. Pertencimento: in, not in (verifica se um elemento existe em uma sequência/coleção).

Diferença Crucial (== vs is):
- == invoca o método dunder `__eq__()` para checar se os VALORES dos objetos são equivalentes.
- is checa se o id(objeto_a) == id(objeto_b) (se ambos referenciam exatamente o MESMO endereço de memória).
"""


def demonstrar_operadores_aritmeticos() -> None:
    print("\n--- 1. OPERADORES ARITMÉTICOS E PRECEDÊNCIA ---")

    a, b = 17, 5

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao_real = a / b       # Retorna float sempre
    divisao_inteira = a // b   # Trunca a parte decimal (floor division)
    modulo = a % b             # Resto da divisão (muito útil para par/ímpar e ciclos)
    potencia = a ** b

    print(f"a = {a}, b = {b}")
    print(f"Divisao Real (a / b): {divisao_real} (tipo: {type(divisao_real).__name__})")
    print(f"Divisao Inteira (a // b): {divisao_inteira} (tipo: {type(divisao_inteira).__name__})")
    print(f"Modulo/Resto (a % b): {modulo}")
    print(f"Exponenciacao (a ** b): {potencia}")

    # Precedência: Parênteses () > Exponenciação ** > Multiplicação/Divisão (*, /, //, %) > Soma/Subtração (+, -)
    resultado = 10 + 2 * 3 ** 2
    print(f"Precedencia (10 + 2 * 3 ** 2): {resultado} (Calculado como: 10 + (2 * 9))")


# ==========================================================
# 2. EXEMPLOS: Identidade (== vs is) e Pertencimento (in)
# ==========================================================
def demonstrar_identidade_e_pertencimento() -> None:
    print("\n--- 2. EXEMPLOS: == vs is e Operador in ---")

    # Listas distintas com os mesmos elementos
    list_1 = [1, 2, 3]
    list_2 = [1, 2, 3]

    print(f"list_1 == list_2: {list_1 == list_2} (Conteudo e valores idênticos)")
    print(f"list_1 is list_2: {list_1 is list_2} (Enderecos de memoria sao DIFERENTES)")

    # Singleton None: SEMPRE use 'is None' ou 'is not None', NUNCA '== None'
    valor: Any = None
    print(f"valor is None: {valor is None} (Forma correta segundo PEP 8)")

    # Operador de pertencimento (in)
    permissoes_usuario = {"READ", "WRITE", "EXECUTE"}
    pode_escrever = "WRITE" in permissoes_usuario
    pode_deletar = "DELETE" in permissoes_usuario

    print(f"Pode escrever? {pode_escrever}")
    print(f"Pode deletar? {pode_deletar}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Curto-Circuito em Avaliações Lógicas
# ==========================================================
def buscar_usuario_no_banco(user_id: int) -> dict[str, str] | None:
    print(f"  [DB Query] Buscando usuario {user_id}...")
    if user_id == 100:
        return {"id": "100", "nome": "Gabriel Sênior"}
    return None


def demonstrar_curto_circuito() -> None:
    print("\n--- 3. EXEMPLO PRÁTICO: Short-Circuit Evaluation ---")

    # Em 'A and B', se A for Falso, B NENHUMA VEZ é executado.
    # Em 'A or B', se A for Verdadeiro, B NENHUMA VEZ é executado.

    is_autenticado = False

    # A chamada de busca no banco NÃO será executada porque is_autenticado é False
    print("Verificando acesso com usuario NAO autenticado:")
    autorizado = is_autenticado and buscar_usuario_no_banco(100) is not None
    print(f"Resultado Autorizado: {autorizado}")

    print("\nVerificando acesso com usuario AUTENTICADO:")
    is_autenticado = True
    autorizado = is_autenticado and buscar_usuario_no_banco(100) is not None
    print(f"Resultado Autorizado: {autorizado}")


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de Operadores de Pertencimento (`in`):
- Operador `in` em Listas/Tuplas: O(n) [Busca Linear de início ao fim].
- Operador `in` em Conjuntos (sets) / Dicionários (keys): O(1) médio [Busca por tabela Hash].

Regra de Ouro de Performance:
Se você precisa verificar a existência de elementos frequentemente em uma grande coleção,
converta a lista para um `set` ou `dict` para transformar O(n) em O(1).
"""


# ==========================================================
# 5. COMPARATIVO: NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    status_codigo = 200

    # [X] NÃO-PYTHONIC:
    print("[X] Nao-Pythonic (Comparacao encadeada verbosa e verificacao explicita de booleano):")
    if status_codigo >= 200 and status_codigo <= 299:
        is_sucesso = True
    else:
        is_sucesso = False
    print(f"Is Sucesso: {is_sucesso}")

    # [OK] PYTHONIC:
    print("[OK] Pythonic (Comparacao encadeada encadeamento de operadores):")
    is_sucesso_pythonic = 200 <= status_codigo <= 299
    print(f"Is Sucesso Pythonic: {is_sucesso_pythonic}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Usar 'is' para comparar strings ou números dinâmicos
    s1 = "hello world"
    s2 = "".join(["hello", " ", "world"])

    print(f"s1 == s2: {s1 == s2} (Valores sao iguais)")
    print(f"s1 is s2: {s1 is s2} (Objetos diferentes na memoria! NUNCA use 'is' para comparar conteudo de str)")

    # Armadilha 2: Atribuição dentro de expressões lógicas (em C/Java a = b retorna valor. Em Python lança SyntaxError)
    # x = (y = 10)  # SyntaxError em Python! Em Python 3.8+ existe o operador Walrus := para isso.


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Qual é a diferença entre '==' e 'is' e quando devemos utilizar cada um?"
A: "'==' verifica a igualdade de valores invocando `__eq__()`. Deve ser utilizado para comparar dados,
    como strings, números, listas e objetos de domínio.
    'is' verifica a igualdade de identidade (mesmo endereço de memória). Deve ser utilizado estritamente
    para comparar Singletons na linguagem, como `is None`, `is True`, `is False`."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma expressão que verifique se um número inteiro é par e positivo ao mesmo tempo.
# Exercício 2: Escreva uma função que verifique se uma permissão solicitada existe em uma coleção de permissões
#              utilizando a estrutura de dados com menor complexidade temporal possível.
# Exercício 3: Explique o resultado da expressão: `False or 0 or [] or "Engenheiro" or True`.


def main() -> None:
    print("==========================================================")
    print("  AULA 02: OPERADORES E EXPRESSÕES EM PYTHON")
    print("==========================================================")
    demonstrar_operadores_aritmeticos()
    demonstrar_identidade_e_pertencimento()
    demonstrar_curto_circuito()
    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 02 executado com sucesso.")


if __name__ == "__main__":
    main()
