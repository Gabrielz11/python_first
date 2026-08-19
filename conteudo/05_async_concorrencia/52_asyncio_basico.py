"""
52_asyncio_basico.py - Programação Assíncrona, Corrotinas, Event Loop e async/await

Objetivos:
1. Dominar os conceitos fundamentais da programação assíncrona com o módulo nativo `asyncio`.
2. Compreender a diferença entre funções síncronas e Corrotinas (`async def`).
3. Entender o papel do Event Loop como orquestrador de multitarefa cooperativa em thread única.
4. Utilizar a instrução `await` para pausar a execução cooperativamente durante operações de I/O.
5. Iniciar a execução do loop assíncrono utilizando o ponto de entrada `asyncio.run()`.
"""

import asyncio
import time


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o asyncio e a Programação Assíncrona?
O `asyncio` é a biblioteca padrão do Python para escrever código concorrente utilizando a sintaxe `async/await`.

Conceitos Fundamentais:
1. Event Loop (Laço de Eventos): É o "coraração" do asyncio. Roda em uma ÚNICA thread e gerencia
   a execução de múltiplas tarefas concorrentes através de I/O não-bloqueante.
2. Corrotina (`async def`): Uma função declarada com `async def`. Quando chamada, ela NÃO executa
   seu código imediatamente; ela retorna um objeto corrotina.
3. Multitarefa Cooperativa: Em vez do SO alternar as threads de forma preempitativa, cada corrotina
   CEDE O CONTROLE voluntariamente de volta ao Event Loop ao utilizar a palavra-chave `await`.
4. `await`: Pausa a execução da corrotina atual até que a operação assíncrona (I/O, banco, rede) seja concluída,
   permitindo que o Event Loop execute OUTRAS corrotinas no intervalo.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CORROTINAS E ASYNCIO.RUN()
# ==========================================================
async def buscar_dados_banco_async(query_id: int) -> dict[str, str]:
    """Corrotina que simula uma consulta a banco de dados não-bloqueante."""
    print(f"  [DB Query {query_id}] Enviando requisição para o banco de dados...")
    # asyncio.sleep cede o controle para o Event Loop sem bloquear a thread!
    await asyncio.sleep(0.1)
    print(f"  [DB Query {query_id}] Resposta recebida do banco de dados!")
    return {"id": str(query_id), "status": "OK"}


async def main_async() -> None:
    print("\n--- 1. FUNDAMENTOS: Executando Corrotina com await ---")

    # Execução sequencial com await
    inicio = time.perf_counter()
    resultado1 = await buscar_dados_banco_async(101)
    resultado2 = await buscar_dados_banco_async(102)
    fim = time.perf_counter()

    print(f"Resultado 1: {resultado1}")
    print(f"Resultado 2: {resultado2}")
    print(f"Tempo total (sequencial await): {(fim - inicio)*1000:.2f} ms")


def demonstrar_fundamentos_asyncio() -> None:
    # asyncio.run() cria o Event Loop, roda a corrotina principal e fecha o loop ao final.
    asyncio.run(main_async())


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PARALELISMO COOPERATIVO
# ==========================================================
async def tarefa_assincrona(nome: str, tempo_espera: float) -> None:
    print(f"  [Tarefa {nome}] Iniciada...")
    await asyncio.sleep(tempo_espera)
    print(f"  [Tarefa {nome}] Concluída após {tempo_espera}s!")


async def demonstrar_cooperacao_async() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Concorrência Cooperativa ---")
    inicio = time.perf_counter()

    # Agendando tarefas concorrentes com asyncio.gather
    await asyncio.gather(
        tarefa_assincrona("A", 0.2),
        tarefa_assincrona("B", 0.1),
        tarefa_assincrona("C", 0.15),
    )
    fim = time.perf_counter()
    print(f"Tempo total concorrente (asyncio.gather): {(fim - inicio)*1000:.2f} ms (Praticamente o tempo da mais longa!)")


def demonstrar_cooperacao() -> None:
    asyncio.run(demonstrar_cooperacao_async())


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class MicrosservicoClienteAsync:
    """Simula um cliente HTTP assíncrono em microsserviços (ex: httpx / aiohttp)."""

    @staticmethod
    async def get_user_profile(user_id: int) -> dict[str, Any]:
        await asyncio.sleep(0.05)  # Simula I/O de rede
        return {"user_id": user_id, "name": "Gabriel", "role": "developer"}


