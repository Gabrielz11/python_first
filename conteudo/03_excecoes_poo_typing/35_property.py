"""
35_property.py - Decoradores @property, @setter, @deleter e Atributos Calculados

Objetivos:
1. Dominar o uso do decorador nativo `@property` para criar getters, setters e deleters idiomáticos.
2. Aplicar o Princípio do Acesso Uniforme (Uniform Access Principle) em POO.
3. Criar atributos calculados em tempo de execução sem armazená-los redundantemente na memória.
4. Adicionar validações de integridade de dados e regras de negócio em atribuições com `@setter`.
5. Prevenir o erro clássico de recursão infinita ao nomear o atributo interno dentro do getter/setter.
"""

from datetime import date


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o decorador @property?
Em Python, o decorador `@property` permite transformar um método de classe em um "atributo somente leitura"
ou associar lógica de validação a acessos e atribuições, mantendo a sintaxe limpa de acesso direto (`objeto.atributo`).

Princípio do Acesso Uniforme:
Em outras linguagens, desenvolvedores costumam criar métodos getters/setters (`get_preco()`, `set_preco()`)
"por precaução" desde o primeiro dia.
Em Python, começamos com atributos públicos simples (`objeto.preco = 10`). Se no futuro precisarmos de validação,
transformamos `preco` em uma `@property` SEM QUEBRAR O CÓDIGO de nenhum cliente que consumia a classe!

Sintaxe dos Decoradores:
- `@property`: Define o Getter (método de leitura).
- `@<atributo>.setter`: Define o Setter (método de escrita com validação).
- `@<atributo>.deleter`: Define o Deleter (método chamado no `del objeto.atributo`).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: GETTER E SETTER COM VALIDAÇÃO
# ==========================================================
class ProdutoComProperty:
    def __init__(self, nome: str, preco_inicial: float) -> None:
        self.nome: str = nome
        self._preco: float = 0.0  # Atributo interno protegido
        self.preco = preco_inicial  # Invoca o setter para validar!

    @property
    def preco(self) -> float:
        """Getter do preço."""
        return self._preco

    @preco.setter
    def preco(self, novo_preco: float) -> None:
        """Setter do preço com validação de regra de negócio."""
        if not isinstance(novo_preco, (int, float)):
            raise TypeError("O preço deve ser um valor numérico.")
        if novo_preco < 0:
            raise ValueError("O preço de um produto não pode ser negativo!")
        self._preco = float(novo_preco)


