"""
21_any_all_sorted.py - Utilitários Nativos: any(), all(), sorted() e Algoritmo Timsort

Objetivos:
1. Dominar o comportamento de avaliação por curto-circuito (Short-Circuit Evaluation) das funções `any()` e `all()`.
2. Compreender a diferença fundamental entre `sorted()` (retorna nova lista) e `list.sort()` (ordenação in-place).
3. Utilizar o parâmetro `key` com `lambda` e funções auxiliares do módulo `operator` (`attrgetter`, `itemgetter`).
4. Entender o funcionamento do algoritmo nativo de ordenação de Python (Timsort) e sua estabilidade.
5. Aplicar validações booleanas e ordenação de DTOs em serviços de backend.
"""

import operator
from typing import NamedTuple


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são any(), all() e sorted()?
São funções built-in de alta performance em CPython projetadas para processar iteráveis de forma limpa e otimizada:

1. any(iterable): Retorna True se pelo menos UM elemento do iterável for avaliado como Truthy.
   Possui curto-circuito: Interrompe a execução assim que encontra o PRIMEIRO elemento True.

2. all(iterable): Retorna True se TODOS os elementos do iterável forem avaliados como Truthy.
   Possui curto-circuito: Interrompe a execução assim que encontra o PRIMEIRO elemento False.

3. sorted(iterable, key=None, reverse=False): Retorna uma NOVA lista contendo todos os elementos
   do iterável ordenados. Utiliza o algoritmo Timsort (híbrido entre Merge Sort e Insertion Sort).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ANY E ALL COM CURTO-CIRCUITO
