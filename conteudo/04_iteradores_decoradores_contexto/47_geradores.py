"""
47_geradores.py - Funções Geradoras, Palavra-chave yield, yield from e Memória O(1)

Objetivos:
1. Dominar o conceito de Geradores (Generators) e o funcionamento da palavra-chave `yield`.
2. Compreender a avaliação preguiçosa (Lazy Evaluation) e o consumo de memória O(1).
3. Utilizar Expressões Geradoras (Generator Expressions) em substituição a List Comprehensions para grandes volumes de dados.
4. Aplicar a delegação de geradores com `yield from`.
5. Desenvolver pipelines de processamento streaming de logs e grandes arquivos CSV no backend.
"""

import sys
from typing import Any, Generator, Iterator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Gerador (Generator) em Python?
Um gerador é uma função especial que produz uma sequência de valores sob demanda (Lazy Evaluation)
utilizando a palavra-chave `yield` em vez de `return`.

Como funciona a palavra-chave `yield`?
1. Quando uma função geradora é chamada, ela NÃO executa o seu corpo imediatamente. Ela retorna um objeto Gerador (`generator`).
2. A cada vez que `next(gerador)` é invocado (ou no loop `for`), a função executa até encontrar a instrução `yield`.
3. O Python "congela" a execução da função naquele ponto exacto, salvando todo o seu estado de variáveis locais e ponteiro de instrução.
4. Na próxima chamada de `next()`, a função "descongela" e retoma a execução exatamente na linha imediatamente após o `yield`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: GERADORES COM YIELD
# ==========================================================
def gerar_sequencia_numerica(limite: int) -> Generator[int, None, None]:
    """Função geradora simples."""
    print("  [Gerador] Inicio da execução...")
    for i in range(1, limite + 1):
        print(f"  [Gerador] Prestes a dar yield no valor: {i}")
        yield i
        print(f"  [Gerador] Retomando após yield do valor: {i}")


def demonstrar_fundamentos_gerador() -> None:
    print("\n--- 1. FUNDAMENTOS: Função Geradora e yield ---")

    gen = gerar_sequencia_numerica(2)

    print(f"Objeto retornado: {gen} (tipo {type(gen).__name__})")

    # Consumindo manualmente com next()
    val1 = next(gen)
    print(f"Valor recebido no chamador: {val1}\n")

    val2 = next(gen)
    print(f"Valor recebido no chamador: {val2}\n")

    try:
        next(gen)
    except StopIteration:
        print("[!] Gerador esgotado (StopIteration disparada).")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: YIELD FROM E EXPRESSÕES GERADORAS
# ==========================================================
def gerador_sub_tarefas() -> Generator[str, None, None]:
    yield "Tarefa 1A"
    yield "Tarefa 1B"


def gerador_principal() -> Generator[str, None, None]:
    yield "Inicio Principal"
    # yield from delega a iteração inteira para outro gerador/iterável
    yield from gerador_sub_tarefas()
    yield "Fim Principal"


