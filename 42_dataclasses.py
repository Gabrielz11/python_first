"""
42_dataclasses.py - Simplificação de Classes de Dados com `@dataclass`

Objetivos:
1. Utilizar o módulo `dataclasses` para autogerar `__init__`, `__repr__`, `__eq__`.
2. Utilizar `frozen=True` para objetos imutáveis e hashable.
3. Utilizar `kw_only=True` e `__post_init__` para validações.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class ItemPedido:
    produto: str
    preco: float
    quantidade: int = 1
    total: float = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "total", self.preco * self.quantidade)


def main() -> None:
    print("==========================================================")
    print("  AULA 42: DATACLASSES E OBJETOS IMUTÁVEIS (FROZEN)")
    print("==========================================================")
    item = ItemPedido(produto="Teclado", preco=150.0, quantidade=2)
    print(f"Item gerado por Dataclass: {item}")
    print(f"Total calculado no __post_init__: R$ {item.total:.2f}")
    print("\n[Concluido] Arquivo 42 executado com sucesso.")


if __name__ == "__main__":
    main()
