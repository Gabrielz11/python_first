"""
23_functools.py - Programação Funcional e Otimizações com o Módulo functools

Objetivos:
1. Dominar os decoradores de caching nativos: `@lru_cache` e `@cache` (Python 3.9+).
2. Compreender a aplicação de `functools.partial` para pré-configuração de funções.
3. Utilizar `@wraps` para preservar os metadados de funções decoradas (`__name__`, `__doc__`).
4. Aplicar o padrão Polymorphic Function com `@singledispatch` e agregação com `reduce`.
5. Implementar barreira de caching e reutilização de utilitários em sistemas de backend.
"""

import time
from functools import cache, lru_cache, partial, reduce, singledispatch, wraps
from typing import Any, Callable


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo functools?
O `functools` é um módulo nativo do Python voltado para programação funcional e manipulação de funções
de alta ordem (funções que operam sobre outras funções).

Principais Utilitários do functools:
1. @lru_cache / @cache: Memoization automatizada. Armazena os resultados de invocações passadas
   de funções com base nos argumentos de entrada (que devem ser hashable).
2. partial: Permite "congelar" uma parte dos argumentos de uma função, criando uma nova função com menor aridade.
3. @wraps: Decorador de decoradores. Mantém os metadados da função original intactos.
4. @singledispatch: Permite criar sobrecarga de funções (Overloading) baseada no tipo do primeiro argumento.
5. reduce: Aplica uma função de 2 argumentos cumulativamente aos itens de uma sequência.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: LRU_CACHE E PARTIAL
# ==========================================================
# Caching com LRU (Least Recently Used) limitando o tamanho a 128 entradas
@lru_cache(maxsize=128)
def calcular_fibonacci_lru(n: int) -> int:
    """Calcula a sequência de Fibonacci de forma recursiva utilizando Caching."""
    if n < 2:
        return n
    return calcular_fibonacci_lru(n - 1) + calcular_fibonacci_lru(n - 2)


def demonstrar_caching_e_partial() -> None:
    print("\n--- 1. FUNDAMENTOS: @lru_cache e functools.partial ---")

    # Medindo tempo com caching em Fibonacci
    inicio = time.perf_counter()
    resultado = calcular_fibonacci_lru(35)
    fim = time.perf_counter()
    print(f"Fibonacci(35) com @lru_cache: {resultado} em {(fim - inicio) * 1000:.4f} ms")

    # Exibindo estatísticas de Cache (Hits, Misses, Maxsize)
    print(f"Estatisticas do Cache: {calcular_fibonacci_lru.cache_info()}")

    # Uso de partial para criar funções especializadas
    def multiplicar(a: int, b: int) -> int:
        return a * b

    dobrar = partial(multiplicar, 2)
    triplicar = partial(multiplicar, 3)

    print(f"functools.partial -> dobrar(10): {dobrar(10)}")
    print(f"functools.partial -> triplicar(10): {triplicar(10)}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: @WRAPS E @SINGLEDISPATCH
# ==========================================================
def meu_decorador_log(func: Callable[..., Any]) -> Callable[..., Any]:
    # Sem @wraps, o nome da função seria substituído por 'wrapper'
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"  [Log Decorador] Executando {func.__name__}...")
        return func(*args, **kwargs)

    return wrapper


@meu_decorador_log
def calcular_imposto_servico(valor: float) -> float:
    """Calcula a aliquota basica de imposto sobre servico."""
    return valor * 0.15


# Polymorphic dispatch baseado no tipo do argumento
@singledispatch
def formatar_para_json(val: Any) -> str:
    return f'"{str(val)}"'


@formatar_para_json.register(int)
@formatar_para_json.register(float)
def _(val: float | int) -> str:
    return str(val)


@formatar_para_json.register(list)
def _(val: list[Any]) -> str:
    return "[" + ", ".join(formatar_para_json(x) for x in val) + "]"


