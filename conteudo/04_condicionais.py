"""
04_condicionais.py - Estruturas Condicionais, Cláusulas de Guarda e Early Returns

Objetivos:
1. Dominar o controle de fluxo condicional com `if`, `elif` e `else`.
2. Utilizar o operador ternário (expressões condicionais) de forma limpa.
3. Aplicar o padrão de projeto Clean Code "Early Return" (Guarda de Condições) para eliminar aninhamento excessivo (Código Spagheti / Arrow Anti-pattern).
4. Compreender a avaliação lógica de condições compostas.
"""

from typing import Any

# ==========================================================
# 1. CONCEITO: Controle de Fluxo e Cláusulas de Guarda
# ==========================================================
"""
O que são Cláusulas de Guarda (Guard Clauses / Early Return)?
Em engenharia de software tradicional, é comum ver código com múltiplos níveis de `if/else` aninhados.
Isso cria o "Arrow Anti-pattern" (o código vai se deslocando para a direita, dificultando a leitura).

O Padrão Early Return prega:
- Avalie as pré-condições ou casos de erro logo no início da função.
- Se a condição de erro for atendida, retorne imediatamente (`return`).
- Mantenha o "caminho feliz" (happy path) principal no nível de indentação base da função.
"""


def demonstrar_condicionais_basicas(idade: int) -> str:
    print(f"\n--- 1. CONCEITO: Avaliando idade={idade} ---")

    if idade < 0:
        return "Idade Invalida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"


# ==========================================================
# 2. EXEMPLOS: Operador Ternário e Condições Compostas
# ==========================================================
def demonstrar_operador_ternario() -> None:
    print("\n--- 2. EXEMPLOS: Operador Ternário ---")

    status_code = 200

    # Sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
    mensagem = "Sucesso" if status_code == 200 else "Erro/Outro Status"
    print(f"Status Code {status_code} -> Mensagem: {mensagem}")

    # Operador ternário atribuindo classe de log
    nivel_log = "ERROR"
    prefixo = "[CRITICO]" if nivel_log == "CRITICAL" or nivel_log == "ERROR" else "[INFO]"
    print(f"Log Level: {nivel_log} -> Prefixo: {prefixo}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Processador de Pedidos de E-commerce
# ==========================================================
def processar_pedido_antipattern(pedido: dict[str, Any] | None) -> str:
    """
    ❌ ABORDAGEM ANINHADA (ARROW ANTI-PATTERN):
    Leitura difícil, muitas camadas de indentação.
    """
    if pedido is not None:
        if "itens" in pedido and len(pedido["itens"]) > 0:
            if pedido.get("pagamento_confirmado"):
                if pedido.get("cliente_ativo"):
                    return "Pedido Processado com Sucesso!"
                else:
                    return "Erro: Cliente Inativo"
            else:
                return "Erro: Pagamento Nao Confirmado"
        else:
            return "Erro: Pedido sem itens"
    else:
        return "Erro: Pedido Nulo"


def processar_pedido_clean_code(pedido: dict[str, Any] | None) -> str:
    """
    ✅ ABORDAGEM CLEAN CODE (EARLY RETURN / GUARD CLAUSES):
    Trata erros primeiro, mantém o fluxo principal limpo e linear sem aninhamento!
    """
    if pedido is None:
        return "Erro: Pedido Nulo"

    if not pedido.get("itens"):
        return "Erro: Pedido sem itens"

    if not pedido.get("pagamento_confirmado"):
        return "Erro: Pagamento Nao Confirmado"

    if not pedido.get("cliente_ativo"):
        return "Erro: Cliente Inativo"

    # Happy Path (Caminho Feliz) sem indentação profunda!
    return "Pedido Processado com Sucesso!"


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de Estruturas Condicionais:
- Complexidade Temporal: O(1) [Constante] para cada comparação de igualdade ou booleanos.
- Complexidade Espacial: O(1).

Dica de Desempenho:
Em cadeias longas de `if / elif`, coloque as condições com maior probabilidade de serem verdadeiras
ou computacionalmente mais baratas NO INÍCIO para tirar proveito da avaliação de curto-circuito.
"""


# ==========================================================
# 5. COMPARATIVO: CÓDIGO ANINHADO VS CÓDIGO LIMPO
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE ARQUITETURA DE CÓDIGO ---")

    pedido_invalido = {"itens": ["Livro Python"], "pagamento_confirmado": False}

    res_ruim = processar_pedido_antipattern(pedido_invalido)
    res_bom = processar_pedido_clean_code(pedido_invalido)

    print(f"Resultado Antipattern: {res_ruim}")
    print(f"Resultado Clean Code: {res_bom}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Aninhar operadores ternários (leitura extremamente confusa!)
    score = 85
    # ❌ Evite ternários aninhados como este:
    resultado_confuso = "A" if score > 90 else ("B" if score > 80 else "C")
    print(f"Ternario Aninhado (Evite!): score {score} -> {resultado_confuso}")

    # Armadilha 2: Comparar com True de forma redundante (`if condicao == True:`)
    is_valido = True
    if is_valido:  # ✅ Forma limpa e correta em Python
        print("Valido via 'if is_valido:'")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é Cyclomatic Complexity (Complexidade Ciclomática) e como o padrão Early Return ajuda a reduzi-la?"
A: "Complexidade Ciclomática mede a quantidade de caminhos de execução independentes no código.
    Cada `if`, `elif`, `for`, `while` incrementa essa métrica.
    O padrão Early Return elimina blocos `else` desnecessários e desaninha o código, tornando a função
    muito mais fácil de testar (menos branch coverage necessário por função) e de manter."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função `validar_transacao_bancaria(saldo: float, valor: float, conta_bloqueada: bool)`
#              utilizando Guard Clauses (Early Return) para tratar os cenários de erro antes do saque.
# Exercício 2: Reescreva uma cadeia de `if / else` de classificação de frete utilizando o operador ternário apenas onde for legível.


def main() -> None:
    print("==========================================================")
    print("  AULA 04: CONDICIONAIS E EARLY RETURNS (CLEAN CODE)")
    print("==========================================================")
    print(demonstrar_condicionais_basicas(25))
    demonstrar_operador_ternario()
    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 04 executado com sucesso.")


if __name__ == "__main__":
    main()
