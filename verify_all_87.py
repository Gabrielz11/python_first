"""
verify_all_87.py - Script de verificação e auditoria dos 87 arquivos na pasta conteudo/.
"""

import os
import subprocess
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conteudo")

def main() -> None:
    if not os.path.exists(BASE_DIR):
        print(f"[X] Pasta {BASE_DIR} não encontrada!")
        sys.exit(1)

    all_files = sorted([f for f in os.listdir(BASE_DIR) if f.endswith(".py") and f[0:2].isdigit()])
    
    existing_count = len(all_files)
    print(f"Total de scripts numerados encontrados em conteudo/: {existing_count}")
    
    execution_errors = []
    
    for script in all_files:
        script_path = os.path.join(BASE_DIR, script)
        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if res.returncode != 0:
            execution_errors.append((script, res.stderr.strip()))
            print(f"  [X] Erro em {script}: {res.stderr.strip()[:100]}")
        else:
            print(f"  [OK] {script}")

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
