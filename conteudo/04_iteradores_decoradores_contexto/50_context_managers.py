"""
50_context_managers.py - Gerenciadores de Contexto (Context Managers, __enter__ e __exit__)

Objetivos:
1. Dominar o Protocolo de Gerenciamento de Contexto do Python (`__enter__` e `__exit__`).
2. Entender como a instrução `with` garante o encerramento e a limpeza determinística de recursos.
3. Compreender a supressão controlada de exceções ao retornar `True` no método `__exit__`.
4. Desenvolver gerenciadores de contexto para transações bancárias, timers de performance e conexões de banco de dados.
5. Evitar a armadilha de engolir exceções indesejadas acidentalmente dentro do `__exit__`.
"""

import time
from typing import Any, Type


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Gerenciador de Contexto (Context Manager)?
Um Gerenciador de Contexto é um objeto em Python projetado para gerenciar a alocação e liberação
determinística de recursos (arquivos, conexões de banco, locks de threads, arquivos temporários).

A Instrução `with`:
A instrução `with objeto as recurso:` simplifica a estrutura tradicional `try...finally`.

Protocolo do Context Manager:
1. `__enter__(self)`:
   - Executado imediatamente antes do bloco interno do `with`.
   - O valor retornado pelo `__enter__` é atribuído à variável especificada após a palavra-chave `as`.
2. `__exit__(self, exc_type, exc_val, exc_tb)`:
   - Executado SEMPRE ao sair do bloco `with` (mesmo que tenha ocorrido uma exceção).
   - Recebe as informações da exceção (`exc_type`, `exc_val`, `exc_tb`). Se não ocorreu erro, os três argumentos serão `None`.
   - Se `__exit__` retornar `True`, a exceção é SUPRIMIDA (engolida) e não propaga. Se retornar `False` ou `None`, a exceção propaga normalmente.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: TIMER E LIMPEZA DE RECURSOS
# ==========================================================
class TimerContextManager:
    """Gerenciador de contexto para medição de tempo de execução de um bloco de código."""

    def __init__(self, descricao: str) -> None:
        self.descricao = descricao
        self.inicio: float = 0.0
        self.fim: float = 0.0

    def __enter__(self) -> "TimerContextManager":
        self.inicio = time.perf_counter()
        print(f"  [Timer] Iniciando bloco '{self.descricao}'...")
        return self  # Permite usar 'with TimerContextManager(...) as t:'

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> bool | None:
        self.fim = time.perf_counter()
        duracao_ms = (self.fim - self.inicio) * 1000
        print(f"  [Timer] Bloco '{self.descricao}' concluído em {duracao_ms:.4f} ms.")
        return False  # Não suprime nenhuma exceção que tenha ocorrido


def demonstrar_fundamentos_context_manager() -> None:
    print("\n--- 1. FUNDAMENTOS: TimerContextManager com 'with' ---")

    with TimerContextManager("Cálculo de Soma") as timer:
        total = sum(range(1, 500_000))
        print(f"  Total calculado no bloco: {total}")

    print(f"Tempo gravado no objeto após o bloco: {(timer.fim - timer.inicio)*1000:.4f} ms")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SUPRESSÃO DE EXCEÇÕES EM __EXIT__
# ==========================================================
class IgnorarExcecoesEspecificas:
    """Context Manager que suprime exceções do tipo especificado."""

    def __init__(self, tipo_excecao: Type[BaseException]) -> None:
        self.tipo_excecao = tipo_excecao

    def __enter__(self) -> "IgnorarExcecoesEspecificas":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> bool:
        if exc_type is not None and issubclass(exc_type, self.tipo_excecao):
            print(f"  [Suppress] Exceção '{exc_type.__name__}' capturada e suprimida com sucesso!")
            return True  # Retornar True SUPRIME a exceção!
        return False  # Propaga outras exceções


