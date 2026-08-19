"""
41_dunder_methods.py - Dunder Methods Avançados (`__len__`, `__getitem__`, `__call__`, `__eq__`)

Objetivos:
1. Implementar protocolos do Python customizando métodos mágicos (dunder methods).
2. Tornar objetos invocáveis como funções (`__call__`).
3. Permitir indexação (`__getitem__`) e tamanho (`__len__`).
"""

class Playlist:
    def __init__(self, nome: str, musicas: list[str]) -> None:
        self.nome = nome
        self.musicas = musicas

    def __len__(self) -> int:
        return len(self.musicas)

    def __getitem__(self, index: int) -> str:
        return self.musicas[index]

    def __call__(self, acao: str) -> None:
        print(f"Ação '{acao}' executada na playlist '{self.nome}'.")


def main() -> None:
    print("==========================================================")
    print("  AULA 41: DUNDER METHODS (__LEN__, __GETITEM__, __CALL__)")
    print("==========================================================")
    p = Playlist("Rock Clássico", ["Bohemian Rhapsody", "Stairway to Heaven"])
    print(f"Tamanho com len(p): {len(p)}")
    print(f"Indexação p[0]: '{p[0]}'")
    p("Tocar Aleatório")
    print("\n[Concluido] Arquivo 41 executado com sucesso.")


if __name__ == "__main__":
    main()
