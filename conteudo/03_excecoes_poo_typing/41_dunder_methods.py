"""
41_dunder_methods.py - Sobrecarga de Operadores e Métodos Mágicos (Dunder Methods)

Objetivos:
1. Dominar o uso dos métodos mágicos (Dunder Methods) para personalizar comportamentos de operadores em classes.
2. Implementar métodos de comparação (`__eq__`, `__lt__`) e utilizar `@functools.total_ordering`.
3. Implementar métodos aritméticos (`__add__`, `__sub__`, `__radd__`) com tratamento gracioso via `NotImplemented`.
4. Criar contêineres customizados com suporte a indexação (`__getitem__`), pertencimento (`__contains__`) e tamanho (`__len__`).
5. Tornar instâncias chamáveis como funções através do método `__call__`.
"""

from functools import total_ordering
from typing import Any, Iterator


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Métodos Dunder (Magic Methods)?
Métodos dunder (Double Underscore) são métodos especiais que começam e terminam com dois sublinhados (ex: `__init__`, `__str__`).
Eles definem a interface do Python para a sobrecarga de operadores e integração de tipos customizados com as funções nativas.

Categorias Principais:
1. Comparação: `__eq__` (==), `__lt__` (<), `__le__` (<=), `__gt__` (>), `__ge__` (>=).
2. Aritmética: `__add__` (+), `__sub__` (-), `__mul__` (*), `__radd__` (adição reversa).
3. Contêiner/Coleção: `__len__` (len()), `__getitem__` (obj[key]), `__setitem__`, `__contains__` (in).
4. Invocação de Função: `__call__` (permite executar o objeto como `objeto()`).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ARITMÉTICA E COMPARAÇÃO (MONEY VALUE OBJECT)
# ==========================================================
@total_ordering  # Gera automaticamente __le__, __gt__, __ge__ se você definir __eq__ e __lt__
class Dinheiro:
    def __init__(self, quantia: float, moeda: str = "BRL") -> None:
        self.quantia = round(float(quantia), 2)
        self.moeda = moeda.upper()

    def __repr__(self) -> str:
        return f"Dinheiro({self.quantia:.2f}, '{self.moeda}')"

    def __eq__(self, outro: Any) -> bool:
        if not isinstance(outro, Dinheiro):
            return False
        return self.quantia == outro.quantia and self.moeda == outro.moeda

    def __lt__(self, outro: Any) -> bool:
        if not isinstance(outro, Dinheiro):
            return NotImplemented
        if self.moeda != outro.moeda:
            raise ValueError(f"Não e possível comparar moedas diferentes: {self.moeda} vs {outro.moeda}")
        return self.quantia < outro.quantia

    def __add__(self, outro: Any) -> "Dinheiro":
        if isinstance(outro, (int, float)):
            return Dinheiro(self.quantia + outro, self.moeda)
        if isinstance(outro, Dinheiro):
            if self.moeda != outro.moeda:
                raise ValueError("Não e possível somar moedas diferentes!")
            return Dinheiro(self.quantia + outro.quantia, self.moeda)
        return NotImplemented

    def __radd__(self, outro: Any) -> "Dinheiro":
        """Permite somas como sum([Dinheiro(10), Dinheiro(20)]) começando do int 0."""
        return self.__add__(outro)


