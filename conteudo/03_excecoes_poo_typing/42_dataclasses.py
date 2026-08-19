"""
42_dataclasses.py - Dataclasses, Imutabilidade (frozen=True) e Métodos Gerados (PEP 557)

Objetivos:
1. Dominar o uso do decorador `@dataclass` introduzido na PEP 557 (Python 3.7+).
2. Compreender os métodos auto-gerados (`__init__`, `__repr__`, `__eq__`, `__hash__`, `__lt__`).
3. Utilizar a função `field()` para configurações avançadas (`default_factory`, `repr=False`, `compare=False`).
4. Criar Objetos de Valor Imutáveis (Immutable Value Objects) utilizando `frozen=True`.
5. Implementar pós-inicialização e validações customizadas utilizando o método `__post_init__`.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são Dataclasses?
Introduzidas na PEP 557, as `@dataclass` fornecem um gerador de boilerplate automatizado para classes
cujo foco principal é armazenar estado (dados).

Benefícios Principais:
1. Eliminação de Boilerplate: O Python gera automaticamente `__init__`, `__repr__` e `__eq__` com base nas Type Annotations.
2. Imutabilidade com `frozen=True`: Transforma a instância em um objeto imutável (hashable), podendo ser usado como chave de dicionário ou elemento de set.
3. `__post_init__`: Permite executar validações ou calcular atributos derivados logo após o `__init__` gerado.
4. Prevenção de Bugs Mutáveis: Bloqueia valores padrão mutáveis (como `lista: list = []`), exigindo `field(default_factory=list)`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: DATACLASS BÁSICA E FROZEN
# ==========================================================
@dataclass(frozen=True)
class EnderecoDTO:
    """DTO de Endereço Imutável (frozen=True)."""

    rua: str
    numero: int
    cidade: str
    cep: str = "00000-000"  # Valor padrão simples


@dataclass
class UsuarioDataclass:
    """Dataclass mutável com pós-inicialização e field(default_factory)."""

    id_usuario: int
    nome: str
    email: str
    tags: list[str] = field(default_factory=list)  # Evita lista mutável compartilhada
    senha_hash: str = field(default=..., repr=False)  # repr=False oculta do __repr__ por segurança
    criado_em: datetime = field(default_factory=datetime.now)
    nome_normalizado: str = field(init=False)  # Não recebido no __init__, calculado no __post_init__

    def __post_init__(self) -> None:
        """Executado automaticamente apos o __init__ gerado."""
        if "@" not in self.email:
            raise ValueError(f"Email invalido: {self.email}")
        self.nome_normalizado = self.nome.strip().lower()


def demonstrar_fundamentos_dataclass() -> None:
    print("\n--- 1. FUNDAMENTOS: @dataclass e __post_init__ ---")

    # Endereço Imutável (frozen)
    end = EnderecoDTO(rua="Av. Paulista", numero=1000, cidade="São Paulo")
    print(f"Endereço Formatado: {end}")

    # Tentativa de alterar atributo em objeto frozen (Dispara FrozenInstanceError)
    try:
        end.numero = 2000  # type: ignore
    except Exception as e:
        print(f"[!] Alteração em frozen=True bloqueada ({type(e).__name__}): {e}")

    # Usuário Dataclass com __post_init__ e repr=False
    usr = UsuarioDataclass(
        id_usuario=101,
        nome=" Gabriel Zilmar ",
        email="gabriel@empresa.com",
        senha_hash="$2b$12$secret_hash_code",
    )

    print(f"\nUsuário (senha_hash oculta pelo repr=False): {usr}")
    print(f"Nome Normalizado via __post_init__: {usr.nome_normalizado!r}")
    print(f"Tags inicializadas via default_factory: {usr.tags}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ORDENAÇÃO AUTOMÁTICA (ORDER=TRUE)
# ==========================================================
@dataclass(order=True)
class ItemEstoque:
    """Dataclass ordenável por prioridade/preço."""

    # O parâmetro order=True utiliza a ordem dos campos na classe para comparar objetos (__lt__)
    preco: float
    nome: str = field(compare=False)  # compare=False ignora o nome na ordenação


def demonstrar_ordenacao_dataclass() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Ordenação com order=True ---")

    i1 = ItemEstoque(preco=150.0, nome="Teclado")
    i2 = ItemEstoque(preco=50.0, nome="Mouse")
    i3 = ItemEstoque(preco=300.0, nome="Monitor")

    itens = [i1, i2, i3]
    itens_ordenados = sorted(itens)

    print("Itens ordenados por preço automaticamente:")
    for item in itens_ordenados:
        print(f"  - R$ {item.preco:.2f}: {item.nome}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
@dataclass
class APIResponsePayload:
    """Payload de resposta padrão para APIs backend."""

    status_code: int
    mensagem: str
    dados: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Response Payload ---")
    response = APIResponsePayload(
        status_code=200,
        mensagem="Sucesso ao recuperar dados",
        dados={"usuario_id": 99},
    )

    print(f"Payload gerado: {response}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: GERAÇÃO DE CÓDIGO
# ==========================================================
"""
Como a Dataclass funciona por baixo dos panos (CPython):
1. O decorador `@dataclass` inspeciona a classe através do dicionário `__annotations__`.
2. O CPython constrói dinamicamente o código Python dos métodos `__init__`, `__repr__`, `__eq__` em formato de string.
3. O CPython compila essas strings para bytecode via `exec()` e insere os métodos no dicionário da classe.
4. Não há nenhum overhead de performance em tempo de execução comparado a escrever os dunders manualmente em CPython.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Geração dos Métodos (Fase de Definição da Classe): Tempo O(F), onde F é o número de campos da dataclass.
- Instanciação de Objetos (`__init__`): Tempo O(F), Espaço O(F).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Escrever __init__, __repr__, __eq__ manualmente repetitivos
    print("[X] Nao-Pythonic (Boilerplate manual extenso):")
    print("  class DTO: def __init__(self, a, b): self.a = a; self.b = b ...")

    # [OK] PYTHONIC: Utilizar @dataclass
    print("\n[OK] Pythonic:")
    print("  @dataclass\n  class DTO:\n      a: int\n      b: str")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. NUNCA utilize atribuições mutáveis padrão como `tags: list = []`. Use `field(default_factory=list)`.
