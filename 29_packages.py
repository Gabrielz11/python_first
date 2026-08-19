"""
29_packages.py - Estrutura de Pacotes e O Arquivo `__init__.py`

Objetivos:
1. Compreender a estrutura de pacotes Python (`__init__.py`).
2. Entender `__all__` para controle de exportação pública no pacote.
3. Conhecer Namespace Packages (PEP 420 - pacotes sem `__init__.py` no Python 3.3+).
"""

def demonstrar_packages() -> None:
    print("\n--- 1. ESTRUTURA DE PACOTES ---")
    print("[OK] Pacotes organizam módulos em diretórios contendo (opcionalmente) `__init__.py`.")
    print("  - `__init__.py`: Executado ao importar o pacote; define a API pública.")
    print("  - `__all__`: Lista de strings definindo o que é exportado em `from pkg import *`.")


def main() -> None:
    print("==========================================================")
    print("  AULA 29: ESTRUTURA DE PACOTES E INTERFACE PÚBLICA")
    print("==========================================================")
    demonstrar_packages()
    print("\n[Concluido] Arquivo 29 executado com sucesso.")


if __name__ == "__main__":
    main()
