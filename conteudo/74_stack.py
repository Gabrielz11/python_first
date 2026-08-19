"""
74_stack.py - Estrutura de Dados Pilha (Stack - LIFO) e Validação de Parênteses

Objetivos:
1. Implementar a estrutura de dados Pilha (LIFO - Last In, First Out).
2. Resolver o algoritmo de validação de parênteses/chaves balanceados em O(n).
"""

def validar_parenteses_balanceados(expressao: str) -> bool:
    pilha: list[str] = []
    mapeamento = {")": "(", "}": "{", "]": "["}

    for char in expressao:
        if char in mapeamento.values():
            pilha.append(char)
        elif char in mapeamento.keys():
            if not pilha or pilha.pop() != mapeamento[char]:
                return False
    return len(pilha) == 0


def main() -> None:
    print("==========================================================")
    print("  AULA 74: PILHA (STACK LIFO) E VALIDAÇÃO DE SÍMBOLOS")
    print("==========================================================")
    e1 = "{ [ ( ) ] }"
    e2 = "{ [ ( ] ) }"
    print(f"Expressão '{e1}' é válida? {validar_parenteses_balanceados(e1)}")
    print(f"Expressão '{e2}' é válida? {validar_parenteses_balanceados(e2)}")
    print("\n[Concluido] Arquivo 74 executado com sucesso.")


if __name__ == "__main__":
    main()