2. Utilize `frozen=True` para Data Transfer Objects (DTOs) e Value Objects que não devam ter seu estado alterado.
3. Utilize `repr=False` no `field()` para atributos com dados sensíveis (senhas, chaves de API, dados pessoais).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar usar valor padrão mutável sem field(default_factory=...)
    try:
        @dataclass
        class ArmadilhaDataclass:
            itens: list = []  # type: ignore # Lança ValueError!
    except ValueError as e:
        print(f"[!] Armadilha 1 (ValueError mutable default em dataclass): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre uma `@dataclass` e uma `NamedTuple` em Python?"
A: "1. Mutabilidade: Por padrão, a `@dataclass` é mutável (pode ser tornada imutável com `frozen=True`). A `NamedTuple` é SEMPRE imutável.
    2. Herança e Tuplas: `NamedTuple` é uma tupla por baixo dos panos (pode ser desempacotada `a, b = obj` e acessada por índice `obj[0]`).
       A `@dataclass` é uma classe normal de Python que não herda de `tuple`.
    3. Recursos: `@dataclass` suporta `__post_init__`, `default_factory` e controle refinado de comparação via `field()`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma dataclass `Cliente` com `id`, `nome`, `email` e `compras: list` usando `default_factory`.
# Exercício 2: Crie uma dataclass `Configuracao` com `frozen=True` contendo `host` e `porta`.
# Exercício 3: Implemente um `__post_init__` em uma dataclass `Triangulo` que valide se a soma de dois lados é maior que o terceiro.


def main() -> None:
    print("==========================================================")
    print("  AULA 42: DATACLASSES, FROZEN=TRUE E MÉTODOS GERADOS")
    print("==========================================================")
    demonstrar_fundamentos_dataclass()
    demonstrar_ordenacao_dataclass()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 42 executado com sucesso.")


if __name__ == "__main__":
    main()
