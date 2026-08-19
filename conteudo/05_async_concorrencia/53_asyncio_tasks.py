"""
53_asyncio_tasks.py - asyncio.Task, TaskGroup, Cancelamento e Concorrência Estruturada

Objetivos:
1. Dominar o agendamento de tarefas concorrentes utilizando `asyncio.create_task()` e `asyncio.gather()`.
2. Conhecer o padrão de Concorrência Estruturada com `asyncio.TaskGroup` (Python 3.11+).
3. Aplicar técnicas de cancelamento de tarefas (`task.cancel()`) e tratamento da exceção `asyncio.CancelledError`.
4. Configurar Timeouts para proteger chamadas externas utilizando `asyncio.timeout()` (Python 3.11+).
5. Tratar exceções em lote com `return_exceptions=True` e `ExceptionGroup`.
"""

import asyncio
import time
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma asyncio.Task?
Uma `Task` (Tarefa) é um wrapper em torno de uma Corrotina responsável por agendar a sua execução
no Event Loop de forma independente e concorrente.

Diferença entre Corrotina e Task:
- Corrotina (`async def`): É um bloco de código assíncrono estático. Ela NÃO roda em segundo plano sozinha.
- Task (`asyncio.create_task(corrotina)`): Agenda a corrotina no Event Loop IMEDIATAMENTE. Ela começa a executar em background na próxima oportunidade do laço.

Concorrência Estruturada com `asyncio.TaskGroup` (Python 3.11+):
Garante o gerenciamento seguro de tarefas filhas dentro de um bloco `async with`.
Se qualquer tarefa do grupo falhar com exceção, o `TaskGroup` cancela automaticamente todas as outras tarefas filhas ativas, evitando tarefas órfãs na memória RAM.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CREATE_TASK E GATHER
# ==========================================================
async def worker_servico(id_worker: int, tempo_espera: float) -> str:
    print(f"  [Worker {id_worker}] Iniciando processamento...")
    await asyncio.sleep(tempo_espera)
    print(f"  [Worker {id_worker}] Finalizado!")
    return f"OK_{id_worker}"


async def demonstrar_create_task_e_gather() -> None:
    print("\n--- 1. FUNDAMENTOS: create_task() e gather() ---")

    # 1. Agendamento com create_task()
    task1 = asyncio.create_task(worker_servico(1, 0.1))
    task2 = asyncio.create_task(worker_servico(2, 0.15))

    # Aguardando a conclusão das tarefas agendadas
    res1 = await task1
    res2 = await task2
    print(f"Resultados individuais: {res1}, {res2}")

    # 2. Agendamento em lote com asyncio.gather()
    resultados = await asyncio.gather(
        worker_servico(10, 0.05),
        worker_servico(20, 0.05),
        worker_servico(30, 0.05),
    )
    print(f"Resultados do gather: {resultados}")


def demonstrar_fundamentos() -> None:
    asyncio.run(demonstrar_create_task_e_gather())


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: TASKGROUP (PYTHON 3.11+)
# ==========================================================
async def demonstrar_taskgroup_async() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: asyncio.TaskGroup (Python 3.11+) ---")

    # TaskGroup garante concorrência estruturada com gerenciador de contexto assíncrono
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(worker_servico(101, 0.1))
            t2 = tg.create_task(worker_servico(102, 0.05))

        print(f"Resultado TaskGroup t1: {t1.result()}")
        print(f"Resultado TaskGroup t2: {t2.result()}")
    except ExceptionGroup as eg:
        print(f"[!] Capturado ExceptionGroup no TaskGroup: {eg}")


def demonstrar_taskgroup() -> None:
    asyncio.run(demonstrar_taskgroup_async())


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: CANCELAMENTO E TIMEOUT
# ==========================================================
async def servico_lento_com_cancelamento() -> None:
    try:
        print("  [Serviço Lento] Processando etapa 1...")
        await asyncio.sleep(0.1)
        print("  [Serviço Lento] Processando etapa 2...")
        await asyncio.sleep(0.5)  # Será cancelado aqui!
    except asyncio.CancelledError:
        print("  [Serviço Lento] Cancelamento recebido! Executando cleanup de recursos...")
        raise  # Re-lança para o Event Loop confirmar o cancelamento


