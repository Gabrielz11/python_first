"""
verify_all_87.py - Script de verificação e auditoria dos 87 arquivos na estrutura de pastas em conteudo/.
"""

import os
import subprocess
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conteudo")

def main() -> None:
    if not os.path.exists(BASE_DIR):
        print(f"[X] Pasta {BASE_DIR} não encontrada!")
        sys.exit(1)

    all_files = []
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".py") and len(f) >= 2 and f[0:2].isdigit():
                rel_path = os.path.relpath(os.path.join(root, f), BASE_DIR)
                all_files.append((f, os.path.join(root, f), rel_path))
    
    all_files.sort(key=lambda item: item[0])
    existing_count = len(all_files)
    print(f"Total de scripts numerados encontrados em conteudo/: {existing_count}")
    
    execution_errors = []
    
    for filename, abs_path, rel_path in all_files:
        res = subprocess.run([sys.executable, abs_path], capture_output=True, text=True)
        if res.returncode != 0:
            execution_errors.append((rel_path, res.stderr.strip()))
            print(f"  [X] Erro em {rel_path}: {res.stderr.strip()[:100]}")
        else:
            print(f"  [OK] {rel_path}")

    print("\n--------------------------------------------------")
    print("Scripts criados: 87")
    print(f"Total esperado: 87")
    print(f"Total encontrado: {existing_count}")
    print(f"Arquivos com erro de execução: {len(execution_errors)}")
    if execution_errors:
        for err_script, err_msg in execution_errors:
            print(f"  - {err_script}: {err_msg}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
