"""
32_classes_objetos.py - Orientação a Objetos (Classes, Instâncias e Estado)

Objetivos:
1. Compreender a criação de classes em Python (`class NomeClasse:`).
2. Diferenciar Atributos de Instância (`self.x`) e Atributos de Classe.
3. Entender o parâmetro `self` (referência explícita à instância).
"""

class ContaBancaria:
    banco: str = "Banco Python S.A."

    def __init__(self, titular: str, saldo_inicial: float) -> None:
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        print(f"[OK] Depósito de R$ {valor:.2f} efetuado para {self.titular}.")


def main() -> None:
    print("==========================================================")
    print("  AULA 32: CLASSES, OBJETOS E ESTADO DE INSTÂNCIA")
    print("==========================================================")
    c1 = ContaBancaria("Ana", 500.0)
    c1.depositar(200.0)
    print(f"Titular: {c1.titular} | Saldo: R$ {c1.saldo:.2f} | Banco: {c1.banco}")
    print("\n[Concluido] Arquivo 32 executado com sucesso.")


if __name__ == "__main__":
    main()
