"""
74_stack.py - Estrutura de Dados Pilha (Stack), LIFO e Validação de Parênteses Balanceados

Objetivos:
1. Dominar a Estrutura de Dados Pilha (Stack) fundamentada no princípio LIFO (Last-In, First-Out).
2. Implementar uma Pilha utilizando o tipo nativo `list` em Python com operações O(1) (`append` e `pop`).
3. Compreender o conceito e funcionamento da Pilha de Chamadas (Call Stack) na execução do CPython.
4. Resolver o problema clássico de entrevista: Validação de Parênteses e Colchetes Balanceados.
5. Desenvolver buffers de Undo/Redo e navegadores de histórico para aplicações de backend.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO DA ESTRUTURA PILHA (STACK)
# ==========================================================
"""
O que é uma Pilha (Stack)?
Uma Pilha e uma estrutura de dados linear que segue estritamente a ordem LIFO (Last-In, First-Out):
O ÚLTIMO elemento a ser inserido e o PRIMEIRO elemento a ser removido.

Operações Fundamentais da Pilha:
- `push(item)`: Insere um elemento no topo da pilha.
- `pop()`: Remove e retorna o elemento localizado no topo da pilha.
- `peek()` / `top()`: Consulta o elemento do topo sem removê-lo.
- `is_empty()`: Verifica se a pilha está vazia.
- `size()`: Retorna o número de elementos contidos na pilha.

Implementação em Python:
A estrutura `list` nativa do Python e perfeita para ser usada como Pilha:
- `lista.append(item)` atua como `push()` em O(1) amortizado.
- `lista.pop()` atua como `pop()` em O(1).
- `lista[-1]` atua como `peek()` em O(1).
"""


# ==========================================================
# 2. IMPLEMENTAÇÃO DIDÁTICA DA CLASSE PILHA (STACK)
# ==========================================================
class Pilha:
    """Implementação orientada a objetos de uma Pilha LIFO."""

    def __init__(self) -> None:
        self._itens: list[Any] = []

    def push(self, item: Any) -> None:
        """Insere no topo O(1)."""
        self._itens.append(item)

    def pop(self) -> Any:
        """Remove do topo O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._itens.pop()

    def peek(self) -> Any:
        """Consulta o topo O(1)."""
        if self.is_empty():
            return None
        return self._itens[-1]

    def is_empty(self) -> bool:
        return len(self._itens) == 0

    def __len__(self) -> int:
        return len(self._itens)


def demonstrar_fundamentos_pilha() -> None:
    print("\n--- 1. FUNDAMENTOS: Operações em Pilha LIFO ---")

    pilha = Pilha()
    pilha.push("Prato 1")
    pilha.push("Prato 2")
    pilha.push("Prato 3")

    print(f"Topo da pilha (peek): {pilha.peek()}")
    print(f"Removendo do topo (pop): {pilha.pop()}")
    print(f"Novo topo (peek): {pilha.peek()}")


# ==========================================================
# 3. PROBLEMA CLÁSSICO DE ENTREVISTA: PARÊNTESES BALANCEADOS
# ==========================================================
"""
Problema: Validar se uma string contendo caracteres `()[]{}` está devidamente balanceada.
- Exemplo Válido: `"{[()]}"` -> Retorna True.
- Exemplo Inválido: `"{[(])}"` -> Retorna False (Fechamento fora de ordem).
- Exemplo Inválido: `"((("` -> Retorna False (Não fechado).

Algoritmo com Pilha em O(N) tempo e O(N) espaço:
1. Percorre cada caractere da string.
2. Se for um caractere de ABERTURA (`(`, `[`, `{`), faz `push` na pilha.
3. Se for um caractere de FECHAMENTO (`)`, `]`, `}`):
   - Se a pilha estiver vazia, retorna False (fechamento sem abertura correspondente).
   - Faz `pop` do topo da pilha. Se o símbolo desempilhado não for o par correspondente, retorna False.
4. No final, a string estará válida apenas se a pilha estiver 100% VAZIA.
"""


