"""
47_geradores.py - Geradores e a Instrução `yield`

Objetivos:
1. Criar funções geradoras utilizando `yield`.
2. Compreender a pausa e retomada de execução de geradores.
3. Utilizar `yield from` para delegar iterações subseqüentes.
"""

from typing import Generator


def gerador_sequencia(limite: int) -> Generator[int, None, None]:
    for i in range(1, limite + 1):
        yield i * 10


def gerador_delegado() -> Generator[str, None, None]:
    yield from ["Etapa A", "Etapa B", "Etapa C"]


def main() -> None:
    print("==========================================================")
    print("  AULA 47: GERADORES E YIELD")
    print("==========================================================")
    gen = gerador_sequencia(3)
    print(f"Próximo valor com next(): {next(gen)}")
    print(f"Próximo valor com next(): {next(gen)}")

    print("Iterando gerador delegado com 'yield from':")
    for etapa in gerador_delegado():
        print(f"  - {etapa}")
    print("\n[Concluido] Arquivo 47 executado com sucesso.")


if __name__ == "__main__":
    main()
