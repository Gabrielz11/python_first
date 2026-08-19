"""
49_decoradores_com_argumentos.py - Fábrica de Decoradores e Decoradores Baseados em Classes

Objetivos:
1. Dominar a criação de Decoradores Parametrizados (Fábrica de Decoradores com 3 níveis de funções aninhadas).
2. Compreender a ordem de avaliação do CPython ao utilizar a sintaxe `@decorador(argumento)`.
3. Criar decoradores utilizando Classes com os métodos `__init__` e `__call__`.
4. Implementar mecanismos reais de Retry com contagem de tentativas e autorização por perfis (RBAC).
5. Prevenir a confusão entre o nível da fábrica, do decorador e da função wrapper.
"""

import time
from functools import wraps
from typing import Any, Callable


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Como funcionam Decoradores que recebem Argumentos?
Um decorador tradicional recebe APENAS a função como parâmetro: `@meu_decorador`.
Quando escrevemos `@meu_decorador(parametro="valor")`, o Python precisa de TRÊS NÍVEIS de funções:

Estrutura de 3 Níveis (Fábrica de Decoradores):
1. Nível 1 (Fábrica / Outer): Recebe os argumentos do decorador (`parametro="valor"`) e retorna o decorador real.
2. Nível 2 (Decorador / Middle): Recebe a função original (`func`) que está sendo decorada.
3. Nível 3 (Wrapper / Inner): Recebe os argumentos da função original (`*args`, `**kwargs`) e executa a lógica.

Alternativa: Decoradores Baseados em Classes
Utilizar uma Classe onde o `__init__` recebe os argumentos do decorador e o `__call__` recebe a função a ser decorada.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: FÁBRICA DE DECORADORES (RETRY)
# ==========================================================
def retry(max_tentativas: int = 3, tempo_espera_segundos: float = 0.1) -> Callable[..., Any]:
    """Nível 1 (Fábrica): Recebe os parâmetros de configuração do retry."""

    def decorador(func: Callable[..., Any]) -> Callable[..., Any]:
        """Nível 2 (Decorador): Recebe a função a ser decorada."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Nível 3 (Wrapper): Executa a função com tentativas."""
            tentativa_atual = 1
            while tentativa_atual <= max_tentativas:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  [Retry] Tentativa {tentativa_atual}/{max_tentativas} falhou: {e}")
                    if tentativa_atual == max_tentativas:
                        raise e
                    time.sleep(tempo_espera_segundos)
                    tentativa_atual += 1

        return wrapper

    return decorador


@retry(max_tentativas=3, tempo_espera_segundos=0.05)
def chamada_instavel_servico(contador_falhas: dict[str, int]) -> str:
    contador_falhas["tentativas"] += 1
    if contador_falhas["tentativas"] < 3:
        raise ConnectionError("Timeout temporário de conexão!")
    return "Sucesso na conexão!"


def demonstrar_fundamentos_retry() -> None:
    print("\n--- 1. FUNDAMENTOS: Decorador de Retry Parametrizado ---")

    estado = {"tentativas": 0}
    resultado = chamada_instavel_servico(estado)
    print(f"Resultado final: {resultado} (Após {estado['tentativas']} tentativas)")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: DECORADOR BASEADO EM CLASSE
# ==========================================================
class RequererPerfil:
    """Decorador baseado em classe para Role-Based Access Control (RBAC)."""

    def __init__(self, perfil_permitido: str) -> None:
        self.perfil_permitido = perfil_permitido

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(usuario_perfil: str, *args: Any, **kwargs: Any) -> Any:
            if usuario_perfil != self.perfil_permitido:
                raise PermissionError(f"Requer perfil '{self.perfil_permitido}', mas recebeu '{usuario_perfil}'.")
            return func(usuario_perfil, *args, **kwargs)

        return wrapper


@RequererPerfil(perfil_permitido="ADMIN")
def alterar_configuracao_sistema(perfil: str, nova_config: str) -> None:
    print(f"  [Sucesso] Configuração alterada para '{nova_config}' pelo perfil {perfil}.")