def demonstrar_wraps_e_singledispatch() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: @wraps e @singledispatch ---")

    # Testando @wraps
    res = calcular_imposto_servico(100.0)
    print(f"Resultado: {res} | Nome Preservado: {calcular_imposto_servico.__name__}")
    print(f"Docstring Preservada: {calcular_imposto_servico.__doc__}")

    # Testando @singledispatch
    print(f"formatar_para_json('texto'): {formatar_para_json('texto')}")
    print(f"formatar_para_json(100): {formatar_para_json(100)}")
    print(f"formatar_para_json([1, 'a', 3.5]): {formatar_para_json([1, 'a', 3.5])}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ServicoTaxasCambio:
    """Simula consulta externa de cotações com Caching de respostas."""

    @staticmethod
    @cache  # @cache e equivalente a @lru_cache(maxsize=None)
    def obter_cotacao(moeda_origem: str, moeda_destino: str) -> float:
        # Simula IO pesado de rede / chamada HTTP
        time.sleep(0.05)
        cotacoes = {("USD", "BRL"): 5.20, ("EUR", "BRL"): 5.65}
        return cotacoes.get((moeda_origem, moeda_destino), 1.0)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Cache de Cotacoes HTTP ---")
    servico = ServicoTaxasCambio()

    t0 = time.perf_counter()
    c1 = servico.obter_cotacao("USD", "BRL")
    t1 = time.perf_counter()
    print(f"Primeira chamada (Sem Cache): USD->BRL = {c1} em {(t1 - t0)*1000:.2f} ms")

    t2 = time.perf_counter()
    c2 = servico.obter_cotacao("USD", "BRL")
    t3 = time.perf_counter()
    print(f"Segunda chamada (COM Cache Hit): USD->BRL = {c2} em {(t3 - t2)*1000:.4f} ms")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE
# ==========================================================
"""
Como o @lru_cache funciona por baixo dos panos:
1. O decorador cria um dicionário interno no CPython para mapear as chaves de argumentos
   (convertidos internamente em uma tupla `args` e `kwargs` ordenados).
2. Para que o argumento funcione no cache, ele DEVE SER HASHABLE (deve implementar `__hash__`).
3. Lista (`list`), Dicionário (`dict`) e Conjunto (`set`) NÃO podem ser passados para funções com @lru_cache,
   lançando `TypeError: unhashable type`.
"""


def demonstrar_internamente_hashable() -> None:
    print("\n--- 4. INTERNO: Exigencia de Objetos Hashable ---")

    @lru_cache
    def processar_tupla(dados: tuple[int, ...]) -> int:
        return sum(dados)

    print(f"Processando tupla hashable (OK): {processar_tupla((1, 2, 3))}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `@lru_cache` / `@cache`:
  - Cache Hit (Sucesso): Tempo O(1) [Busca no Dict CPython], Espaço O(1).
  - Cache Miss (Falha): Executa a função decorada e armazena no dict.
  - Espaço Total do Cache: O(maxsize) ou O(N) entradas.
- `functools.reduce(func, seq)`: Tempo O(N), Espaço O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # Multiplicar todos os elementos de uma lista
    numeros = [1, 2, 3, 4, 5]

    # [X] NÃO-PYTHONIC: Loop manual acumulador
    print("[X] Nao-Pythonic (Loop acumulador manual):")
    produto_manual = 1
    for n in numeros:
        produto_manual *= n
    print(f"  Resultado: {produto_manual}")

    # [OK] PYTHONIC: functools.reduce ou math.prod
    print("\n[OK] Pythonic (functools.reduce):")
    produto_reduce = reduce(lambda acc, val: acc * val, numeros)
    print(f"  Resultado (reduce): {produto_reduce}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre utilize `@wraps(func)` ao criar decoradores customizados em Python.
2. Evite usar `@cache` sem `maxsize` em funções que recebem um número infinito de parâmetros únicos para evitar vazamento de memória (Memory Leak).
3. Nunca passe argumentos mutáveis (como listas) para funções decoradas com `@lru_cache`. Passe tuplas.
4. Para limpar o cache de uma função em testes ou em runtime, invoque `sua_funcao.cache_clear()`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    @lru_cache
    def processar_lista(items: Any) -> int:
        return len(items)

    # Armadilha 1: TypeError ao passar listas mutáveis (unhashable)
    try:
        processar_lista([1, 2, 3])  # Lança TypeError
    except TypeError as e:
        print(f"[!] Armadilha 1 (TypeError unhashable type 'list'): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que acontece com os metadados de uma função quando ela é decorada sem o uso do `functools.wraps`?"
A: "Sem o `@wraps(func)`, os atributos da função decorada (como `__name__`, `__doc__`, `__annotations__` e `__module__`)
    são sobrescritos pelos metadados da função interna `wrapper` do decorador.
    Isso prejudica ferramentas de documentação (Sphinx), frameworks web (FastAPI/Flask) e depuração de stack traces."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `fatorial(n: int)` com `@lru_cache` e meça a diferença de tempo entre a primeira e a segunda chamada.
# Exercício 2: Utilize `functools.partial` para criar uma função `converter_para_centimetros` a partir de uma função genérica de conversão de unidades.
# Exercício 3: Implemente um decorador `@medir_tempo` que utilize `functools.wraps` e calcule o tempo de execução de qualquer função de backend.


def main() -> None:
    print("==========================================================")
    print("  AULA 23: PROGRAMAÇÃO FUNCIONAL COM FUNCTOOLS")
    print("==========================================================")
    demonstrar_caching_e_partial()
    demonstrar_wraps_e_singledispatch()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_hashable()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 23 executado com sucesso.")


if __name__ == "__main__":
    main()
