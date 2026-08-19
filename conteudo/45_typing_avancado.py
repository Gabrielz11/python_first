"""
45_typing_avancado.py - Typing Avançado (`Protocol`, `Generic[T]`, `TypeVar`, `TypedDict`)

Objetivos:
1. Definir subtipagem estrutural com `Protocol` (Duck typing checado estaticamente).
2. Criar coleções genéricas e algoritmos genéricos com `TypeVar` e `Generic[T]`.
3. Estruturar dicionários com esquema estático usando `TypedDict`.
"""

from typing import Generic, Protocol, TypedDict, TypeVar


class UsuarioPayload(TypedDict):
    id: int
    nome: str


class Renderizavel(Protocol):
    def renderizar(self) -> str: ...


class ComponenteBotao:
    def renderizar(self) -> str:
        return "<button>Clique aqui</button>"


T = TypeVar("T")


class Repositorio(Generic[T]):
    def __init__(self) -> None:
        self._itens: list[T] = []

    def adicionar(self, item: T) -> None:
        self._itens.append(item)

    def listar(self) -> list[T]:
        return self._itens


def main() -> None:
    print("==========================================================")
    print("  AULA 45: TYPING AVANÇADO (PROTOCOL, GENERICS, TYPEDDICT)")
    print("==========================================================")
    repo = Repositorio[int]()
    repo.adicionar(10)
    repo.adicionar(20)
    print(f"Itens do repositório genérico: {repo.listar()}")
    print("\n[Concluido] Arquivo 45 executado com sucesso.")


if __name__ == "__main__":
    main()
