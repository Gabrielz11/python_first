"""
69_design_patterns.py - Padrões de Projeto (Strategy, Factory, Adapter, Observer)

Objetivos:
1. Implementar Design Patterns clássicos adaptados ao dinamismo do Python.
"""

from typing import Callable


# 1. Strategy Pattern via Funções de Primeira Classe em Python!
def estrategia_desconto_padrao(valor: float) -> float:
    return valor


def estrategia_desconto_black_friday(valor: float) -> float:
    return valor * 0.70


class CarrinhoCompras:
    def __init__(self, estrategia_desconto: Callable[[float], float]) -> None:
        self.itens: list[float] = []
        self.estrategia_desconto = estrategia_desconto

    def adicionar_item(self, valor: float) -> None:
        self.itens.append(valor)

    def calcular_total(self) -> float:
        subtotal = sum(self.itens)
        return self.estrategia_desconto(subtotal)


def main() -> None:
    print("==========================================================")
    print("  AULA 69: DESIGN PATTERNS EM PYTHON (STRATEGY)")
    print("==========================================================")
    carrinho_bf = CarrinhoCompras(estrategia_desconto=estrategia_desconto_black_friday)
    carrinho_bf.adicionar_item(100.0)
    carrinho_bf.adicionar_item(200.0)
    print(f"Total com Strategy Black Friday (30% off): R$ {carrinho_bf.calcular_total():.2f}")
    print("\n[Concluido] Arquivo 69 executado com sucesso.")


if __name__ == "__main__":
    main()
