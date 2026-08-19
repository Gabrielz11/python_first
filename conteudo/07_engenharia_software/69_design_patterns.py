"""
69_design_patterns.py - Padrões de Projeto Clássicos (GoF) em Python: Singleton, Strategy e Observer

Objetivos:
1. Dominar a implementação idiomática de Padrões de Projeto (Design Patterns - GoF) em Python.
2. Compreender a implementação do Singleton Pattern via Metaclasse.
3. Aplicar o Strategy Pattern de forma limpa aproveitando First-Class Functions em Python.
4. Implementar o Observer Pattern (Publisher-Subscriber) para comunicação desacoplada de eventos.
5. Identificar quando os recursos nativos do Python (como Módulos e Funções) dispensam a complexidade de padrões GoF tradicionais.
"""

from typing import Any, Callable


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Design Patterns (Padrões de Projeto)?
Padrões de Projeto são soluções reutilizáveis para problemas comuns de arquitetura de software,
catalogados pelo Gang of Four (GoF).

Padrões em Python (Estilo Pythonic vs Estilo Clássico):
Muitos padrões GoF foram criados para contornar limitações de linguagens estáticas (como C++ e Java dos anos 90).
Em Python:
1. Singleton: Pode ser alcançado simplesmente criando um MÓDULO Python (módulos são Singletons nativos!).
2. Strategy: Pode ser implementado passando FUNÇÕES diretamente como argumentos (já que funções são objetos de primeira classe).
3. Factory: Pode ser implementado elegantemente via `@classmethod`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: SINGLETON VIA METACLASSE
# ==========================================================
class SingletonMeta(type):
    """Metaclasse que garante que apenas UMA instância de uma classe exista na memória."""

    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            instancia = super().__call__(*args, **kwargs)
            cls._instances[cls] = instancia
        return cls._instances[cls]


class LoggerCentral(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.logs: list[str] = []

    def log(self, msg: str) -> None:
        self.logs.append(msg)


def demonstrar_singleton() -> None:
    print("\n--- 1. FUNDAMENTOS: Singleton Pattern via Metaclasse ---")

    logger1 = LoggerCentral()
    logger2 = LoggerCentral()

    logger1.log("Log 1 gravado por logger1")

    print(f"logger1 is logger2? {logger1 is logger2} (Mesma referência na RAM)")
    print(f"Logs vistos por logger2: {logger2.logs}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: STRATEGY PATTERN COM FUNÇÕES
# ==========================================================
# Em Python, o Strategy Pattern não precisa de N classes! Basta passar funções!
def estrategia_desconto_estudante(valor: float) -> float:
    return valor * 0.50


def estrategia_desconto_black_friday(valor: float) -> float:
    return valor * 0.70


def calcular_checkout(valor_total: float, estrategia: Callable[[float], float]) -> float:
    """Função de checkout que consome o Strategy Pattern via Callable."""
    return estrategia(valor_total)


def demonstrar_strategy() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Strategy Pattern com Callables ---")

    v1 = calcular_checkout(100.0, estrategia_desconto_estudante)
    v2 = calcular_checkout(100.0, estrategia_desconto_black_friday)

    print(f"Preço com Estratégia Estudante (50%): R$ {v1:.2f}")
    print(f"Preço com Estratégia Black Friday (30% off): R$ {v2:.2f}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO: OBSERVER PATTERN
# ==========================================================
class EventNotifierSubject:
    """Publisher do Observer Pattern para notificação desacoplada de eventos."""

    def __init__(self) -> None:
        self._observers: list[Callable[[str, dict[str, Any]], None]] = []

    def inscrever(self, observer: Callable[[str, dict[str, Any]], None]) -> None:
        self._observers.append(observer)

    def notificar(self, evento: str, dados: dict[str, Any]) -> None:
        print(f"  [Subject] Evento '{evento}' disparado para {len(self._observers)} observadores:")
        for obs in self._observers:
            obs(evento, dados)


def listener_email(evento: str, dados: dict[str, Any]) -> None:
    print(f"    - [Observer Email] Notificação enviada para {dados.get('email')}")


def listener_analytics(evento: str, dados: dict[str, Any]) -> None:
    print(f"    - [Observer Analytics] Métrica registrada para evento {evento}")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Observer Pattern (Event Bus) ---")

    event_bus = EventNotifierSubject()
    event_bus.inscrever(listener_email)
    event_bus.inscrever(listener_analytics)

    event_bus.notificar("USER_REGISTERED", {"email": "gabriel@empresa.com"})


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: MÓDULOS COMO SINGLETONS
# ==========================================================
"""
Por que Módulos Python são o Singleton perfeito:
1. O CPython armazena todos os módulos importados no dicionário global `sys.modules`.
2. A primeira vez que você faz `import meu_modulo`, o CPython executa o arquivo e salva a instância no `sys.modules`.
3. Importações subsequentes em qualquer arquivo da aplicação retornam exatamente o MESMO objeto de módulo.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Singleton (Lookup em Metaclasse): Tempo O(1), Espaço O(1).
- Strategy Pattern (Chamada de Função First-Class): Tempo O(1), Espaço O(1).
- Observer Pattern (Disparo de Notificação para N Observadores): Tempo O(N), Espaço O(N).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Implementar Strategy Pattern criando 10 classes pesadas com interfaces no estilo Java
    print("[X] Nao-Pythonic (Over-engineering de Strategy):")
    print("  class EstA(Strategy): ... \n  class EstB(Strategy): ...  # 10 arquivos desnecessários!")

    # [OK] PYTHONIC: Passar funções limpas diretamente como parâmetros
    print("\n[OK] Pythonic:")
    print("  def est_a(v): ... \n  calcular(v, estrategia=est_a)  # Conciso e elegante!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Aproveite as características nativas do Python (First-Class Functions, Módulos, Decoradores) para implementar Design Patterns de forma simples.
2. Utilize o Singleton Pattern apenas para recursos verdadeiramente únicos (como Pools de Conexão ou Logger Central).
3. Utilize o Observer Pattern para desacoplar a lógica de negócio principal de ações secundárias (como envio de e-mails, auditorias ou analytics).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Usar Singleton em excesso transformando objetos em estado global compartilhado difícil de testar
    print("[!] Armadilha 1: Abuso de Singleton transforma código em Estado Global difícil de resetar durante testes unitários!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o conceito de 'Funções como Cidadãs de Primeira Classe' (First-Class Functions) simplifica a implementação do Strategy Pattern em Python?"
A: "Em linguagens como Java tradicional, o Strategy Pattern exige a criação de uma Interface e a implementação de uma Classe concreta para cada estratégia.
    Em Python, como funções são objetos de primeira classe, elas podem ser atribuídas a variáveis, salvas em dicionários e passadas diretamente como argumentos de funções.
    Dessa forma, uma simples função Python atua diretamente como uma Estratégia concreta, eliminando o boilerplate de criar múltiplas classes."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um módulo Python e comprove que ele se comporta como um Singleton nativo ao alterar um atributo seu em dois arquivos.
# Exercício 2: Escreva uma função `processar_texto(texto: str, transformador: Callable[[str], str]) -> str` testando com `str.upper` e `str.strip`.
# Exercício 3: Implemente o Observer Pattern para notificar quando a temperatura de um sensor ultrapassar 40 graus.


def main() -> None:
    print("==========================================================")
    print("  AULA 69: PADRÕES DE PROJETO CLÁSSICOS (GOF) EM PYTHON")
    print("==========================================================")
    demonstrar_singleton()
    demonstrar_strategy()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 69 executado com sucesso.")


if __name__ == "__main__":
    main()
