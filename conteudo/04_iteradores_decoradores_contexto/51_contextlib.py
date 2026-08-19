"""
51_contextlib.py - Utilitários do Módulo contextlib, @contextmanager e ExitStack

Objetivos:
1. Dominar a criação de Gerenciadores de Contexto baseados em funções com o decorador `@contextlib.contextmanager`.
2. Utilizar `contextlib.suppress` para ignorar exceções conhecidas de forma idiomática e sem blocos `try/pass`.
3. Redirecionar saídas do terminal de forma temporária com `contextlib.redirect_stdout`.
4. Gerenciar múltiplos recursos dinâmicos ou imprevisíveis utilizando `contextlib.ExitStack`.
5. Garantir que a instrução `try...finally` seja usada corretamente em funções decoradas com `@contextmanager`.
"""

import io
import sys
from contextlib import ExitStack, contextmanager, redirect_stdout, suppress
from typing import Generator, Iterator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo contextlib?
O `contextlib` é um módulo nativo da biblioteca padrão que fornece utilitários de alto nível para trabalhar
e criar Gerenciadores de Contexto de forma extremamente sucinta.

Principais Utilitários:
1. `@contextmanager`: Transforma uma função geradora contendo uma única instrução `yield` em um Context Manager completo
   (eliminando a necessidade de escrever uma classe com `__enter__` e `__exit__`).
2. `suppress(*exceptions)`: Suprime exceções especificadas de forma limpa.
3. `redirect_stdout(new_target)`: Redireciona a saída padrão `sys.stdout` temporariamente.
4. `ExitStack`: Permite empilhar e gerenciar dinamicamente múltiplos gerenciadores de contexto (útil quando o número de arquivos a abrir é desconhecido em tempo de compilação).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: @CONTEXTMANAGER E YIELD
# ==========================================================
@contextmanager
def conexao_simulada(db_name: str) -> Generator[str, None, None]:
    """Gerenciador de contexto baseado em função com @contextmanager."""
    print(f"  [Setup] Abrindo conexão com o banco '{db_name}'...")
    conexao_handle = f"HANDLE_{db_name.upper()}"
    try:
        yield conexao_handle  # O valor do yield é atribuído ao 'as' do bloco with
    finally:
        # Tudo após o yield dentro do bloco finally é executado ao sair do with!
        print(f"  [Cleanup] Fechando conexão com o banco '{db_name}'.")


