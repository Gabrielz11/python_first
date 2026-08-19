"""
31_excecoes_customizadas.py - Criando Exceções Customizadas de Domínio em Python

Objetivos:
1. Aprender a projetar e implementar hierarquias de exceções de domínio customizadas derivadas de `Exception`.
2. Adicionar atributos de contexto (status HTTP, códigos de erro, payload de detalhes) a instâncias de erro.
3. Integrar exceções customizadas com middlewares de tratamento global em aplicações web (FastAPI/Flask/Django).
4. Sobrescrever os métodos `__init__` e `__str__` para formatação clara de relatórios de erro.
5. Evitar a poluição e ambiguidades no tratamento de exceções genéricas em arquiteturas limpas (Clean Architecture).
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Por que criar Exceções Customizadas?
Exceções nativas do Python (como `ValueError` ou `KeyError`) são genéricas demais para expressar regras
de negócio de uma aplicação comercial.

Vantagens de Exceções Customizadas:
1. Expressividade do Domínio: Erros como `SaldoInsuficienteError` ou `UsuarioNaoEncontradoError`
   tornam o código autodocumentável.
2. Tratamento Seletivo: Permite capturar exatamente o erro de negócio desejado no controlador da API
   sem capturar acidentalmente um erro técnico de sintaxe.
3. Atributos de Contexto: Permite acoplar metadados úteis (ex: `codigo_erro="USER_NOT_FOUND"`, `status_code=404`)
   que serão automaticamente convertidos em respostas JSON pelo middleware.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: HIERARQUIA DE EXCEÇÕES DE DOMÍNIO
# ==========================================================
class AplicacaoBaseError(Exception):
    """Exceção base de toda a aplicação backend."""

    def __init__(self, mensagem: str, codigo_erro: str = "INTERNAL_ERROR", status_code: int = 500) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.codigo_erro = codigo_erro
        self.status_code = status_code

    def __str__(self) -> str:
        return f"[{self.codigo_erro}] {self.mensagem} (HTTP {self.status_code})"


class EntidadeNaoEncontradaError(AplicacaoBaseError):
    """Lançada quando um recurso solicitado não existe no banco de dados."""

    def __init__(self, entidade: str, id_recurso: Any) -> None:
        super().__init__(
            mensagem=f"{entidade} com ID '{id_recurso}' não foi encontrado.",
            codigo_erro="ENTITY_NOT_FOUND",
            status_code=404,
        )
        self.entidade = entidade
        self.id_recurso = id_recurso


class RegraNegocioError(AplicacaoBaseError):
    """Lançada quando uma operação viola uma regra de negócio."""

    def __init__(self, mensagem: str, codigo_erro: str = "BUSINESS_RULE_VIOLATION") -> None:
        super().__init__(mensagem=mensagem, codigo_erro=codigo_erro, status_code=422)


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: USO PRÁTICO DAS EXCEÇÕES
# ==========================================================
def demonstrar_uso_excecoes_customizadas() -> None:
    print("\n--- 1. FUNDAMENTOS: Disparando e Capturando Exceções de Domínio ---")

    try:
        raise EntidadeNaoEncontradaError(entidade="Usuario", id_recurso=9941)
    except AplicacaoBaseError as e:
        print(f"Exceção capturada via classe base: {e}")
        print(f"  - Mensagem: {e.mensagem}")
        print(f"  - Código do erro: {e.codigo_erro}")
        print(f"  - Status HTTP sugerido: {e.status_code}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ContaBancaria:
    """Entidade de domínio simulando operações bancárias."""

    def __init__(self, id_conta: str, saldo_inicial: float) -> None:
        self.id_conta = id_conta
        self.saldo = saldo_inicial

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise RegraNegocioError("O valor de saque deve ser maior que zero.", codigo_erro="INVALID_AMOUNT")
        if valor > self.saldo:
            raise RegraNegocioError(
                f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}, Valor solicitado: R$ {valor:.2f}.",
                codigo_erro="INSUFFICIENT_FUNDS",
            )
        self.saldo -= valor


def middleware_tratamento_erros_api(func: Any, *args: Any) -> dict[str, Any]:
    """Simula um middleware de framework web (FastAPI/Flask) tratando exceções."""
    try:
        func(*args)
        return {"status": 200, "body": {"message": "Operação realizada com sucesso"}}
    except AplicacaoBaseError as e:
        # Captura tratada de erros de negócio de forma genérica e padronizada
        return {
            "status": e.status_code,
            "body": {"error_code": e.codigo_erro, "message": e.mensagem},
        }
    except Exception as e:
        # Fallback de erro não esperado
        return {
            "status": 500,
            "body": {"error_code": "UNEXPECTED_ERROR", "message": f"Erro interno: {e}"},
        }


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Middleware de API REST ---")
    conta = ContaBancaria(id_conta="ACC-101", saldo_inicial=500.0)

    # Cenário 1: Saque Válido
    res1 = middleware_tratamento_erros_api(conta.sacar, 200.0)
    print(f"Resultado Saque R$ 200: {res1}")

    # Cenário 2: Saque com Saldo Insuficiente (Dispara RegraNegocioError)
    res2 = middleware_tratamento_erros_api(conta.sacar, 1000.0)
    print(f"Resultado Saque R$ 1000 (Regra Violada): {res2}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: TUPLE ARGS E DISPATCH
# ==========================================================
"""
Como o CPython armazena dados de Exceções Customizadas:
1. `BaseException.args`: Quando chamamos `super().__init__(mensagem)`, o Python armazena os argumentos
   passados em uma tupla interna chamada `self.args`.
