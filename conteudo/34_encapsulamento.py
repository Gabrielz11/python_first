"""
34_encapsulamento.py - Encapsulamento, Atributos Protegidos (`_`) e Privados (`__`)

Objetivos:
1. Compreender a convenção de visibilidade em Python.
2. Atributos protegidos por convenção (`_atributo`).
3. Atributos privados via Name Mangling (`__atributo` vira `_NomeClasse__atributo`).
"""

class ContaProtegida:
    def __init__(self, titular: str, saldo_inicial: float) -> None:
        self.titular = titular
        self._saldo_protegido = saldo_inicial
        self.__segredo_privado = "hash_token_123"

    def obter_saldo(self) -> float:
        return self._saldo_protegido


def main() -> None:
    print("==========================================================")
    print("  AULA 34: ENCAPSULAMENTO E NAME MANGLING")
    print("==========================================================")
    c = ContaProtegida("Carlos", 1000.0)
    print(f"Saldo via método público: R$ {c.obter_saldo():.2f}")
    print(f"Acesso via Name Mangling (_ContaProtegida__segredo_privado): {c._ContaProtegida__segredo_privado}")
    print("\n[Concluido] Arquivo 34 executado com sucesso.")


if __name__ == "__main__":
    main()
