"""
58_cpu_vs_io_bound.py - Benchmark Comparativo: CPU-Bound vs I/O-Bound (Asyncio vs Threads vs Processos)

Objetivos:
1. Compreender a diferença fundamental entre gargalos I/O-Bound (redes/disco) e gargalos CPU-Bound (processamento pesado).
2. Escolher a estratégia ideal de concorrência/paralelismo para cada cenário de arquitetura de software.
3. Executar benchmarks práticos comprovando a eficiência de cada modelo em CPython.
4. Identificar o impacto do GIL nas estratégias de Threads vs Multiprocessing.
5. Construir uma Matriz de Decisão para projetos de alta performance no backend.
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Classificação de Gargalos de Performance:

1. Tarefas I/O-Bound (Bound to Input/Output):
   - O tempo de execução é limitado pela velocidade de resposta de periféricos ou redes externos (espera de banco de dados, chamadas HTTP, leitura de arquivos do disco).
   - A CPU passa a maior parte do tempo OCIOSA aguardando retornos.
   - Soluções Ideais em Python:
     - `asyncio`: Ultra-eficiente para milhares de conexões simultâneas em thread única (Menor consumo de RAM).
     - `threading` / `ThreadPoolExecutor`: Ótimo para código síncrono legado de I/O.

2. Tarefas CPU-Bound (Bound to Central Processing Unit):
   - O tempo de execução é limitado pela velocidade da CPU executando instruções matemáticas/lógicas sem espera (cálculos de matrizes, compressão de imagens, machine learning).
   - O GIL bloqueia o ganho de performance ao usar Threads em CPython!
   - Solução Ideal em Python:
     - `multiprocessing` / `ProcessPoolExecutor`: Cria processos independentes na RAM, ignorando o GIL e paralelizando em N núcleos.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: TAREFA I/O-BOUND (BENCHMARK)
# ==========================================================
def tarefa_io_sincrona(id_req: int) -> str:
    time.sleep(0.05)  # Simula I/O
    return f"OK_{id_req}"


async def tarefa_io_assincrona(id_req: int) -> str:
    await asyncio.sleep(0.05)  # Simula I/O assíncrono
    return f"OK_{id_req}"


def demonstrar_benchmark_io_bound() -> None:
    print("\n--- 1. BENCHMARK I/O-BOUND: Síncrono vs Threads vs Asyncio ---")

    requisicoes = list(range(10))

    # 1. Síncrono Sequencial
    t0 = time.perf_counter()
    _ = [tarefa_io_sincrona(i) for i in requisicoes]
    t1 = time.perf_counter()
    print(f"1. Síncrono Sequencial: {(t1 - t0)*1000:.2f} ms")

    # 2. Multithreading (ThreadPoolExecutor)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        _ = list(executor.map(tarefa_io_sincrona, requisicoes))
    t1 = time.perf_counter()
    print(f"2. ThreadPoolExecutor (5 Threads): {(t1 - t0)*1000:.2f} ms (Excelente ganho no I/O!)")

    # 3. Asyncio
    async def rodar_async():
        await asyncio.gather(*[tarefa_io_assincrona(i) for i in requisicoes])

    t0 = time.perf_counter()
    asyncio.run(rodar_async())
    t1 = time.perf_counter()
    print(f"3. Asyncio (Thread única): {(t1 - t0)*1000:.2f} ms (Excelente ganho no I/O!)")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: TAREFA CPU-BOUND (BENCHMARK DO GIL)
# ==========================================================
def tarefa_cpu_bound(n: int) -> int:
    """Cálculo pesado de CPU."""
    soma = 0
    for i in range(n):
        soma += i * i
    return soma


def demonstrar_benchmark_cpu_bound() -> None:
    print("\n--- 2. BENCHMARK CPU-BOUND: Threads vs Processos (Gargalo do GIL) ---")

    lotes_cpu = [10_000_000, 10_000_000, 10_000_000, 10_000_000]

    # 1. Threads para CPU-Bound (Bloqueado pelo GIL!)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(tarefa_cpu_bound, lotes_cpu))
    t1 = time.perf_counter()
    print(f"1. ThreadPoolExecutor (CPU-Bound): {(t1 - t0)*1000:.2f} ms (Sem ganho por causa do GIL!)")

    # 2. Processos para CPU-Bound (Bypass do GIL!)
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(tarefa_cpu_bound, lotes_cpu))
    t1 = time.perf_counter()
    print(f"2. ProcessPoolExecutor (CPU-Bound): {(t1 - t0)*1000:.2f} ms (Paralelismo real nos núcleos!)")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: MATRIZ DE DECISÃO
# ==========================================================
def demonstrar_matriz_decisao() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Matriz de Decisão Arquitetural ---")
    print("""
    +------------------------+--------------------------+---------------------------------+
    | Tipo de Problema       | Tecnologia Recomendada    | Motivo Principal                |
    +------------------------+--------------------------+---------------------------------+
    | APIs HTTP / WebSockets | asyncio (FastAPI/Tornado)| Milhares de conexões com pouca  |
    | (I/O Concorrente)      |                          | memória RAM em 1 thread.        |
    +------------------------+--------------------------+---------------------------------+
    | Script I/O Síncrono    | ThreadPoolExecutor       | Paraleliza bibliotecas bloquean-|
    | (Web Scraping / Files) |                          | tes sem reescrever código.      |
    +------------------------+--------------------------+---------------------------------+
    | Processamento de Dados | ProcessPoolExecutor /    | Desvia do GIL e distribui       |
    | (ML / Imagens / Math)  | Celery Worker            | a carga nos núcleos da CPU.     |
    +------------------------+--------------------------+---------------------------------+
    """)


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: CONTEXT SWITCH VS PROCESS FORK
# ==========================================================
"""
Resumo dos Custos Internos:
- Asyncio Coroutines: Troca de contexto ultra-leve em espaço de usuário (Nível de código Python) -> ~100 nanosegundos.
- OS Threads: Troca de contexto em espaço de Kernel do SO (Salva registradores de CPU) -> ~1 a 10 microsegundos.
- OS Processes: Criação de um espaço de memória inteiramente novo -> ~1 a 10 milissegundos (na inicialização do `spawn`).
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- I/O-Bound (N tarefas de tempo T): Tempo sequencial O(N*T) reduzido para O(max(T)) com concorrência.
- CPU-Bound (N tarefas pesadas em C núcleos): Tempo reduzido para O(N / C) com `ProcessPoolExecutor`.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Misturar abordagens sem analisar se o problema é CPU-bound ou I/O-bound
    print("[X] Nao-Pythonic:")
    print("  Tentar usar `asyncio` para acelerar um processamento pesado de imagens de 10GB.")

    # [OK] PYTHONIC: Escolher a ferramenta exata para a natureza do problema
    print("\n[OK] Pythonic:")
    print("  Use asyncio para I/O massivo de rede; use ProcessPoolExecutor para tarefas pesadas de CPU!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Regra de Ouro: Meça antes de otimizar (Profile before Optimizing). Identifique se o gargalo é de I/O ou CPU.
2. Para APIs Web modernas de alto tráfego (FastAPI), priorize o modelo assíncrono (`asyncio`).
3. Se precisar executar cálculos pesados dentro de uma aplicação `asyncio`, descarregue a tarefa pesada usando `loop.run_in_executor(ProcessPoolExecutor, func)`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Achar que colocar `async def` na frente de uma função com cálculo matemático pesado vai deixá-la mais rápida
    print("[!] Armadilha 1: `async def` NÃO torna o código de CPU mais rápido; apenas permite ceder o controle em operações de I/O!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Se o seu servidor backend em Python estiver enfrentando alta latência sob carga, como você diagnostica se o problema é CPU-Bound ou I/O-Bound e qual a solução?"
A: "1. Diagnóstico: Inspeciono a utilização de CPU e I/O do servidor (via `top`, `htop` ou métricas do APM).
       - Se a utilização de CPU estiver perto de 100% em 1 núcleo enquanto a máquina tem 8 núcleos, o problema é CPU-Bound travado pelo GIL.
       - Se a utilização de CPU estiver baixa (< 10%), mas a latência alta, o problema é I/O-Bound (esperando respostas lentas de banco de dados ou APIs externas).
    2. Solução:
       - Para I/O-Bound: Migro as chamadas para I/O não-bloqueante via `asyncio` ou aumento o pool de workers/threads com `ThreadPoolExecutor`.
       - Para CPU-Bound: Adiciono um pool de multiprocessamento com `ProcessPoolExecutor` ou descarrego a tarefa para um worker desacoplado como Celery/RabbitMQ."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função que meça o tempo de execução de 20 chamadas simuladas de I/O com `ThreadPoolExecutor` vs `asyncio`.
# Exercício 2: Escreva um script que compare o tempo de cálculo de números primos entre `ThreadPoolExecutor` e `ProcessPoolExecutor`.
# Exercício 3: Implemente uma corrotina `asyncio` que chame uma função CPU-Bound desacoplada via `loop.run_in_executor`.


def main() -> None:
    print("==========================================================")
    print("  AULA 58: CPU-BOUND VS I/O-BOUND - GUIA DEFINITIVO")
    print("==========================================================")
    demonstrar_benchmark_io_bound()
    demonstrar_benchmark_cpu_bound()
    demonstrar_matriz_decisao()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 58 executado com sucesso.")


if __name__ == "__main__":
    main()
