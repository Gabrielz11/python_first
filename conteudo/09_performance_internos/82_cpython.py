"""
82_cpython.py - CPython Internals, Compilação para Bytecode, Módulo dis e PyObject

Objetivos:
1. Compreender a arquitetura e funcionamento interno da implementação de referência do Python (CPython).
2. Entender as etapas do pipeline de execução: Código-Fonte -> Tokens -> Árvore Sintática (AST) -> Bytecode -> Máquina Virtual (PVM).
3. Inspecionar o bytecode CPython gerado para funções utilizando a biblioteca nativa `dis`.
4. Conhecer a estrutura de C `PyObject` (`ob_refcnt` e `ob_type`) que suporta todos os objetos em Python.
5. Analisar o laço de avaliação de frames (`ceval.c` / `PyEval_EvalFrameDefault`).
"""

import dis
import sys
from typing import Any


# ==========================================================
# 1. CONCEITO: ARQUITETURA DO CPYTHON
# ==========================================================
"""
O que é o CPython?
CPython e a implementação oficial e padrão da linguagem Python, escrita em C e mantida pela Python Software Foundation.

Pipeline de Execução em CPython:
1. Lexer / Tokenizer: Converte o código-fonte em texto em uma sequência de Tokens.
2. Parser: Transforma os Tokens em uma Árvore Sintática Abstrata (AST - Abstract Syntax Tree).
3. Compiler: Compila a AST em Bytecode (instruções de baixo nível independentes de plataforma).
4. Python Virtual Machine (PVM): A VM baseada em pilha (Stack-based Virtual Machine) que executa o Bytecode dentro do laço `ceval.c`.

A Estrutura de C `PyObject`:
Em CPython, absolutamente tudo em nível Python (inteiros, strings, funções, módulos, listas) e um ponteiro para uma struct C chamada `PyObject`:
```c
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;          // Contador de Referências para Garbage Collection
    struct _typeobject *ob_type;   // Ponteiro para o tipo do objeto (ex: PyLong_Type)
} PyObject;
```
Por isso, até mesmo o inteiro `1` em Python consome ~28 bytes de memória RAM no CPython (devido aos metadados do `PyObject`).
"""


# ==========================================================
# 2. INSPEÇÃO DE BYTECODE COM O MÓDULO DIS
# ==========================================================
def calcular_soma_exemplo(a: int, b: int) -> int:
    resultado = a + b
    return resultado


def demonstrar_inspecao_bytecode() -> None:
    print("\n--- 1. FUNDAMENTOS: Inspeção de Bytecode com dis.dis() ---")
    print("Bytecode gerado para 'calcular_soma_exemplo':\n")

    # Exibe as instruções de bytecode emitidas pelo CPython
    dis.dis(calcular_soma_exemplo)


# ==========================================================
# 3. COMPARATIVO DE BYTECODE: GLOBAL VS LOCAL VARIABLE LOOKUP
# ==========================================================
"""
Por que a busca por Variáveis Locais e mais rápida que Variáveis Globais no CPython?
- Variáveis Locais usam a instrução `LOAD_FAST` (acesso por índice em um array fixo de C em tempo O(1)).
- Variáveis Globais usam a instrução `LOAD_GLOBAL` (exige busca por chave em dicionário `globals()` em tempo de execução).
"""

fator_global = 10


def calcular_global(x: int) -> int:
    return x * fator_global


def calcular_local(x: int) -> int:
    fator_local = 10
    return x * fator_local


def demonstrar_comparativo_bytecode() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: LOAD_FAST vs LOAD_GLOBAL ---")

    print("\nBytecode com Variável Global (LOAD_GLOBAL):")
    dis.dis(calcular_global)

    print("\nBytecode com Variável Local (LOAD_FAST):")
    dis.dis(calcular_local)


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Otimização de Loops de Alta Performance ---")
    print("  Dica de Otimização CPython em Hot Loops:")
    print("  Armazenar funções globais (como `math.sin` ou `str.upper`) em variáveis locais dentro da função reduz chamadas LOAD_GLOBAL para LOAD_FAST!")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Otimizações de Bytecode:
- Instrução `LOAD_FAST`: Acesso O(1) ultra-rápido por índice no array de frame local do C.
- Instrução `LOAD_GLOBAL`: Busca O(1) médio em dicionário de globais.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é o Bytecode em Python e como ele difere do código de máquina compilado de C/C++?"
A: "1. Código de Máquina (C/C++): E compilado diretamente para instruções assembly nativas da arquitetura do processador (x86_64, ARM) e executado diretamente pela CPU de forma binária.
    2. Bytecode (Python): E uma representação intermediária independente de plataforma (platform-independent bytecode). O CPython gera instruções de 16 bits (como `LOAD_FAST`, `BINARY_ADD`) que são interpretadas por uma Máquina Virtual de pilha escrita em C (`ceval.c`)."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Utilize `dis.dis()` para inspecionar o bytecode de uma função que concatena duas strings via f-string vs operator `+`.
# Exercício 2 (Intermediário): Inspecione o bytecode de uma List Comprehension `[x*2 for x in nums]` e compare com um loop `for` manual com `append()`.
# Exercício 3 (Desafio / Entrevista): Inspecione os atributos internos do objeto de código de uma função usando `funcao.__code__.co_code` e `funcao.__code__.co_varnames`.


def main() -> None:
    print("==========================================================")
    print("  AULA 82: CPYTHON INTERNALS, COMPILAÇÃO E BYTECODE")
    print("==========================================================")
    demonstrar_inspecao_bytecode()
    demonstrar_comparativo_bytecode()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 82 executado com sucesso.")


if __name__ == "__main__":
    main()
