"""
55_threads.py - Multithreading, Concorrência de I/O, GIL e Sincronização com Lock

Objetivos:
1. Compreender o módulo `threading` e o modelo de execução multithread do Python.
2. Entender o papel e o impacto do Global Interpreter Lock (GIL) do CPython na execução de threads.
3. Identificar quando utilizar Threads (operações I/O-Bound) e quando evitá-las (tarefas CPU-Bound).
4. Prevenir Condições de Corrida (Race Conditions) utilizando travas de sincronização (`threading.Lock`).
5. Gerenciar o ciclo de vida de Threads com `start()` e `join()`.
"""

import threading
import time
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Threads e como funciona o GIL em Python?
Uma Thread (linha de execução) é a menor unidade de código gerenciada pelo sistema operacional dentro de um processo.

O Global Interpreter Lock (GIL):
Em CPython, o GIL é um Mutex interno que permite que APENAS UMA Thread execute bytecode Python
a cada instante, mesmo em computadores com múltiplos núcleos de processamento (Multi-core CPUs).

Impactos Práticos do GIL:
1. Para Tarefas I/O-Bound (Rede, Banco de Dados, Disco):
   THREADS SÃO ALTAMENTE EFICIENTES! Quando uma thread inicia uma operação de I/O (ex: `requests.get()`),
   ela LIBERA o GIL enquanto aguarda a resposta, permitindo que outra thread execute normalmente.
2. Para Tarefas CPU-Bound (Cálculos matemáticos, processamento de imagem):
   Threads NÃO trazem ganho de performance em CPython por causa do bloqueio do GIL!
   Nesses casos, deve-se utilizar o módulo `multiprocessing`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CRIAÇÃO DE THREADS E JOIN
# ==========================================================
def worker_download_simulado(id_download: int, tempo_espera: float) -> None:
    print(f"  [Thread {id_download}] Iniciando download em background...")
    # Durante o time.sleep() (que simula I/O), o CPython LIBERA o GIL!
    time.sleep(tempo_espera)
    print(f"  [Thread {id_download}] Download concluído em {tempo_espera}s!")


def demonstrar_fundamentos_threads() -> None:
    print("\n--- 1. FUNDAMENTOS: Criando e Aguardando Threads (start/join) ---")

    inicio = time.perf_counter()

    # Instanciando 3 Threads OS nativas
    t1 = threading.Thread(target=worker_download_simulado, args=(1, 0.2))
    t2 = threading.Thread(target=worker_download_simulado, args=(2, 0.15))
    t3 = threading.Thread(target=worker_download_simulado, args=(3, 0.1))

    # Inicia a execução concorrente das threads no SO
    t1.start()
    t2.start()
    t3.start()

    # join() bloqueia a thread principal até que as worker threads terminem
    t1.join()
    t2.join()
    t3.join()

    fim = time.perf_counter()
    print(f"Tempo total concorrente de 3 downloads: {(fim - inicio)*1000:.2f} ms")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SINCRONIZAÇÃO E RACE CONDITIONS (LOCK)
# ==========================================================
saldo_compartilhado = 0
trava_saldo = threading.Lock()


def incrementar_saldo_com_trava(quantidade: int) -> None:
    global saldo_compartilhado
    for _ in range(quantidade):
        # O gerenciador de contexto 'with trava_saldo' garante aquisição e liberação atômica do Lock
        with trava_saldo:
            saldo_compartilhado += 1


