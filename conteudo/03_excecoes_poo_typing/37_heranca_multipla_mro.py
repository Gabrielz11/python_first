"""
37_heranca_multipla_mro.py - Herança Múltipla e MRO (Method Resolution Order / Algoritmo C3)

Objetivos:
1. Trabalhar com herança múltipla em Python.
2. Compreender a ordem de resolução de métodos (MRO - Method Resolution Order).
3. Inspecionar o MRO com `.mro()` ou `.__mro__`.
"""

class Logavel:
    def log(self, mensagem: str) -> None:
        print(f"[LOG] {mensagem}")


class ConexaoBD:
    def conectar(self) -> None:
        print("[BD] Conectado ao banco de dados.")


class RepositorioUsuario(ConexaoBD, Logavel):
    def salvar(self, usuario: str) -> None:
        self.conectar()
        self.log(f"Usuário '{usuario}' salvo no banco.")


def main() -> None:
    print("==========================================================")
    print("  AULA 37: HERANÇA MÚLTIPLA E MRO (METHOD RESOLUTION ORDER)")
    print("==========================================================")
    repo = RepositorioUsuario()
    repo.salvar("Gabriel")
    print("\nOrdem de Resolução de Métodos (MRO):")
    for cls in RepositorioUsuario.mro():
        print(f"  - {cls.__name__}")
    print("\n[Concluido] Arquivo 37 executado com sucesso.")


if __name__ == "__main__":
    main()
