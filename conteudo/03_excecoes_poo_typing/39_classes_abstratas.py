"""
39_classes_abstratas.py - Classes Abstratas, Módulo abc, @abstractmethod e Contratos de Interface

Objetivos:
1. Dominar a criação de Classes Abstratas (ABCs) em Python utilizando o módulo nativo `abc` (`ABC` e `@abstractmethod`).
2. Entender como o Python valida contratos de interface impedindo a instanciação direta de classes abstratas incompletas.
3. Definir propriedades abstratas combinando `@property` com `@abstractmethod`.
4. Desenvolver Arquiteturas Limpas (Clean Architecture / DDD) desacoplando a camada de domínio da infraestrutura.
5. Inspecionar o atributo `__abstractmethods__` gerenciado pelo metaclasse `ABCMeta`.
"""

from abc import ABC, abstractmethod
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma Classe Abstrata (ABC) em Python?
Uma Classe Base Abstrata (Abstract Base Class - ABC) é uma classe projetada especificamente para servir
de modelo (contrato) para outras classes. Ela NÃO DEVE ser instanciada diretamente.

Características das ABCs:
1. `abc.ABC`: Classe base que ativa o comportamento de validação estrita no CPython.
2. `@abstractmethod`: Decorador aplicado aos métodos que TODA subclasse concreta OBRIGATORIAMENTE deve implementar.
3. Garantia em Tempo de Instanciação: Se uma subclasse esquecer de implementar um único `@abstractmethod`,
   o CPython recusa a instanciação lançando um `TypeError` no exato momento do `__new__`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CONTRATOS DE INTERFACE
# ==========================================================
class BaseNotificador(ABC):
    """Contrato de Interface Abstrato para envio de notificações."""

    @abstractmethod
    def enviar(self, mensagem: str, destinatario: str) -> bool:
        """Método abstrato obrigatorio."""
        pass

    @property
    @abstractmethod
    def canal_nome(self) -> str:
        """Propriedade abstrata obrigatoria."""
        pass


class EmailNotificadorConcreto(BaseNotificador):
    """Subclasse Concreta que satisfaz totalmente o contrato."""

    @property
    def canal_nome(self) -> str:
        return "SMTP_EMAIL"

    def enviar(self, mensagem: str, destinatario: str) -> bool:
        print(f"  [{self.canal_nome}] Enviando email para {destinatario}: {mensagem}")
        return True


