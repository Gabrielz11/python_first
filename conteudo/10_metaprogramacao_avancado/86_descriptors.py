"""
86_descriptors.py - Protocolo de Descriptors (__get__, __set__, __delete__, __set_name__) e Validação de Atributos

Objetivos:
1. Dominar o Protocolo de Descriptors (Descriptor Protocol), a ferramenta mais poderosa de reutilização de lógica de atributos em Python.
2. Compreender os métodos do protocolo: `__get__`, `__set__`, `__delete__` e `__set_name__` (PEP 487).
3. Diferenciar Data Descriptors (possuem `__set__`/`__delete__`) de Non-Data Descriptors (possuem apenas `__get__`).
4. Entender como `@property`, `@classmethod` e `@staticmethod` funcionam internamente no CPython através de Descriptors.
5. Aprender a Ordem de Busca de Atributos (Descriptor Lookup Order) e evitar a armadilha de salvar estado no próprio Descriptor.
"""

from typing import Any, Type


# ==========================================================
# 1. CONCEITO DE DESCRIPTORS
# ==========================================================
"""
O que é um Descriptor?
Um Descriptor e um objeto Python que define comportamentos customizados de acesso a atributos
implementando um ou mais dos métodos do Protocolo de Descriptors na sua classe:

1. `__get__(self, instance, owner)`: Chamado ao LER o atributo.
2. `__set__(self, instance, value)`: Chamado ao ATRIBUIR valor ao atributo.
3. `__delete__(self, instance)`: Chamado ao DELETAR o atributo.
4. `__set_name__(self, owner, name)` (PEP 487 - Python 3.6+): Invocado automaticamente na criação da classe cliente para capturar o nome da variável.

Tipos de Descriptors:
- Data Descriptor: Implementa pelo menos `__set__` ou `__delete__`. Possui a MAIOR PRECEDÊNCIA na ordem de busca de atributos!
- Non-Data Descriptor: Implementa apenas `__get__` (ex: funções normais e `@staticmethod`).

Ordem de Busca de Atributos (Descriptor Lookup Order):
1. Data Descriptor na classe (se existir).
2. Dicionário da Instância (`instance.__dict__`).
3. Non-Data Descriptor na classe (se existir).
4. Dicionário da Classe (`Class.__dict__`).
5. `__getattr__()` (fallback se não encontrou nada).
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: VALIDATING DESCRIPTOR COM PEP 487
# ==========================================================
class CampoTextoValidado:
    """Data Descriptor para validação de tipo string com tamanho mínimo usando __set_name__."""

    def __init__(self, tamanho_minimo: int = 1) -> None:
        self.tamanho_minimo = tamanho_minimo
        self.name_in_instance = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        # PEP 487: Chamado automaticamente na compilação da classe cliente!
        self.name_in_instance = name

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self  # Acesso via classe (ex: Usuario.nome) retorna o próprio descriptor
        # Lê o valor diretamente do __dict__ da instância para evitar estado compartilhado!
        return instance.__dict__.get(self.name_in_instance)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError(f"O campo '{self.name_in_instance}' deve ser uma string, mas recebeu {type(value).__name__}.")
        if len(value) < self.tamanho_minimo:
            raise ValueError(f"O campo '{self.name_in_instance}' deve ter pelo menos {self.tamanho_minimo} caracteres.")

        # Guarda o valor no __dict__ da instância individual
        instance.__dict__[self.name_in_instance] = value


class NumeroPositivoValidado:
    """Data Descriptor para validação de números positivos."""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self.name_in_instance = name

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.name_in_instance)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"O campo '{self.name_in_instance}' deve ser um número maior que zero.")
        instance.__dict__[self.name_in_instance] = value


# ==========================================================
# 3. USO DOS DESCRIPTORS EM CLASSES DE NEGÓCIO
# ==========================================================
class ProdutoModel:
    # Aplicando os Descriptors de forma declarativa e reutilizável
    nome = CampoTextoValidado(tamanho_minimo=3)
    preco = NumeroPositivoValidado()

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


def demonstrar_fundamentos_descriptors() -> None:
    print("\n--- 1. FUNDAMENTOS: ProdutoModel com Descriptors ---")

    p1 = ProdutoModel(nome="Notebook Pro", preco=4500.0)
    print(f"Produto P1: {p1.nome} - R$ {p1.preco:.2f}")

    try:
        p2 = ProdutoModel(nome="Ab", preco=100.0)  # Nome curto demais!
    except ValueError as e:
        print(f"  [Validação Descriptor Sucesso]: {e}")

    try:
        p3 = ProdutoModel(nome="Teclado", preco=-50.0)  # Preço negativo!
    except ValueError as e:
        print(f"  [Validação Descriptor Sucesso]: {e}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 2. APLICAÇÃO BACKEND: Como o @property usa Descriptors ---")
    print("  Em Python, o decorador `@property` nada mais e do que uma classe que implementa o Protocolo de Descriptors!")
    print("  Quando você escreve `@property`, o Python instancia um Data Descriptor contendo os métodos fget, fset e fdel.")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Complexidade:
- Invocação de `__get__` / `__set__` em Descriptors: Tempo O(1), Espaço O(1).
- Armazenamento: Gravar no `instance.__dict__` consome Espaço O(1) adicional por instância.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a armadilha fatal ao armazenar o valor do atributo dentro de uma variável `self.valor` no próprio objeto Descriptor?"
A: "O objeto Descriptor e instanciado apenas UMA vez no nível de CLASSE (compartilhado por todas as instâncias da classe cliente).
    Se você armazenar o valor em `self.valor` dentro do Descriptor, TODAS as instâncias da classe cliente passarão a compartilhar e sobrescrever o mesmo valor entre si!
    A forma correta e SEMPRE armazenar o valor dentro do dicionário da instância individual (`instance.__dict__[self.name_in_instance]`)."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Crie um Descriptor `EmailValido` que valide se o valor atribuído contém um `@` e um ponto `.`.
# Exercício 2 (Intermediário): Crie um Non-Data Descriptor `LazyProperty` que calcule o valor de uma função pesada apenas na primeira leitura e salve o resultado no `instance.__dict__`.
# Exercício 3 (Desafio / Entrevista): Escreva uma didática recriação do decorador `@property` criando uma classe `MinhaProperty` que implemente `__get__` e `__set__`.


def main() -> None:
    print("==========================================================")
    print("  AULA 86: PROTOCOLO DE DESCRIPTORS (__GET__, __SET__, __SET_NAME__)")
    print("==========================================================")
    demonstrar_fundamentos_descriptors()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 86 executado com sucesso.")


if __name__ == "__main__":
    main()
