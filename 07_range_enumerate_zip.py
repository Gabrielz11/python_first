"""
07_range_enumerate_zip.py - Iteração Idiomática com range(), enumerate() e zip()

Objetivos:
1. Dominar o gerador de sequências numéricas imutável `range(start, stop, step)`.
2. Compreender a iteração indexada elegante com `enumerate()`.
3. Iterar sobre múltiplas coleções simultaneamente com `zip()` e utilizar `strict=True` (Python 3.10+).
4. Entender por que `for i in range(len(lista))` é um antipadrão (código Não-Pythonic).
"""



# ==========================================================
# 1. CONCEITO: Por que `range(len(lista))` é um Antipadrão?
# ==========================================================
"""
Em C ou Java antigo, o acesso aos elementos de um array é feito indexando via `array[i]`.
Em Python, o laço `for` itera DIRETAMENTE sobre os OBJETOS da sequência.

Se você escreve:
    for i in range(len(lista)):
        item = lista[i]

Você está adicionando uma camada extra de indireção desnecessária (buscando a chave pelo índice a cada iteração).

Se você precisa APENAS dos elementos:
    for item in lista:

Se você precisa do ÍNDICE E do ELEMENTO ao mesmo tempo:
    for i, item in enumerate(lista):
"""


def demonstrar_range() -> None:
    print("\n--- 1. CONCEITO: Funcionamento do range() ---")

    # range(start, stop, step) é um objeto iterável imutável de memória O(1)!
    # Ele gera os números sob demanda (Lazy Evaluation).
    r = range(0, 10, 2)
    print(f"Objeto range: {r} | Convertido em lista: {list(r)}")
    print(f"Tamanho na memória de range(1_000_000): {range(1_000_000).__sizeof__()} bytes (Constante O(1))")


# ==========================================================
# 2. EXEMPLOS: `enumerate()` e `zip()`
# ==========================================================
def demonstrar_enumerate_e_zip() -> None:
    print("\n--- 2. EXEMPLOS: enumerate() e zip() ---")

    produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
    precos = [4500.00, 150.00, 300.00, 1200.00]
    estoque = [10, 50, 30, 15]

    # 1. Enumerate (Índice + Elemento, começando no índice 1)
    print("Listagem com Enumerate (start=1):")
    for idx, prod in enumerate(produtos, start=1):
        print(f"  Item #{idx}: {prod}")

    # 2. Zip (Agrupando 3 listas em paralelo em tuplas)
    print("\nListagem unificada com Zip:")
    for prod, preco, qtd in zip(produtos, precos, estoque, strict=False):
        print(f"  Produto: {prod:<10} | R$ {preco:>7.2f} | Estoque: {qtd} un")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Processador de Relatórios com `zip(strict=True)`
# ==========================================================
def processar_folha_pagamento(funcionarios: list[str], salarios: list[float]) -> dict[str, float]:
    """
    Usa zip(strict=True) do Python 3.10+ para garantir que ambas as listas possuem rigorosamente o mesmo tamanho.
    Se o tamanho for diferente, lança ValueError em vez de truncar silenciosamente!
    """
    print("\n--- 3. EXEMPLO PRÁTICO: Zip estrito (strict=True) ---")

    folha: dict[str, float] = {}

    try:
        # strict=True lança ValueError se as sequências tiverem tamanhos desiguais
        for func, sal in zip(funcionarios, salarios, strict=True):
            folha[func] = sal
    except ValueError as e:
        print(f"  [ERRO DE INTEGRIDADE] Listas com tamanhos divergentes! -> {e}")

    return folha


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade Temporal e Espacial de `range`, `enumerate` e `zip`:
- `range(n)`: Criação O(1) de tempo e O(1) de espaço (não aloca uma lista de n elementos na memória).
- `enumerate(sequencia)`: Gerador lazy. O(1) espaço adicional.
- `zip(seq1, seq2)`: Gerador lazy. O(1) espaço adicional. Iteração total leva O(min(n, m)) tempo.
"""


# ==========================================================
# 5. COMPARATIVO: NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    nomes = ["Alice", "Bob", "Charlie"]
    cargos = ["Dev Sênior", "Tech Lead", "Architect"]

    # [X] NÃO-PYTHONIC (Usando range(len()) para indexar duas listas):
    print("[X] Nao-Pythonic (range(len(nomes))):")
    for i in range(len(nomes)):
        nome = nomes[i]
        cargo = cargos[i]
        print(f"  {i}: {nome} -> {cargo}")

    # [OK] PYTHONIC (Usando enumerate() e zip()):
    print("\n[OK] Pythonic (zip + enumerate):")
    for i, (nome, cargo) in enumerate(zip(nomes, cargos, strict=False), start=1):
        print(f"  #{i}: {nome} -> {cargo}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: O `zip()` tradicional sem strict=True silencia dados truncados!
    l1 = [1, 2, 3, 4, 5]
    l2 = ["a", "b"]

    # Sem strict=True, o zip para na MENOR sequência, descartando 3, 4 e 5 sem avisar!
    resultado_truncado = list(zip(l1, l2, strict=False))
    print(f"Zip tradicional truncado (sem erro!): {resultado_truncado}")

    # Armadilha 2: Tentar reutilizar o mesmo objeto gerador de zip() ou enumerate() duas vezes.
    # Geradores em Python são EXAURÍVEIS (consumidos uma única vez).
    z = zip([1, 2], ["x", "y"], strict=False)
    list(z)  # Consome o gerador
    reuso = list(z)  # Agora está VAZIO!
    print(f"Reutilizando gerador zip exaurido: {reuso} (Lista Vazia)")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que `range(1_000_000)` não consome megabytes de memória em Python 3?"
A: "Em Python 3, `range` não é uma função que retorna uma lista, mas sim um tipo de sequência imutável 'lazy'.
    Ele calcula os valores sob demanda com base em seus atributos internos (start, stop, step) e utiliza
    espaço de memória constante O(1), independentemente do tamanho da faixa."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Dadas duas listas de números inteiros de mesmo tamanho, use `zip()` e uma compreensão de lista para
#              retornar a soma elemento a elemento das duas listas.
# Exercício 2: Use `enumerate()` para imprimir uma lista de tarefas concluídas, marcando com "[OK]" os índices pares e "[ ]" os ímpares.


def main() -> None:
    print("==========================================================")
    print("  AULA 07: ITERAÇÃO IDIOMÁTICA COM RANGE, ENUMERATE E ZIP")
    print("==========================================================")
    demonstrar_range()
    demonstrar_enumerate_e_zip()

    # Teste de folha de pagamento válida vs inválida
    funcs = ["Ana", "Bruno", "Carla"]
    sals = [12000.0, 15000.0, 18000.0]
    print(processar_folha_pagamento(funcs, sals))

    # Teste com erro de tamanho no Zip Estrito
    sals_incompleto = [12000.0]
    processar_folha_pagamento(funcs, sals_incompleto)

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 07 executado com sucesso.")


if __name__ == "__main__":
    main()