def validar_parenteses_balanceados(expressao: str) -> bool:
    pilha: list[str] = []
    mapeamento = {")": "(", "]": "[", "}": "{"}

    for char in expressao:
        if char in "([{":
            pilha.append(char)
        elif char in ")]}":
            if not pilha:
                return False
            topo = pilha.pop()
            if topo != mapeamento[char]:
                return False

    return len(pilha) == 0


def demonstrar_validacao_parenteses() -> None:
    print("\n--- 2. PROBLEMA CLÁSSICO: Validação de Parênteses Balanceados ---")

    testes = [
        ("{[()]}", True),
        ("{[(])}", False),
        ("((()", False),
        ("()[]{}", True),
    ]

    for expr, esperado in testes:
        resultado = validar_parenteses_balanceados(expr)
        status = "PASS" if resultado == esperado else "FAIL"
        print(f"  [{status}] Expressao: {expr:10s} -> Retornou {resultado} (Esperado: {esperado})")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class UndoRedoManager:
    """Gerenciador de Ações Undo/Redo usando duas Pilhas."""

    def __init__(self) -> None:
        self.pilha_undo = Pilha()
        self.pilha_redo = Pilha()

    def executar_acao(self, acao: str) -> None:
        print(f"  [Executar] {acao}")
        self.pilha_undo.push(acao)
        # Limpa o redo ao fazer uma nova ação
        self.pilha_redo = Pilha()

    def undo(self) -> str | None:
        if self.pilha_undo.is_empty():
            return None
        acao = self.pilha_undo.pop()
        self.pilha_redo.push(acao)
        print(f"  [Undo] Desfeita ação: {acao}")
        return acao


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Sistema de Undo/Redo ---")
    manager = UndoRedoManager()

    manager.executar_acao("Digitar Texto")
    manager.executar_acao("Formatar Negrito")
    manager.undo()


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Resumo de Complexidades na Pilha (list Python):
- Push (`lista.append()`): Tempo O(1) amortizado, Espaço O(1).
- Pop (`lista.pop()`): Tempo O(1), Espaço O(1).
- Peek (`lista[-1]`): Tempo O(1), Espaço O(1).
- Espaço Total da Estrutura: O(N) onde N é o número de elementos na pilha.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como funciona a Call Stack (Pilha de Chamadas) em um interpretador de linguagem como o CPython?"
A: "A Call Stack e a pilha gerenciada pelo interpretador para rastrear as chamadas de funções ativas em tempo de execução.
    Quando uma função A chama uma função B, o CPython empilha (push) um novo Frame de Execução (contendo variáveis locais e o ponteiro da instrução).
    Quando B finaliza seu retorno, o CPython desempilha (pop) o frame de B, devolvendo o controle e o resultado para a função A no topo da pilha.
    Se a pilha ultrapassar o limite máximo de profundidade (devido a uma recursão infinita, por exemplo), o CPython dispara `RecursionError`."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma função `inverter_string_com_pilha(texto: str) -> str` utilizando uma Pilha.
# Exercício 2 (Intermediário): Implemente uma `MinStack` (Pilha de Mínimo) que suporte operações `push`, `pop`, `top` e obtenção do elemento MÍNIMO em tempo O(1) constante.
# Exercício 3 (Desafio / Entrevista): Avalie uma expressão matemática na Notação Polonesa Reversa (Reverse Polish Notation / Postfix) usando uma Pilha (ex: `["2", "1", "+", "3", "*"]` -> 9).


def main() -> None:
    print("==========================================================")
    print("  AULA 74: ESTRUTURA DE DADOS PILHA (STACK) E LIFO")
    print("==========================================================")
    demonstrar_fundamentos_pilha()
    demonstrar_validacao_parenteses()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 74 executado com sucesso.")


if __name__ == "__main__":
    main()