async def endpoint_controller_async() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Async Controller ---")
    client = MicrosservicoClienteAsync()
    perfil = await client.get_user_profile(1001)
    print(f"Perfil retornado pelo controller assíncrono: {perfil}")


def demonstrar_aplicacao_backend() -> None:
    asyncio.run(endpoint_controller_async())


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: SYSTEM CALLS SELECT/EPOLL
# ==========================================================
"""
Como o Event Loop do asyncio funciona por baixo dos panos:
1. O Event Loop utiliza seletores de I/O de baixo nível do Sistema Operacional (`select()`, `epoll()` no Linux, `kqueue()` no macOS, `IOCP` no Windows).
2. Quando você faz `await socket.recv()`, o asyncio registra o Socket File Descriptor no `epoll` do SO e coloca a corrotina em estado "pausado".
3. A thread fica livre para processar outras corrotinas enquanto o SO aguarda os dados da placa de rede.
4. Assim que a placa de rede recebe os bytes, o SO notifica o `epoll`, e o Event Loop acorda a corrotina pausada.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Troca de Contexto Assíncrona (Context Switch entre corrotinas): Tempo O(1) [Em espaço de usuário, ultra-rápida sem overhead de Kernel].
- Espaço: O(N) onde N é o número de objetos Corrotina/Task na memória RAM do Event Loop.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar time.sleep() bloqueante dentro de uma função async
    print("[X] Nao-Pythonic (Bloqueando o Event Loop):")
    print("  async def f(): time.sleep(1)  # PERIGO! Bloqueia TODAS as corrotinas do servidor!")

    # [OK] PYTHONIC: Usar asyncio.sleep() não-bloqueante
    print("\n[OK] Pythonic:")
    print("  async def f(): await asyncio.sleep(1)  # Cede o controle para o Event Loop!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. NUNCA utilize funções síncronas bloqueantes (como `time.sleep()`, `requests.get()`, `urllib.request`) dentro de corrotinas `async def`.
2. Utilize o ponto de entrada `asyncio.run(main())` para inicializar a aplicação (evite manipular loops manuais com `get_event_loop()`).
3. Toda função declarada com `async def` DEVE ser invocada com a palavra-chave `await` (ou agendada via `create_task`).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    async def corrotina_exemplo() -> str:
        return "dados"

    # Armadilha 1: Chamar uma corrotina sem o operador await
    res = corrotina_exemplo()  # [!] Retorna o objeto corrotina, NÃO executa o código!
    print(f"[!] Armadilha 1 (Esqueceu o await): Retornou objeto {type(res).__name__}")
    # Para evitar o RuntimeWarning: coroutine was never awaited, fechamos manualmente o objeto de teste
    res.close()


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o asyncio consegue gerenciar milhares de conexões simultâneas usando apenas uma única thread?"
A: "O asyncio opera em um modelo de I/O Não-Bloqueante com Multitarefa Cooperativa.
    Em aplicações tradicionais (I/O bloqueante), cada conexão exige uma Thread do SO que passa a maior parte do tempo ociosa esperando a rede.
    No asyncio, existe apenas uma thread rodando um Event Loop acoplado a chamadas de sistema eficientes (como `epoll` no Linux).
    Quando uma corrotina espera por I/O de rede (`await`), ela cede voluntariamente o controle ao Event Loop, permitindo que a mesma thread processe milhares de outras requisições sem gastar memória alocando novas Threads do SO."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma corrotina `async def consultar_cotacao(moeda: str) -> float` que simule um atraso de 0.1s e retorne o valor da moeda.
# Exercício 2: Escreva uma função assíncrona que execute a consulta das moedas "USD", "EUR" e "GBP" simultaneamente usando `asyncio.gather`.
# Exercício 3: Escreva uma corrotina que tente conectar a um serviço assíncrono e dispare um timeout com `asyncio.timeout`.


def main() -> None:
    print("==========================================================")
    print("  AULA 52: PROGRAMAÇÃO ASSÍNCRONA, EVENT LOOP E ASYNC/AWAIT")
    print("==========================================================")
    demonstrar_fundamentos_asyncio()
    demonstrar_cooperacao()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 52 executado com sucesso.")


if __name__ == "__main__":
    main()
