"""
46_iteradores.py - Protocolo de Iteração, Iteradores Customizados e StopIteration

Objetivos:
1. Dominar o Protocolo de Iteração do Python (`__iter__` e `__next__`).
2. Entender a diferença entre um Objeto Iterável (Iterable) e um Objeto Iterador (Iterator).
3. Compreender a exceção nativa `StopIteration` e seu papel na interrupção de loops `for`.
4. Criar iteradores customizados mantendo o estado interno de iteração em memória O(1).
5. Prevenir a armadilha do esgotamento (exhaustion) de iteradores em pipelines de dados.
"""

from typing import Any, Iterator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o Protocolo de Iteração?
Em Python, a iteração (como o loop `for x in colecao:`) não depende do conhecimento do tamanho da coleção,
mas sim da implementação do Protocolo de Iteração.

Diferença entre Iterável e Iterador:
1. Iterável (Iterable):
   - Qualquer objeto que implemente o método `__iter__()` (ou `__getitem__`).
   - Retorna um novo objeto Iterador quando passado para `iter(obj)`.
   - Exemplos: `list`, `dict`, `tuple`, `str`, `set`.

2. Iterador (Iterator):
   - Um objeto que representa um fluxo de dados (stream).
   - Implementa o método `__next__()` que retorna o próximo elemento, um de cada vez.
   - Quando não restarem mais elementos, o `__next__()` DEVE lançar a exceção `StopIteration`.
   - Implementa o método `__iter__()` retornando a SI MESMO (`return self`).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ITERADOR CUSTOMIZADO DE CONTADEM
# ==========================================================
class ContadorIterador:
    """Iterador customizado que conta de inicio ate fim."""

    def __init__(self, inicio: int, fim: int) -> None:
        self.atual = inicio
        self.fim = fim

    def __iter__(self) -> "ContadorIterador":
        # Todo Iterador DEVE retornar a si mesmo no __iter__()
        return self

    def __next__(self) -> int:
        if self.atual > self.fim:
            # Sinaliza o fim da iteração para o loop for
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor


