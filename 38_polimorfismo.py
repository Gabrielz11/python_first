"""
38_polimorfismo.py - Polimorfismo e Duck Typing em Python

Objetivos:
1. Compreender o polimorfismo baseado na filosofia Duck Typing:
   "Se anda como um pato e quaca como um pato, então é um pato!"
2. Executar comportamentos diferentes sob a mesma interface sem necessidade de hierarquia estrita.
"""

from typing import Any


class Pato:
    def quacar(self) -> str:
        return "Quack quack!"


class Pessoa:
    def quacar(self) -> str:
        return "Eu estou imitando um pato!"


def fazer_quacar(objeto: Any) -> None:
    print(f"Resultado: {objeto.quacar()}")


def main() -> None:
    print("==========================================================")
    print("  AULA 38: POLIMORFISMO E DUCK TYPING")
    print("==========================================================")
    fazer_quacar(Pato())
    fazer_quacar(Pessoa())
    print("\n[Concluido] Arquivo 38 executado com sucesso.")


if __name__ == "__main__":
    main()
