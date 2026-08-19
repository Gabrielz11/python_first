"""
56_multiprocessing.py - Multiprocessamento, Paralelismo CPU-Bound e Bypass do GIL

Objetivos:
1. Dominar o uso do módulo `multiprocessing` para alcançar verdadeiro Paralelismo em Python.
2. Compreender a diferença entre Concorrência (Threads/Asyncio) e Paralelismo Real (Processos).
3. Entender como o `multiprocessing` desvia (bypass) do GIL criando múltiplos processos Python isolados na RAM.
4. Utilizar `multiprocessing.Pool` para paralelizar tarefas CPU-Bound entre múltiplos núcleos da CPU.
5. Evitar a armadilha fatal de não utilizar `if __name__ == '__main__':` em sistemas Windows e macOS.
"""

import multiprocessing
import os
import time
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo multiprocessing?
Ao contrário do módulo `threading` (que executa múltiplas threads sujeitas ao GIL em uma única instância do CPython),
o `multiprocessing` cria MÚLTIPLOS PROCESSOS Python independentes no sistema operacional.

Vantagens Principais:
1. Verdadeiro Paralelismo Multi-Core: Cada processo filho possui a sua própria instância do interpretador CPython e seu próprio GIL.
   Dessa forma, o código consegue utilizar 100% de todos os núcleos físicos do processador (CPU-Bound).
2. Memória Isolada: Cada processo possui seu próprio espaço de memória RAM. Se um processo filho estourar ou falhar, os outros continuam intactos.

Comunicação Inter-Processos (IPC):
Como os processos têm memória isolada, a troca de dados entre eles exige serialização (via `pickle`) utilizando `Queue`, `Pipe` ou `Pool`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: MULTIPROCESSING.POOL
# ==========================================================
def calcular_fatorial_cpu_bound(n: int) -> int:
    """Função CPU-Bound que realiza cálculo pesado em um núcleo."""
    pid = os.getpid()
    # print(f"  [Processo PID {pid}] Calculando fatorial de {n}...")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return n  # Retorna apenas a confirmação para simplificar output


def demonstrar_fundamentos_pool() -> None:
    print("\n--- 1. FUNDAMENTOS: Paralelismo com multiprocessing.Pool ---")

    # Identifica o número de núcleos lógicos disponíveis na máquina
    qtd_cores = multiprocessing.cpu_count()
    print(f"Número de núcleos de CPU detectados na máquina: {qtd_cores}")

    numeros = [5000, 6000, 7000, 8000]

    # Execução Paralela distribuída entre os núcleos da CPU
    t0 = time.perf_counter()
    with multiprocessing.Pool(processes=min(4, qtd_cores)) as pool:
        resultados = pool.map(calcular_fatorial_cpu_bound, numeros)
    t1 = time.perf_counter()

    print(f"Resultados processados nos núcleos: {resultados}")
    print(f"Tempo de execução paralela: {(t1 - t0)*1000:.2f} ms")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PROCESS SEPARADO COM QUEUE
# ==========================================================
def worker_processo_queue(queue_ipc: Any, dados: list[int]) -> None:
    pid = os.getpid()
    soma_parcial = sum(x * x for x in dados)
    queue_ipc.put((pid, soma_parcial))


