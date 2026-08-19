"""
56_multiprocessing.py - Paralelismo Real de CPU com `multiprocessing`

Objetivos:
1. Superar a trava do GIL utilizando múltiplos processos isolados do SO.
2. Utilizar `multiprocessing.Process` para tarefas CPU-bound.
"""

import multiprocessing
import os


def tarefa_cpu(id_proc: int) -> None:
    PID = os.getpid()
    print(f"  [Processo {id_proc}] Rodando no PID do SO: {PID}")


def main() -> None:
    print("==========================================================")
    print("  AULA 56: MULTIPROCESSING E PARALELISMO REAL DE CPU")
    print("==========================================================")
    processos = [multiprocessing.Process(target=tarefa_cpu, args=(i,)) for i in range(2)]
    for p in processos:
        p.start()
    for p in processos:
        p.join()
    print("\n[Concluido] Arquivo 56 executado com sucesso.")


if __name__ == "__main__":
    main()
