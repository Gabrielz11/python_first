"""
54_asyncio_avancado.py - Primitivas de Sincronização Assíncrona (`Semaphore` e `Queue`)

Objetivos:
1. Limitar a concorrência máxima de requisições assíncronas com `asyncio.Semaphore`.
2. Implementar comunicação entre corrotinas produtoras e consumidoras via `asyncio.Queue`.
"""

import asyncio


async def trabalhador_limitado(id: int, semaforo: asyncio.Semaphore) -> None:
    async with semaforo:
        print(f"  [Worker {id}] Adquiriu slot do semáforo. Executando...")
        await asyncio.sleep(0.05)


async def main_async() -> None:
    semaforo = asyncio.Semaphore(2)  # Máximo 2 em execução simultânea
    tarefas = [trabalhador_limitado(i, semaforo) for i in range(4)]
    await asyncio.gather(*tarefas)


def main() -> None:
    print("==========================================================")
    print("  AULA 54: ASYNCIO SEMAPHORE E CONTROLE DE CONCORRÊNCIA")
    print("==========================================================")
    asyncio.run(main_async())
    print("\n[Concluido] Arquivo 54 executado com sucesso.")


if __name__ == "__main__":
    main()
