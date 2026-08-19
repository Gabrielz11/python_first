"""
08_funcoes.py - Funções, Assinaturas, Parâmetros Posicionais, Nomeados e Operadores / e *

Objetivos:
1. Dominar a criação de funções em Python 3.12+ utilizando `def` e `return`.
2. Compreender a diferença entre parâmetros e argumentos.
3. Utilizar valores padrão imutáveis com segurança.
4. Aplicar os operadores `/` (Positional-only) e `*` (Keyword-only) introduzidos na PEP 570 e PEP 3102.
5. Garantir o princípio Clean Code da Responsabilidade Única (Single Responsibility Principle).
"""



# ==========================================================
# 1. CONCEITO: Assinatura de Função e Operadores / e *
# ==========================================================
"""
Em Python moderno (3.8+), a assinatura de uma função pode restringir COMO os argumentos são passados:

Sintaxe Geral da Assinatura:
def funcao(pos_only1, pos_only2, /, pos_or_kw, *, kw_only1, kw_only2):

1. ` / ` (Barra): Todos os parâmetros À ESQUERDA da barra DEVEM ser passados APENAS por Posição.
   Tentativas de passá-los por nome (ex: `pos_only1="val"`) lançam TypeError.

2. ` * ` (Asterisco isolado): Todos os parâmetros À DIREITA do asterisco DEVEM ser passados APENAS por Nome (Keyword-only).
   Tentativas de passá-los por posição lançam TypeError.

Por que isso importa na Engenharia de Software?
- Positional-only (`/`): Permite renomear parâmetros internos na biblioteca sem quebrar a API dos clientes.
- Keyword-only (`*`): Força o chamador a ser explícito em parâmetros booleanos ou de configuração, aumentando a legibilidade.
"""


def calcular_desconto(
    preco_original: float,
    percentual_desconto: float,
    /,  # Posicional Apenas (Positional-only)
    *,
    imposto_adicional: float = 0.0,
    arredondar: bool = True,  # Keyword-only
) -> float:
    """Calcula o valor final de um produto aplicando desconto e imposto."""
    print(f"\n--- 1. CONCEITO: Calculando desconto em R$ {preco_original} ---")

    desconto = preco_original * (percentual_desconto / 100)
    preco_com_desconto = preco_original - desconto
    valor_final = preco_com_desconto + imposto_adicional

    if arredondar:
        return round(valor_final, 2)
    return valor_final


# ==========================================================
# 2. EXEMPLOS: Parâmetros Padrão e Retornos Múltiplos
# ==========================================================
def obter_estatisticas_numericas(valores: list[float]) -> tuple[float, float, float]:
    """
    Retorna uma tupla contendo (mínimo, máximo, média).
    Demonstração de retorno múltiplo desempacotável.
    """
    if not valores:
        return 0.0, 0.0, 0.0

    minimo = min(valores)
    maximo = max(valores)
    media = sum(valores) / len(valores)

    return minimo, maximo, media


