"""
46_iteradores.py - Protocolo de Iteração em Python (`__iter__` e `__next__`)

Objetivos:
1. Compreender o protocolo de iteração (`iter()` e `next()`).
2. Criar um iterador customizado do zero implementando `__iter__` e `__next__`.
3. Tratar a exceção `StopIteration` no término da sequência.
"""

class ContadorRegressivo:
    def __init__(self, inicio: int) -> None:
        self.atual = inicio

    def __iter__(self) -> "ContadorRegressivo":
        return self

    def __next__(self) -> int:
        if self.atual <= 0:
            raise StopIteration
        valor = self.atual
        self.atual -= 1
        return valor


def main() -> None:
    print("==========================================================")
    print("  AULA 46: PROTOCOLO DE ITERAÇÃO (__ITER__ E __NEXT__)")
    print("==========================================================")
    contador = ContadorRegressivo(3)
    for num in contador:
        print(f"  - Contagem: {num}")
    print("\n[Concluido] Arquivo 46 executado com sucesso.")


if __name__ == "__main__":
    main()
