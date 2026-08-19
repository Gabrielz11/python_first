"""
50_context_managers.py - Context Managers Customizados (`__enter__` e `__exit__`)

Objetivos:
1. Criar gerenciadores de contexto com suporte à instrução `with`.
2. Tratar exceções dentro do método `__exit__`.
"""

from typing import Any


class GerenciadorRecurso:
    def __init__(self, nome_recurso: str) -> None:
        self.nome_recurso = nome_recurso

    def __enter__(self) -> "GerenciadorRecurso":
        print(f"[RECURSO] Adquirindo '{self.nome_recurso}'...")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool | None:
        print(f"[RECURSO] Liberando '{self.nome_recurso}'.")
        if exc_type is not None:
            print(f"  [!] Exceção suprimida no exit: {exc_val}")
            return True
        return False


def main() -> None:
    print("==========================================================")
    print("  AULA 50: CONTEXT MANAGERS (__ENTER__ E __EXIT__)")
    print("==========================================================")
    with GerenciadorRecurso("Conexao_DB_Test"):
        print("  [Op] Executando queries dentro do contexto...")
        raise RuntimeError("Falha temporária de rede!")
    print("\n[Concluido] Arquivo 50 executado com sucesso.")


if __name__ == "__main__":
    main()
