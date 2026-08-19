"""
43_enum.py - Enumerações e Modelagem de Domínio (`enum.Enum`)

Objetivos:
1. Modelar constantes de domínio seguras com `enum.Enum` e `enum.auto()`.
2. Garantir segurança de tipos e legibilidade comparado a strings/inteiros mágicos.
"""

from enum import Enum, auto


class StatusPedido(Enum):
    PENDENTE = auto()
    PAGO = auto()
    ENVIADO = auto()
    CANCELADO = auto()


def processar_pedido(status: StatusPedido) -> None:
    if status == StatusPedido.PAGO:
        print("[OK] Pedido pago. Preparando envio.")
    else:
        print(f"[!] Pedido no status: {status.name}")


def main() -> None:
    print("==========================================================")
    print("  AULA 43: MODELAGEM DE DOMÍNIO COM ENUM")
    print("==========================================================")
    processar_pedido(StatusPedido.PAGO)
    processar_pedido(StatusPedido.PENDENTE)
    print("\n[Concluido] Arquivo 43 executado com sucesso.")


if __name__ == "__main__":
    main()
