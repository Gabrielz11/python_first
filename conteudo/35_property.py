"""
35_property.py - Modificadores de Acesso com `@property` (Getters & Setters Idiomáticos)

Objetivos:
1. Utilizar decoradores `@property`, `@<prop>.setter` e `@<prop>.deleter`.
2. Adicionar validação de dados em atributos sem quebrar a interface pública da classe.
"""

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self._salario = salario

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, novo_valor: float) -> None:
        if novo_valor <= 0:
            raise ValueError("O salário deve ser um valor positivo!")
        self._salario = novo_valor


def main() -> None:
    print("==========================================================")
    print("  AULA 35: GETTERS E SETTERS IDIOMÁTICOS COM @PROPERTY")
    print("==========================================================")
    f = Funcionario("Bia", 5000.0)
    print(f"Salário inicial de {f.nome}: R$ {f.salario:.2f}")
    f.salario = 6000.0
    print(f"Salário atualizado: R$ {f.salario:.2f}")
    try:
        f.salario = -100.0
    except ValueError as e:
        print(f"[X] Validação de setter funcionou: {e}")
    print("\n[Concluido] Arquivo 35 executado com sucesso.")


if __name__ == "__main__":
    main()
