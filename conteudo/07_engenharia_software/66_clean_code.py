"""
66_clean_code.py - Princípios de Clean Code, Nomenclatura Expressiva e Refatoração em Python

Objetivos:
1. Dominar os princípios de Clean Code (Código Limpo) adaptados para a linguagem Python.
2. Aplicar Nomenclatura Intencional (Intention-Revealing Names) para variáveis, funções e classes.
3. Projetar funções pequenas com Responsabilidade Única (SRP no nível de função).
4. Eliminar o antipadrão de Flag Arguments (`flag=True`) e magic numbers no código.
5. Escrever código autodocumentável minimizando comentários redundantes.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Clean Code em Python?
Clean Code (Código Limpo) é aquele que é simples, direto, expressivo e fácil de ser lido e mantido por qualquer desenvolvedor da equipe.

Regras Fundamentais de Clean Code:
1. Nomes Significativos: Nomes de variáveis e funções devem revelar a intenção.
   - Ruim: `def proc(d, t): ...`
   - Bom: `def processar_pagamento(dados_cartao: dict, valor_total: float): ...`
2. Funções Pequenas e Focadas: Uma função deve fazer Apenas Uma Coisa (Do One Thing) e fazê-la bem.
3. Limite de Parâmetros: O número ideal de parâmetros de uma função é de 0 a 2.
4. Evite Flag Arguments (`flag=True`): Parâmetros booleanos indicam que a função faz mais de uma coisa. Divida em duas funções separadas.
5. Regra do Escoteiro (Boy Scout Rule): "Deixe o código mais limpo do que como você o encontrou."
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: REFATORAÇÃO DE CÓDIGO SUJO
# ==========================================================
# --- [X] CÓDIGO SUJO (DIRTY CODE) ---
def p_usr(u, a, f):
    """Função confusa, nomes obscuros, múltiplos parâmetros e flag booleana."""
    if f:
        if a > 18:
            return u.upper() + "_VIP"
        else:
            return u.lower()
    else:
        return "INATIVO"


# --- [OK] CÓDIGO LIMPO (CLEAN CODE REFATORADO) ---
IDADE_MINIMA_MAIORIDADE: int = 18


def formatar_usuario_vip(nome_usuario: str) -> str:
    return f"{nome_usuario.upper()}_VIP"


def formatar_usuario_comum(nome_usuario: str) -> str:
    return nome_usuario.lower()


def processar_perfil_usuario(nome_usuario: str, idade: int, conta_ativa: bool) -> str:
    """Função refatorada com responsabilidade clara e nomes autodocumentáveis."""
    if not conta_ativa:
        return "INATIVO"

    if idade >= IDADE_MINIMA_MAIORIDADE:
        return formatar_usuario_vip(nome_usuario)

    return formatar_usuario_comum(nome_usuario)


def demonstrar_fundamentos_clean_code() -> None:
    print("\n--- 1. FUNDAMENTOS: Refatoração Clean Code ---")

    res_sujo = p_usr("gabriel", 25, True)
    res_limpo = processar_perfil_usuario("gabriel", 25, conta_ativa=True)

    print(f"Resultado do Código Sujo: {res_sujo}")
    print(f"Resultado do Código Limpo: {res_limpo}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ELIMINANDO MAGIC NUMBERS
# ==========================================================
# [X] RUIM: Magic numbers soltos sem explicação
def calcular_imposto_ruim(valor: float) -> float:
    return valor * 0.275 - 896.00  # O que significa 0.275 e 896.00?


# [OK] BOM: Constantes nomeadas expressivas
ALIQUOTA_IMPOSTO_RENDA_MAXIMA: float = 0.275
PARCELA_DEDUTIVEL_IMPOSTO: float = 896.00


def calcular_imposto_renda(valor_bruto: float) -> float:
    """Calcula imposto de renda com constantes nomeadas."""
    return (valor_bruto * ALIQUOTA_IMPOSTO_RENDA_MAXIMA) - PARCELA_DEDUTIVEL_IMPOSTO


def demonstrar_magic_numbers() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Eliminando Magic Numbers ---")
    imposto = calcular_imposto_renda(5000.00)
    print(f"Imposto de Renda Calculado: R$ {imposto:.2f}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class OrderValidationService:
    """Serviço backend com validações encapsuladas e expressivas."""

    @staticmethod
    def validar_pedido_para_checkout(pedido: dict[str, Any]) -> None:
        OrderValidationService._validar_itens_nao_vazios(pedido.get("itens", []))
        OrderValidationService._validar_cliente_ativo(pedido.get("cliente", {}))

    @staticmethod
    def _validar_itens_nao_vazios(itens: list[Any]) -> None:
        if not itens:
            raise ValueError("O pedido deve conter pelo menos um item.")

    @staticmethod
    def _validar_cliente_ativo(cliente: dict[str, Any]) -> None:
        if not cliente.get("ativo", False):
            raise PermissionError("Cliente encontra-se inativo no sistema.")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Order Validation Service ---")
    pedido_valido = {"itens": [{"id": 1}], "cliente": {"ativo": True}}

    try:
        OrderValidationService.validar_pedido_para_checkout(pedido_valido)
        print("  [Clean Code] Pedido validado com sucesso!")
    except Exception as e:
        print(f"  [Erro] {e}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: COGNITIVE COMPLEXITY
# ==========================================================
"""
Complexidade Cognitiva (Cognitive Complexity):
1. É a métrica de quão difícil um bloco de código é para a mente humana compreender.
2. Loops aninhados (`for` dentro de `for`), múltiplos `if/else` encadeados e retornos no meio do código aumentam drasticamente a complexidade cognitiva.
3. Clean Code visa manter a Complexidade Cognitiva de cada função o mais próxima de 1 possível.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Funções refatoradas em Clean Code mantêm a mesma complexidade assintótica O(N) do código original, porém ganham legibilidade e testabilidade.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Comentários que apenas repetem o que o código faz
    print("[X] Nao-Pythonic (Comentários redundantes):")
    print("  i = i + 1  # Incrementa o i em 1 (Comentário inútil!)")

    # [OK] PYTHONIC: Código limpo e autodocumentável
    print("\n[OK] Pythonic:")
    print("  contador_tentativas += 1  # O próprio nome da variável explica o propósito!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize nomes de funções no verbo imperativo (`calcular_desconto()`, `enviar_email()`).
2. Utilize nomes de classes em substantivos (`UsuarioRepository`, `OrderService`).
3. Limite o tamanho de cada função a no máximo 15-20 linhas de código.
4. Prefira Early Returns (`guard clauses`) para eliminar aninhamentos profundos de `if/else`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Flag Arguments (Passar booleano como argumento de comportamento)
    print("[!] Armadilha 1: Passar `processar(dados, enviar_email=True)` viola o SRP. Crie `processar_e_notificar()` ou separe as responsabilidades.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que são Guard Clauses (Cláusulas de Guarda) e como elas ajudam a melhorar o Clean Code em Python?"
A: "Guard Clauses são verificações de pré-condição colocadas logo no início da função que retornam ou lançam uma exceção antecipadamente.
    Elas eliminam a necessidade de aninhar múltiplos blocos `if/else` profundos (Código em forma de Pirâmide),
    mantendo o fluxo principal do código alinhado à esquerda e facilitando a leitura sequencial da função."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Refatore a função `def calc(x, y, z): return x * y - z` aplicando nomenclatura limpa e Type Hints.
# Exercício 2: Substitua um bloco com 3 `if` aninhados por Guard Clauses com retornos antecipados.
# Exercício 3: Identifique e elimine 2 magic numbers em um código financeiro criando constantes com `UPPER_SNAKE_CASE`.


def main() -> None:
    print("==========================================================")
    print("  AULA 66: PRINCÍPIOS DE CLEAN CODE E NOMENCLATURA")
    print("==========================================================")
    demonstrar_fundamentos_clean_code()
    demonstrar_magic_numbers()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 66 executado com sucesso.")


if __name__ == "__main__":
    main()
