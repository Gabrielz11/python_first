"""
30_excecoes.py - Tratamento de Exceções, Fluxo try/except/else/finally e Exception Chaining

Objetivos:
1. Dominar o tratamento de exceções em Python utilizando a estrutura `try/except/else/finally`.
2. Compreender a árvore de hierarquia nativa de exceções (`BaseException` vs `Exception`).
3. Aplicar Encadeamento de Exceções (Exception Chaining - `raise NewException from e`) para preservar o contexto original do erro.
4. Diferenciar a responsabilidade de cada bloco (`else` para o caminho feliz, `finally` para limpeza/cleanup determinístico).
5. Desenvolver padrões de resiliência e captura limpa de erros em serviços de backend.
"""

import sys
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma Exceção em Python?
Uma exceção é um objeto que representa um erro ocorrido durante a execução do código, interrompendo
o fluxo normal de instruções caso não seja capturada.

Estrutura Completa do Bloco de Tratamento de Erros:
- `try`: Contém o código arriscado que pode lançar exceções.
- `except ExceptionType`: Captura exceções do tipo especificado (ou suas subclasses).
- `else`: EXECUTADO APENAS se NENHUMA exceção ocorrer dentro do bloco `try` (caminho feliz).
- `finally`: EXECUTADO SEMPRE, independentemente de ter ocorrido exceção ou não (ideal para liberação de conexões/arquivos).

Hierarquia Base de Exceções:
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception (Subclasse base de TODAS as exceções de aplicação)
      ├── ArithmeticError (ZeroDivisionError, OverflowError)
      ├── LookupError (IndexError, KeyError)
      ├── ValueError
      └── TypeError
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: TRY / EXCEPT / ELSE / FINALLY
# ==========================================================
def demonstrar_fluxo_try_except_else_finally(numerador: float, denominador: float) -> None:
    print(f"\n--- 1. FUNDAMENTOS: Executando Divisão ({numerador} / {denominador}) ---")

    resultado = 0.0
    try:
        resultado = numerador / denominador
    except ZeroDivisionError as e:
        print(f"  [except] Erro de divisão por zero capturado: {e}")
    except TypeError as e:
        print(f"  [except] Tipos incompatíveis: {e}")
    else:
        # Executado APENAS se o try for concluído sem erros!
        print(f"  [else] Divisão executada com sucesso! Resultado = {resultado}")
    finally:
        # Executado SEMPRE (cleanup)
        print("  [finally] Bloco de limpeza finalizado (sempre roda).")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: EXCEPTION CHAINING (RAISE FROM)
# ==========================================================
class DatabaseConnectionError(Exception):
    """Exceção customizada de infraestrutura."""

    pass


def conectar_banco_dados(host: str) -> None:
    if host == "invalid_host":
        raise TimeoutError("Falha de rede ao conectar no IP 192.168.1.50")


