"""
37_heranca_multipla_mro.py - Herança Múltipla, Problema do Diamante, Algoritmo C3 e Mixins

Objetivos:
1. Dominar o funcionamento de Herança Múltipla em Python (uma subclasse herdando de duas ou mais classes).
2. Compreender a resolução do Problema do Diamante (Diamond Problem).
3. Entender a Ordem de Resolução de Métodos (Method Resolution Order - MRO) e o algoritmo C3 Linearization.
4. Aplicar o Padrão Mixin para composição de comportamentos em arquiteturas backend.
5. Inspecionar o MRO de classes via `Classe.mro()` ou `Classe.__mro__`.
"""

import json
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
r"""
O que é Herança Múltipla e MRO em Python?
Ao contrário de linguagens como C# ou Java tradicional, o Python permite que uma classe herde diretamente de múltiplas superclasses.

O Problema do Diamante (Diamond Problem):
Ocorre quando uma classe D herda de B e C, e tanto B quanto C herdam da mesma classe base A:
       A
      / \
     B   C
      \ /
       D
Qual implementação de método da classe A deve ser executada se B e C a sobrescreverem?

A Solução do Python: C3 Linearization (MRO)
Desde o Python 2.3, o CPython resolve a hierarquia de herança múltipla utilizando o algoritmo estrito
C3 Linearization. O MRO garante:
1. Ordem de Precedência Local: As classes filhas são checadas antes das classes pai.
2. Ordem de Declaração: A ordem em que as superclasses são listadas entre parênteses é preservada (`class D(B, C)` -> B vem antes de C).
3. Mono-tonocidade: Nenhuma classe pai é visitada duas vezes.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: INSPEÇÃO DO MRO
# ==========================================================
class A:
    def quem_sou_eu(self) -> str:
        return "Classe A"


class B(A):
    def quem_sou_eu(self) -> str:
        return f"Classe B -> {super().quem_sou_eu()}"


class C(A):
    def quem_sou_eu(self) -> str:
        return f"Classe C -> {super().quem_sou_eu()}"


class D(B, C):
    """Herança Múltipla em Diamante: D herda de B e C (nesta ordem)."""

    def quem_sou_eu(self) -> str:
        return f"Classe D -> {super().quem_sou_eu()}"


def demonstrar_fundamentos_mro() -> None:
    print("\n--- 1. FUNDAMENTOS: Inspecionando a Ordem do MRO ---")

    instancia_d = D()
    print(f"Resultado de D().quem_sou_eu():\n  {instancia_d.quem_sou_eu()}")

    print("\nOrdem de Resolução de Métodos (D.mro()):")
    for idx, cls in enumerate(D.mro(), start=1):
        print(f"  {idx}. {cls.__name__}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PADRÃO MIXIN
# ==========================================================
"""
O que é um Mixin em Python?
Um Mixin é uma classe pequena e altamente especializada projetada para injetar comportamentos
ou funcionalidades extras em outras classes via Herança Múltipla.

Características dos Mixins:
1. Não devem ser instanciados sozinhos (não possuem `__init__` próprio ou dependem do construtor das subclasses).
2. Não possuem estado interno independente.
3. Servem apenas para fornecer métodos utilitários reutilizáveis.
"""


class JSONSerializerMixin:
    """Mixin que adiciona a funcionalidade de serialização em JSON para qualquer classe."""

    def to_json(self) -> str:
        # Acessa os atributos da própria instância através do __dict__
        dados = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return json.dumps(dados, default=str, ensure_ascii=False)


class LoggableMixin:
    """Mixin que adiciona capacidade de logging para auditoria de ações."""

    def log_acao(self, acao: str) -> None:
        nome_classe = self.__class__.__name__
        print(f"  [Audit Log] {nome_classe} executou a ação: {acao}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class BaseEntity:
    def __init__(self, entity_id: int) -> None:
        self.entity_id = entity_id


class OrderModel(BaseEntity, JSONSerializerMixin, LoggableMixin):
    """Modelo de Pedido composto com múltiplos Mixins em produção."""

    def __init__(self, order_id: int, cliente: str, valor_total: float) -> None:
        super().__init__(order_id)
        self.cliente = cliente
        self.valor_total = valor_total

    def finalizar_compra(self) -> None:
        self.log_acao("FINALIZAR_COMPRA")
        print(f"  Pedido {self.entity_id} finalizado. JSON Payload: {self.to_json()}")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Entidade Composta por Mixins ---")
    pedido = OrderModel(5001, "Gabriel Zilmar", 1250.00)
    pedido.finalizar_compra()


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ALGORITMO C3 LINEARIZATION
# ==========================================================
"""
Como o CPython calcula o MRO (C3 Linearization):
1. Para qualquer classe C, o MRO é representado por `L(C) = C + merge(L(Pai1), L(Pai2), ..., Pai1, Pai2)`.
2. Se a hierarquia de herança violar a monotonicidade (ex: tentar criar um ciclo de herança onde A vem antes de B e depois B antes de A),
   o CPython recusa a definição da classe e lança `TypeError: Cannot create a consistent method resolution order (MRO)`.
