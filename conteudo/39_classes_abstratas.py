"""
39_classes_abstratas.py - Classes Abstratas e Métodos Abstratos (`abc.ABC`, `@abstractmethod`)

Objetivos:
1. Definir contratos de interface com `abc.ABC` e `@abstractmethod`.
2. Impedir a instanciação direta de classes base incompletas.
3. Garantir que subclasses implementem todos os métodos obrigatórios.
"""

from abc import ABC, abstractmethod


class ProcessadorPagamento(ABC):
    @abstractmethod
    def processar(self, valor: float) -> bool:
        pass


class PagamentoPix(ProcessadorPagamento):
    def processar(self, valor: float) -> bool:
        print(f"[PIX] Pagamento de R$ {valor:.2f} processado com sucesso.")
        return True


def main() -> None:
    print("==========================================================")
    print("  AULA 39: CLASSES ABSTRATAS (ABC E ABSTRACTMETHOD)")
    print("==========================================================")
    pix = PagamentoPix()
    pix.processar(150.0)
    try:
        _ = ProcessadorPagamento()  # type: ignore
    except TypeError as e:
        print(f"[X] Impedida instanciação de ABC: {e}")
    print("\n[Concluido] Arquivo 39 executado com sucesso.")


if __name__ == "__main__":
    main()
