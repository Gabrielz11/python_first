"""
70_repository_pattern.py - Padrão de Repositório (Repository Pattern)

Objetivos:
1. Isolar a lógica de acesso a dados da lógica de negócios.
2. Definir uma interface de repositório genérica para persistência de dados.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class UsuarioEntidade:
    id: int
    nome: str
    email: str


class RepositorioUsuarioInterface(ABC):
    @abstractmethod
    def obter_por_id(self, id: int) -> UsuarioEntidade | None:
        pass

    @abstractmethod
    def salvar(self, usuario: UsuarioEntidade) -> None:
        pass


class RepositorioUsuarioMemoria(RepositorioUsuarioInterface):
    def __init__(self) -> None:
        self._db: dict[int, UsuarioEntidade] = {}

    def obter_por_id(self, id: int) -> UsuarioEntidade | None:
        return self._db.get(id)

    def salvar(self, usuario: UsuarioEntidade) -> None:
        self._db[usuario.id] = usuario
        print(f"[REPO MEMÓRIA] Usuário {usuario.nome} salvo com sucesso.")


def main() -> None:
    print("==========================================================")
    print("  AULA 70: REPOSITORY PATTERN E CAMADA DE PERSISTÊNCIA")
    print("==========================================================")
    repo: RepositorioUsuarioInterface = RepositorioUsuarioMemoria()
    u = UsuarioEntidade(1, "Ana Maria", "ana@empresa.com")
    repo.salvar(u)

    recuperado = repo.obter_por_id(1)
    print(f"Usuário recuperado do repositório: {recuperado}")
    print("\n[Concluido] Arquivo 70 executado com sucesso.")


if __name__ == "__main__":
    main()