def demonstrar_exception_chaining() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Exception Chaining (raise ... from e) ---")

    try:
        try:
            conectar_banco_dados("invalid_host")
        except TimeoutError as err_original:
            # Exception Chaining (PEP 3134): Envolva o erro de baixo nível em uma exceção de domínio
            raise DatabaseConnectionError("Impossível inicializar o repositório de usuários") from err_original
    except DatabaseConnectionError as e:
        print(f"[Capturado] Exceção de alto nível: {e}")
        print(f"[Causa Raiz] Exceção original (__cause__): {e.__cause__}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class RepositorioUsuarioMock:
    """Simula um repositório com gerenciamento de transações resiliente."""

    def __init__(self) -> None:
        self.em_transacao = False

    def iniciar_transacao(self) -> None:
        self.em_transacao = True
        print("  [DB] Transacao iniciada.")

    def rollback(self) -> None:
        self.em_transacao = False
        print("  [DB] Rollback executado (alteracoes desfeitas).")

    def commit(self) -> None:
        self.em_transacao = False
        print("  [DB] Commit executado com sucesso.")

    def salvar(self, dados: dict[str, Any]) -> None:
        if "email" not in dados:
            raise ValueError("Email e obrigatorio")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Gerenciamento Transacional ---")
    repo = RepositorioUsuarioMock()

    # Tentativa com erro
    repo.iniciar_transacao()
    try:
        repo.salvar({"nome": "Gabriel"})  # Sem email!
    except ValueError as e:
        print(f"  [Erro] Falha ao salvar: {e}")
        repo.rollback()
    else:
        repo.commit()
    finally:
        print(f"  [Status] Transacao ativa? {repo.em_transacao}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: STACK UNWINDING
# ==========================================================
"""
Como o CPython executa o Tratamento de Exceções:
1. Zero-Cost Exceptions (Python 3.11+): O CPython não adiciona instruções de overhead no bytecode dentro do bloco `try`.
   Em vez disso, ele mantém uma tabela de exceções estática (Exception Table) mapeando os endereços de memória do bytecode.
2. Stack Unwinding (Desenrolamento da Call Stack): Quando uma exceção é disparada (`raise`), o CPython
   percorre a pilha de chamadas voltando de função em função procurando por um bloco `except` compatível.
3. Se a pilha for desfeita até a raiz sem nenhum `except` capturá-la, o interpretador encerra a thread
   e imprime o Traceback no `stderr`.
"""


def demonstrar_internamente_traceback() -> None:
    print("\n--- 4. INTERNO: Inspeção da Call Stack com sys.exc_info() ---")
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        tipo, valor, tb = sys.exc_info()
        print(f"Tipo da excecao: {tipo.__name__ if tipo else None}")
        print(f"Mensagem: {valor}")
        print(f"Objeto Traceback em CPython: {tb}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Bloco `try` executado com sucesso (Python 3.11+): Tempo O(1), Espaço O(1) adicional (Zero-Cost).
- Lançamento e captura de exceção (`raise`): Tempo O(D), onde D é a profundidade da Call Stack (precisa desenrolar a pilha e capturar o traceback).
- Memória: A criação do objeto Traceback retém referências para todos os frames de variáveis locais da chamada.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Captura Genérica Nua (bare except:) que esconde até KeyboardInterrupt
    print("[X] Nao-Pythonic (bare except):")
    print("  try: ... except: print('Deu erro!')  # ANTIPADRÃO GRAVE! Mascara falhas de sistema.")

    # [OK] PYTHONIC: Captura de Exception específica
    print("\n[OK] Pythonic:")
    try:
        valor = int("invalido")
    except ValueError as e:
        print(f"  Capturado erro especifico de tipo/valor: {e}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. NUNCA utilize `except:` sem especificar a classe de exceção. Capture no mínimo `except Exception:`.
2. Mantenha os blocos `try` o mais enxutos possível para evitar capturar exceções não intencionais.
3. Utilize o bloco `else` para colocar instruções que dependem do sucesso do `try`, isolando-as da captura de erro.
4. Utilize `raise NovoErro from erro_original` ao retransmitir exceções para manter a rastreabilidade do log (causa raiz).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Retornar valor dentro do bloco `finally` sobrescreve retornos anteriores e engole exceções!
    def funcao_armadilha() -> str:
        try:
            raise ValueError("Erro importante no processamento!")
        finally:
            return "Sucesso Falso"  # [!] NUNCA use return dentro do finally! Engole a exceção ValueError!

    resultado_oculto = funcao_armadilha()
    print(f"[!] Armadilha (Return no finally engoliu exceção!): Retornou '{resultado_oculto}'")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre `BaseException` e `Exception` em Python e por que você deve herdar de `Exception` ao criar erros customizados?"
A: "`BaseException` é a classe raiz de TODA a hierarquia de exceções de Python.
    Ela inclui sinais do sistema operacional e de controle da JVM/CPython como `SystemExit`, `KeyboardInterrupt` (Ctrl+C) e `GeneratorExit`.
    Se você capturar `except BaseException:`, impedirá o usuário de interromper o programa pelo teclado!
    `Exception` é a classe base destinada a todos os erros lógicos e de aplicação. Sua classe de erro customizada deve SEMPRE herdar de `Exception`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `converter_para_int(val: Any) -> int | None` que utilize `try/except (ValueError, TypeError)` e retorne `None` em caso de erro.
# Exercício 2: Escreva uma função que leia um arquivo e garanta o fechamento via `finally` (sem usar `with`), simulando o gerenciamento manual.
# Exercício 3: Escreva uma função `processar_pagamento(cartao_id: str)` que lance uma exceção `CartaoInvalidoError` derivada de `Exception` usando `raise ... from`.


def main() -> None:
    print("==========================================================")
    print("  AULA 30: TRATAMENTO DE EXCEÇÕES E EXCEPTION CHAINING")
    print("==========================================================")
    demonstrar_fluxo_try_except_else_finally(10.0, 2.0)
    demonstrar_fluxo_try_except_else_finally(10.0, 0.0)
    demonstrar_exception_chaining()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_traceback()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 30 executado com sucesso.")


if __name__ == "__main__":
    main()
