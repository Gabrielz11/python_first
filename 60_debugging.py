"""
60_debugging.py - Técnicas de Debugging Nativo em Python (`breakpoint()`)

Objetivos:
1. Utilizar o depurador nativo `breakpoint()` (PDB embutido no Python 3.7+).
2. Inspecionar variáveis, call stack e fluxo de execução interativo.
"""

def calcular_media(notas: list[float]) -> float:
    total = sum(notas)
    quantidade = len(notas)
    # Descomente a linha abaixo para depuração interativa durante o desenvolvimento:
    # breakpoint()
    return total / quantidade


def main() -> None:
    print("==========================================================")
    print("  AULA 60: DEBUGGING COM BREAKPOINT()")
    print("==========================================================")
    media = calcular_media([8.5, 9.0, 7.5])
    print(f"Média calculada: {media:.2f}")
    print("\n[Concluido] Arquivo 60 executado com sucesso.")


if __name__ == "__main__":
    main()
