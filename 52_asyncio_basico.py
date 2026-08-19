"""
52_asyncio_basico.py - Programação Assíncrona com `asyncio`, Corrotinas e Event Loop

Objetivos:
1. Compreender o Event Loop e execução não-bloqueante I/O.
2. Definir corrotinas com `async def` e pausá-las com `await`.
3. Executar o ponto de entrada assíncrono com `asyncio.run()`.
"""

import asyncio


async def buscar_dados_async(id_req: int) -> str:
    print(f"  [Req {id_req}] Iniciando I/O não-bloqueante...")
    await asyncio.sleep(0.1)  # Simula I/O de rede sem bloquear a thread
    print(f"  [Req {id_req}] I/O concluído.")
    return f"Dados_Req_{id_req}"


async def main_async() -> None:
    res = await buscar_dados_async(1)
    print(f"Resultado recebido: {res}")


def main() -> None:
    print("==========================================================")
    print("  AULA 52: PROGRAMAÇÃO ASSÍNCRONA COM ASYNCIO")
    print("==========================================================")
    asyncio.run(main_async())
    print("\n[Concluido] Arquivo 52 executado com sucesso.")


if __name__ == "__main__":
    main()