def demonstrar_decorador_classe() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Decorador Baseado em Classe ---")

    alterar_configuracao_sistema("ADMIN", "DEBUG_MODE=TRUE")

    try:
        alterar_configuracao_sistema("USER", "DEBUG_MODE=TRUE")
    except PermissionError as e:
        print(f"[!] {e}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def rate_limiter(limite_requisicoes: int) -> Callable[..., Any]:
    """Fábrica de decoradores que limita a quantidade de chamadas a uma rota."""

    def decorador(func: Callable[..., Any]) -> Callable[..., Any]:
        contagem = 0

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal contagem
            if contagem >= limite_requisicoes:
                raise RuntimeError(f"Rate limit excedido! Máximo de {limite_requisicoes} chamadas permitidas.")
            contagem += 1
            print(f"  [RateLimiter] Requisição {contagem}/{limite_requisicoes} autorizada.")
            return func(*args, **kwargs)

        return wrapper

    return decorador


@rate_limiter(limite_requisicoes=2)
def consultar_saldo_api() -> float:
    return 1500.00


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Rate Limiter Controller ---")
    print(f"Chamada 1: R$ {consultar_saldo_api():.2f}")
    print(f"Chamada 2: R$ {consultar_saldo_api():.2f}")

    try:
        consultar_saldo_api()  # Excede limite!
    except RuntimeError as e:
        print(f"[!] {e}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ORDEM DE AVALIAÇÃO
# ==========================================================
"""
Como o CPython avalia `@fabrica(arg)`:
1. Quando o interpretador lê `@fabrica(10)`, ele PRIMEIRO executa a função `fabrica(10)`.
2. A chamada `fabrica(10)` retorna a função `decorador`.
3. Em seguida, o Python aplica a decoração equivalente a: `minha_funcao = decorador(minha_funcao)`.
4. É por isso que é estritamente necessário ter os 3 níveis de funções aninhadas!
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Invocação do Decorador Parametrizado: Tempo O(1), Espaço O(1) adicional para manter as variáveis do Nível 1 na Closure.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Tentar usar 2 níveis para um decorador que recebe argumentos
    print("[X] Nao-Pythonic (Misturar argumentos da fábrica com a função):")
    print("  def dec(func, arg): ...  # Não funciona com a sintaxe @dec(arg)!")

    # [OK] PYTHONIC: 3 níveis de funções (Fábrica -> Decorador -> Wrapper) ou Decorador de Classe
    print("\n[OK] Pythonic:")
    print("  def fabrica(arg): def decorador(func): def wrapper(*a, **k): ... return wrapper; return decorador")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize nomes expressivos para as funções internas (`decorador` no meio, `wrapper` dentro).
2. Utilize `nonlocal` na `wrapper` se precisar modificar variáveis do escopo da fábrica ou do decorador.
3. Se a lógica do decorador for muito complexa, prefira uma Classe com `__init__` e `__call__` em vez de 3 níveis de funções.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer os parênteses ao chamar um decorador parametrizado com valores padrão
    # Exemplo: `@retry` sem parênteses passa a função `func` como primeiro argumento para `max_tentativas`!
    print("[!] Cuidado: Se o decorador recebe argumentos (mesmo com valores padrão), você DEVE chamá-lo com parênteses: @retry()")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Explique como funciona um decorador com argumentos e por que ele precisa de 3 níveis de funções aninhadas?"
A: "Um decorador com argumentos exige 3 níveis de funções devido à sintaxe `@fabrica(arg)`:
    - O 1º nível (Fábrica) é invocado imediatamente com os argumentos do decorador (`arg`) e deve RETORNAR o 2º nível.
    - O 2º nível (Decorador) é o decorador real que recebe a função de destino (`func`) como argumento e RETORNA o 3º nível.
    - O 3º nível (Wrapper) é a Closure que intercepta a execução real recebendo `*args` e `**kwargs` no momento em que a função é chamada."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma fábrica de decoradores `@multiplicar_retorno(fator: int)` que multiplique o retorno numérico da função decorada pelo fator.
# Exercício 2: Escreva um decorador parametrizado `@validar_tipos(tipo_esperado: type)` que valide o tipo do retorno da função.
# Exercício 3: Implemente um decorador baseado em classe `TemporizadorLog(prefixo: str)` que imprima o prefixo e o tempo de execução da função.


def main() -> None:
    print("==========================================================")
    print("  AULA 49: FÁBRICA DE DECORADORES E DECORADORES DE CLASSE")
    print("==========================================================")
    demonstrar_fundamentos_retry()
    demonstrar_decorador_classe()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 49 executado com sucesso.")


if __name__ == "__main__":
    main()
