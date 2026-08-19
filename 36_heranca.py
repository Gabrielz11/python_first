"""
36_heranca.py - Herança Simples e Sobrescrita de Métodos com `super()`

Objetivos:
1. Compreender herança simples entre classes (`class SubClasse(BaseClasse):`).
2. Utilizar `super().__init__()` para reusar a inicialização da classe pai.
3. Sobrescrever métodos mantendo acoplamento coeso.
"""

class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def descrever(self) -> str:
        return f"{self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.portas = portas

    def descrever(self) -> str:
        base = super().descrever()
        return f"Carro: {base} com {self.portas} portas"


def main() -> None:
    print("==========================================================")
    print("  AULA 36: HERANÇA SIMPLES E USO DE SUPER()")
    print("==========================================================")
    c = Carro("Toyota", "Corolla", 4)
    print(f"Descrição: {c.descrever()}")
    print("\n[Concluido] Arquivo 36 executado com sucesso.")


if __name__ == "__main__":
    main()