# ==========================================================
def demonstrar_any_e_all() -> None:
    print("\n--- 1. FUNDAMENTOS: any() e all() com Curto-Circuito ---")

    status_servidores = [True, True, False, True]

    # Todos os servidores estão online?
    todos_online = all(status_servidores)
    print(f"Todos os servidores estao online (all)? {todos_online}")

    # Existe pelo menos um servidor online?
    algum_online = any(status_servidores)
    print(f"Existe pelo menos um servidor online (any)? {algum_online}")

    # Demonstrando Short-Circuit com Gerador
    def verificar_item(n: int) -> bool:
        print(f"  [Log Interno] Checando elemento: {n}")
        return n > 10

    numeros = [1, 5, 12, 20, 30]
    print("Executando any() com gerador (interrompe no 12):")
    tem_maior_que_dez = any(verificar_item(x) for x in numeros)
    print(f"Resultado any: {tem_maior_que_dez}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SORTED() E OPERATOR.ATTRGETTER
# ==========================================================
class Transacao(NamedTuple):
    id: int
    valor: float
    categoria: str


def demonstrar_ordenacao_customizada() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: sorted() e operator.attrgetter ---")

    transacoes = [
        Transacao(1, 450.0, "Alimentacao"),
        Transacao(2, 1200.0, "Eletronicos"),
        Transacao(3, 150.0, "Transporte"),
        Transacao(4, 1200.0, "Viagem"),
    ]

    # 1. Ordenação por valor crescente (usando lambda)
    por_valor = sorted(transacoes, key=lambda t: t.valor)
    print("Ordenado por valor (crescente):")
    for t in por_valor:
        print(f"  ID {t.id}: R$ {t.valor:.2f} ({t.categoria})")

    # 2. Ordenação por Múltiplos Critérios: Valor Decrescente, Categoria Crescente
    # Utilizando operator.attrgetter para maior performance em CPython
    por_multiplos_criterios = sorted(
        transacoes,
        key=operator.attrgetter("valor", "categoria"),
        reverse=True,
    )
    print("\nOrdenado por valor (decrescente) e categoria:")
    for t in por_multiplos_criterios:
        print(f"  ID {t.id}: R$ {t.valor:.2f} ({t.categoria})")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class RegraValidacaoUsuario:
    """Motor de validação de elegibilidade de usuários em checkout."""

    @staticmethod
    def validar_requisitos(usuario: dict[str, bool]) -> tuple[bool, str]:
        # Tabela de requisitos de elegibilidade
        requisitos = [
            (usuario.get("email_verificado", False), "Email nao verificado"),
            (usuario.get("maior_de_idade", False), "Usuario menor de idade"),
            (not usuario.get("conta_bloqueada", True), "Conta encontra-se bloqueada"),
        ]

        # all() garante que TODOS os critérios sejam satisfeitos
        elegivel = all(status for status, _ in requisitos)

        if elegivel:
            return True, "Elegivel para compra"
        
        # Encontra a primeira falha para relatar
        falhas = [msg for status, msg in requisitos if not status]
        return False, f"Reprovado: {', '.join(falhas)}"


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Validador de Elegibilidade de Checkout ---")
    user_ok = {"email_verificado": True, "maior_de_idade": True, "conta_bloqueada": False}
    user_suspeito = {"email_verificado": True, "maior_de_idade": False, "conta_bloqueada": False}

    print(f"User OK: {RegraValidacaoUsuario.validar_requisitos(user_ok)}")
    print(f"User Suspeito: {RegraValidacaoUsuario.validar_requisitos(user_suspeito)}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: TIMSORT E ESTABILIDADE
# ==========================================================
"""
Como o Python ordena (Timsort):
1. Desenvolvido por Tim Peters em 2002 para o CPython.
2. É um algoritmo derivado do Merge Sort e Insertion Sort.
3. Identifica "runs" (sub-sequências que já estão naturalmente ordenadas nos dados de entrada).
4. É um algoritmo ESTÁVEL (Stable Sort): Se dois elementos possuem chaves de ordenação iguais,
   a sua ordem relativa original no iterável de entrada é garantida e mantida intacta.

Diferença entre sorted(x) e x.sort():
- `sorted(x)`: Funciona com qualquer iterável e gera uma NOVA `list`.
- `x.sort()`: É um método exclusivo do tipo `list` que modifica os dados in-place (retorna None) economizando memória.
"""


def demonstrar_estabilidade_timsort() -> None:
    print("\n--- 4. INTERNO: Ordenacao Estavel (Stable Sort) ---")
    # Produtos originalmente em ordem de inserção (ID)
    produtos = [
        {"id": 1, "tipo": "A", "preco": 10},
        {"id": 2, "tipo": "B", "preco": 10},
        {"id": 3, "tipo": "A", "preco": 5},
    ]

    # Ordenar por preco mantém ID 1 antes de ID 2 (estabilidade)
    ordenados = sorted(produtos, key=operator.itemgetter("preco"))
    print("Produtos ordenados por preco (mantendo ordem original de IDs empatados):")
    for p in ordenados:
        print(f"  Preco {p['preco']} -> ID {p['id']}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `any()` e `all()`:
  - Tempo: O(N) no pior caso (quando precisa checar até o final), O(1) no melhor caso (curto-circuito imediato).
  - Espaço: O(1) quando usado com expressões geradoras `any(f(x) for x in lista)`.
- `sorted()` (Timsort):
  - Tempo Pior Caso: O(N log N).
  - Tempo Melhor Caso (dados pré-ordenados): O(N).
  - Espaço Adicional: O(N) para alocar a nova lista retornada.
- `list.sort()` (In-Place):
  - Tempo: O(N log N).
  - Espaço Adicional: O(N) interno para buffers do Timsort em C.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    precos = [12.0, 99.0, 5.0, 150.0]

    # [X] NÃO-PYTHONIC: Loop manual para checar se existe item barato
    print("[X] Nao-Pythonic (Loop manual com flag):")
    tem_barato = False
    for p in precos:
        if p < 10.0:
            tem_barato = True
            break
    print(f"  Tem item < 10: {tem_barato}")

    # [OK] PYTHONIC: any() com expressão geradora
    print("\n[OK] Pythonic:")
    tem_barato_py = any(p < 10.0 for p in precos)
    print(f"  Tem item < 10 (any): {tem_barato_py}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre passe expressões geradoras `any(x > 0 for x in dados)` para `any()` e `all()` em vez de List Comprehension `any([x > 0 for x in dados])` para preservar a memória e o curto-circuito.
2. Prefira `operator.itemgetter` ou `operator.attrgetter` no parâmetro `key` do `sorted()`. São escritos em C e mais rápidos que lambdas.
3. Lembre-se que `all([])` (lista vazia) retorna True (conceito de vacuous truth na lógica matemática).
4. Lembre-se que `any([])` (lista vazia) retorna False.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Usar List Comprehension dentro de any/all destrói o benefício do curto-circuito!
    contagem_execucoes = 0

    def f_com_side_effect(n: int) -> bool:
        nonlocal contagem_execucoes
        contagem_execucoes += 1
        return n == 1

    # [!] Errado: Cria a lista inteira ANTES de chamar any()
    _ = any([f_com_side_effect(x) for x in range(1, 100)])
    print(f"[!] Armadilha List Comprehension no any(): Executou {contagem_execucoes} vezes (Deveria ser 1!)")

    # [OK] Correto: Expressão geradora
    contagem_execucoes = 0
    _ = any(f_com_side_effect(x) for x in range(1, 100))
    print(f"[OK] Expressao Geradora no any(): Executou {contagem_execucoes} vez (Curto-circuito preservado!)")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual o resultado de `all([])` e `any([])` em Python e qual o raciocínio por trás?"
A: "1. `all([])` retorna `True`. O motivo é a regra matemática da Verdade Vaciosa (Vacuous Truth): 
       Como não existe nenhum elemento na lista vazia que infrinja a condição (não há nenhum False), a premissa é verdadeira.
    2. `any([])` retorna `False`. Como não existe nenhum elemento Truthy na lista vazia, a condição de haver ao menos um falha."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `todos_positivos(numeros: list[int]) -> bool` usando `all()`.
# Exercício 2: Dada uma lista de dicionários representando livros `[{"titulo": "X", "paginas": 300}, ...]`,
#              ordene os livros por número de páginas usando `sorted()` e `operator.itemgetter`.
# Exercício 3: Escreva uma função que verifique se uma string contém pelo menos um caractere maiúsculo,
#              pelo menos um dígito e pelo menos um caractere especial utilizando `any()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 21: UTILITÁRIOS NATIVOS: ANY(), ALL(), SORTED()")
    print("==========================================================")
    demonstrar_any_e_all()
    demonstrar_ordenacao_customizada()
    demonstrar_aplicacao_backend()
    demonstrar_estabilidade_timsort()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 21 executado com sucesso.")


if __name__ == "__main__":
    main()
