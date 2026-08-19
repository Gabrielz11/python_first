"""
84_profiling.py - Profiling de Código, cProfile, pstats, timeit e tracemalloc

Objetivos:
1. Dominar as ferramentas de Profiling (Análise de Desempenho) e Benchmarking em Python.
2. Identificar gargalos de CPU utilizando o profiler determinístico nativo `cProfile`.
3. Analisar e ordenar estatísticas de desempenho com o módulo `pstats`.
4. Medir o tempo de execução de pequenos trechos de código com precisão usando `timeit`.
5. Rastrear alocações de memória RAM e detectar vazamentos de memória (Memory Leaks) com `tracemalloc`.
"""

import cProfile
import pstats
import time
import timeit
import tracemalloc
from typing import Any


# ==========================================================
# 1. CONCEITO DE PROFILING E BENCHMARKING
# ==========================================================
"""
O que é Profiling?
Profiling e a análise dinâmica do programa para medir o consumo de tempo de CPU, chamadas de funções e alocação de memória RAM.

A Regra de Donald Knuth:
"Otimização prematura e a raiz de todos os males." (Premature optimization is the root of all evil).
Antes de modificar qualquer código para torná-lo "mais rápido", você DEVE medir (Profile) para descobrir onde o programa realmente passa a maior parte do tempo!

Ferramentas Nativas em Python:
1. `cProfile`: Profiler determinístico escrito em C com baixíssimo overhead. Mede a frequência e o tempo de cada função.
2. `pstats`: Utilitário para formatar, filtrar e ordenar relatórios gerados pelo `cProfile`.
3. `timeit`: Módulo para benchmark preciso de trechos curtos de código.
4. `tracemalloc`: Módulo para rastrear alocações de memória RAM em nível de bloco Python.
"""


# ==========================================================
# 2. SINTAXE E DEMONSTRAÇÃO DO CPROFILE E PSTATS
# ==========================================================
def funcao_rapida() -> None:
    time.sleep(0.01)


def funcao_lenta_gargalo() -> None:
    time.sleep(0.1)


def fluxo_principal_app() -> None:
    """Simulação de fluxo de backend com um gargalo oculto."""
    for _ in range(5):
        funcao_rapida()
    funcao_lenta_gargalo()


def demonstrar_cprofile() -> None:
    print("\n--- 1. FUNDAMENTOS: Profiling de CPU com cProfile e pstats ---")

    # Inicia o profiler determinístico
    profiler = cProfile.Profile()
    profiler.enable()

    # Executa a função que queremos analisar
    fluxo_principal_app()

    profiler.disable()

    # Formata e exibe os resultados usando pstats
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")  # Ordena por tempo cumulativo
    print("Estatísticas do Profiler (Top 5 funções mais lentas):\n")
    stats.print_stats(5)


# ==========================================================
# 3. BENCHMARK COM TIMEIT E MEMORY PROFILING COM TRACEMALLOC
# ==========================================================
def demonstrar_timeit_e_tracemalloc() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: timeit e tracemalloc ---")

    # 1. Benchmark de Precisão com timeit
    tempo_comp = timeit.timeit("sum([x * 2 for x in range(100)])", number=10_000)
    tempo_gen = timeit.timeit("sum(x * 2 for x in range(100))", number=10_000)

    print(f"Tempo List Comprehension (10k ops) : {tempo_comp * 1000:.2f} ms")
    print(f"Tempo Generator Expression (10k ops): {tempo_gen * 1000:.2f} ms")

    # 2. Rastreamento de Memória com tracemalloc
    tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot()
    # Aloca uma grande estrutura na memória
    dados_temporarios = [dict(id=i, valor=str(i)) for i in range(50_000)]
    snapshot2 = tracemalloc.take_snapshot()

    top_stats = snapshot2.compare_to(snapshot1, "lineno")
    print("\nTop 2 Alocações de Memória RAM registradas pelo tracemalloc:")
    for stat in top_stats[:2]:
        print(f"  {stat}")

    tracemalloc.stop()


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Profiling de Middleware ---")
    print("  Em produção, utilize APMs (Application Performance Monitoring) como Datadog, New Relic ou Py-Spy (Sampling Profiler)")
    print("  para inspecionar chamadas de API sem causar overhead em ambiente real!")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Overhead de Profilers:
- `cProfile`: Profiler determinístico com overhead de CPU baixo (~10-30% de redução de velocidade durante o teste).
- `tracemalloc`: Registra todas as alocações Python com overhead moderado de memória RAM.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre um Deterministic Profiler (como `cProfile`) e um Sampling Profiler (como `py-spy`)?"
A: "1. Deterministic Profiler (`cProfile`): Intercepta TODAS as entradas e saídas de funções no evento do interpretador. Garante precisão exata do número de chamadas (`ncalls`), mas introduz um pequeno overhead e não é recomendado para rodar 24/7 em produção.
    2. Sampling Profiler (`py-spy`): Coleta amostras periodicamente (ex: a cada 1ms) inspecionando o estado da pilha de chamadas da thread do lado de fora do processo do SO. Possui overhead praticamente ZERO e pode ser anexado a processos de produção em tempo real sem reiniciar o servidor."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Utilize `timeit.timeit()` para comparar o tempo de verificação de pertencimento `x in lista` vs `x in set` para 100.000 elementos.
# Exercício 2 (Intermediário): Escreva um decorador `@profile_tempo` que meça e imprima o tempo de execução de qualquer função usando `time.perf_counter()`.
# Exercício 3 (Desafio / Entrevista): Utilize `tracemalloc` para identificar exatamente qual linha de um script alocou a maior quantidade de dicionários na memória RAM.


def main() -> None:
    print("==========================================================")
    print("  AULA 84: PROFILING DE CÓDIGO, CPROFILE, TIMEIT E TRACEMALLOC")
    print("==========================================================")
    demonstrar_cprofile()
    demonstrar_timeit_e_tracemalloc()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 84 executado com sucesso.")


if __name__ == "__main__":
    main()
