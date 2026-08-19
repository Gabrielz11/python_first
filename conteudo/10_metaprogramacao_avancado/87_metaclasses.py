"""
87_metaclasses.py - Metaclasses, type, Interceptação da Criação de Classes e __init_subclass__

Objetivos:
1. Dominar o conceito de Metaclasses em Python ("Classes criam objetos, Metaclasses criam classes").
2. Compreender a metaclasse nativa padrão de todas as classes em Python: `type`.
3. Interceptar e alterar a criação de classes utilizando os métodos `__new__` e `__init__` em metaclasses.
4. Conhecer a alternativa moderna `__init_subclass__` (PEP 487) para personalização leve de subclasses.
5. Construir um Registro Automático de Classes (Class Registry Pattern) e validadores de contrato em tempo de importação.
"""

from typing import Any, Type


# ==========================================================
# 1. CONCEITO DE METACLASSES E TYPE
# ==========================================================
"""
O que é uma Metaclasse?
Em Python, absolutamente tudo e um objeto — incluindo as próprias Classes!
Como qualquer objeto precisa de uma classe para ser instanciado, as Classes precisam de uma METACLASSE para serem criadas.

A Regra de Ouro da Metaprogramação:
- Instância e criada por -> Classe
- Classe e criada por -> Metaclasse (por padrão, a metaclasse nativa `type`)

Hierarquia de Instanciação:
  objeto_x = MinhaClasse()   # MinhaClasse e o tipo de objeto_x
  MinhaClasse = type(...)    # type e a metaclasse de MinhaClasse

Como criar uma Metaclasse Customizada:
Uma metaclasse e qualquer classe que herde diretamente de `type`:
```python
class MinhaMetaclasse(type):
    def __new__(mcs, name, bases, namespace):
        # mcs: a própria metaclasse
        # name: nome da classe sendo criada (str)
        # bases: tupla de classes pai das quais ela herda
        # namespace: dicionário contendo métodos e atributos da classe
        return super().__new__(mcs, name, bases, namespace)
```

Frase Famosa de Tim Peters (Autor do Zen do Python):
"Metaclasses são magia mais profunda do que 99% dos usuários deveriam se preocupar. Se você se pergunta se precisa delas, você não precisa."
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: METACLASSE DE VALIDAÇÃO DE CONTRATO
# ==========================================================
class ValidarContratoMeta(type):
    """Metaclasse que obriga todas as suas subclases a possuírem o atributo 'versao_api'."""

    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> Any:
        # Ignora a validação para a própria classe base abstrata
        if name != "BaseAPIContract":
            if "versao_api" not in namespace:
                raise TypeError(f"A classe '{name}' viola o contrato! Deve definir o atributo de classe 'versao_api'.")
            if not isinstance(namespace["versao_api"], str):
                raise TypeError(f"O atributo 'versao_api' na classe '{name}' deve ser uma string.")

            # Exemplo de transformação metaprogramática: Forçar prefixo nos métodos
            print(f"  [Metaclasse ValidarContratoMeta] Classe '{name}' validada com sucesso em tempo de importação!")

        return super().__new__(mcs, name, bases, namespace)


class BaseAPIContract(metaclass=ValidarContratoMeta):
    """Classe base que aplica a metaclasse de validação."""
    pass


# Subclasse VÁLIDA
class EndpointUsuariosAPI(BaseAPIContract):
    versao_api = "v1.0"


def demonstrar_fundamentos_metaclasses() -> None:
    print("\n--- 1. FUNDAMENTOS: Validação de Classes com Metaclasse ---")
    print(f"Classe EndpointUsuariosAPI criada com versão: {EndpointUsuariosAPI.versao_api}")

    print("\nTentando criar classe inválida sem 'versao_api':")
    try:
        # A validação ocorre no momento em que o Python lê a definição da classe (Tempo de Importação)!
        class EndpointInvalidoAPI(BaseAPIContract):
            pass
    except TypeError as e:
        print(f"  [Erro Metaclasse Capturado]: {e}")


# ==========================================================
# 3. ALTERNATIVA MODERNA: __INIT_SUBCLASS__ (PEP 487)
# ==========================================================
"""
Por que usar `__init_subclass__` (PEP 487 - Python 3.6+)?
Na imensa maioria dos casos onde antes se usava uma Metaclasse simples para registrar ou validar subclasses,
o método especial `__init_subclass__` resolve o problema de forma muito mais simples e sem os conflitos de metaclasse!
"""


class PluginBaseRegistry:
    """Registro Automático de Plugins usando __init_subclass__ (PEP 487)."""

    _plugins_registrados: dict[str, Type["PluginBaseRegistry"]] = {}

    def __init_subclass__(cls, plugin_name: str | None = None, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if plugin_name:
            cls._plugins_registrados[plugin_name] = cls
            print(f"  [__init_subclass__] Plugin '{plugin_name}' registrado automaticamente!")


class PluginPDFExporter(PluginBaseRegistry, plugin_name="pdf"):
    pass


class PluginCSVExporter(PluginBaseRegistry, plugin_name="csv"):
    pass


def demonstrar_init_subclass() -> None:
    print("\n--- 2. ALTERNATIVA LEVE: __init_subclass__ (PEP 487) ---")
    print(f"Plugins registrados no dicionário global: {list(PluginBaseRegistry._plugins_registrados.keys())}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Metaclasses em Frameworks Reais ---")
    print("  Frameworks empresariais como Django ORM (`models.Model`), Pydantic (`BaseModel`) e SQLAlchemy")
    print("  utilizam Metaclasses para converter definições declarativas de campos em tabelas de BD e schemas de validação!")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Execução de Metaclasses:
- Tempo de Execução: Ocorre uma única vez em Tempo de Importação (Import Time) durante a inicialização do programa.
- Overhead de Instanciação: Nulo durante a chamada de métodos runtime.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre a execução do método `__new__` e do método `__init__` dentro de uma Metaclasse?"
A: "1. `__new__(mcs, name, bases, namespace)`: E executado PRIMEIRO. Ele e responsável por CRIAR e ALOCAR o próprio objeto de Classe na memória RAM. É dentro do `__new__` que você pode modificar a tupla de herança (`bases`) ou adicionar/alterar atributos do dicionário (`namespace`) antes da classe existir.
    2. `__init__(cls, name, bases, namespace)`: E executado SEGUNDO, após a classe já ter sido criada pelo `__new__`. Ele e usado apenas para inicializar configurações adicionais do objeto de classe recém-criado."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Crie uma metaclasse `UpperAttributesMeta` que converta todos os nomes de atributos de classe declarados em minúsculas para MAIÚSCULAS no `namespace`.
# Exercício 2 (Intermediário): Implemente um registro de comandos CLI utilizando `__init_subclass__(command_name="...")`.
# Exercício 3 (Desafio / Entrevista): Escreva uma metaclasse `SingletonMetaclass` que garanta a existência de apenas uma instância por classe.


def main() -> None:
    print("==========================================================")
    print("  AULA 87: METACLASSES, TYPE E INTERCEPTAÇÃO DE CLASSES")
    print("==========================================================")
    demonstrar_fundamentos_metaclasses()
    demonstrar_init_subclass()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 87 executado com sucesso.")


if __name__ == "__main__":
    main()
