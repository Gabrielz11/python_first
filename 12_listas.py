"""
12_listas.py - Estrutura de Dados List (Array Dinâmico) e Análise de Complexidade Big O

Objetivos:
1. Dominar a estrutura `list` em Python 3.12+: criação, slicing, mutabilidade e métodos de manipulação.
2. Compreender a implementação interna do CPython (Array Dinâmico de Ponteiros).
3. Analisar exaustivamente a complexidade Big O temporal e espacial de cada operação em listas.
4. Diferenciar Cópias Rasas (Shallow Copy) de Cópias Profundas (Deep Copy).
"""

import copy

# ==========================================================
# 1. CONCEITO: Como a `list` Funciona Internamente no CPython?
# ==========================================================
"""
Em CPython, uma `list` NÃO é uma lista encadeada (Linked List)!
Ela é um ARRAY DINÂMICO DE PONTEIROS para objetos na Heap.

Características do Array Dinâmico:
- Reserva um bloco contíguo de endereços de memória contendo ponteiros.
- Possui um tamanho alocado superior ao tamanho atual (Over-allocation) para amortizar o custo de novos appends.

Tabela de Complexidade Temporal (Big O) da List:
-----------------------------------------------------------------------------
Operação                      Sintaxe                  Complexidade Big O
-----------------------------------------------------------------------------
Acesso por Índice             `lista[i]`               O(1) [Constante]
Atribuição por Índice         `lista[i] = x`           O(1) [Constante]
Adicionar ao Final            `lista.append(x)`        O(1) Amortizado
Remover do Final              `lista.pop()`            O(1) [Constante]
Inserir no Início/Meio        `lista.insert(0, x)`     O(n) [Desloca elementos!]
Remover do Início/Meio        `lista.pop(0)`           O(n) [Desloca elementos!]
Busca por Valor               `x in lista`             O(n) [Busca Linear]
Remover por Valor             `lista.remove(x)`        O(n) [Busca + Deslocamento]
Fatiamento (Slicing)          `lista[a:b]`             O(k) [k = b - a (cópia)]
Ordenação Nativa              `lista.sort()`           O(n log n) [Timsort]
-----------------------------------------------------------------------------
"""


def demonstrar_operacoes_basicas() -> None:
    print("\n--- 1. CONCEITO: Operações e Métodos de Manipulação de Listas ---")

    frutas = ["Maçã", "Banana", "Laranja"]

    # Append (O(1) Amortizado): Adiciona ao final
    frutas.append("Uva")

    # Extend (O(k)): Adiciona múltiplos elementos de outro iterável ao final
    frutas.extend(["Manga", "Abacaxi"])

    # Insert (O(n)): Insere em posição específica deslocando os subsequentes para a direita
    frutas.insert(1, "Morango")

    print(f"Lista após append, extend e insert: {frutas}")

    # Pop (O(1) no final, O(n) no início/meio)
    ultimo_item = frutas.pop()  # Remove e retorna "Abacaxi" (O(1))
    primeiro_item = frutas.pop(0)  # Remove "Maçã" deslocando todos os outros (O(n))

    print(f"Item removido do final: '{ultimo_item}' | Item removido do início: '{primeiro_item}'")
    print(f"Lista restante: {frutas}")