def demonstrar_yield_from_e_expressions() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: yield from & Expressões Geradoras ---")

    # 1. Delegação com yield from
    print("Consumindo gerador principal com yield from:")
    for item in gerador_principal():
        print(f"  - {item}")

    # 2. Expressão Geradora (Generator Expression) vs List Comprehension
    # Sintaxe com parênteses () em vez de colchetes []
    gen_exp = (x**2 for x in range(5))
    print(f"\nExpressao Geradora criada: {gen_exp}")
    print(f"Valores consumidos: {list(gen_exp)}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def ler_linhas_log_streaming(linhas_mock: list[str]) -> Generator[dict[str, str], None, None]:
    """Simula leitura streaming de um grande arquivo de log sem alocar a lista inteira na RAM."""
    for linha in linhas_mock:
        if "ERROR" in linha or "WARNING" in linha:
            partes = linha.split("|")
            yield {"level": partes[0].strip(), "mensagem": partes[1].strip()}


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Processing Streaming Log Engine ---")

    logs_mock = [
        "INFO | Sistema inicializado",
        "ERROR | Conexao recusada no banco Postgres",
        "INFO | Requisicao recebida GET /status",
        "WARNING | Uso de CPU acima de 80%",
    ]

    pipeline = ler_linhas_log_streaming(logs_mock)

    print("Alertas extraidos em streaming:")
    for alerta in pipeline:
        print(f"  [Alerta] {alerta['level']}: {alerta['mensagem']}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: COMPARAÇÃO DE MEMÓRIA
# ==========================================================
"""
Como o Gerador funciona no CPython:
1. Objeto `PyGenObject`: Uma função contendo `yield` é compilada com a flag `CO_GENERATOR` no seu code object.
2. Frame da Função: Ao dar `yield`, o frame da função (`PyFrameObject`) NÃO é destruído nem desempilhado da memória Heap.
   Ele permanece congelado até a próxima chamada de `next()`.
3. Economia de Memória: Em vez de alocar 1 milhão de inteiros em uma lista (vários Megabytes),
   um gerador mantém apenas o ponteiro do estado atual (poucos Bytes).
"""


def demonstrar_internamente_comparativo_memoria() -> None:
    print("\n--- 4. INTERNO: Comparativo de Memória RAM (Lista vs Gerador) ---")

    elementos = 100000

    # List Comprehension (Aloca todos os inteiros na RAM)
    lista_ram = [x for x in range(elementos)]

    # Generator Expression (Aloca apenas a estrutura do gerador)
    gerador_ram = (x for x in range(elementos))

    print(f"Tamanho da Lista com {elementos} elementos: {sys.getsizeof(lista_ram)} Bytes")
    print(f"Tamanho da Expressão Geradora: {sys.getsizeof(gerador_ram)} Bytes (Constante O(1)!)")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Produção e consumo de cada item (`yield` / `next()`): Tempo O(1), Espaço O(1) constante!
- Iterar sobre N elementos via Gerador: Tempo O(N), Espaço O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Acumular lista intermediária gigante na memória para retornar
    print("[X] Nao-Pythonic (Criar e retornar lista gigante):")
    print("  def ler_dados(): res = []; for x in dados: res.append(x); return res  # OOM em arquivos grandes!")

    # [OK] PYTHONIC: Utilizar yield para streaming lazy
    print("\n[OK] Pythonic:")
    print("  def ler_dados(): for x in dados: yield x  # Memória O(1) impecável!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize Geradores para qualquer processamento de I/O, arquivos grandes, logs ou queries paginadas de banco de dados.
2. Utilize `yield from` para delegar a iteração entre geradores aninhados em vez de loops `for` manuais.
3. Não converta um gerador para `list(gerador)` a menos que você realmente precise indexar os dados ou re-iterar sobre eles.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar re-iterar sobre um gerador esgotado
    gen = (x for x in [1, 2, 3])
    _ = sum(gen)  # Consome o gerador

    # Tentar re-utilizar o gerador esgotado resulta em 0!
    soma_segunda = sum(gen)
    print(f"[!] Armadilha 1 (Gerador Esgotado): Segunda soma = {soma_segunda}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença de alocação de memória entre `[x for x in range(1_000_000)]` e `(x for x in range(1_000_000))`?"
A: "1. `[x for ...]` é uma List Comprehension. Ela calcula e armazena todos os 1.000.000 de inteiros simultaneamente na RAM, consumindo vários Megabytes (Espaço O(N)).
    2. `(x for ...)` é uma Expressão Geradora. Ela cria uma estrutura lazy que calcula cada número sob demanda, um a um, à medida que é solicitado, consumindo apenas cerca de 200 Bytes de memória RAM (Espaço O(1))."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função geradora `gerar_pares(limite: int)` que produza apenas números pares usando `yield`.
# Exercício 2: Escreva um pipeline com dois geradores encadeados: o primeiro gera números, o segundo multiplica cada número por 10.
# Exercício 3: Escreva um gerador que leia um arquivo de texto linha por linha e dê `yield` apenas nas linhas que contenham determinada palavra-chave.


def main() -> None:
    print("==========================================================")
    print("  AULA 47: FUNÇÕES GERADORAS, YIELD E MEMÓRIA O(1)")
    print("==========================================================")
    demonstrar_fundamentos_gerador()
    demonstrar_yield_from_e_expressions()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_comparativo_memoria()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 47 executado com sucesso.")


if __name__ == "__main__":
    main()
