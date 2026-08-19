"""
13_tuplas.py - Estrutura de Dados Tuple (Imutabilidade, Hashability e Desempenho)

Objetivos:
1. Dominar a estrutura `tuple` em Python 3.12+: criação, imutabilidade e unpacking.
2. Compreender a implementação interna do CPython (Armazenamento Estático e Freelist).
3. Entender Hashability: por que tuplas podem ser chaves de dicionários e elementos de sets.
4. Analisar a diferença de desempenho e pegada de memória entre `tuple` e `list`.
"""

import sys
from typing import Any

# ==========================================================
# 1. CONCEITO: Como a `tuple` Funciona Internamente no CPython?
# ==========================================================
"""
Em CPython, uma `tuple` é uma sequência IMUTÁVEL de referências a objetos.

Características Internas no CPython:
- Tamanho Fixo: Alocada em um único bloco contíguo de memória sem over-allocation.
- Custo de Alocação Menor: CPython mantém uma "Freelist" de tuplas pequenas descartadas
  para reutilizá-las rapidamente sem requisitar nova memória ao sistema operacional.
- Imutabilidade Contida: A tupla em si não pode ter seus ponteiros alterados após a criação.
  Porém, se contiver um objeto MUTÁVEL (ex: uma lista), o conteúdo do objeto mutável PODE mudar.

Tabela Comparativa: Tuple vs List
-----------------------------------------------------------------------------
Característica               Tuple                    List
-----------------------------------------------------------------------------
Mutabilidade                 Imutável                 Mutável
Tamanho na Memória           Menor (sem reservado)    Maior (com over-allocation)
Velocidade de Criação        Mais Rápida              Mais Lenta
Pode ser Chave de Dict?      Sim (se só tiver hash)   Não (unhashable)
Uso Típico                   Dados heterogêneos/fixos Coleções homogêneas/dinâmicas
-----------------------------------------------------------------------------
"""


def demonstrar_operacoes_basicas() -> None:
    print("\n--- 1. CONCEITO: Sintaxe, Unpacking e Tupla de 1 Elemento ---")

    # Sintaxe: Parênteses são opcionais, a vírgula é o que define a tupla!
    tupla_simples = (10, 20, 30)
    tupla_sem_parenteses = 40, 50, 60

    # ⚠️ ARMADILHA CLÁSSICA: Tupla de 1 elemento precisa de VÍRGULA!
    nao_e_tupla = (42)  # int!
    e_tupla = (42,)  # tuple!

    print(f"Tipo de (42): {type(nao_e_tupla)} | Tipo de (42,): {type(e_tupla)}")

    # Unpacking (Desempacotamento elegante)
    x, y, z = tupla_simples
    print(f"Unpacking (x, y, z): {x}, {y}, {z}")

    # Unpacking parcial usando `*` (Extended Unpacking)
    primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
    print(f"Extended Unpacking -> Primeiro: {primeiro} | Meio: {meio} | Último: {ultimo}")


# ==========================================================
# 2. HASHABILITY: Tuplas como Chaves de Dicionários / Sets
# ==========================================================
def demonstrar_hashability() -> None:
    print("\n--- 2. EXEMPLO: Hashability e Objetos Imutáveis ---")

    # Para ser chave de dicionário ou elemento de set, o objeto deve implementar __hash__ estável.
    coordenadas_cache: dict[tuple[float, float], str] = {
        (-23.5505, -46.6333): "São Paulo",
        (-22.9068, -43.1729): "Rio de Janeiro",
    }

    ponto = (-23.5505, -46.6333)
    cidade = coordenadas_cache.get(ponto, "Desconhecida")
    print(f"Busca por chave de tupla {ponto}: {cidade}")

    # Teste de Hash:
    print(f"Hash da tupla (1, 2): {hash((1, 2))}")


# ==========================================================
# 3. COMPARATIVO DE PERFORMANCE E MEMÓRIA: Tuple vs List
# ==========================================================
def demonstrar_desempenho_memoria() -> None:
    print("\n--- 3. COMPARATIVO: Pegada de Memória (sys.getsizeof) ---")

    elementos = list(range(1000))
    lista_ex = list(elementos)
    tupla_ex = tuple(elementos)

    tamanho_lista = sys.getsizeof(lista_ex)
    tamanho_tupla = sys.getsizeof(tupla_ex)

    print(f"Tamanho de List (1000 ints): {tamanho_lista} bytes")
    print(f"Tamanho de Tuple (1000 ints): {tamanho_tupla} bytes")
    print(f"Economia de memória com Tuple: {tamanho_lista - tamanho_tupla} bytes ({((tamanho_lista - tamanho_tupla) / tamanho_lista) * 100:.1f}%)")


# ==========================================================
# 4. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Modificar elemento mutável dentro de tupla imutável
    tupla_com_lista: tuple[Any, ...] = (1, 2, [10, 20])
    print(f"Tupla original com lista interna: {tupla_com_lista}")

    try:
        # Tentar atribuição com += gera TypeError E AINDA ASSIM altera a lista!
        tupla_com_lista[2] += [30, 40]
    except TypeError as e:
        print(f"[!] TypeError capturado ao tentar `+=` em tupla: {e}")

    # A lista FOI alterada internamente porque é o mesmo objeto na Heap!
    print(f"Resultado após a falha de atribuição: {tupla_com_lista} (A lista mudou!)")

    # Armadilha 2: Tentar usar tupla contendo lista como chave de dict
    try:
        dict_invalido = {tupla_com_lista: "teste"}
    except TypeError as e:
        print(f"[X] Não pode ser chave de dict se contiver elemento unhashable: {e}")


# ==========================================================
# 5. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Uma tupla em Python é sempre imutável e hashable?"
A: "A tupla é sempre imutável no nível do seu container (seus ponteiros não podem ser alterados).
    No entanto, ela SÓ É HASHABLE se TODOS os seus elementos internos também forem hashable.
    Se uma tupla contiver uma `list` ou outro objeto mutável, a chamada `hash(tupla)` lançará
    um `TypeError: unhashable type: 'list'`, impedindo seu uso como chave de dicionário ou em sets."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `obter_estatisticas(numeros: list[float]) -> tuple[float, float, float]`
#              que retorne a média, o valor mínimo e o valor máximo em uma única tupla desempacotável.
# Exercício 2: Escreva uma função que receba uma lista de tuplas `(nome, idade, nota)` e ordene
#              a lista prioritariamente pela nota (decrescente) e secundariamente pela idade (crescente).


def main() -> None:
    print("==========================================================")
    print("  AULA 13: ESTRUTURA DE DADOS TUPLE E HASHABILITY")
    print("==========================================================")
    demonstrar_operacoes_basicas()
    demonstrar_hashability()
    demonstrar_desempenho_memoria()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 13 executado com sucesso.")


if __name__ == "__main__":
    main()
