"""
57_concurrent_futures.py - Abstração de Alto Nível: ThreadPoolExecutor, ProcessPoolExecutor e Futures

Objetivos:
1. Dominar o módulo `concurrent.futures` e suas abstrações de alto nível para concorrência e paralelismo.
2. Utilizar `ThreadPoolExecutor` para operações I/O-Bound e `ProcessPoolExecutor` para tarefas CPU-Bound com a mesma API unificada.
3. Compreender a anatomia dos objetos `Future` (estados: PENDING, RUNNING, CANCELLED, FINISHED).
4. Processar resultados à medida que são concluídos utilizando a função `as_completed()`.
5. Garantir o encerramento determinístico de pool de trabalhadores com o gerenciador de contexto `with Executor(...)`.
"""

from concurrent.futures import (
    Future,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)
import time
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo concurrent.futures?
Introduzido na PEP 3148 (Python 3.2), o `concurrent.futures` fornece uma interface de altíssimo nível
para a execução assíncrona e paralela de tarefas por meio de pools de trabalhadores.

Abstrações Principais:
1. `Executor`: Classe base abstrata que gerencia o ciclo de vida dos workers.
   - `ThreadPoolExecutor`: Gerencia um pool de Threads OS (Ideal para I/O-Bound).
   - `ProcessPoolExecutor`: Gerencia um pool de Processos OS (Ideal para CPU-Bound).
2. `Future`: Representa o resultado final de uma operação assíncrona que pode ainda não ter sido concluída.
   - Permite consultar o status (`.done()`), cancelar (`.cancel()`) e obter o resultado (`.result()`).
3. `as_completed(futures)`: Retorna um iterador que dá `yield` nos objetos Future à medida que eles são FINALIZADOS (independente da ordem de envio).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: THREADPOOLEXECUTOR E AS_COMPLETED
# ==========================================================
def buscar_dados_servico(servico_id: int) -> dict[str, Any]:
    """Simula requisição de I/O de rede."""
    tempo_simulado = 0.1 if servico_id == 2 else 0.05
    time.sleep(tempo_simulado)
    return {"id": servico_id, "status": 200, "dados": f"Payload_{servico_id}"}