def demonstrar_fundamentos_abc() -> None:
    print("\n--- 1. FUNDAMENTOS: Validação de Contrato com ABC ---")

    # Instanciando a classe concreta
    notificador = EmailNotificadorConcreto()
    notificador.enviar("Bem-vindo ao sistema!", "usuario@empresa.com")

    # Tentativa de instanciar a classe abstrata diretamente
    try:
        _ = BaseNotificador()  # type: ignore # Lança TypeError!
    except TypeError as e:
        print(f"[!] TypeError ao tentar instanciar BaseNotificador abstrata: {e}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SUBCLASSE INCOMPLETA
# ==========================================================
class NotificadorIncompleto(BaseNotificador):
    """Esqueceu de implementar o método enviar()!"""

    @property
    def canal_nome(self) -> str:
        return "INCOMPLETO"


def demonstrar_subclasse_incompleta() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Subclasse Incompleta ---")

    try:
        _ = NotificadorIncompleto()  # type: ignore
    except TypeError as e:
        print(f"[!] CPython barrou instanciação da subclasse incompleta: {e}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class AbstractUserRepository(ABC):
    """Contrato de Repositório de Usuários (Clean Architecture / Domain)."""

    @abstractmethod
    def buscar_por_id(self, user_id: int) -> dict[str, Any] | None:
        pass

    @abstractmethod
    def salvar(self, user_data: dict[str, Any]) -> int:
        pass


class InMemoryUserRepository(AbstractUserRepository):
    """Implementação concreta do repositório em memória para testes."""

    def __init__(self) -> None:
        self._db: dict[int, dict[str, Any]] = {}
        self._counter = 1

    def salvar(self, user_data: dict[str, Any]) -> int:
        new_id = self._counter
        user_data["id"] = new_id
        self._db[new_id] = user_data
        self._counter += 1
        return new_id

    def buscar_por_id(self, user_id: int) -> dict[str, Any] | None:
        return self._db.get(user_id)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: AbstractUserRepository ---")
    repo: AbstractUserRepository = InMemoryUserRepository()

    uid = repo.salvar({"nome": "Gabriel", "email": "gabriel@empresa.com"})
    usuario = repo.buscar_por_id(uid)
    print(f"Usuario recuperado via interface abstrata: {usuario}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: __ABSTRACTMETHODS__
# ==========================================================
"""
Como o CPython controla Classes Abstratas:
1. O metaclasse `ABCMeta` inspeciona a classe durante a compilação e coleta os nomes de todos os métodos
   decorados com `@abstractmethod` em um `frozenset` atribuído à propriedade `__abstractmethods__`.
2. Ao executar `__new__` para criar um objeto, o CPython verifica se `len(cls.__abstractmethods__) > 0`.
   Se a contagem for maior que 0, a instanciação é bloqueada imediatamente com `TypeError`.
"""


def demonstrar_internamente_abstractmethods() -> None:
    print("\n--- 4. INTERNO: Atributo __abstractmethods__ no CPython ---")
    print(f"Métodos abstratos pendentes em BaseNotificador: {BaseNotificador.__abstractmethods__}")
    print(f"Métodos abstratos pendentes em NotificadorIncompleto: {NotificadorIncompleto.__abstractmethods__}")
    print(f"Métodos abstratos pendentes em EmailNotificadorConcreto: {EmailNotificadorConcreto.__abstractmethods__}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Validação de Classe Abstrata na Instanciação (`__new__`): Checagem do tamanho do frozenset `__abstractmethods__` -> Tempo O(1), Espaço O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Lançar NotImplementedError manualmente no corpo de funções sem usar o módulo abc
    print("[X] Nao-Pythonic (NotImplementedError manual sem abc.ABC):")
    print("  class Base: def enviar(self): raise NotImplementedError()  # Só falha se o método for INVOCADO!")

    # [OK] PYTHONIC: Utilizar abc.ABC com @abstractmethod
    print("\n[OK] Pythonic (abc.ABC + @abstractmethod):")
    print("  Falha IMEDIATAMENTE no momento de instanciar a classe se faltar algum método!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize o módulo `abc` para definir contratos de interface estritos entre módulos de domínios e infraestrutura.
2. Mantenha os contratos abstratos focados em interfaces coesas (Interface Segregation Principle).
3. Combine `@property` e `@abstractmethod` aplicando a ordem correta de decoradores:
   `@property` por FORA, `@abstractmethod` por DENTRO.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Inverter a ordem dos decoradores @property e @abstractmethod
    class DecoradorErrado(ABC):
        @property
        @abstractmethod
        def meu_attr(self) -> str:
            pass

    print("[!] Lembre-se: A ordem correta e @property em cima, @abstractmethod em baixo!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença de comportamento entre lançar `raise NotImplementedError` em um método e decorá-lo com `@abstractmethod`?"
A: "1. `raise NotImplementedError()` só dispara uma exceção se a aplicação tentar EXECUTAR (chamar) aquele método específico em runtime.
    2. `@abstractmethod` (combinado com `abc.ABC`) bloqueia a INSTANCIAÇÃO da classe inteira logo no momento do `__new__`,
       impedindo que o objeto seja criado na memória se o contrato de interface não tiver sido 100% satisfeito."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe abstrata `BaseDatabaseConnector` com métodos abstratos `conectar()` e `desconectar()`.
# Exercício 2: Implemente uma classe concreta `PostgresConnector` e comprove que ela pode ser instanciada.
# Exercício 3: Crie uma propriedade abstrata `@property` + `@abstractmethod` para representar a string de conexão.


def main() -> None:
    print("==========================================================")
    print("  AULA 39: CLASSES ABSTRATAS E CONTRATOS DE INTERFACE")
    print("==========================================================")
    demonstrar_fundamentos_abc()
    demonstrar_subclasse_incompleta()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_abstractmethods()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 39 executado com sucesso.")


if __name__ == "__main__":
    main()