"""


def demonstrar_internamente_mro_inconsistente() -> None:
    print("\n--- 4. INTERNO: Tentativa de MRO Inconsistente ---")

    class X: pass
    class Y: pass
    class A_C3(X, Y): pass
    class B_C3(Y, X): pass

    try:
        # Tentar herdar de A_C3 (X depois Y) e B_C3 (Y depois X) é contraditório!
        type("C_Invalida", (A_C3, B_C3), {})
    except TypeError as e:
        print(f"[!] TypeError capturado com sucesso (C3 Linearization falhou): {e}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Cálculo de MRO de uma classe (Tempo de compilação): Tempo O(N * K) via algoritmo C3 Linearization.
- Resolução de Chamada de Método em Runtime: CPython utiliza o cache interno do MRO -> Tempo O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Herança Múltipla com classes de negócio pesadas e acopladas
    print("[X] Nao-Pythonic (Herança Múltipla de 5 classes de domínio com __init__ conflitantes):")
    print("  class MultiplesBugs(ServicoA, ServicoB, ServicoC): ...  # Caos de inicialização!")

    # [OK] PYTHONIC: Utilizar Herança Múltipla EXCLUSIVAMENTE com o Padrão Mixin
    print("\n[OK] Pythonic:")
    print("  class ServicoUnico(BaseService, JSONMixin, AuditLogMixin): ...  # Limpo e modular!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize Herança Múltipla prioritariamente para aplicar o padrão Mixin.
2. Nomeie classes Mixin com o sufixo `Mixin` (ex: `DictConvertibleMixin`).
3. Mantenha os Mixins focados em uma única responsabilidade (Single Responsibility Principle).
4. Utilize sempre `super()` para garantir que a cadeia inteira de inicialização do MRO seja respeitada.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Ignorar a ordem de declaração dos Mixins na lista de superclasses
    # A classe especificada mais à esquerda possui maior precedência no MRO.
    class MixinA:
        def executar(self) -> None:
            print("  MixinA")

    class MixinB:
        def executar(self) -> None:
            print("  MixinB")

    class TesteA(MixinA, MixinB): pass
    class TesteB(MixinB, MixinA): pass

    print("Ordem de execução em TesteA(MixinA, MixinB):")
    TesteA().executar()
    print("Ordem de execução em TesteB(MixinB, MixinA):")
    TesteB().executar()


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o Python resolve o Diamond Problem e qual o algoritmo utilizado?"
A: "O Python resolve o Diamond Problem utilizando o algoritmo C3 Linearization para calcular a Ordem de Resolução de Métodos (MRO).
    Esse algoritmo cria uma lista linearizada de precedência garantindo que:
    1. Subclasses venham antes das superclasses.
    2. A ordem de declaração entre parênteses seja mantida.
    3. Nenhuma classe seja visitada mais de uma vez.
    A ordem final pode ser inspecionada chamando `Classe.mro()`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie dois Mixins `DataHoraCriacaoMixin` e `RepresentacaoDictMixin` e aplique-os em uma classe `ProdutoModel`.
# Exercício 2: Monte uma hierarquia em Diamante (A -> B, C -> D) e imprima o resultado de `D.mro()` explicando a ordem dos elementos.
# Exercício 3: Escreva uma função que receba uma classe e retorne True se ela contiver algum Mixin em sua hierarquia de herança.


def main() -> None:
    print("==========================================================")
    print("  AULA 37: HERANÇA MÚLTIPLA, DIAMANTE E ALGORITMO C3 MRO")
    print("==========================================================")
    demonstrar_fundamentos_mro()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_mro_inconsistente()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 37 executado com sucesso.")


if __name__ == "__main__":
    main()