def demonstrar_process_e_queue() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Process e Queue (IPC) ---")

    fila_ipc: Any = multiprocessing.Queue()
    fatia_dados = list(range(10_000))

    # Criando um processo independente
    p = multiprocessing.Process(target=worker_processo_queue, args=(fila_ipc, fatia_dados))
    p.start()
    p.join()

    pid, resultado = fila_ipc.get()
    print(f"Resultado recebido do processo filho (PID {pid}): {resultado}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class DataProcessorParallelEngine:
    """Motor backend para processamento paralelo de grandes lotes de dados."""

    @staticmethod
    def processar_lote_em_paralelo(lotes: list[list[int]]) -> list[int]:
        with multiprocessing.Pool() as pool:
            # starmap ou map distribuem o trabalho nos processos trabalhadores
            resultados = pool.map(sum, lotes)
        return resultados


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Parallel Data Processor ---")
    lotes_dados = [list(range(1000)), list(range(1000, 2000)), list(range(2000, 3000))]

    totais = DataProcessorParallelEngine.processar_lote_em_paralelo(lotes_dados)
    print(f"Totais acumulados de cada lote: {totais}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: FORK VS SPAWN
# ==========================================================
"""
Mecanismos de Criação de Processos no SO (Start Methods):
1. `fork` (Padrão no Linux): Clona o processo pai na memória usando a otimização Copy-on-Write do Kernel. Rápido, porém pode causar deadlocks com threads.
2. `spawn` (Padrão no Windows e macOS): Inicia uma nova instância limpa do Python a partir do zero.
   Recarrega o módulo principal. Por isso, EXIGE estritamente a proteção `if __name__ == '__main__':`.
3. Pickle: Toda a comunicação e envio de argumentos entre processos é realizada serializando os objetos via `pickle`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Criação de Processo (`Process.start()` / `Pool()`):
  - Tempo: O(1) + Overhead de inicialização do CPython (no modo `spawn`, pode demorar alguns ms).
  - Espaço: O(M), aloca uma nova área de memória RAM separada no SO para o processo filho.
- Ganho de Performance em CPU-Bound: Divisão ideal do tempo de execução por N núcleos (Speedup ≈ N cores).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar Threads para tentar acelerar um loop pesado de matemática
    print("[X] Nao-Pythonic (Threads para CPU-Bound):")
    print("  threading.Thread(target=calculo_matematico)  # Bloqueado pelo GIL, sem ganho real!")

    # [OK] PYTHONIC: Utilizar multiprocessing.Pool
    print("\n[OK] Pythonic:")
    print("  multiprocessing.Pool().map(calculo_matematico, dados)  # Paralelismo real em N núcleos!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. OBRIGATÓRIO: Sempre coloque o ponto de entrada da aplicação dentro de `if __name__ == '__main__':`.
   Caso contrário, no Windows e macOS (modo `spawn`), o programa entrará em um loop infinito de criação de processos filhos!
2. Evite passar objetos gigantescos como argumentos para os processos filhos, pois a serialização via `pickle` consumirá mais tempo do que a própria execução.
3. Utilize `multiprocessing.Pool` com o Gerenciador de Contexto `with` para garantir o encerramento correto dos workers.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar passar funções lambda ou objetos não-pickláveis para processos filhos
    # sintaxe_errada = pool.map(lambda x: x*2, dados) -> PicklingError: Can't pickle local object
    print("[!] Armadilha 1: Tentar passar lambdas ou funções aninhadas para multiprocessing.Pool falha com PicklingError!")
    print("    Solução: Declare funções normais no escopo global do módulo.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre a criação de processos no Linux (`fork`) e no Windows (`spawn`) no módulo multiprocessing?"
A: "1. `fork` (Linux): O Kernel clona o processo pai exatamente como ele está na memória (Copy-on-Write). É muito rápido e preserva o estado inicial de variáveis.
    2. `spawn` (Windows / macOS): Um processo Python inteiramente novo é lançado a partir do zero. O Python precisa re-importar o módulo principal.
       Essa re-importação exige obrigatoriamente a proteção `if __name__ == '__main__':` no código para evitar um loop infinito de bootstrapping de processos."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função CPU-bound `verificar_primo(n: int) -> bool` e paralelize o teste de uma lista de números grandes usando `multiprocessing.Pool`.
# Exercício 2: Compare o tempo de processamento de um loop matemático pesado usando 1 processo vs N processos com `multiprocessing.Pool`.
# Exercício 3: Crie dois processos usando `multiprocessing.Process` que troquem mensagens utilizando `multiprocessing.Pipe()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 56: MULTIPROCESSAMENTO, PARALELISMO E BYPASS DO GIL")
    print("==========================================================")
    demonstrar_fundamentos_pool()
    demonstrar_process_e_queue()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 56 executado com sucesso.")


if __name__ == "__main__":
    main()
