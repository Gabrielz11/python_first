"""
85_getattr_getattribute.py - Metaprogramação Avançada (`__getattr__` vs `__getattribute__`)

Objetivos:
1. Compreender o acesso a atributos dinâmicos com `__getattr__` (fallback quando o atributo não existe).
2. Compreender `__getattribute__` (intercepta TODOS os acessos a qualquer atributo).
"""

class ObjetoDinamico:
    def __init__(self) -> None:
        self.nome = "Existente"

    def __getattr__(self, item: str) -> str:
        # Chamado APENAS se o atributo não for encontrado no dicionário do objeto
        return f"Atributo_Dinamico_{item}"


def main() -> None:
    print("==========================================================")
    print("  AULA 85: METAPROGRAMAÇÃO (__GETATTR__ VS __GETATTRIBUTE__)")
    print("==========================================================")
    obj = ObjetoDinamico()
    print(f"Atributo real (.nome): {obj.nome}")
    print(f"Atributo dinâmico (.qualquer_coisa): {obj.qualquer_coisa}")
    print("\n[Concluido] Arquivo 85 executado com sucesso.")


if __name__ == "__main__":
    main()
