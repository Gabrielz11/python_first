"""
33_init_str_repr.py - Representação de Objetos (`__init__`, `__str__` e `__repr__`)

Objetivos:
1. Compreender o construtor `__init__`.
2. Diferenciar `__str__` (amigável ao usuário final) de `__repr__` (técnico/para desenvolvedor).
3. Seguir a regra: `__repr__` deve idealmente retornar código Python válido para recriar o objeto.
"""

class Usuario:
    def __init__(self, id: int, username: str) -> None:
        self.id = id
        self.username = username

    def __str__(self) -> str:
        return f"Usuário '{self.username}' (ID: {self.id})"

    def __repr__(self) -> str:
        return f"Usuario(id={self.id!r}, username={self.username!r})"


def main() -> None:
    print("==========================================================")
    print("  AULA 33: REPRESENTAÇÃO DE OBJETOS (__STR__ E __REPR__)")
    print("==========================================================")
    u = Usuario(101, "gabriel")
    print(f"Saída com __str__ (print): {u}")
    print(f"Saída com __repr__ (repr): {repr(u)}")
    print("\n[Concluido] Arquivo 33 executado com sucesso.")


if __name__ == "__main__":
    main()