def demonstrar_fundamentos_dunder() -> None:
    print("\n--- 1. FUNDAMENTOS: Comparação e Aritmética Customizada ---")

    d1 = Dinheiro(100.50, "BRL")
    d2 = Dinheiro(50.25, "BRL")
    d3 = Dinheiro(100.50, "BRL")

    print(f"d1: {d1} | d2: {d2}")
    print(f"d1 == d3? {d1 == d3} (__eq__)")
    print(f"d1 > d2? {d1 > d2} (__lt__ via total_ordering)")

    soma = d1 + d2
    print(f"Soma d1 + d2: {soma} (__add__)")

    # Testando sum() com __radd__
    total_lista = sum([Dinheiro(10), Dinheiro(20), Dinheiro(30)])
    print(f"Soma de lista via sum(): {total_lista}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PIPELINE COM __CALL__ E COLEÇÃO
# ==========================================================
class ValidadorFiltro:
    """Instância chamável via __call__ agindo como uma função."""

    def __init__(self, limite_minimo: float) -> None:
        self.limite_minimo = limite_minimo

    def __call__(self, valor: float) -> bool:
        return valor >= self.limite_minimo


class ColecaoCarrinho:
    """Coleção customizada implementando protocolo de contêiner."""

    def __init__(self) -> None:
        self.itens: list[dict[str, Any]] = []

    def adicionar(self, item: dict[str, Any]) -> None:
        self.itens.append(item)

    def __len__(self) -> int:
        return len(self.itens)

    def __getitem__(self, index: int) -> dict[str, Any]:
        return self.itens[index]

    def __contains__(self, nome_item: Any) -> bool:
        return any(i["nome"] == nome_item for i in self.itens)


def demonstrar_call_e_colecao() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: __call__ e Container Dunders ---")

    # Objeto chamável (__call__)
    filtro_100 = ValidadorFiltro(limite_minimo=100.0)
    print(f"filtro_100(150.0) -> {filtro_100(150.0)}")
    print(f"filtro_100(50.0) -> {filtro_100(50.0)}")

    # Container dunders (__len__, __getitem__, __contains__)
    carrinho = ColecaoCarrinho()
    carrinho.adicionar({"nome": "Mouse", "preco": 80.0})
    carrinho.adicionar({"nome": "Monitor", "preco": 1200.0})

    print(f"Tamanho do carrinho len(): {len(carrinho)}")
    print(f"Acesso por indice carrinho[0]: {carrinho[0]}")
    print(f"'Monitor' in carrinho? {'Monitor' in carrinho}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class MiddlewaresPipeline:
    """Pipeline de execução de middlewares usando __call__."""

    def __init__(self) -> None:
        self.handlers: list[Any] = []

    def registrar(self, handler: Any) -> None:
        self.handlers.append(handler)

    def __call__(self, payload: dict[str, Any]) -> dict[str, Any]:
        for h in self.handlers:
            payload = h(payload)
        return payload


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Pipeline Callable ---")

    def middleware_uppercase(data: dict[str, Any]) -> dict[str, Any]:
        data["msg"] = data["msg"].upper()
        return data

    def middleware_add_timestamp(data: dict[str, Any]) -> dict[str, Any]:
        data["ts"] = "2026-08-19"
        return data

    pipeline = MiddlewaresPipeline()
    pipeline.registrar(middleware_uppercase)
    pipeline.registrar(middleware_add_timestamp)

    res = pipeline({"msg": "nova mensagem de webhook"})
    print(f"Payload processado no pipeline chamavel: {res}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: NOTIMPLEMENTED VS TYPEERROR
# ==========================================================
"""
Como o CPython lida com o retorno de `NotImplemented`:
1. Quando executamos `a + b`, o Python primeiro tenta chamar `a.__add__(b)`.
2. Se `a.__add__(b)` retornar a constante especial `NotImplemented` (e NÃO lançar um TypeError!),
   o CPython tenta a operação reversa chamando `b.__radd__(a)`.
3. Se `b.__radd__(a)` também retornar `NotImplemented`, o CPython finalmente lança um `TypeError: unsupported operand type(s)`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Métodos dunder de operadores (`__eq__`, `__add__`): Dependem da implementação interna -> Tempo O(1), Espaço O(1).
- `__getitem__` em listas envelopadas: Tempo O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Lançar TypeError diretamente dentro do método __add__
    print("[X] Nao-Pythonic (Lançar TypeError em __add__):")
    print("  def __add__(self, other): raise TypeError()  # Impede a tentativa do __radd__ do segundo operando!")

    # [OK] PYTHONIC: Retornar a constante nativa NotImplemented
    print("\n[OK] Pythonic:")
    print("  def __add__(self, other): return NotImplemented  # Permite o fallback gracioso para __radd__!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize `@functools.total_ordering` para economizar código ao implementar comparações (`__eq__` + `__lt__`).
2. NUNCA lance `TypeError` dentro de métodos aritméticos (`__add__`, `__sub__`). Retorne a constante `NotImplemented`.
3. Utilize `__call__` para classes que mantêm estado de configuração e se comportam como funções (ex: Decoradores, Pipelines).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Confundir a constante `NotImplemented` com a exceção `NotImplementedError`
    # - `NotImplemented`: É um valor Singleton retornado pelos dunders de operador.
    # - `NotImplementedError`: É uma exceção lançada quando um método abstrato não foi implementado.
    print("[!] Cuidado: Retorne 'NotImplemented' (Singleton), NÃO lance 'NotImplementedError' (Exception) em operadores aritméticos!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre a constante `NotImplemented` e a exceção `NotImplementedError` em Python?"
A: "1. `NotImplemented` é um valor especial (objeto singleton) que deve ser RETORNADO por métodos dunder de operadores
       (como `__add__`, `__eq__`) para indicar que o tipo do segundo argumento não é suportado por aquele método.
       Isso avisa o CPython para tentar a chamada refletida no segundo objeto (`__radd__`).
    2. `NotImplementedError` é uma EXCEÇÃO que deve ser LANÇADA (`raise`) para indicar que uma função ou método abstrato não foi implementado pela subclasse."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Vetor2D(x, y)` que suporte adição de vetores `v1 + v2` via `__add__` e multiplicação por escalar `v1 * 3` via `__mul__`.
# Exercício 2: Implemente a comparação de igualdade `__eq__` e menor que `__lt__` em `Vetor2D` para calcular a magnitude do vetor.
# Exercício 3: Crie uma classe `ContadorExecucoes` que implemente `__call__` para contar quantas vezes ela foi invocada.


def main() -> None:
    print("==========================================================")
    print("  AULA 41: SOBRECARGA DE OPERADORES E DUNDER METHODS")
    print("==========================================================")
    demonstrar_fundamentos_dunder()
    demonstrar_call_e_colecao()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 41 executado com sucesso.")


if __name__ == "__main__":
    main()