def demonstrar_fundamentos_property() -> None:
    print("\n--- 1. FUNDAMENTOS: @property e @setter com Validação ---")

    p = ProdutoComProperty("Teclado Mecânico", 250.0)
    print(f"Produto: {p.nome} | Preco lido via @property: R$ {p.preco:.2f}")

    # Atualizando o preço via setter
    p.preco = 300.0
    print(f"Preco atualizado via @setter: R$ {p.preco:.2f}")

    # Tentativa de atribuir preço negativo (Dispara ValueError)
    try:
        p.preco = -50.0
    except ValueError as e:
        print(f"[!] Validação do Setter barrou preço negativo: {e}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ATRIBUTOS CALCULADOS
# ==========================================================
class Funcionario:
    def __init__(self, primeiro_nome: str, sobrenome: str, ano_nascimento: int) -> None:
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    @property
    def nome_completo(self) -> str:
        """Atributo calculado dinamico (sem redundancia de memoria)."""
        return f"{self.primeiro_nome} {self.sobrenome}"

    @property
    def idade_aproximada(self) -> int:
        """Calcula a idade baseada no ano atual."""
        ano_atual = date.today().year
        return ano_atual - self.ano_nascimento


def demonstrar_atributos_calculados() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Atributos Calculados Dinâmicos ---")
    func = Funcionario("Gabriel", "Zilmar", 1990)

    print(f"Nome Completo: {func.nome_completo}")
    print(f"Idade Calculada via @property: {func.idade_aproximada} anos")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class PedidoDomain:
    """Entidade de Pedido com desconto e totalização dinâmica."""

    def __init__(self, id_pedido: int, itens: list[dict[str, float]]) -> None:
        self.id_pedido = id_pedido
        self.itens = itens
        self._percentual_desconto: float = 0.0

    @property
    def percentual_desconto(self) -> float:
        return self._percentual_desconto

    @percentual_desconto.setter
    def percentual_desconto(self, valor: float) -> None:
        if not (0.0 <= valor <= 0.5):  # Máximo de 50% de desconto
            raise ValueError("Desconto deve estar entre 0% e 50%.")
        self._percentual_desconto = valor

    @property
    def subtotal(self) -> float:
        return sum(item["preco"] for item in self.itens)

    @property
    def valor_total(self) -> float:
        return self.subtotal * (1.0 - self._percentual_desconto)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Entidade PedidoDomain ---")
    itens_pedido = [{"preco": 100.0}, {"preco": 200.0}]
    pedido = PedidoDomain(1001, itens_pedido)

    print(f"Subtotal: R$ {pedido.subtotal:.2f}")
    pedido.percentual_desconto = 0.10  # 10% de desconto
    print(f"Valor Total com 10% de Desconto: R$ {pedido.valor_total:.2f}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: DESCRITORES (DESCRIPTORS)
# ==========================================================
"""
Como o @property funciona por baixo dos panos (Descriptor Protocol):
1. Em Python, `@property` é uma classe nativa imbutida que implementa o Protocolo de Descriptor.
2. Quando declaramos `@property def preco(self): ...`, o Python armazena um objeto da classe `property`
   no dicionário da CLASSE (`Classe.__dict__['preco']`).
3. Quando você acessa `instancia.preco`, o CPython intercepta o acesso e invoca o método dunder
   `__get__` do descriptor `property`, que por sua vez executa a sua função getter.
"""


def demonstrar_internamente_descriptor() -> None:
    print("\n--- 4. INTERNO: O objeto property no __dict__ da Classe ---")
    prop_obj = getattr(ProdutoComProperty, "preco")
    print(f"Tipo de ProdutoComProperty.preco: {type(prop_obj)}")
    print(f"O objeto property é um Descriptor? {hasattr(prop_obj, '__get__')}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Leitura de `@property`: Tempo O(1) + Tempo da função getter.
- Escrita via `@setter`: Tempo O(1) + Tempo de validação da função setter.
- Espaço: O(1) [Zero acréscimo de memória por instância].
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Getters e Setters estilo Java
    print("[X] Nao-Pythonic (Métodos manuais get/set):")
    print("  objeto.set_preco(100) -> print(objeto.get_preco())")

    # [OK] PYTHONIC: Atributos diretos com @property
    print("\n[OK] Pythonic (@property):")
    print("  objeto.preco = 100 -> print(objeto.preco)  # Sintaxe natural e limpa!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Mantenha as funções getter `@property` Rápidas e Baratas. Evite chamadas de I/O de rede ou queries pesadas em banco dentro de um getter!
2. O nome do atributo interno protegido (ex: `_preco`) DEVE ser diferente do nome da propriedade (ex: `preco`).
3. Utilize `@property` para expor dados calculados de forma transparente.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Recursão Infinita ao usar o mesmo nome da property no setter
    class RecursaoErrada:
        def __init__(self) -> None:
            self.valor = 10

        @property
        def valor(self) -> int:
            return self.valor  # [!] ERRO: Esqueceu o _ ! Chama a própria property recursivamente!

    try:
        r = RecursaoErrada()
        _ = r.valor
    except AttributeError as e:
        print(f"[!] Armadilha 1 capturada (Esqueceu o setter): {e}")
    except RecursionError as e:
        print(f"[!] Armadilha 1 (RecursionError no getter): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como o decorador `@property` se relaciona com o Princípio do Acesso Uniforme em Python?"
A: "O Princípio do Acesso Uniforme estabelece que todos os serviços oferecidos por um objeto devem ser acessados através de uma sintaxe uniforme.
    Em Python, isso significa que o código cliente pode acessar um atributo simples (`objeto.x`) sem se preocupar se ele é um valor direto armazenado na memória ou um cálculo derivado em runtime.
    O `@property` permite que os desenvolvedores comecem com atributos simples e adicionem validações ou cálculos dinâmicos posteriormente sem quebrar a API pública da classe."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Retangulo` com propriedades `largura` e `altura` (com setters que não permitam valores <= 0) e uma propriedade calculada `area`.
# Exercício 2: Crie uma classe `Termostato` que armazene a temperatura interna em Celsius (`_celsius`), mas ofereça propriedades `@property` para ler e alterar em Fahrenheit.
# Exercício 3: Escreva uma classe com `@deleter` que limpe um log ou reset o estado ao executar `del objeto.propriedade`.


def main() -> None:
    print("==========================================================")
    print("  AULA 35: DECORADORES @PROPERTY, @SETTER E @DELETER")
    print("==========================================================")
    demonstrar_fundamentos_property()
    demonstrar_atributos_calculados()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_descriptor()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 35 executado com sucesso.")


if __name__ == "__main__":
    main()
