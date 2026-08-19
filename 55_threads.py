"""
55_threads.py - Multithreading em Python (`threading.Thread` e `Lock`)

Objetivos:
1. Compreender o funcionamento de Threads para operações I/O-bound.
2. Compreender a limitação do GIL (Global Interpreter Lock) no CPython.
3. Evitar Race Conditions utilizando `threading.Lock`.
"""

import threading

contador_compartilhado = 0
lock = threading.Lock()


def incrementar_contador() -> None:
    global contador_compartilhado
    for _ in range(10000):
        with lock:
            contador_compartilhado += 1


def main() -> None:
    print("==========================================================")
    print("  AULA 55: MULTITHREADING E THREADING.LOCK")
    print("==========================================================")
    t1 = threading.Thread(target=incrementar_contador)
    t2 = threading.Thread(target=incrementar_contador)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Valor final do contador sincronizado com Lock: {contador_compartilhado}")
    print("\n[Concluido] Arquivo 55 executado com sucesso.")


if __name__ == "__main__":
    main()
