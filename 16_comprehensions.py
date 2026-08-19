"""
16_comprehensions.py - Comprehensions (List, Set, Dict) e Generator Expressions

Objetivos:
1. Dominar a sintaxe idiomática de List, Set e Dict Comprehensions em Python 3.12+.
2. Compreender Generator Expressions (Avaliação Preguiçosa e Economia de Memória).
3. Entender a otimização de bytecode no CPython (`LIST_APPEND` vs `.append()`).
4. Reconhecer limites de legibilidade: quando usar Comprehension vs Loop Tradicional.
"""

import sys

# ==========================================================
# 1. CONCEITO: Por que Comprehensions são Mais Rápidas?
# ==========================================================
"""
No CPython, uma List Comprehension NÃO é apenas um "açúcar sintático" para um loop `for`.

Diferença de Bytecode:
- Loop `for` com `lista.append(x)`:
  Faz um lookup de atributo `.append` a CADA iteração + chamada de função via pilha CPython.
- List Comprehension:
  Executa a instrução especializada em C chamada `LIST_APPEND`, evitando o lookup de atributo
  e reduzindo substancialmente a sobrecarga de chamadas de função!

Tabela de Sintaxe de Comprehensions:
-----------------------------------------------------------------------------
Tipo                    Sintaxe                                    Retorno
-----------------------------------------------------------------------------
List Comprehension      `[expr for item in iter if cond]`           `list` (Eager)
Set Comprehension       `{expr for item in iter if cond}`           `set` (Eager)
Dict Comprehension      `{key: val for item in iter if cond}`       `dict` (Eager)
Generator Expression    `(expr for item in iter if cond)`           `generator` (Lazy)
-----------------------------------------------------------------------------
"""


def demonstrar_list_set_dict_comprehensions() -> None:
    print("\n--- 1. CONCEITO: List, Set e Dict Comprehensions ---")

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 1. List Comprehension com Filtro (`if` no final)
    pares_ao_quadrado = [n**2 for n in numeros if n % 2 == 0]
    print(f"Pares ao quadrado (List Comprehension): {pares_ao_quadrado}")

    # 2. List Comprehension com Operador Ternário (Transformação `if-else` antes do `for`)
    rotulos = ["Par" if n % 2 == 0 else "Ímpar" for n in numeros]
    print(f"Rótulos Par/Ímpar: {rotulos[:5]}...")

    # 3. Set Comprehension (Gera conjunto de valores únicos)
    palavras = ["python", "java", "python", "c++", "go", "java"]
    tamanhos_unicos = {len(p) for p in palavras}
    print(f"Tamanhos únicos de palavras (Set Comprehension): {tamanhos_unicos}")

    # 4. Dict Comprehension (Mapeamento chave-valor)
    quadrados_dict = {n: n**2 for n in numeros if n <= 5}
    print(f"Mapeamento número -> quadrado (Dict Comprehension): {quadrados_dict}")


# ==========================================================
# 2. GENERATOR EXPRESSIONS: AVALIAÇÃO PREGUIÇOSA (LAZY)
# ==========================================================
def demonstrar_generator_expressions() -> None:
    print("\n--- 2. EXEMPLO: Memory Footprint (List vs Generator Expression) ---")

    TAMANHO = 1_000_000

    # List Comprehension: Aloca TODOS os 1.000.000 de inteiros na memória de uma só vez (Eager)
    lista_gigante = [x * 2 for x in range(TAMANHO)]

    # Generator Expression: Cria um iterador que calcula o próximo valor SOB DEMANDA (Lazy)
    generator_gigante = (x * 2 for x in range(TAMANHO))

    tamanho_memoria_lista = sys.getsizeof(lista_gigante)
    tamanho_memoria_gen = sys.getsizeof(generator_gigante)

    print(f"Memória alocada para List Comprehension ({TAMANHO} itens): {tamanho_memoria_lista / (1024 * 1024):.2f} MB")
    print(f"Memória alocada para Generator Expression ({TAMANHO} itens): {tamanho_memoria_gen} bytes")
    print(f"[*] Economia de memória com Generator Expression: {tamanho_memoria_lista / max(tamanho_memoria_gen, 1):.0f}x menor!")


# ==========================================================
# 3. BOA PRÁTICA: QUANDO NÃO USAR COMPREHENSIONS (ABUSO)
# ==========================================================
def demonstrar_boas_praticas() -> None:
    print("\n--- 3. LEGIBILIDADE: Evitando Abuso de Comprehensions ---")

    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # [X] RUIM: Comprehension aninhada complexa que prejudica a leitura do código
    flat_complexo = [num for linha in matriz for num in linha if num % 2 == 0]

    # [OK] BOM / PYTHONIC: Se a lógica for muito complexa, prefira loops claros ou funções auxiliares!
    flat_claro: list[int] = []
    for linha in matriz:
        for num in linha:
            if num % 2 == 0:
                flat_claro.append(num)

    print(f"Matriz achatada (Apenas pares): {flat_complexo}")
    print("  -> Regra de Ouro Sênior: Se a comprehension exige mais de um `for` ou múltiplas linhas para ser lida, prefira um loop tradicional!")


# ==========================================================
# 4. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Efeitos colaterais dentro de Comprehension (ex: print())
    # Comprehensions são para CRIAR dados, NÃO para executar procedimentos sem retorno!
    # [X] RUIM: `[print(x) for x in range(5)]` -> Gera uma lista inútil de `[None, None, ...]`!

    # Armadilha 2: Tentar reutilizar um Generator Expression já esgotado
    gen = (n for n in range(3))
    print(f"Primeiro consumo do generator: {list(gen)}")
    print(f"Segundo consumo do MESMO generator (Esgotado!): {list(gen)}")


# ==========================================================
# 5. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Qual é a diferença funcional e de performance entre `sum([x for x in range(10000)])` e `sum(x for x in range(10000))`?"
A: "O primeiro passa uma List Comprehension inteira como argumento, alocando uma lista temporária
    com 10.000 inteiros na memória Heap.
    O segundo passa uma Generator Expression direta. O `sum()` consome o iterador elemento a elemento
    em O(1) memória espacial sem alocar a lista intermediária."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Dado um dicionário de produtos e preços `{"caneta": 2.50, "caderno": 15.00, "borracha": 1.20}`,
#              use Dict Comprehension para criar um novo dict aplicando um desconto de 10% apenas nos produtos que custam mais de R$ 2,00.
# Exercício 2: Escreva uma Generator Expression que gere o quadrado de todos os números de 1 a 1.000.000,
#              e utilize a função `next()` para consumir apenas os 3 primeiros valores.


def main() -> None:
    print("==========================================================")
    print("  AULA 16: COMPREHENSIONS E GENERATOR EXPRESSIONS")
    print("==========================================================")
    demonstrar_list_set_dict_comprehensions()
    demonstrar_generator_expressions()
    demonstrar_boas_praticas()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 16 executado com sucesso.")


if __name__ == "__main__":
    main()