def demonstrar_race_condition_e_lock() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Prevenindo Race Conditions com Lock ---")
    global saldo_compartilhado
    saldo_compartilhado = 0

    threads = []
    # Cria 5 threads alterando o mesmo recurso compartilhado
    for _ in range(5):
        t = threading.Thread(target=incrementar_saldo_com_trava, args=(10_000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Saldo compartilhado final esperado (50.000): {saldo_compartilhado}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ThreadedLogFlusherService:
    """Serviço backend de descarregamento assíncrono de logs em Thread separada."""

    def __init__(self) -> None:
        self._buffer: list[str] = []
        self._lock = threading.Lock()

    def adicionar_log(self, mensagem: str) -> None:
        with self._lock:
            self._buffer.append(mensagem)

    def flush_in_background(self) -> None:
        t = threading.Thread(target=self._executar_flush, daemon=True)
        t.start()

    def _executar_flush(self) -> None:
        with self._lock:
            if self._buffer:
                print(f"  [Flusher Thread] Salvando {len(self._buffer)} logs no disco...")
                self._buffer.clear()


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Daemon Thread Logger ---")
    flusher = ThreadedLogFlusherService()

    flusher.adicionar_log("LOG 1: Servidor iniciado")
    flusher.adicionar_log("LOG 2: Requisicao HTTP 200")
    flusher.flush_in_background()
    time.sleep(0.05)


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: KERNEL THREADS E GIL
# ==========================================================
"""
Como as Threads funcionam no CPython:
1. Cada `threading.Thread` em Python mapeia diretamente para uma Thread real do Sistema Operacional (`pthread` no POSIX / Windows Native Thread).
2. Chaveamento de Threads (GIL Release): A cada N instruções de bytecode (ou durante chamadas de sistema I/O),
   o CPython libera a trava do GIL e permite que o escalonador do SO coloque outra thread em execução.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Criação de Thread (`Thread.start()`): Chamada de sistema do SO (sys_clone / CreateThread) -> Tempo O(1), Espaço O(1) de pilha no SO (geralmente 8MB por thread).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Alterar dados compartilhados entre threads sem nenhuma sincronização
    print("[X] Nao-Pythonic (Acesso a estado mutável global sem Lock):")
    print("  global conta; conta += 1  # Causa inconsistências e corrupção de dados!")

    # [OK] PYTHONIC: Utilizar threading.Lock com gerenciador de contexto `with lock:`
    print("\n[OK] Pythonic:")
    print("  with lock:\n      conta += 1  # Operação atômica thread-safe!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize Threads para concorrência de I/O (I/O-Bound), NUNCA para aceleração de cálculos intensivos de CPU (CPU-Bound).
2. Proteja SEMPRE o acesso a variáveis ou estruturas mutáveis compartilhadas entre threads com `threading.Lock`.
3. Sempre chame `.join()` nas threads filhas antes de encerrar o programa principal para garantir a conclusão do trabalho.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Impasse / Deadlock ao tentar adquirir dois Locks em ordem invertida em duas threads
    print("[!] Armadilha 1 (Deadlock): Adquirir Lock A -> Lock B em uma thread e Lock B -> Lock A em outra faz o programa travar infinitamente!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é o GIL (Global Interpreter Lock) do CPython e por que ele não impede o ganho de performance em tarefas I/O-Bound com multithreading?"
A: "O GIL é um Mutex global que garante que apenas uma Thread execute bytecode Python a cada instante de tempo para proteger o gerenciamento de memória por Reference Counting do CPython.
    No entanto, quando uma Thread executa uma chamada de sistema de I/O (como ler um arquivo do disco ou aguardar uma resposta de rede HTTP),
    o CPython LIBERA a trava do GIL durante o tempo de espera do I/O em nível de código C, permitindo que outra Thread assuma o GIL e execute seu código em paralelo."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função que dispare 5 Threads para simular o download concorrente de 5 arquivos e meça o tempo total com `time.perf_counter()`.
# Exercício 2: Crie uma classe `BancoSeguro` com um atributo `_saldo` protegido por `threading.Lock` e execute depósitos e saques concorrentes em 10 threads.
# Exercício 3: Escreva uma função que tente realizar um cálculo puramente matemático usando 4 threads e comprove que o tempo não reduz em CPython.


def main() -> None:
    print("==========================================================")
    print("  AULA 55: MULTITHREADING, CONCORRÊNCIA DE I/O E GIL")
    print("==========================================================")
    demonstrar_fundamentos_threads()
    demonstrar_race_condition_e_lock()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 55 executado com sucesso.")


if __name__ == "__main__":
    main()