async def demonstrar_cancelamento_async() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Cancelamento de Tarefas e Timeout ---")

    task = asyncio.create_task(servico_lento_com_cancelamento())

    # Aguarda um pequeno intervalo e cancela a tarefa
    await asyncio.sleep(0.15)
    print("  [Controller] Tempo limite excedido! Cancelando tarefa em background...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("  [Controller] Tarefa cancelada com sucesso.")


def demonstrar_cancelamento() -> None:
    asyncio.run(demonstrar_cancelamento_async())


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: GARBAGE COLLECTION E STRONG REFERENCES
# ==========================================================
"""
Armadilha de Referências Fracas (Python 3.11+ / PEP 654 Warning):
1. O `asyncio.create_task()` guarda apenas uma referência fraca (weak reference) da tarefa dentro do Event Loop.
2. Se você criar uma tarefa em background sem armazenar seu retorno em uma variável ou conjunto (`background_tasks.add(task)`),
   o Garbage Collector do CPython pode DESTRUIR a tarefa no meio da execução!
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Criar uma Task (`asyncio.create_task`): Tempo O(1), Espaço O(1).
- `asyncio.gather(N tasks)`: Executa N tarefas concorrentemente em tempo max(T1, T2, ..., TN).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Manter tarefas assíncronas soltas sem tratamento de cancelamento
    print("[X] Nao-Pythonic:")
    print("  t = asyncio.create_task(f())  # Se falhar ou for esquecida, vaza exceções!")

    # [OK] PYTHONIC: Utilizar asyncio.TaskGroup (Python 3.11+)
    print("\n[OK] Pythonic (Concorrência Estruturada):")
    print("  async with asyncio.TaskGroup() as tg:\n      tg.create_task(f())  # Cancela automaticamente em caso de falha!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize `asyncio.TaskGroup` em novos projetos (Python 3.11+) para garantir a Concorrência Estruturada.
2. Ao usar `asyncio.gather()`, considere usar `return_exceptions=True` se quiser capturar erros sem interromper todas as outras tarefas.
3. Sempre capture e re-lance `asyncio.CancelledError` dentro de corrotinas que precisam realizar cleanup ao serem canceladas.
4. Mantenha referências fortes para tarefas de background de longa duração para evitar a coleta indesejada pelo Garbage Collector.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    async def armadilha_async() -> None:
        # Armadilha 1: Esquecer de tratar a exceção em gather() sem return_exceptions=True
        async def falhar(): raise ValueError("Erro na API")
        async def ok(): return "OK"

        try:
            # Sem return_exceptions=True, uma única falha aborta a leitura imediata
            await asyncio.gather(falhar(), ok())
        except ValueError as e:
            print(f"[!] Armadilha 1 (gather sem return_exceptions abortou): {e}")

        # Com return_exceptions=True, captura o erro como objeto de retorno!
        res = await asyncio.gather(falhar(), ok(), return_exceptions=True)
        print(f"[OK] Gather com return_exceptions=True: {res}")

    asyncio.run(armadilha_async())


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é Concorrência Estruturada (Structured Concurrency) em asyncio e por que o `asyncio.TaskGroup` foi introduzido no Python 3.11?"
A: "Concorrência Estruturada é o paradigma onde o ciclo de vida de tarefas concorrentes é vinculado a um escopo de código bem definido (como um bloco `async with`).
    Antes do Python 3.11, ao disparar tarefas soltas com `create_task()` ou `gather()`, se uma tarefa falhava, as outras podiam continuar rodando descontroladas em background (tarefas órfãs).
    O `asyncio.TaskGroup` garante que se QUALQUER tarefa dentro do grupo falhar, todas as outras tarefas filhas do mesmo grupo são automaticamente canceladas e seus erros consolidados em um `ExceptionGroup`, evitando vazamentos de recursos."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie três tarefas assíncronas que simulem consultas a serviços externos com tempos diferentes e execute-as via `asyncio.gather`.
# Exercício 2: Escreva um programa usando `asyncio.TaskGroup` (ou `asyncio.gather`) onde uma das tarefas lança um `ValueError` e trate o erro corretamente.
# Exercício 3: Crie uma tarefa de background que imprima um contador a cada 0.1s e cancele essa tarefa após 0.3s usando `task.cancel()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 53: ASYNCIO TASKS, TASKGROUP E CANCELAMENTO")
    print("==========================================================")
    demonstrar_fundamentos()
    demonstrar_taskgroup()
    demonstrar_cancelamento()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 53 executado com sucesso.")


if __name__ == "__main__":
    main()
