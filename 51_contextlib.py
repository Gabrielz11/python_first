"""
51_contextlib.py - Utilitários do Módulo `contextlib` (`@contextmanager`, `suppress`, `ExitStack`)

Objetivos:
1. Criar gerenciadores de contexto baseados em geradores usando `@contextmanager`.
2. Utilizar `contextlib.suppress` para ignorar exceções específicas de forma limpa.
"""

from contextlib import contextmanager, suppress
from typing import Generator


@contextmanager
def gerenciar_transacao() -> Generator[str, None, None]:
    print("[TRANSACAO] Iniciando transação ACID...")
    try:
        yield "ID_TRANSACAO_99"
    finally:
        print("[TRANSACAO] Encerrando / Commit da transação.")


def main() -> None:
    print("==========================================================")
    print("  AULA 51: MÓDULO CONTEXTLIB E @CONTEXTMANAGER")
    print("==========================================================")
    with gerenciar_transacao() as tx_id:
        print(f"  [WORK] Processando dados sob transação {tx_id}")

    # Suprimindo FileNotFoundError elegantemente
    with suppress(FileNotFoundError):
        import os
        os.remove("arquivo_inexistente_123.txt")

    print("\n[Concluido] Arquivo 51 executado com sucesso.")


if __name__ == "__main__":
    main()