def demonstrar_fundamentos_iterador() -> None:
    print("\n--- 1. FUNDAMENTOS: ContadorIterador e StopIteration ---")

    contador = ContadorIterador(1, 3)

    # Execução manual com next()
    print(f"Manual next(contador): {next(contador)}")
    print(f"Manual next(contador): {next(contador)}")
    print(f"Manual next(contador): {next(contador)}")

    try:
        next(contador)  # Lança StopIteration!
    except StopIteration:
        print("[!] StopIteration capturada com sucesso ao atingir o fim.")

    # Uso idiomático no loop for
    print("\nIterando via loop for:")
    for num in ContadorIterador(10, 13):
        print(f"  Item: {num}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ITERADOR DE PAGINAÇÃO API
# ==========================================================
class CursorPaginadoAPI:
    """Iterador que navega por páginas de registros de uma API simulada."""

    def __init__(self, total_paginas: int) -> None:
        self.pagina_atual = 1
        self.total_paginas = total_paginas

    def __iter__(self) -> "CursorPaginadoAPI":
        return self

    def __next__(self) -> dict[str, Any]:
        if self.pagina_atual > self.total_paginas:
            raise StopIteration

        dados_pagina = {
            "pagina": self.pagina_atual,
            "itens": [f"Item_{self.pagina_atual}_A", f"Item_{self.pagina_atual}_B"],
        }
        self.pagina_atual += 1
        return dados_pagina


def demonstrar_cursor_paginado() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Cursor de Paginação API ---")
    cursor = CursorPaginadoAPI(total_paginas=3)

    for pagina in cursor:
        print(f"  Página recebida ({pagina['pagina']}): {pagina['itens']}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class BatchStreamIterator:
    """Iterador backend para processar registros em lotes (Stream Batching)."""

    def __init__(self, colecao: list[Any], tamanho_lote: int) -> None:
        self.colecao = colecao
        self.tamanho_lote = tamanho_lote
        self.indice = 0

    def __iter__(self) -> "BatchStreamIterator":
        return self

    def __next__(self) -> list[Any]:
        if self.indice >= len(self.colecao):
            raise StopIteration

        lote = self.colecao[self.indice : self.indice + self.tamanho_lote]
        self.indice += self.tamanho_lote
        return lote


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Processador em Lotes ---")
    dados_banco = [f"Reg_{i}" for i in range(1, 10)]
    stream = BatchStreamIterator(dados_banco, tamanho_lote=3)

    for num_lote, lote in enumerate(stream, start=1):
        print(f"  [Batch {num_lote}] Processado: {lote}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: O LOOP FOR EM CPYTHON
# ==========================================================
"""
Como o loop `for x in obj:` funciona sob o capô no CPython:
1. O CPython obtém o iterador executando `iterador = iter(obj)` (que chama o slot C `tp_iter`).
2. Entra em um loop `WHILE` interno em C chamando `item = next(iterador)` (que chama o slot C `tp_iternext`).
3. Ao capturar `StopIteration`, o CPython trata a exceção silenciosamente em C e encerra o loop `for` graciosamente.
"""


def demonstrar_internamente_loop_for_manual() -> None:
    print("\n--- 4. INTERNO: Desmistificando o loop FOR com WHILE e iter() ---")
    frutas = ["Maçã", "Banana", "Laranja"]

    # Desconstrução exata do que o CPython faz internamente no loop for:
    iterador_manual = iter(frutas)
    while True:
        try:
            item = next(iterador_manual)
            print(f"  [While Manual] Item: {item}")
        except StopIteration:
            print("  [While Manual] StopIteration capturada. Loop encerrado.")
            break


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Obtenção do Iterador (`iter(obj)`): Tempo O(1), Espaço O(1).
- Avanço de Elemento (`next(it)`): Tempo O(1), Espaço O(1) de memória (processamento lazy streaming).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    lista = [10, 20, 30]

    # [X] NÃO-PYTHONIC: Acesso manual por índice com range(len(lista))
    print("[X] Nao-Pythonic (Iteração por índice):")
    for i in range(len(lista)):
        print(f"  Index {i}: {lista[i]}")

    # [OK] PYTHONIC: Iterar diretamente sobre o iterável
    print("\n[OK] Pythonic (Iteração direta no iterável):")
    for val in lista:
        print(f"  Valor: {val}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Lembre-se: Iteradores são de USO ÚNICO (Esgotáveis). Uma vez percorridos até o fim, tentar iterar novamente resultará em `StopIteration` imediata.
2. Todo Iterador customizado DEVE implementar o método `__iter__` retornando a si mesmo (`return self`).
3. Utilize expressões geradoras ou funções com `yield` (Geradores) sempre que quiser criar um iterador sem a necessidade de escrever uma classe completa com `__iter__` e `__next__`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar re-iterar sobre um iterador já esgotado
    it = iter([1, 2, 3])
    _ = list(it)  # Consome o iterador totalmente

    # Segunda tentativa de consumo retorna lista vazia!
    segunda_tentativa = list(it)
    print(f"[!] Armadilha 1 (Iterador Esgotado): Segunda tentativa retornou {segunda_tentativa}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença técnica entre um `Iterable` e um `Iterator` em Python?"
A: "1. `Iterable` é qualquer objeto que possui o método `__iter__()` e produz um novo `Iterator` quando passado para `iter(obj)`. Podem ser re-iterados múltiplas vezes (ex: listas, tuplas, dicts).
    2. `Iterator` é o objeto de fluxo de dados que mantém o estado da iteração e implementa o método `__next__()` para avançar elemento por elemento. É esgotável (uma vez percorrido, não pode ser reiniciado sem instanciar um novo)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um iterador customizado `RegressivaIterator(inicio: int)` que conte regressivamente até 0 e dispare `StopIteration`.
# Exercício 2: Escreva um iterador `FibonacciIterator(limite_quantidade: int)` que gere os N primeiros números da sequência de Fibonacci.
# Exercício 3: Escreva uma função que receba um iterador e comprove se ele está esgotado ou se ainda possui elementos.


def main() -> None:
    print("==========================================================")
    print("  AULA 46: PROTOCOLO DE ITERAÇÃO E ITERADORES CUSTOMIZADOS")
    print("==========================================================")
    demonstrar_fundamentos_iterador()
    demonstrar_cursor_paginado()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_loop_for_manual()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 46 executado com sucesso.")


if __name__ == "__main__":
    main()