# ==========================================================
# 2. EXEMPLOS: Shallow Copy vs Deep Copy
# ==========================================================
def demonstrar_copia_rasa_vs_profunda() -> None:
    print("\n--- 2. EXEMPLOS: Shallow Copy vs Deep Copy em Listas Aninhadas ---")

    # Lista contendo sub-listas mutáveis
    original = [[1, 2], [3, 4]]

    # 1. Cópia Rasa (Shallow Copy): Copia apenas o container principal. As sub-listas são O MESMO OBJETO na memória!
    copia_rasa = original.copy()  # ou original[:]

    # 2. Cópia Profunda (Deep Copy): Recursivamente duplica o container E todos os seus objetos internos!
    copia_profunda = copy.deepcopy(original)

    # Modificando o primeiro elemento da sub-lista interna no objeto original
    original[0][0] = 999

    print(f"Original modificado: {original}")
    print(f"Cópia Rasa (AFETADA pela modificação interna!): {copia_rasa}")
    print(f"Cópia Profunda (ISOLADA e intacta): {copia_profunda}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Gerenciador de Buffer/Fila (O Porquê de Evitar `list.pop(0)`)
# ==========================================================
def processar_fila_incompativel_pop0(pedidos: list[str]) -> None:
    """
    [X] ABORDAGEM INEFICIENTE O(n²) usando list como Fila (FIFO).
    A cada `pedidos.pop(0)`, o CPython precisa reindexar e mover n-1 ponteiros na memória!
    Para listas de 100.000 itens, isso causa degradação catastrófica de desempenho.
    """
    print("\n--- 3. EXEMPLO PRÁTICO: Custo de list.pop(0) vs deque ---")

    # Copiando para não alterar a entrada
    fila = pedidos.copy()
    processados = 0

    # Simulação: cada pop(0) custa O(n)
    while fila:
        item = fila.pop(0)  # O(n) a cada iteração! Total = O(n²)
        processados += 1

    print(f"Processados {processados} itens com pop(0). Complexidade Total = O(n²)")
    print("  -> Solução Sênior: Para filas FIFO, NUNCA use list.pop(0)! Use `collections.deque.popleft()` -> O(1)!")


# ==========================================================
# 4. COMPARATIVO: CÓDIGO INEFICIENTE VS CÓDIGO OTIMIZADO
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 4. COMPARATIVO DE PERFORMANCE ---")

    numeros = [5, 2, 9, 1, 7, 3]

    # [X] NÃO-PYTHONIC (Criar lista nova e buscar o menor manualmente):
    menor_val = numeros[0]
    for n in numeros:
        if n < menor_val:
            menor_val = n

    # [OK] PYTHONIC (Usar a função built-in `min()` em O(n)):
    menor_pythonic = min(numeros)
    print(f"[OK] Menor valor usando min(numeros): {menor_pythonic}")


# ==========================================================
# 5. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Criar lista de listas usando multiplicação `[[0] * 3] * 3`
    # Isso cria 3 referências para A MESMA sub-lista na memória!
    grade_errada = [[0] * 3] * 3
    grade_errada[0][0] = 1  # Modifica a coluna 0 de TODAS as linhas!
    print(f"[X] Grade criada com `[[0]*3]*3`: {grade_errada} (Modificou todas as linhas!)")

    # [OK] CORRETO (Usar List Comprehension para instanciar sub-listas distintas):
    grade_correta = [[0] * 3 for _ in range(3)]
    grade_correta[0][0] = 1
    print(f"[OK] Grade criada com List Comprehension: {grade_correta} (Modificou apenas a linha 0)")


# ==========================================================
# 6. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Qual é a complexidade temporal da inserção em uma `list` no Python e por que `append()` é O(1) Amortizado?"
A: "A inserção no final (`append`) é O(1) amortizado porque o CPython pré-aloca espaço extra (over-allocation).
    Quando a capacidade é excedida, o CPython aloca um novo bloco de memória cerca de 1.125x a 1.5x maior e copia os elementos.
    Como essa realocação acontece com pouca frequência, o custo médio por append permanece O(1).
    Já a inserção no início (`insert(0, val)`) é estritamente O(n) porque todos os n elementos existentes precisam ter seus ponteiros deslocados uma posição à direita."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função que receba uma lista de inteiros e remova todos os elementos duplicados
#              mantendo a ORDEM ORIGINAL de aparição em O(n) temporal (Dica: use dict.fromkeys ou um set auxiliar de visitados).
# Exercício 2: Dada uma lista de números, rotacione seus elementos k posições à direita usando slicing (ex: `[1, 2, 3, 4, 5]` com k=2 -> `[4, 5, 1, 2, 3]`).


def main() -> None:
    print("==========================================================")
    print("  AULA 12: ESTRUTURA DE DADOS LIST E ANÁLISE BIG O")
    print("==========================================================")
    demonstrar_operacoes_basicas()
    demonstrar_copia_rasa_vs_profunda()

    amostra_pedidos = [f"pedido_{i}" for i in range(1000)]
    processar_fila_incompativel_pop0(amostra_pedidos)

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 12 executado com sucesso.")


if __name__ == "__main__":
    main()
