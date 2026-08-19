"""
85_getattr_getattribute.py - Interceptação de Atributos, __getattr__, __getattribute__ e __setattr__

Objetivos:
1. Dominar os métodos especiais de Interceptação Dinâmica de Atributos (`__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`).
2. Diferenciar a invocação de `__getattr__` (executado APENAS se o atributo NÃO for encontrado) da invocação de `__getattribute__` (executado para TODAS as buscas).
3. Prevenir a armadilha fatal de Reculsão Infinita (Stack Overflow) ao utilizar `__getattribute__` e `__setattr__`.
4. Utilizar `super().__getattribute__()` e `object.__setattr__()` para acesso seguro à memória do objeto.
5. Construir Proxies Dinâmicos para clientes de API e mecanismos de Lazy Loading.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO DE INTERCEPTAÇÃO DE ATRIBUTOS
# ==========================================================
"""
Como o Python resolve a busca de um atributo (`objeto.nome`):
1. Chamada de `__getattribute__(self, name)`:
   - Invocado incondicionalmente para QUALQUER acesso a atributo em uma classe.
   - Se encontrar o atributo no `__dict__` da instância, na classe ou em descriptors, ele o retorna.
2. Chamada de `__getattr__(self, name)`:
   - Invocado APENAS como FALLBACK quando o atributo pedindo NÃO EXISTE no `__dict__` da instância nem na hierarquia de classes.

A Armadilha da Recursão Infinita:
- Dentro de `__getattribute__(self, name)`, acessar `self.qualquer_coisa` ou `self.__dict__` invoca `__getattribute__` novamente, gerando um loop infinito!
- Correção: Usar sempre `super().__getattribute__(name)`.
- Dentro de `__setattr__(self, name, value)`, atribuições do tipo `self.attr = val` geram loop infinito!
- Correção: Usar sempre `object.__setattr__(self, name, value)` ou `self.__dict__[name] = value`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: __GETATTR__ VS __GETATTRIBUTE__
# ==========================================================
class DynamicConfigFallback:
    """Demonstração de __getattr__ como fallback para atributos inexistentes."""

    def __init__(self) -> None:
        self.host = "localhost"

    def __getattr__(self, name: str) -> Any:
        # Invocado APENAS para atributos inexistentes (ex: porta, timeout)
        print(f"  [__getattr__ Fallback] Atributo '{name}' não existe fisicamente. Retornando valor padrão.")
        return f"DEFAULT_{name.upper()}"


class AuditedAttributeTracker:
    """Demonstração de __getattribute__ para interceptação incondicional e auditoria."""

    def __init__(self, usuario: str) -> None:
        object.__setattr__(self, "usuario", usuario)
        object.__setattr__(self, "acessos", 0)

    def __getattribute__(self, name: str) -> Any:
        # Usamos super().__getattribute__ para evitar recursão infinita!
        acessos_atuais = super().__getattribute__("acessos")
        if name != "acessos":
            object.__setattr__(self, "acessos", acessos_atuais + 1)
            print(f"  [Audit __getattribute__] Acesso ao atributo '{name}' registrado.")
        return super().__getattribute__(name)


def demonstrar_fundamentos_atributos() -> None:
    print("\n--- 1. FUNDAMENTOS: __getattr__ vs __getattribute__ ---")

    # 1. __getattr__
    cfg = DynamicConfigFallback()
    print(f"Acesso a 'host' existente (não chama __getattr__): {cfg.host}")
    print(f"Acesso a 'port' inexistente (chama __getattr__): {cfg.port}")

    # 2. __getattribute__
    print("\n2. Auditoria com __getattribute__:")
    user = AuditedAttributeTracker("Gabriel")
    _ = user.usuario
    print(f"Total de acessos registrados via auditoria: {user.acessos}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PROXY DE API DINÂMICO
# ==========================================================
class DynamicAPIClientProxy:
    """Proxy dinâmico que converte chamadas de métodos inexistentes em rotas de API HTTP."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def __getattr__(self, name: str) -> Any:
        # Converte client.get_users() em chamada da rota '/get_users'
        def rota_dinamica(*args: Any, **kwargs: Any) -> dict[str, Any]:
            endpoint = f"{self.base_url}/{name}"
            print(f"  [API Proxy] Disparando requisição HTTP GET para: {endpoint} com args={args}")
            return {"status": 200, "url": endpoint, "data": "payload_simulado"}

        return rota_dinamica


def demonstrar_proxy_api() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Dynamic API Client Proxy ---")
    client = DynamicAPIClientProxy("https://api.empresa.com/v1")

    # Métodos get_users e get_orders NÃO foram definidos fisicamente na classe!
    res1 = client.get_users(limite=10)
    res2 = client.get_orders(id=99)

    print(f"Resultado do endpoint dinâmico 1: {res1}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Dynamic Attributes in ORMs ---")
    print("  ORMs como Django ORM e SQLAlchemy utilizam __getattr__ para carregar relacionamentos de forma perezosa (Lazy Loading)!")


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL (RESUMO)
# ==========================================================
"""
Análise de Complexidade:
- Interceptação com `__getattr__`: Tempo O(1) [Executado apenas na falha de dicionário].
- Interceptação com `__getattribute__`: Adiciona overhead O(1) em TODAS as buscas de atributos da classe.
"""


# ==========================================================
# 6. PERGUNTAS DE ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre os métodos mágicos `__getattr__` e `__getattribute__` e como evitar recursão infinita?"
A: "1. `__getattr__(self, name)` e o método de fallback: e chamado APENAS se o atributo pesquisado NÃO for encontrado no `__dict__` da instância nem na classe.
    2. `__getattribute__(self, name)` e o interceptador incondicional: e executado para TODAS as buscas de atributos.
    3. Prevenção de Recursão Infinita: Dentro de `__getattribute__`, nunca acesse `self.atributo` diretamente. Utilize sempre `super().__getattribute__(name)` ou `object.__getattribute__(self, name)`."
"""


# ==========================================================
# 7. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1 (Básico): Escreva uma classe `DicionarioObjeto` que permita acessar chaves de dicionário usando sintaxe de ponto (ex: `d.nome` em vez de `d['nome']`) via `__getattr__`.
# Exercício 2 (Intermediário): Crie uma classe `ApenasLeitura` que impeça a modificação de qualquer atributo disparando `AttributeError` dentro de `__setattr__`.
# Exercício 3 (Desafio / Entrevista): Implemente um gerador de rotas encadeadas estilo `api.v1.users.get()` usando `__getattr__`.


def main() -> None:
    print("==========================================================")
    print("  AULA 85: INTERCEPTAÇÃO DE ATRIBUTOS (__GETATTR__ E __GETATTRIBUTE__)")
    print("==========================================================")
    demonstrar_fundamentos_atributos()
    demonstrar_proxy_api()
    demonstrar_aplicacao_backend()
    print("\n[Concluido] Arquivo 85 executado com sucesso.")


if __name__ == "__main__":
    main()