2. Impressão do Traceback: Se a exceção não for capturada, o CPython invoca `str(excecao)` que
   por padrão imprime a mensagem contida em `self.args[0]`.
3. Herança Múltipla: Exceções customizadas podem implementar mixins (ex: `JSONSerializableMixin`) para expor facilidades de conversão.
"""


def demonstrar_internamente_args() -> None:
    print("\n--- 4. INTERNO: Atributo self.args da BaseException ---")
    err = EntidadeNaoEncontradaError("Produto", 50)
    print(f"Atributo self.args da excecao: {err.args}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Instanciação de Exceção Customizada (`raise MinhaExcecao()`): Tempo O(1), Espaço O(1).
- Captura em Bloco `except`: Tempo O(1) para resolver a hierarquia de herança no CPython (`issubclass()`).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar ValueError genérico para erros de negócio com mensagens em texto solto
    print("[X] Nao-Pythonic (Uso de ValueError genérico):")
    print("  raise ValueError('ERRO_SALDO_INSUFICIENTE_404')  # Dificulta o parse no controlador!")

    # [OK] PYTHONIC: Exceções de classe fortemente tipadas com atributos
    print("\n[OK] Pythonic:")
    print("  raise SaldoInsuficienteError(saldo_atual=100.0, valor_saque=500.0)")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre herde sua exceção base da aplicação de `Exception` (NUNCA de `BaseException`).
2. Adicione o sufixo `Error` ou `Exception` ao nome das classes (ex: `PagamentoInvalidoError`).
3. Crie uma classe base comum para todas as exceções do seu projeto/módulo (`AplicacaoBaseError`).
   Isso permite que quem usa sua biblioteca possa capturar TODAS as suas exceções com um único bloco `except AplicacaoBaseError:`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Criar exceções que herdam de BaseException
    class ErroErradoBase(BaseException):  # [!] ERRADO!
        pass

    try:
        raise ErroErradoBase("Erro perigoso")
    except Exception:
        print("[!] Esse bloco 'except Exception' NAO vai capturar ErroErradoBase!")
    except BaseException as e:
        print(f"[!] Capturado apenas por causa do BaseException: {type(e).__name__}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como você desenharia o sistema de exceções de um microsserviço de e-commerce em Python?"
A: "Criaria uma hierarquia bem definida:
    1. `EcommerceBaseError(Exception)`: Classe base do projeto com atributos `error_code` e `http_status`.
    2. `DomainError(EcommerceBaseError)`: Erros de regra de negócio (ex: `EstoqueInsuficienteError`, `CupomExpiradoError`).
    3. `InfrastructureError(EcommerceBaseError)`: Erros de serviços externos/DB (ex: `PaymentGatewayTimeoutError`).
    Essa separação permite que o middleware HTTP trate erros de domínio retornando 4xx (Bad Request/Unprocessable Entity)
    e erros de infraestrutura retornando 5xx (Internal Server Error) com alertas de monitoramento."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma exceção customizada `SenhaInvalidaError` que receba o motivo da rejeição (ex: "Sem caracteres especiais") e armazene como atributo.
# Exercício 2: Crie uma hierarquia de erros para um sistema de arquivos: `FileError` -> `FileNotFoundDomainError`, `FileTooLargeError`.
# Exercício 3: Escreva uma função que simule um parser de formulário de cadastro e lance `CampoObrigatorioError(campo="email")` se o campo não estiver preenchido.


def main() -> None:
    print("==========================================================")
    print("  AULA 31: CRIANDO EXCEÇÕES CUSTOMIZADAS DE DOMÍNIO")
    print("==========================================================")
    demonstrar_uso_excecoes_customizadas()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_args()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 31 executado com sucesso.")


if __name__ == "__main__":
    main()