def demonstrar_thread_pool_as_completed() -> None:
    print("\n--- 1. FUNDAMENTOS: ThreadPoolExecutor e as_completed() ---")

    servicos = [1, 2, 3, 4]

    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit envia tarefas individuais e retorna um objeto Future imediatamente
        futures_map = {executor.submit(buscar_dados_servico, s_id): s_id for s_id in servicos}

        # as_completed entrega as tarefas à medida que FINALIZAM (em ordem de conclusão!)
        print("Processando respostas à medida que concluem (as_completed):")
        for future in as_completed(futures_map):
            s_id = futures_map[future]
            try:
                resultado = future.result()  # Bloqueia apenas até o resultado deste future específico
                print(f"  [OK] Serviço {s_id} finalizado: {resultado}")
            except Exception as e:
                print(f"  [Erro] Serviço {s_id} falhou: {e}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: EXECUTOR.MAP
# ==========================================================
def quadrado_num(x: int) -> int:
    return x * x


def demonstrar_executor_map() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: executor.map() ---")

    numeros = [1, 2, 3, 4, 5]

    with ThreadPoolExecutor(max_workers=2) as executor:
        # executor.map mantém a ORDEM ORIGINAL dos elementos de entrada
        resultados = executor.map(quadrado_num, numeros)
        print(f"Resultados via executor.map() (em ordem original): {list(resultados)}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ParallelBatchProcessorBackend:
    """Processador de lotes backend que escolhe a estratégia de pool."""

    @staticmethod
    def processar_io_em_lote(itens: list[int]) -> list[dict[str, Any]]:
        with ThreadPoolExecutor(max_workers=4) as executor:
            resultados = list(executor.map(buscar_dados_servico, itens))
        return resultados


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Batch Processor ---")
    itens_processar = [10, 20, 30]
    res = ParallelBatchProcessorBackend.processar_io_em_lote(itens_processar)
    print(f"Lote finalizado com sucesso via ThreadPoolExecutor: {len(res)} itens")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ANATOMIA DO OBJETO FUTURE
# ==========================================================
"""
Estados Internos de um Objeto Future:
1. PENDING: A tarefa foi enviada ao pool, mas ainda não começou a executar.
2. RUNNING: A tarefa está em execução ativa por um trabalhador.
3. CANCELLED: A tarefa foi cancelada via `.cancel()` antes de começar a rodar.
4. FINISHED: A tarefa foi concluída com sucesso ou lançou uma exceção.

Tratamento Transparente de Exceções:
Se uma função executada dentro de um Future lançar uma exceção, ela NÃO quebra a thread trabalhadora!
A exceção é capturada e armazenada dentro do próprio objeto Future. Ela só é relançada quando você invoca `.result()`.
"""


def demonstrar_internamente_future_exception() -> None:
    print("\n--- 4. INTERNO: Captura de Exceções em Objetos Future ---")

    def funcao_com_erro() -> None:
        raise ValueError("Erro intencional no worker!")

    with ThreadPoolExecutor() as executor:
        future = executor.submit(funcao_com_erro)
        time.sleep(0.05)  # Aguarda execução

        print(f"Future concluído? {future.done()}")
        print(f"Exceção capturada internamente no Future: {future.exception()}")

        try:
            future.result()  # Invocação do result() relança o ValueError
        except ValueError as e:
            print(f"[!] Capturada exceção ao chamar future.result(): {e}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `executor.submit(func, *args)`: Tempo O(1), Espaço O(1).
- `as_completed(futures)`: Tempo O(N) para iterar nos resultados, Espaço O(N).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Criar e gerenciar pools manuais de threading.Thread com arrays de joins
    print("[X] Nao-Pythonic (Gerenciamento manual de threads soltas):")
    print("  threads = []; for x in dados: t = Thread(...); threads.append(t); t.start()  # Difícil de recuperar retornos!")

    # [OK] PYTHONIC: Utilizar concurrent.futures.ThreadPoolExecutor
    print("\n[OK] Pythonic:")
    print("  with ThreadPoolExecutor() as ex: res = list(ex.map(func, dados))  # Limpo e encapsulado!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre utilize o gerenciador de contexto `with Executor(...) as executor:` para garantir que a liberação dos workers ocorra no final.
2. Escolha `ThreadPoolExecutor` para tarefas I/O-Bound (redes, APIs, arquivos).
3. Escolha `ProcessPoolExecutor` para tarefas CPU-Bound (cálculos matemáticos, processamento de imagem).
4. Utilize `as_completed()` quando quiser processar resultados imediatamente assim que cada worker finalizar.
5. Utilize `executor.map()` quando precisar preservar a ordem estrita dos elementos de entrada.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Ignorar o retorno dos futures criados com submit()
    # Se a função worker lançar uma exceção e você não chamar `.result()` ou `.exception()`, o erro será silenciado!
    print("[!] Armadilha 1: Se você não chamar future.result(), exceções lançadas dentro do worker serão engolidas silenciosamente!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre a função `as_completed()` e o método `executor.map()` no módulo `concurrent.futures`?"
A: "1. `executor.map()`: Retorna os resultados estritamente na MESMA ORDEM em que os elementos foram passados de entrada.
       Se a primeira tarefa for a mais lenta, ela bloqueará a iteração mesmo que as tarefas seguintes já tenham finalizado.
    2. `as_completed()`: Retorna os objetos `Future` à medida que são CONCLUÍDOS no tempo (Out-of-Order Execution).
       Permite processar respostas rápidas imediatamente sem ter que aguardar as tarefas lentas."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função que faça downloads simulados de 5 URLs utilizando `ThreadPoolExecutor` e `as_completed()`.
# Exercício 2: Escreva um programa usando `ProcessPoolExecutor` para calcular a soma de quadrados de 4 grandes sequências numéricas em paralelo.
# Exercício 3: Crie um executor que lance exceções em 2 de 5 tarefas e trate os erros individualmente ao iterar com `as_completed()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 57: CONCURRENT.FUTURES, EXECUTORS E FUTURES")
    print("==========================================================")
    demonstrar_thread_pool_as_completed()
    demonstrar_executor_map()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_future_exception()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 57 executado com sucesso.")


if __name__ == "__main__":
    main()
