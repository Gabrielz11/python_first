"""
54_asyncio_avancado.py - Sincronização Assíncrona: asyncio.Queue, Semaphore, Event e Lock

Objetivos:
1. Dominar o padrão Produtor-Consumidor (Producer-Consumer) assíncrono utilizando `asyncio.Queue`.
2. Limitar a concorrência máxima de requisições paralelas utilizando `asyncio.Semaphore`.
3. Sincronizar o estado de inicialização de microsserviços via `asyncio.Event`.
4. Evitar condições de corrida (Race Conditions) em estado compartilhado assíncrono com `asyncio.Lock`.
5. Prevenir travamentos (Deadlocks) causados pelo esquecimento de `queue.task_done()`.
"""

import asyncio
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Primitivas de Sincronização Assíncrona do asyncio:
Assim como na programação multithreaded, o código concorrente assíncrono precisa de ferramentas
para coordenar o acesso a recursos compartilhados e o ritmo de processamento:

1. `asyncio.Queue`: Fila FIFO (First-In, First-Out) não-bloqueante projetada para o padrão Produtor-Consumidor.
2. `asyncio.Semaphore(value)`: Limita o número de corrotinas que podem acessar um recurso simultaneamente (ex: limitar a 5 conexões ativas na API).
3. `asyncio.Event`: Mecanismo simples de sinalização de flag booleana. Uma corrotina aguarda (`await event.wait()`) até que outra dispare (`event.set()`).
4. `asyncio.Lock`: Mutex (Mutual Exclusion) assíncrono para garantir que apenas UMA corrotina altere uma variável/estado por vez.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: PRODUTOR-CONSUMIDOR COM ASYNCIO.QUEUE
# ==========================================================
async def produtor(queue: asyncio.Queue[str], quantidade: int) -> None:
    for i in range(1, quantidade + 1):
        item = f"Item_{i}"
        await queue.put(item)
        print(f"  [Produtor] Colocou {item} na fila (Tamanho atual: {queue.qsize()})")
        await asyncio.sleep(0.02)


async def consumidor(id_consumidor: int, queue: asyncio.Queue[str]) -> None:
    while True:
        # Pega um item da fila assíncrona
        item = await queue.get()
        print(f"  [Consumidor {id_consumidor}] Processando {item}...")
        await asyncio.sleep(0.05)
        # Notifica a fila que o item foi totalmente processado
        queue.task_done()


async def demonstrar_queue_produtor_consumidor() -> None:
    print("\n--- 1. FUNDAMENTOS: asyncio.Queue (Produtor-Consumidor) ---")
    queue: asyncio.Queue[str] = asyncio.Queue()

    # Inicia 2 trabalhadores (consumidores) em background
    workers = [
        asyncio.create_task(consumidor(1, queue)),
        asyncio.create_task(consumidor(2, queue)),
    ]

    # Produz 5 itens na fila
    await produtor(queue, 5)

    # Aguarda até que TODOS os itens da fila tenham sido processados via task_done()
    await queue.join()
    print("  [Queue] Todos os itens foram processados!")

    # Cancela os workers que estavam em loop infinito
    for w in workers:
        w.cancel()


def demonstrar_fundamentos() -> None:
    asyncio.run(demonstrar_queue_produtor_consumidor())


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SEMAPHORE PARA RATE LIMITING
# ==========================================================
async def requisitar_api_externa(id_req: int, semaforo: asyncio.Semaphore) -> None:
    # O bloco 'async with semaforo' garante que apenas N corrotinas entrem aqui simultaneamente
    async with semaforo:
        print(f"  [HTTP Req {id_req}] Slot adquirido no semáforo. Baixando dados...")
        await asyncio.sleep(0.1)
        print(f"  [HTTP Req {id_req}] Download concluído. Liberando slot.")


async def demonstrar_semaforo_async() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Limitação Concorrente com Semaphore ---")

    # Limita a no máximo 2 requisições simultâneas
    semaforo = asyncio.Semaphore(2)

    tarefas = [requisitar_api_externa(i, semaforo) for i in range(1, 6)]
    await asyncio.gather(*tarefas)