def demonstrar_supressao_excecao() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Supressão de Exceções em __exit__ ---")

    with IgnorarExcecoesEspecificas(ZeroDivisionError):
        _ = 10 / 0  # Divisão por zero suprimida!

    print("Execução continuou normalmente após o bloco with com exceção suprimida.")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class DatabaseTransactionContext:
    """Gerenciador de contexto simulando controle transacional de Banco de Dados."""

    def __init__(self, banco_nome: str) -> None:
        self.banco_nome = banco_nome
        self.em_transacao = False

    def __enter__(self) -> "DatabaseTransactionContext":
        self.em_transacao = True
        print(f"  [DB {self.banco_nome}] Conexao aberta e Transação iniciada.")
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> bool | None:
        if exc_type is not None:
            print(f"  [DB {self.banco_nome}] Erro detectado ({exc_val}). Executando ROLLBACK!")
            self.em_transacao = False
            return False  # Propaga o erro para o chamador tratar

        print(f"  [DB {self.banco_nome}] Bloco concluído sem erros. Executando COMMIT!")
        self.em_transacao = False
        return None


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Gerenciador Transacional DB ---")

    # Sucesso
    with DatabaseTransactionContext("Postgres_Prod") as db:
        print("    Persistindo usuario no banco...")

    # Falha com Rollback
    print()
    try:
        with DatabaseTransactionContext("Postgres_Prod") as db:
            print("    Persistindo pedido no banco...")
            raise ValueError("Falha de validação de dados no campo 'email'")
    except ValueError as e:
        print(f"  [Controller] Capturada exceção de rollback: {e}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: INSTRUÇÃO SETUPWITH
# ==========================================================
"""
Como o CPython executa a instrução `with`:
1. No bytecode do CPython, a palavra-chave `with` emite as instruções `SETUP_WITH` ou `BEFORE_WITH`.
2. O CPython chama `__enter__()` no objeto.
3. Garante uma entrada na Exception Table para capturar qualquer sinal de erro ou instrução de `return` dentro do bloco.
4. Ao sair do bloco (por término natural, return ou raise), o CPython invoca `__exit__(exc_type, exc_val, exc_tb)`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Execução de `__enter__` e `__exit__`: Dependem da implementação interna -> Tempo O(1), Espaço O(1).
- Garantia de Limpeza: Garantida pelo CPython com overhead nulo no caminho feliz.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Gerenciamento manual com try...finally solto
    print("[X] Nao-Pythonic (try...finally manual):")
    print("  recurso = abrir()\n  try: ... \n  finally: recurso.fechar()  # Verborrágico e sujeito a esquecimento!")

    # [OK] PYTHONIC: Utilizar Gerenciadores de Contexto com with
    print("\n[OK] Pythonic:")
    print("  with GerenciadorRecurso() as r:\n      ...  # Limpo, elegante e seguro!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Retorne `False` ou `None` no método `__exit__` por padrão. Retorne `True` APENAS se você realmente pretende suprimir a exceção capturada.
2. O método `__enter__` deve retornar a si mesmo ou o recurso a ser utilizado no bloco `as`.
3. Garanta que todas as conexões, sockets ou arquivos abertos sejam liberados incondicionalmente no `__exit__`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Retornar True incondicionalmente em __exit__ e engolir todos os erros da aplicação
    class ContextoPerigoso:
        def __enter__(self) -> "ContextoPerigoso": return self
        def __exit__(self, *args: Any) -> bool:
            return True  # [!] PERIGO: Engole SyntaxError, NameError, TypeError!

    with ContextoPerigoso():
        _ = 10 / 0  # Silenciado sem aviso!

    print("[!] Armadilha 1 (Engoliu o erro sem dar print de traceback): O código continuou sem você saber do erro!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que acontece se uma exceção for disparada dentro de um bloco `with` e qual o papel do retorno do método `__exit__`?"
A: "1. Se ocorrer uma exceção dentro do bloco `with`, o CPython interrompe a execução do bloco e chama `__exit__(exc_type, exc_val, exc_tb)` passando as informações do erro.
    2. Se o método `__exit__` retornar `True`, o CPython entende que o erro foi tratado e SUPRIME a exceção, continuando o programa após o bloco `with`.
    3. Se retornar `False` ou `None`, a exceção continua seu fluxo normal de propagação (Stack Unwinding) podendo ser capturada por um `except` externo."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `ArquivoTemporarioContext` que crie um arquivo no `__enter__` e o delete incondicionalmente no `__exit__`.
# Exercício 2: Escreva um gerenciador de contexto `AlterarDiretorioContext(novo_caminho: str)` que mude o diretório de trabalho com `os.chdir` no `__enter__` e restaure o diretório original no `__exit__`.
# Exercício 3: Crie um gerenciador de contexto que conte a quantidade de exceções do tipo `KeyError` ocorridas dentro de um bloco de código.


def main() -> None:
    print("==========================================================")
    print("  AULA 50: GERENCIADORES DE CONTEXTO E INSTRUÇÃO WITH")
    print("==========================================================")
    demonstrar_fundamentos_context_manager()
    demonstrar_supressao_excecao()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 50 executado com sucesso.")


if __name__ == "__main__":
    main()
