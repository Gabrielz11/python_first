"""
83_memory_management.py - Gerenciamento de Memória em Python, Reference Counting, Garbage Collector e __slots__

Objetivos:
1. Dominar o Modelo de Gerenciamento de Memória do CPython (Reference Counting + Cyclic Garbage Collector).
2. Utilizar a função `sys.getrefcount()` para inspecionar a contagem de referências de objetos.
3. Compreender a coleta de lixo por Gerações (Gerações 0, 1 e 2) e o módulo `gc`.
4. Entender o papel do alocador de pequenos objetos `PyMalloc`, Arenas e Pools.
5. Aplicar a otimização de economia extrema de memória RAM utilizando `__slots__` em classes com milhões de instâncias.
"""

import gc
import sys
from typing import Any


# ==========================================================
# 1. CONCEITO DE GERENCIAMENTO DE MEMÓRIA EM CPYTHON
# ==========================================================
"""
Como o CPython Gerencia a Memória RAM:
 O gerenciamento de memória em CPython e composto por duas camadas principais:

1. Contagem de Referências (Reference Counting - Primário):
   - Cada objeto possui o campo `ob_refcnt`.
   - Sempre que uma variável aponta para o objeto, o contador e INCREMENTADO.
   - Sempre que a variável sai de escopo ou e deletada (`del x`), o contador e DECREMENTADO.
   - Quando `ob_refcnt == 0`, o CPython LIBERA a memória do objeto IMEDIATAMENTE (Desalocação Determinística).

2. Garbage Collector Cíclico (Cyclic GC - Secundário):
   - O Reference Counting falha quando existem Referências Circulares (ex: Objeto A aponta para B e B aponta para A).
   - Nesses casos, a contagem nunca chega a zero por conta própria!
   - O módulo `gc` implementa um Garbage Collector Cíclico baseado em 3 Gerações (Generation 0, 1 e 2) para detectar e destruir ciclos de objetos inacessíveis.

3. Alocador de Memória `PyMalloc`:
   - Para evitar chamadas de sistema frequentes ao SO (`malloc`/`free`), o CPython gerencia seus próprios blocos de memória para pequenos objetos (<= 512 bytes) organizados em Arenas (256KB) e Pools (4KB).
"""


# ==========================================================
# 2. DEMONSTRAÇÃO DE REFERENCE COUNTING E GC CÍCLICO
# ==========================================================
def demonstrar_reference_counting() -> None:
    print("\n--- 1. FUNDAMENTOS: Reference Counting com sys.getrefcount() ---")

    # Criando um novo objeto na memória
    meu_objeto = [1, 2, 3]

    # sys.getrefcount adiciona +1 temporário na contagem ao receber a variável como parâmetro
    ref_count_1 = sys.getrefcount(meu_objeto)
    print(f"Contagem de referências de 'meu_objeto' (esperado 2): {ref_count_1}")

    outra_ref = meu_objeto
    ref_count_2 = sys.getrefcount(meu_objeto)
    print(f"Contagem após criar 'outra_ref' (esperado 3): {ref_count_2}")

    del outra_ref
    ref_count_3 = sys.getrefcount(meu_objeto)
    print(f"Contagem após deletar 'outra_ref' (esperado 2): {ref_count_3}")


def demonstrar_coleta_ciclos() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Coleta de Referências Circulares com gc ---")

    class NoCircular:
        def __init__(self, nome: str) -> None:
            self.nome = nome
            self.referencia: Any = None

    # Criando ciclo circular A <-> B
    node_a = NoCircular("Nó A")
    node_b = NoCircular("Nó B")
    node_a.referencia = node_b
    node_b.referencia = node_a

    # Deletando as variáveis locais
    del node_a
    del node_b

    # O Garbage Collector Cíclico identifica e destrói o ciclo inacessível
    coletados = gc.collect()
    print(f"Objetos inalcançáveis coletados pelo Garbage Collector: {coletados}")


# ==========================================================
# 3. OTIMIZAÇÃO DE MEMÓRIA COM __SLOTS__
# ==========================================================
"""
Economia de Memória RAM com `__slots__`:
- Por padrão, toda classe Python armazena seus atributos dinâmicos em um dicionário interno `__dict__`.
- O dicionário `__dict__` consome cerca de 104 bytes por instância!
- Ao definir `__slots__ = ('attr1', 'attr2')`, o CPython elimina o dicionário `__dict__` e aloca um array C contíguo fixo de ponteiros.
- Economia de até 70% de memória RAM em instâncias massivas!
"""


class PontoSemSlots:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class PontoComSlots:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def demonstrar_otimizacao_slots() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Economia de RAM com __slots__ ---")

    p_normal = PontoSemSlots(1.0, 2.0)
    p_slots = PontoComSlots(1.0, 2.0)

    tam_normal = sys.getsizeof(p_normal) + sys.getsizeof(p_normal.__dict__)
    tam_slots = sys.getsizeof(p_slots)

    print(f"Tamanho em bytes (Sem __slots__): {tam_normal} bytes (contando __dict__)")
    print(f"Tamanho em bytes (Com __slots__): {tam_slots} bytes")
    print(f"Economia de memória: ~{((tam_normal - tam_slots) / tam_normal)*100:.1f}%")


# ==========================================================
# 4. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Complexidade de Memória:
- Reference Counting: Desalocação O(1) imediata no momento em que a contagem chega a 0.
- Garbage Collection Cíclico: Execução periódica O(N) nas Gerações 0, 1 e 2.
- Atributos com `__slots__`: Redução de Espaço por instância de ~150 bytes para ~48 bytes em CPython 64-bit.
"""


# ==========================================================
# 5. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o CPython gerencia a memória e qual a diferença entre Reference Counting e o Garbage Collector cíclico do módulo `gc`?"
A: "1. Reference Counting: E a estratégia primária. Cada objeto possui um contador de referências. Quando o contador chega a 0, a memória do objeto é liberada imediatamente em O(1).
    2. Cyclic Garbage Collector: E o mecanismo secundário (módulo `gc`). Ele existe porque a contagem de referências isolada não consegue desalocar objetos que possuem referências circulares entre si (A aponta para B e B aponta para A). O GC divide os objetos em 3 Gerações e inspeciona periodicamente os grafos de objetos para detectar e destruir ciclos inacessíveis."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Utilize `sys.getrefcount()` para verificar o número de referências de um número inteiro pequeno (como `1`) e explique por que a contagem é alta (Interning/Caching).
# Exercício 2 (Intermediário): Crie uma classe `LogEntry` com `__slots__` e instancie 10.000 objetos medindo o consumo com `tracemalloc`.
# Exercício 3 (Desafio / Entrevista): Escreva um código que force uma referência circular entre dois objetos e use `gc.collect()` para medir quantos objetos foram destruídos.


def main() -> None:
    print("==========================================================")
    print("  AULA 83: GERENCIAMENTO DE MEMÓRIA, GC E __SLOTS__")
    print("==========================================================")
    demonstrar_reference_counting()
    demonstrar_coleta_ciclos()
    demonstrar_otimizacao_slots()
    print("\n[Concluido] Arquivo 83 executado com sucesso.")


if __name__ == "__main__":
    main()
