"""
67_solid.py - Princípios SOLID em Python (SRP, OCP, LSP, ISP, DIP)

Objetivos:
1. Compreender a aplicação prática dos 5 princípios SOLID na Engenharia de Software Backend.
"""

from abc import ABC, abstractmethod


# 1. Single Responsibility Principle (SRP)
class NotificadorEmail:
    def enviar_email(self, destinatario: str, mensagem: str) -> None:
        print(f"[EMAIL] Enviado para {destinatario}: '{mensagem}'")


# 2. Open/Closed Principle (OCP) & Dependency Inversion (DIP)
class MeioPagamento(ABC):
    @abstractmethod
    def pagar(self, quantia: float) -> None:
        pass


class PagamentoCartao(MeioPagamento):
    def pagar(self, quantia: float) -> None:
        print(f"[CARTAO] Pago R$ {quantia:.2f}")


class PagamentoPix(MeioPagamento):
    def pagar(self, quantia: float) -> None:
        print(f"[PIX] Pago R$ {quantia:.2f}")


class ServicoCheckout:
    def __init__(self, meio_pagamento: MeioPagamento, notificador: NotificadorEmail) -> None:
        self.meio_pagamento = meio_pagamento
        self.notificador = notificador

    def finalizar_compra(self, valor: float, email_cliente: str) -> None:
        self.meio_pagamento.pagar(valor)
        self.notificador.enviar_email(email_cliente, f"Compra de R$ {valor:.2f} confirmada!")


def main() -> None:
    print("==========================================================")
    print("  AULA 67: PRINCÍPIOS SOLID NA PRÁTICA")
    print("==========================================================")
    notificador = NotificadorEmail()
    pix = PagamentoPix()
    checkout = ServicoCheckout(meio_pagamento=pix, notificador=notificador)
    checkout.finalizar_compra(250.0, "cliente@empresa.com")
    print("\n[Concluido] Arquivo 67 executado com sucesso.")


if __name__ == "__main__":
    main()
