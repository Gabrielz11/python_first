"""
25_arquivos.py - Manipulação de Arquivos e Context Manager `with`

Objetivos:
1. Abrir, ler e escrever arquivos de forma segura utilizando `with open(...)`.
2. Compreender os modos de abertura (`r`, `w`, `a`, `b`, `+`).
3. Tratar encoding UTF-8 explicitamente para evitar erros de plataforma.
"""

import os


def demonstrar_arquivos() -> None:
    filename = "temp_exemplo.txt"
    print("\n--- 1. ESCRITA E LEITURA SEGURA COM `with` ---")

    # Escrita segura em UTF-8
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Linha 1: Aprendendo Python Sênior\n")
        f.write("Linha 2: Manipulação segura de arquivos\n")

    print(f"[OK] Arquivo '{filename}' criado.")

    # Leitura linha a linha (O(1) memória por linha)
    with open(filename, "r", encoding="utf-8") as f:
        for num, linha in enumerate(f, start=1):
            print(f"  [Linha {num}] {linha.strip()}")

    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)
        print("[OK] Arquivo temporário removido.")


def main() -> None:
    print("==========================================================")
    print("  AULA 25: MANIPULAÇÃO DE ARQUIVOS E I/O SEGURO")
    print("==========================================================")
    demonstrar_arquivos()
    print("\n[Concluido] Arquivo 25 executado com sucesso.")


if __name__ == "__main__":
    main()