def demonstrar_semaforo() -> None:
    asyncio.run(demonstrar_semaforo_async())


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: ASYNCIO.EVENT
# ==========================================================
async def aguardar_inicializacao_banco(event_banco_pronto: asyncio.Event) -> None:
    print("  [Serviço Web] Aguardando sinal do banco de dados estar pronto...")
    await event_banco_pronto.wait()  # Pausa a corrotina até event_banco_pronto.set() ser chamado
    print("  [Serviço Web] Sinal recebido! Aceitando requisições HTTP.")


async def inicializar_banco_dados(event_banco_pronto: asyncio.Event) -> None:
    print("  [Banco de Dados] Conectando e executando migrações...")
    await asyncio.sleep(0.1)
    print("  [Banco de Dados] Migrações concluídas. Disparando sinal event.set()!")
    event_banco_pronto.set()  # Notifica todas as corrotinas que esperavam em .wait()


async def demonstrar_event_async() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Sinalização de Estado com asyncio.Event ---")
    event_banco = asyncio.Event()

    await asyncio.gather(
        aguardar_inicializacao_banco(event_banco),
        inicializar_banco_dados(event_banco),
    )


def demonstrar_event() -> None:
    asyncio.run(demonstrar_event_async())


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: DENTRO DO ASYNCIO.QUEUE
# ==========================================================
"""
Como o `asyncio.Queue` funciona por baixo dos panos:
1. Mantém uma deque interna para armazenar os itens (`collections.deque`).
2. Mantém duas filas de Objetos `Future` assíncronos: `_getters` (corrotinas aguardando itens) e `_putters` (corrotinas aguardando vaga em filas com limite de tamanho).
3. Quando `queue.put()` é chamado em uma fila com vaga, ele resolve o `Future` do próximo consumidor em `_getters`, acordando a corrotina consumidora imediatamente.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `queue.put()` / `queue.get()`: Tempo O(1) [Operação de inserção/remoção em deque CPython], Espaço O(N).
- `asyncio.Semaphore`: Tempo O(1) de aquisição/liberação de trava.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar listas normais e time.sleep para simular filas assíncronas
    print("[X] Nao-Pythonic (Listas normais em async):")
    print("  if len(lista) == 0: await asyncio.sleep(0.1)  # Polling ineficiente!")

    # [OK] PYTHONIC: Utilizar asyncio.Queue nativo
    print("\n[OK] Pythonic:")
    print("  item = await queue.get()  # Aguarda eficientemente o sinal do Event Loop!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre chame `queue.task_done()` para cada item retirado de um `asyncio.Queue` após o processamento ser concluído.
2. Utilize `async with semaforo:` para adquirir e liberar semáforos de forma segura garantindo a liberação do slot em caso de erro.
3. Utilize `asyncio.Lock` se duas ou mais corrotinas alterarem o mesmo dicionário ou lista compartilhada no escopo global.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer de chamar `queue.task_done()`, fazendo `queue.join()` travar em um Deadlock Infinito!
    print("[!] Armadilha 1: Esquecer queue.task_done() faz o await queue.join() travar para sempre!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como implementar o padrão Producer-Consumer em asyncio de forma que a aplicação saiba exatamente quando todas as tarefas foram processadas?"
A: "1. Utiliza-se um `asyncio.Queue` compartilhado entre o produtor e os trabalhadores consumidores.
    2. O produtor coloca itens na fila via `await queue.put(item)`.
    3. Cada consumidor retira um item via `item = await queue.get()`, processa o dado e OBRIGATORIAMENTE executa `queue.task_done()`.
    4. O chamador principal executa `await queue.join()`, que bloqueia até que a contagem de tarefas não finalizadas chegue a zero."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma fila `asyncio.Queue(maxsize=3)` e teste o comportamento do produtor ao tentar colocar mais de 3 itens.
# Exercício 2: Escreva uma função que limite o download simultâneo de 10 URLs a no máximo 3 requisições paralelas usando `asyncio.Semaphore(3)`.
# Exercício 3: Crie um `asyncio.Lock` protegendo uma variável `saldo_compartilhado` atualizada por 5 corrotinas concorrentes.


def main() -> None:
    print("==========================================================")
    print("  AULA 54: SINCRONIZAÇÃO ASSÍNCRONA, QUEUE E SEMAPHORE")
    print("==========================================================")
    demonstrar_fundamentos()
    demonstrar_semaforo()
    demonstrar_event()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 54 executado com sucesso.")


if __name__ == "__main__":
    main()