# ==========================================================
# 3. EXEMPLO PRÁTICO: API Client de Envio de E-mail
# ==========================================================
def enviar_email(
    destinatario: str,
    assunto: str,
    corpo: str,
    /,  # Argumentos principais devem ser posicionais
    *,
    tentativas_retry: int = 3,
    prioridade_alta: bool = False,
) -> bool:
    """
    Função de infraestrutura com parâmetros explícitos.
    """
    print(f"\n--- 3. EXEMPLO PRÁTICO: Enviando e-mail para '{destinatario}' ---")
    print(f"  Assunto: {assunto}")
    print(f"  Configurações -> Retry: {tentativas_retry} | Alta Prioridade: {prioridade_alta}")
    return True


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de Chamada de Função em Python:
- Chamada de Função (`funcao()`): O(1) Temporal para criação do Frame na Stack.
- Passagem de Argumentos: O(1) [Apenas cópia do ponteiro do objeto na memória!].
- Retorno de múltiplos valores: O(1) de tempo (criação de uma tupla imutável leve).
"""


# ==========================================================
# 5. COMPARATIVO: CÓDIGO CONFUSO VS CÓDIGO EXPLÍCITO (KEYWORD-ONLY)
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE LEGIBILIDADE ---")

    # [X] NÃO-PYTHONIC (Booleano solto como parâmetro positional: o que significa True, False?):
    # enviar_email("usr@mail.com", "Ola", "Texto", 3, True) # Difícil ler o que é '3' e 'True'

    # [OK] PYTHONIC (Keyword-only obriga a nomear os argumentos de configuração):
    print("[OK] Chamada com Keyword-only explícita:")
    enviar_email("usr@mail.com", "Boas-vindas", "Seja bem-vindo!", tentativas_retry=5, prioridade_alta=True)


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha Fatal em Python: Usar Objetos Mutáveis (como list/dict) em Valores Padrão de Parâmetros!
    # O valor padrão é avaliado APENAS UMA VEZ na definição da função (tempo de carregamento do módulo).
    # Todos os chamadores compartilham o MESMO objeto mutável!

    # [X] ERRADO:
    def adicionar_item_errado(item: str, lista: list[str] = []) -> list[str]:
        lista.append(item)
        return lista

    print("[X] Efeito Colateral de Default Mutavel (lista=[]):")
    res1 = adicionar_item_errado("Item A")
    res2 = adicionar_item_errado("Item B")  # Deveria ter apenas "Item B", mas herdou "Item A"!
    print(f"  Chamada 1: {res1}")
    print(f"  Chamada 2 (Poluida!): {res2}")

    # [OK] CORRETO (Padrão Sentinel `None`):
    def adicionar_item_correto(item: str, lista: list[str] | None = None) -> list[str]:
        if lista is None:
            lista = []
        lista.append(item)
        return lista

    print("\n[OK] Padrão Correto com Sentinel `None` (lista=None):")
    c1 = adicionar_item_correto("Item A")
    c2 = adicionar_item_correto("Item B")
    print(f"  Chamada 1: {c1}")
    print(f"  Chamada 2: {c2}")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista (Pegadinha Sênior):
Q: "O que acontece se definirmos `def func(a, b=[])` em Python?"
A: "O objeto lista vazia `[]` é instanciado uma única vez durante a definição/compilação da função.
    Caso a função modifique a lista, todas as invocações subsequentes que não passarem o parâmetro `b`
    vão mutar e reutilizar essa mesma lista na memória. A solução correta é definir `b: list | None = None`
    e instanciar uma nova lista dentro da função."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função de busca em banco de dados `buscar_usuarios(query, /, *, limite=10, offset=0)`
#              garantindo que `query` seja estritamente posicional e `limite`/`offset` sejam estritamente nomeados.
# Exercício 2: Escreva uma função que calcule a média ponderada de uma lista de notas e seus pesos correspondentes,
#              retornando tanto a média final quanto o status "Aprovado" ou "Reprovado".


def main() -> None:
    print("==========================================================")
    print("  AULA 08: FUNÇÕES, ASSINATURAS E PARÂMETROS POSICIONAIS/NOMEADOS")
    print("==========================================================")

    # Chamada válida respeitando Positional-only e Keyword-only
    valor_final = calcular_desconto(100.0, 15.0, imposto_adicional=5.0, arredondar=True)
    print(f"Valor Final Calculado: R$ {valor_final}")

    # Retorno múltiplo com unpacking
    notas = [7.5, 8.0, 9.5, 6.0, 10.0]
    v_min, v_max, v_med = obter_estatisticas_numericas(notas)
    print(f"Estatísticas: Mín={v_min}, Máx={v_max}, Média={v_med:.2f}")

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 08 executado com sucesso.")


if __name__ == "__main__":
    main()
