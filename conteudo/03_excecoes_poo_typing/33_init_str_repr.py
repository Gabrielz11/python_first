"""
33_init_str_repr.py - Representação de Objetos com __init__, __str__ e __repr__

Objetivos:
1. Dominar o papel dos métodos dunder `__init__`, `__str__` e `__repr__` em classes Python.
2. Compreender a diferença fundamental entre `__str__` (voltado para o usuário final) e `__repr__` (inequívoco para desenvolvedores/debug).
3. Entender a regra de fallback do CPython quando `__str__` não está definido (`__str__` recai para `__repr__`).
4. Aplicar boas práticas de segurança ao ocultar dados sensíveis (senhas/PII) na representação de texto.
5. Desenvolver representações limpas de DTOs e entidades para sistemas de logs em produção.
"""


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são __str__ e __repr__?
São dois métodos dunder (double underscore) cruciais que definem como um objeto é convertido para string:

1. __str__(self) -> str:
   - Objetivo: Representação legível e informal para o USUÁRIO FINAL.
   - Chamado por: `str(obj)`, `print(obj)`, f-strings `{obj}`.

2. __repr__(self) -> str:
   - Objetivo: Representação inequívoca, formal e técnica para o DESENVOLVEDOR (Debugging/REPL).
   - Idealmente, a string retornada pelo `__repr__` deve parecer um código Python válido que consiga recriar o objeto:
     `eval(repr(obj)) == obj` (quando praticável).
   - Chamado por: `repr(obj)`, ao inspecionar objetos dentro de listas/dicionários, ou no REPL do terminal.

Regra de Fallback:
Se uma classe implementar apenas `__repr__`, o Python usará o `__repr__` como fallback para o `__str__`.
Se uma classe implementar apenas `__str__`, inspecionar o objeto no REPL ou dentro de uma lista continuará mostrando o ponteiro padrão `<... object at 0x...>`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: IMPLEMENTANDO STR E REPR
# ==========================================================
class Produto:
    def __init__(self, sku: str, nome: str, preco: float) -> None:
        self.sku = sku
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        # User-facing: bonito para o cliente
        return f"{self.nome} - R$ {self.preco:.2f}"

    def __repr__(self) -> str:
        # Developer-facing: inequívoco para debug
        return f"Produto(sku={self.sku!r}, nome={self.nome!r}, preco={self.preco!r})"


