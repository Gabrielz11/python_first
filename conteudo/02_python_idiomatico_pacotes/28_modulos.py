"""
28_modulos.py - Organização e Importação de Módulos em Python

Objetivos:
1. Compreender como o Python localiza módulos através de `sys.path`.
2. Utilizar `import`, `from ... import ...`, alias `as` e importações relativas vs absolutas.
3. Entender a variável especial `__name__` e a guarda `if __name__ == '__main__':`.
"""

import sys


def demonstrar_modulos() -> None:
    print("\n--- 1. SYS.PATH E MECANISMO DE IMPORTAÇÃO ---")
    print(f"Módulo atual `__name__`: {__name__}")
    print("Primeiros caminhos em `sys.path`:")
    for path in sys.path[:3]:
        print(f"  - {path}")


def main() -> None:
    print("==========================================================")
    print("  AULA 28: MÓDULOS E MECANISMO DE IMPORTAÇÃO")
    print("==========================================================")
    demonstrar_modulos()
    print("\n[Concluido] Arquivo 28 executado com sucesso.")


if __name__ == "__main__":
    main()
