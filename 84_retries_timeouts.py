"""
84_retries_timeouts.py - Resiliência em HTTP (Retries com Exponential Backoff)

Objetivos:
1. Implementar o padrão de resiliência com tentativas de reexecução (Retries) e Exponential Backoff.
"""

from typing import Any, Callable
import time


def executar_com_retry(func: Callable[[], Any], max_tentativas: int = 3, delay_base: float = 0.05) -> Any:
    for tentativa in range(1, max_tentativas + 1):
        try:
            return func()
        except Exception as e:
            if tentativa == max_tentativas:
                print(f"[X] Tentativa {tentativa}/{max_tentativas} falhou. Esgotado!")
                raise
            espera = delay_base * (2 ** (tentativa - 1))
            print(f"[!] Tentativa {tentativa} falhou: {e}. Aguardando {espera:.3f}s...")
            time.sleep(espera)


def main() -> None:
    print("==========================================================")
    print("  AULA 84: RESILIÊNCIA HTTP E EXPONENTIAL BACKOFF")
    print("==========================================================")
    contador = 0
    def operacao_instavel() -> str:
        nonlocal contador
        contador += 1
        if contador < 2:
            raise ConnectionError("Falha de rede temporária")
        return "Sucesso na conexão!"

    res = executar_com_retry(operacao_instavel)
    print(f"Resultado final: {res}")
    print("\n[Concluido] Arquivo 84 executado com sucesso.")


if __name__ == "__main__":
    main()
