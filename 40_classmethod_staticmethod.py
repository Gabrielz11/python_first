"""
40_classmethod_staticmethod.py - `@classmethod` vs `@staticmethod`

Objetivos:
1. Compreender `@classmethod` (acessa a classe `cls`, ideal para construtores alternativos / Factory Methods).
2. Compreender `@staticmethod` (funções utilitárias sem acesso a `self` ou `cls`).
"""

class Data:
    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_string(cls, string_data: str) -> "Data":
        ano, mes, dia = map(int, string_data.split("-"))
        return cls(dia, mes, ano)

    @staticmethod
    def eh_ano_bissexto(ano: int) -> bool:
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def main() -> None:
    print("==========================================================")
    print("  AULA 40: @CLASSMETHOD E @STATICMETHOD")
    print("==========================================================")
    d = Data.de_string("2026-08-19")
    print(f"Data criada via @classmethod: {d.dia}/{d.mes}/{d.ano}")
    print(f"Ano 2024 é bissexto? (via @staticmethod): {Data.eh_ano_bissexto(2024)}")
    print("\n[Concluido] Arquivo 40 executado com sucesso.")


if __name__ == "__main__":
    main()