def demonstrar_fundamentos_str_repr() -> None:
    print("\n--- 1. FUNDAMENTOS: Diferença entre __str__ e __repr__ ---")

    p = Produto("SKU-994", "Notebook Gamer", 4500.00)

    # Chamada explícita de str() -> invoca __str__
    print(f"Versao str(p) [User]: {str(p)}")

    # Chamada explícita de repr() -> invoca __repr__
    print(f"Versao repr(p) [Dev]: {repr(p)}")

    # Objeto dentro de uma lista sempre usa __repr__
    catalogo = [p]
    print(f"Inspecionando dentro de lista: {catalogo}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: SEGURANÇA E MASCARAMENTO DE PII
# ==========================================================
class UsuarioAutenticado:
    def __init__(self, user_id: int, email: str, senha_hash: str) -> None:
        self.user_id = user_id
        self.email = email
        self.senha_hash = senha_hash  # Dado sensível!

    def __repr__(self) -> str:
        # MASCARAMENTO DE DADOS SENSÍVEIS (PII Security Best Practice)
        return (
            f"UsuarioAutenticado(user_id={self.user_id!r}, "
            f"email={self.email!r}, senha_hash='***REDACTED***')"
        )


def demonstrar_mascaramento_seguranca() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Mascaramento de Senhas em Logs ---")
    usr = UsuarioAutenticado(101, "gabriel@empresa.com", "$2b$12$eImiTXuWVfxh...")
    print(f"Log de Debug seguro: {usr!r}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class LogTracebackContext:
    """DTO para enriquecimento de contextos de logs em microsserviços."""

    def __init__(self, correlation_id: str, service_name: str, status_code: int) -> None:
        self.correlation_id = correlation_id
        self.service_name = service_name
        self.status_code = status_code

    def __repr__(self) -> str:
        return (
            f"<{self.service_name} correlation_id={self.correlation_id} "
            f"status={self.status_code}>"
        )


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Contexto de Log de Microsserviços ---")
    ctx = LogTracebackContext("req-abc-123", "OrderService", 200)
    print(f"[LOG] Requisicao processada: {ctx!r}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: SLOTS CPYTON
# ==========================================================
"""
Como o CPython despacha `str()` e `repr()`:
1. No nível da C-API do CPython (`typeobject.c`), a struct `PyTypeObject` possui os ponteiros de função `tp_str` e `tp_repr`.
2. Quando `repr(obj)` é invocado, o CPython chama a função C apontada por `tp_repr`.
3. Quando `str(obj)` é invocado:
   - O CPython verifica se `tp_str` está definido.
   - Se `tp_str` não foi sobrescrito pela subclasse, o CPython redireciona a chamada para `tp_repr`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `__str__` / `__repr__`:
  - Tempo: O(1) na maioria dos casos (depende da complexidade da interpolação de strings dos atributos).
  - Espaço: O(K), onde K é o tamanho em caracteres da string gerada.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Implementar apenas __str__ e deixar o __repr__ padrão feio
    print("[X] Nao-Pythonic (Sem __repr__):")
    print("  Exibe: <__main__.Classe object at 0x0000020A...>")

    # [OK] PYTHONIC: Priorizar __repr__ inequívoco primeiro
    print("\n[OK] Pythonic:")
    print("  Implementar __repr__ garante uma boa visualização em REPL, listas, logs e print()!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Regra de Ouro: Sempre implemente `__repr__` em todas as suas classes de modelo. Se precisar de uma representação amigável ao usuário final, implemente também o `__str__`.
2. Utilize a notação `!r` dentro de f-strings para aplicar `repr()` automaticamente aos atributos: `f"{self.nome!r}"`.
3. NUNCA exponha credenciais, chaves privadas ou senhas nos retornos de `__str__` ou `__repr__`.
4. Os métodos `__str__` e `__repr__` devem OBRIGATORIAMENTE retornar objetos do tipo `str`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Retornar algo que não seja string em __str__ ou __repr__
    class ClasseErrada:
        def __str__(self) -> str:
            return 12345  # type: ignore # Lança TypeError!

    try:
        str(ClasseErrada())
    except TypeError as e:
        print(f"[!] Armadilha 1 (TypeError: __str__ returned non-string): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre os métodos `__str__` e `__repr__` em Python e qual a regra de fallback entre eles?"
A: "1. `__str__` visa legibilidade informal para o usuário final, acionado por `str()` e `print()`.
    2. `__repr__` visa ser uma representação técnica e inequívoca para o desenvolvedor (debug/REPL).
    3. Regra de Fallback: Se `__str__` não for definido, o Python automaticamente usa o `__repr__`.
       No entanto, se `__repr__` não for definido, o Python NÃO usa o `__str__` para exibições técnicas (como dentro de listas),
       exibindo apenas a representação padrão do CPython `<... object at 0x...>`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Livro` com `titulo`, `autor` e `paginas`. Implemente `__str__` e `__repr__`.
# Exercício 2: Crie uma classe `TransacaoBancaria` que mascare o número da conta no `__repr__` exibindo apenas os últimos 4 dígitos.
# Exercício 3: Escreva uma função que receba uma lista de objetos customizados e imprima a diferença de saída entre `print([obj])` e `for o in lista: print(o)`.


def main() -> None:
    print("==========================================================")
    print("  AULA 33: REPRESENTAÇÃO DE OBJETOS COM STR E REPR")
    print("==========================================================")
    demonstrar_fundamentos_str_repr()
    demonstrar_mascaramento_seguranca()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 33 executado com sucesso.")


if __name__ == "__main__":
    main()