def demonstrar_fundamentos_contextlib() -> None:
    print("\n--- 1. FUNDAMENTOS: @contextmanager ---")

    with conexao_simulada("Postgres_Dev") as conn:
        print(f"  Executando query utilizando a conexão: {conn}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SUPPRESS, REDIRECT_STDOUT E EXITSTACK
# ==========================================================
def demonstrar_suppress_e_redirect() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: suppress e redirect_stdout ---")

    # 1. contextlib.suppress (Substitui try: ... except FileNotFoundError: pass)
    dicionario = {"a": 1}
    with suppress(KeyError):
        del dicionario["chave_inexistente"]  # Suprimido silenciosamente e limpo!
    print("Dicionario apos suppress(KeyError): OK")

    # 2. contextlib.redirect_stdout (Captura prints do terminal em um buffer de memória)
    buffer_memoria = io.StringIO()
    with redirect_stdout(buffer_memoria):
        print("Esta mensagem NAO vai para o terminal! Foi capturada pelo buffer.")

    conteudo_capturado = buffer_memoria.getvalue().strip()
    print(f"Mensagem capturada pelo redirect_stdout: {conteudo_capturado!r}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: EXITSTACK
# ==========================================================
def demonstrar_exitstack_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Gerenciamento Dinâmico com ExitStack ---")

    nomes_bancos = ["DB_Usuarios", "DB_Pedidos", "DB_Estoque"]

    # ExitStack permite abrir N conexões dinamicamente e fechar TODAS na ordem inversa ao sair!
    with ExitStack() as stack:
        handles = [
            stack.enter_context(conexao_simulada(nome))
            for nome in nomes_bancos
        ]
        print(f"  Todas as {len(handles)} conexoes abertas com sucesso: {handles}")

    print("Todas as conexoes do ExitStack foram encerradas na ordem reversa!")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: _GENERATORCONTEXTMANAGER
# ==========================================================
"""
Como o `@contextmanager` funciona por baixo dos panos:
1. O decorador envolve a função geradora na classe interna `_GeneratorContextManager`.
2. Ao entrar no `with`, o `__enter__` executa `next(gerador)`, avançando a função até o `yield`.
3. Ao sair do `with`, o `__exit__` retoma o gerador. Se ocorreu uma exceção no bloco `with`,
   o `__exit__` a injeta de volta na função geradora via `gerador.throw(exc_type, exc_val, exc_tb)`.
4. Por isso, a instrução `yield` em um `@contextmanager` DEVE estar dentro de um bloco `try...finally`!
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Invocação de `@contextmanager`: Tempo O(1), Espaço O(1).
- `ExitStack`: Tempo O(N) para abrir e fechar N gerenciadores de contexto, Espaço O(N) para a pilha de cleanup.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Bloco try...except pass para engolir exceção esperada
    print("[X] Nao-Pythonic (try...except pass):")
    print("  try:\n      os.remove('arq.txt')\n  except FileNotFoundError:\n      pass")

    # [OK] PYTHONIC: Utilitário contextlib.suppress
    print("\n[OK] Pythonic (contextlib.suppress):")
    print("  with suppress(FileNotFoundError):\n      os.remove('arq.txt')  # Limpo e autodocumentável!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Em funções com `@contextmanager`, envolva a instrução `yield` OBRIGATORIAMENTE dentro de um bloco `try...finally`.
2. Utilize `contextlib.suppress` para ignorar exceções pontuais e inofensivas (como remoção de arquivos inexistentes).
3. Utilize `ExitStack` quando precisar gerenciar um número variável ou dinâmico de conexões ou arquivos simultâneos.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer o try...finally em um @contextmanager
    @contextmanager
    def contexto_sem_finally() -> Generator[str, None, None]:
        print("  [Setup] Abrindo recurso...")
        yield "RECURSO"
        # [!] ERRO: Se o bloco 'with' lançar exceção, esta linha NUNCA será executada!
        print("  [Cleanup Sem Finally] Fechando recurso...")

    try:
        with contexto_sem_finally():
            raise ValueError("Erro no bloco with!")
    except ValueError:
        print("[!] Armadilha 1 (Sem try/finally, o código de cleanup abaixo do yield foi pulado por causa do erro!)")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o decorador `@contextmanager` do módulo `contextlib` converte uma função com `yield` em um Gerenciador de Contexto?"
A: "O decorador envolve a função geradora em uma classe `_GeneratorContextManager` que implementa `__enter__` e `__exit__`:
    - No `__enter__`, ele executa `next(gerador)` para rodar o código até o `yield` e retornar o valor produzido.
    - No `__exit__`, se ocorreu uma exceção dentro do bloco `with`, ele a retransmite para dentro do gerador chamando `gerador.throw(exc_type, exc_val, exc_tb)`.
      Se não ocorreu erro, ele chama `next(gerador)` novamente para executar o código de cleanup localizado após o `yield`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um gerenciador de contexto com `@contextmanager` que abra uma conexão fictícia com Redis e garanta o fechamento no `finally`.
# Exercício 2: Escreva um código que utilize `contextlib.suppress(ZeroDivisionError, KeyError)` para ignorar múltiplos tipos de erros.
# Exercício 3: Utilizando `ExitStack`, abra 3 arquivos de texto temporários simultaneamente e escreva uma linha em cada um.


def main() -> None:
    print("==========================================================")
    print("  AULA 51: UTILITÁRIOS DO MÓDULO CONTEXTLIB E EXITSTACK")
    print("==========================================================")
    demonstrar_fundamentos_contextlib()
    demonstrar_suppress_e_redirect()
    demonstrar_exitstack_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 51 executado com sucesso.")


if __name__ == "__main__":
    main()
