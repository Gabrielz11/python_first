"""
11_lambda.py - Funções Anônimas (Lambda), map(), filter() e Ordenação Customizada

Objetivos:
1. Compreender a sintaxe e limitações de funções anônimas (`lambda`).
2. Utilizar `lambda` com `sorted()`, `min()`, `max()`, `map()` e `filter()`.
3. Entender quando uma função nomeada (`def`) é amplamente preferível a uma expressão `lambda`.
4. Comparar `map()` e `filter()` com List Comprehensions idiomáticas.
"""

from typing import Any

# ==========================================================
# 1. CONCEITO: O que é uma Expressão Lambda em Python?
# ==========================================================
"""
Uma expressão `lambda` é uma forma concisa de definir uma FUNÇÃO ANÔNIMA (sem nome) em uma única linha.

Sintaxe:
lambda argumentos: expressao

Limitações Importantes em Python:
- Só pode conter UMA ÚNICA EXPRESSÃO.
- O resultado dessa expressão é retornado IMPLICITAMENTE (não se usa a palavra `return`).
- Não permite instruções compostas (como `if/else` em blocos, `try/except`, `for`, `while` ou atribuições com `=`).
- PEP 8 recomenda fortemente NÃO atribuir uma lambda a uma variável (`funcao = lambda x: ...`). Use `def` nesses casos!
"""


def demonstrar_lambda_basica() -> None:
    print("\n--- 1. CONCEITO: Expressão Lambda ---")

    # Lambda sendo usada inline como chave de ordenação
    usuarios = [
        {"nome": "Carla", "idade": 29, "score": 950},
        {"nome": "Bruno", "idade": 34, "score": 880},
        {"nome": "Ana", "idade": 22, "score": 990},
    ]

    # Ordenando por score usando lambda como parâmetro key=
    usuarios_ordenados = sorted(usuarios, key=lambda u: u["score"], reverse=True)

    print("Usuários ordenados por Score (Decrescente):")
    for u in usuarios_ordenados:
        print(f"  - {u['nome']}: Score {u['score']} (Idade {u['idade']})")


# ==========================================================
# 2. EXEMPLOS: Uso de Lambda com map() e filter()
# ==========================================================
def demonstrar_map_e_filter() -> None:
    print("\n--- 2. EXEMPLOS: map() e filter() ---")

    precos_brutos = [100.0, 250.0, 50.0, 400.0, 15.0]

    # 1. filter(): Filtra apenas os preços acima de R$ 80.0
    # Retorna um iterador Lazy!
    precos_altos = list(filter(lambda p: p > 80.0, precos_brutos))
    print(f"Preços filtrados (> R$ 80.0) com filter(): {precos_altos}")

    # 2. map(): Aplica imposto de 10% em cada preço
    # Retorna um iterador Lazy!
    precos_com_imposto = list(map(lambda p: round(p * 1.10, 2), precos_brutos))
    print(f"Preços transformados (+10%) com map(): {precos_com_imposto}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Ordenação Complexa de Pedidos em E-commerce
# ==========================================================
def processar_fila_pedidos(pedidos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Ordena pedidos por prioridade de entrega e depois pelo valor total.
    """
    print("\n--- 3. EXEMPLO PRÁTICO: Ordenação de Pedidos com Tupla de Chaves ---")

    # Ordenação multinível usando Tupla em Lambda:
    # 1º critério: Is VIP (True vem antes de False)
    # 2º critério: Valor do Pedido (Decrescente)
    pedidos_priorizados = sorted(
        pedidos,
        key=lambda p: (p["is_vip"], p["valor_total"]),
        reverse=True,
    )

    return pedidos_priorizados


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de Lambda com sorted(), map(), filter():
- `sorted(colecao, key=lambda ...)`: O(n log n) Temporal (Algoritmo Timsort nativo do Python).
- `map()` e `filter()`: O(n) Temporal e O(1) Espacial (pois são geradores Lazy consumidos sob demanda).

Comparativo de Performance:
- List Comprehensions (`[p * 1.1 for p in precos]`) costumam ser MAIS RÁPIDAS que `list(map(lambda p: ..., precos))`
  no CPython porque evitam o overhead da chamada de função para cada elemento!
"""


# ==========================================================
# 5. COMPARATIVO: MAP/FILTER VS LIST COMPREHENSION (PYTHONIC)
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO: Lambda/map/filter vs List Comprehension ---")

    valores = [1, 2, 3, 4, 5, 6]

    # [X] MENOS PYTHONIC (Verboso, exige list() e lambda):
    res_map = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, valores)))
    print(f"[X] Com map() e filter(): {res_map}")

    # [OK] PYTHONIC (Claro, legível e mais rápido em Python):
    res_comp = [x * 2 for x in valores if x % 2 == 0]
    print(f"[OK] Com List Comprehension: {res_comp}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Atribuir uma lambda a uma variável (Atrapalha Tracebacks e fere PEP 8)
    # [X] Evite:
    # somar = lambda a, b: a + b

    # [OK] Prefira:
    def somar(a: float, b: float) -> float:
        return a + b

    print(f"[OK] Usando def em vez de atribuir lambda: somar(5, 10) = {somar(5, 10)}")

    # Armadilha 2: Late Binding em lambdas dentro de laços de repetição (Closure em Loop)!
    multiplicadores = [lambda x: x * i for i in range(3)]
    # Esperado: 0, 1, 2. Mas como `i` é avaliado tardiamente, todas usam i=2!
    resultados = [m(10) for m in multiplicadores]
    print(f"[!] Armadilha Late Binding em Loop: {resultados} (Todas usam i=2 final!)")

    # [OK] Solução para Late Binding: passar default argument `i=i` no lambda
    multiplicadores_corretos = [lambda x, i=i: x * i for i in range(3)]
    res_correto = [m(10) for m in multiplicadores_corretos]
    print(f"[OK] Solução Late Binding (i=i): {res_correto}")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual o problema do Late Binding em funções lambdas criadas dentro de um loop e como corrigi-lo?"
A: "Em Python, o escopo da variável iteradora é resolvido quando a lambda é EXECUTADA, e não quando ela é DEFINIDA.
    Isso faz com que todas as lambdas vejam o último valor assumido pela variável do loop.
    A correção consiste em capturar o valor no momento da definição utilizando parâmetros padrão (`lambda x, i=i: x * i`)."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Dada uma lista de tuplas `[(1, "B"), (3, "A"), (2, "C")]`, ordene pelo segundo elemento da tupla usando `lambda`.
# Exercício 2: Reescreva o filtro `list(filter(lambda x: x.startswith("A"), lista_strings))` utilizando uma List Comprehension.


def main() -> None:
    print("==========================================================")
    print("  AULA 11: FUNÇÕES ANÔNIMAS (LAMBDA), MAP, FILTER E SORTED")
    print("==========================================================")
    demonstrar_lambda_basica()
    demonstrar_map_e_filter()

    lista_pedidos = [
        {"id": 1, "is_vip": False, "valor_total": 500.0},
        {"id": 2, "is_vip": True, "valor_total": 150.0},
        {"id": 3, "is_vip": True, "valor_total": 890.0},
    ]
    p_ord = processar_fila_pedidos(lista_pedidos)
    print(f"Pedidos Priorizados: {p_ord}")

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 11 executado com sucesso.")


if __name__ == "__main__":
    main()
