"""
53_asyncio_tasks.py - Concorrência Assíncrona (`asyncio.create_task` e `asyncio.gather`)

Objetivos:
1. Executar múltiplas corrotinas simultaneamente no Event Loop com `asyncio.gather()`.
2. Criar tarefas em segundo plano com `asyncio.create_task()`.
"""

import asyncio


async def tarefa_assincrona(nome: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Resultado_{nome}"


async def main_async() -> None:
    print("Executando 3 tarefas concorrentes em paralelo no Event Loop:")
    resultados = await asyncio.gather(
        tarefa_assincrona("T1", 0.1),
        tarefa_assincrona("T2", 0.05),
        tarefa_assincrona("T3", 0.08),
    )
    print(f"Todos resultados coletados: {resultados}")


def main() -> None:
    print("==========================================================")
    print("  AULA 53: ASYNCIO GATHER E CRIAÇÃO DE TASKS")
    print("==========================================================")
    asyncio.run(main_async())
    print("\n[Concluido] Arquivo 53 executado com sucesso.")


if __name__ == "__main__":
    main()
