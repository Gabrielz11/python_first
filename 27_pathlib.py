"""
27_pathlib.py - Orientação a Objetos no Sistema de Arquivos (`pathlib.Path`)

Objetivos:
1. Substituir o módulo legado `os.path` pelo moderno e orientando a objetos `pathlib.Path`.
2. Manipular caminhos de forma multiplataforma (Windows/Linux/macOS).
3. Utilizar o operador barra `/` para composição de caminhos.
"""

from pathlib import Path


def demonstrar_pathlib() -> None:
    print("\n--- 1. MANIPULAÇÃO DE CAMINHOS COM PATHLIB ---")

    # Instanciando o diretório atual
    cwd = Path.cwd()
    print(f"Diretório atual (CWD): {cwd}")

    # Composição de caminhos usando o operador `/`
    subpath = cwd / "pasta_teste" / "arquivo.json"
    print(f"Caminho composto: {subpath}")
    print(f"Nome do arquivo (.name): {subpath.name}")
    print(f"Extensão (.suffix): {subpath.suffix}")
    print(f"Diretório pai (.parent): {subpath.parent}")


def main() -> None:
    print("==========================================================")
    print("  AULA 27: ORIENTAÇÃO A OBJETOS COM PATHLIB")
    print("==========================================================")
    demonstrar_pathlib()
    print("\n[Concluido] Arquivo 27 executado com sucesso.")


if __name__ == "__main__":
    main()
