"""
48_decoradores.py - Decoradores de Funções, Closures e Preservação de Metadados com @wraps

Objetivos:
1. Compreender o padrão Decorator em Python e o conceito de Funções como Cidadãs de Primeira Classe (First-Class Citizens).
2. Dominar a criação de Closures (funções internas que capturam o escopo léxico externo).
3. Entender a sintaxe `@decorador` (açúcar sintático para `func = decorador(func)`).
4. Utilizar `*args` e `**kwargs` para criar decoradores genéricos compatíveis com qualquer assinatura.
5. Garantir a preservação de metadados (`__name__`, `__doc__`) utilizando o decorador nativo `@functools.wraps`.
"""

import time
from functools import wraps
from typing import Any, Callable


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Decorador (Decorator)?
Em Python, um Decorador é uma função que recebe outra função como argumento, estende ou altera
o seu comportamento sem modificar o seu código fonte original, e retorna uma nova função envelopada.

Fundamentos Necessários:
1. First-Class Functions: Funções em Python podem ser passadas como argumentos, atribuídas a variáveis e retornadas por outras funções.
2. Closures (Fechamentos): Uma função interna que mantém o acesso às variáveis do escopo da função externa onde foi criada.
3. Açúcar Sintático (`@decorador`):
   Escrever:
   @meu_decorador
   def minha_funcao(): pass

   É exatamente equivalente a:
   def minha_funcao(): pass
   minha_funcao = meu_decorador(minha_funcao)
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: DECORADOR DE TEMPO DE EXECUÇÃO
# ==========================================================
def medir_tempo_execucao(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorador básico que mede o tempo de execução de uma função."""

    @wraps(func)  # OBRIGATÓRIO: Preserva __name__ e __doc__ da função original!
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        duracao_ms = (fim - inicio) * 1000
        print(f"  [Benchmark] Função '{func.__name__}' executada em {duracao_ms:.4f} ms")
        return resultado

    return wrapper


@medir_tempo_execucao
def processar_calculo_demorado(limite: int) -> int:
    """Calcula a soma dos números de 1 até o limite."""
    return sum(range(1, limite + 1))


def demonstrar_fundamentos_decorador() -> None:
    print("\n--- 1. FUNDAMENTOS: Decorador de Benchmark ---")

    res = processar_calculo_demorado(1_000_000)
    print(f"Resultado do calculo: {res}")
    print(f"Nome da funcao preservado por @wraps: {processar_calculo_demorado.__name__!r}")
    print(f"Docstring preservada por @wraps: {processar_calculo_demorado.__doc__!r}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: DECORADOR DE AUTENTICAÇÃO / PERMISSÃO
# ==========================================================
def requerer_autenticacao(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorador de autorização que simula um middleware de rota."""

    @wraps(func)
    def wrapper(usuario: dict[str, Any], *args: Any, **kwargs: Any) -> Any:
        if not usuario.get("autenticado", False):
            raise PermissionError(f"Acesso negado para o usuário {usuario.get('nome', 'Anônimo')}.")
        print(f"  [Auth] Acesso liberado para usuário: {usuario.get('nome')}")
        return func(usuario, *args, **kwargs)

    return wrapper


@requerer_autenticacao
def deletar_relatorio(usuario: dict[str, Any], id_relatorio: int) -> bool:
    """Deleta um relatório do sistema."""
    print(f"  [Sucesso] Relatorio ID {id_relatorio} deletado com sucesso.")
    return True


def demonstrar_decorador_autenticacao() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Decorador de Autenticação ---")

    user_valido = {"nome": "Gabriel", "autenticado": True}
    user_invalido = {"nome": "Visitante", "autenticado": False}

    deletar_relatorio(user_valido, 101)

    try:
        deletar_relatorio(user_invalido, 102)
    except PermissionError as e:
        print(f"[!] {e}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def log_execucao_api(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorador de logging estruturado para rotas de API."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"  [API Log] Chamada recebida na rota '{func.__name__}'")
        try:
            resultado = func(*args, **kwargs)
            print(f"  [API Log] Rota '{func.__name__}' finalizada com sucesso.")
            return resultado
        except Exception as e:
            print(f"  [API Log] Rota '{func.__name__}' falhou com erro: {e}")
            raise e

    return wrapper


@log_execucao_api
def criar_pedido_controller(dados: dict[str, Any]) -> dict[str, Any]:
    return {"status": 201, "pedido_id": 9941}


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: API Controller Decorator ---")
    res = criar_pedido_controller({"cliente": "Empresa X"})
    print(f"Resultado do Controller: {res}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: CLOSURES E CELL OBJECTS
# ==========================================================
"""
Como os Decoradores e Closures funcionam no CPython:
1. Uma Closure ocorre quando uma função interna (`wrapper`) faz referência a variáveis da função externa (`func`).
2. O CPython armazena as variáveis capturadas do escopo externo em uma tupla especial chamada `__closure__`.
3. Cada elemento da tupla `__closure__` é um objeto `cell` (célula de memória CPython) que guarda o ponteiro para o valor original.
"""


def demonstrar_internamente_closure() -> None:
    print("\n--- 4. INTERNO: Inspeção do Atributo __closure__ ---")
    print(f"Closure de processar_calculo_demorado: {processar_calculo_demorado.__closure__}")
    if processar_calculo_demorado.__closure__:
        print(f"Conteúdo da célula da closure: {processar_calculo_demorado.__closure__[0].cell_contents}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Invocação da Função Decorada: Tempo O(1) de overhead para passar pelo `wrapper` + tempo da função original.
- Espaço: O(1) para armazenar o objeto `cell` da Closure na memória Heap.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Aplicar decorador sem o @functools.wraps
    print("[X] Nao-Pythonic (Sem @wraps):")
    print("  Sobrescreve __name__ da função original por 'wrapper' e apaga a docstring!")

    # [OK] PYTHONIC: Sempre usar @wraps(func)
    print("\n[OK] Pythonic:")
    print("  @wraps(func) garante que ferramentas de documentação, logs e testes reconheçam a função original!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. SEMPRE utilize `@functools.wraps(func)` na função interna `wrapper` do seu decorador.
2. Utilize sempre a assinatura `*args, **kwargs` na função wrapper para permitir que seu decorador funcione com qualquer função.
3. Certifique-se de RETORNAR o resultado da função original dentro do `wrapper` (`return func(*args, **kwargs)`).
4. Certifique-se de RETORNAR a função `wrapper` no final do seu decorador.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Esquecer de retornar a função wrapper no final do decorador
    def decorador_com_bug(func: Callable[..., Any]) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        # [!] ERRO: Esqueceu de fazer 'return wrapper'! Retorna None por padrão!

    @decorador_com_bug  # type: ignore
    def minha_func(): pass

    print(f"[!] Armadilha 1 (Esqueceu de retornar wrapper): minha_func virou {minha_func}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é uma Closure em Python e como ela se relaciona com o funcionamento de um Decorador?"
A: "Uma Closure é uma função que 'lembra' do seu ambiente de criação. Ela é uma função interna que mantém o acesso
    às variáveis do escopo de uma função externa mesmo após a função externa ter terminado sua execução.
    No padrão Decorator, a função `wrapper` é uma Closure que captura e retém a referência da função original `func`
    no seu atributo `__closure__`, permitindo executá-la e modificar seu comportamento antes e depois de sua chamada."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um decorador `@converter_para_maiusculo` que converta o retorno string de qualquer função para letras maiúsculas.
# Exercício 2: Escreva um decorador `@retry_suave` que tente executar uma função até 3 vezes caso ocorra alguma exceção antes de lançar o erro.
# Exercício 3: Crie um decorador que verifique se os argumentos numéricos passados para a função são estritamente maiores que zero.


def main() -> None:
    print("==========================================================")
    print("  AULA 48: DECORADORES DE FUNÇÕES, CLOSURES E @WRAPS")
    print("==========================================================")
    demonstrar_fundamentos_decorador()
    demonstrar_decorador_autenticacao()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_closure()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 48 executado com sucesso.")


if __name__ == "__main__":
    main()
