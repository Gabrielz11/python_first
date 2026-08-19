"""
18_python_idiomatico.py - Código Pythonic, Filosofia PEP 20, EAFP vs LBYL e Truthiness

Objetivos:
1. Compreender a filosofia do código "Pythonic" fundamentada no Zen do Python (PEP 20).
2. Dominar a diferença técnica e prática entre EAFP (Easier to Ask Forgiveness) e LBYL (Look Before You Leap).
3. Utilizar o sistema de Truthiness e Falsiness nativo do Python de forma limpa e expressiva.
4. Aplicar padrões idiomáticos em pipelines de dados e controladores de backend.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é código Pythonic?
Código Pythonic é aquele que não apenas executa uma tarefa corretamente, mas o faz utilizando
as convenções, idiomatismos e construções projetadas para a linguagem Python. Segue os princípios
da PEP 20 (The Zen of Python), priorizando legibilidade, simplicidade e clareza sobre truques obscuros.

Dois paradigmas fundamentais de controle de fluxo em programação:

1. LBYL (Look Before You Leap):
   Verifica pré-condições explicitamente antes de executar uma ação.
   Exemplo: if "chave" in dicionario: valor = dicionario["chave"]
   Útil quando a checagem é rápida e o cenário de ausência é muito comum.

2. EAFP (Easier to Ask for Forgiveness than Permission):
   Assume que a operação vai dar certo e trata exceções se falhar.
   É a abordagem preferida e fortemente idiomática em Python.
   Exemplo: try: valor = dicionario["chave"] except KeyError: ...
   Evita race conditions (como TOCTOU - Time of Check to Time of Use) em I/O e concorrência.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: EAFP VS LBYL
# ==========================================================
def demonstrar_eafp_vs_lbyl() -> None:
    print("\n--- 1. FUNDAMENTOS: EAFP VS LBYL ---")
    payload: dict[str, Any] = {"usuario_id": 101, "perfil": "admin"}

    # Approach LBYL (Look Before You Leap)
    if "email" in payload:
        email_lbyl = payload["email"]
    else:
        email_lbyl = "nao_informado@sistema.com"
    print(f"[LBYL] Email extraido: {email_lbyl}")

    # Approach EAFP (Easier to Ask for Forgiveness than Permission)
    try:
        email_eafp = payload["email"]
    except KeyError:
        email_eafp = "nao_informado@sistema.com"
    print(f"[EAFP] Email extraido: {email_eafp}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: TRUTHINESS E FALSINESS
# ==========================================================
def demonstrar_truthiness() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Truthiness Nativismo ---")

    # Valores considerados FALSY em Python:
    # None, False, 0, 0.0, "", [], (), {}, set(), range(0)
    valores_testados: list[Any] = [None, 0, "", [], {"status": "ok"}, [1, 2, 3]]

    for val in valores_testados:
        # Maniera Pythonic de testar se a coleção/valor está preenchida
        if val:
            print(f"Valor {val!r} -> AVALIADO COMO TRUTHY")
        else:
            print(f"Valor {val!r} -> AVALIADO COMO FALSY")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ConfiguracaoServico:
    """Simula um leitor de configuração resiliente de backend usando EAFP."""

    def __init__(self, fonte_dados: dict[str, str]) -> None:
        self._fonte = fonte_dados

    def obter_porta() -> int:
        raise NotImplementedError

    def obter_parametro(self, chave: str, padrao: Any) -> Any:
        try:
            # Tenta conversão direta
            valor_raw = self._fonte[chave]
            return int(valor_raw) if valor_raw.isdigit() else valor_raw
        except (KeyError, ValueError):
            # Fallback seguro via EAFP
            return padrao


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Parser Resiliente EAFP ---")
    env_vars = {"PORTA": "8080", "TIMEOUT": "invalido"}
    config = ConfiguracaoServico(env_vars)

    porta = config.obter_parametro("PORTA", 3000)
    timeout = config.obter_parametro("TIMEOUT", 30)
    db_host = config.obter_parametro("DB_HOST", "localhost")

    print(f"Porta configurada: {porta} (tipo {type(porta).__name__})")
    print(f"Timeout configurado (fallback aplicado): {timeout}")
    print(f"Host do Banco: {db_host}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE
# ==========================================================
"""
Como o Python avalia a Truthiness de um objeto:
1. O interpretador CPython chama o método dunder `obj.__bool__()`.
2. Se `__bool__()` não estiver definido na classe do objeto, o CPython tenta chamar `obj.__len__()`.
3. Se `__len__()` retornar 0, o objeto é avaliado como False; se maior que 0, como True.
4. Se nem `__bool__` nem `__len__` existirem, a instância do objeto customizado é avaliada como True por padrão.

Custo do try/except (EAFP em CPython 3.11+):
- Nas versões modernas do Python (Zero-Cost Exception Handling), o bloco `try` que NÃO lança exceção
  tem custo nulo (0 ns adicionais).
- Apenas quando a exceção ocorre (caminho triste) há o custo de montar o traceback.
"""


def demonstrar_internamente() -> None:
    print("\n--- 4. COMO FUNCIONA INTERNAMENTE: __bool__ e __len__ ---")

    class SacolaCompras:
        def __init__(self, itens: list[str]) -> None:
            self.itens = itens

        def __len__(self) -> int:
            return len(self.itens)

    sacola_vazia = SacolaCompras([])
    sacola_cheia = SacolaCompras(["Notebook", "Mouse"])

    print(f"Sacola vazia é avaliada como: {bool(sacola_vazia)} (via __len__ == 0)")
    print(f"Sacola cheia é avaliada como: {bool(sacola_cheia)} (via __len__ > 0)")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Complexidade de Operações Idiomáticas:
- Avaliação de Truthiness de coleções nativas (`if lista:`): O(1) de tempo e O(1) de espaço.
- Operação EAFP em Dicionários (`try ... except KeyError`):
  - Caso com sucesso (sem exceção): O(1) de tempo.
  - Caso com erro: O(1) de tempo para capturar, porém com overhead de traceback se a exceção for frequente.
- Regra de Ouro: Se a falha for exceção (rara, < 5% das vezes), use EAFP. Se a falha for a norma (> 50%), prefira LBYL para evitar overhead de exceção.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    elementos = ["Servidor-01", "Servidor-02", "Servidor-03"]

    # [X] NÃO-PYTHONIC: Iteração por índice manual e checagem explícita de len > 0
    print("[X] Nao-Pythonic:")
    if len(elementos) > 0:
        for i in range(len(elementos)):
            print(f"  Index {i}: {elementos[i]}")

    # [OK] PYTHONIC: Truthiness direto e enumerate
    print("\n[OK] Pythonic:")
    if elementos:
        for idx, item in enumerate(elementos):
            print(f"  Index {idx}: {item}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Nunca faça comparações explícitas com Booleans: `if ativo == True:` é antipadrão. Use `if ativo:`.
2. Prefira `is None` para checar ausência de valor em vez de `if not valor:`, pois `0` ou `""` podem ser valores válidos.
3. Utilize `dict.get(chave, padrao)` para buscas simples com fallback.
4. Mantenha os blocos `try` o menores possíveis para evitar capturar exceções indesejadas por engano.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Confundir Falsy com None em parâmetros numéricos
    def processar_desconto(taxa: float | None = None) -> float:
        # ERRADO: if not taxa -> trata taxa 0.0 como se fosse None!
        # CORRETO: if taxa is None
        if taxa is None:
            return 5.0  # Desconto padrão
        return taxa

    print(f"Desconto para taxa 0.0 (Correto): {processar_desconto(0.0)}%")
    print(f"Desconto para taxa None (Padrao): {processar_desconto(None)}%")

    # Armadilha 2: Exceção genérica demais em EAFP
    try:
        dados = {"resultado": 10 / 2}
        _ = dados["resultado_inexistente"]
    except Exception as e:  # [!] Muito amplo: mascara erros internos
        print(f"[!] Capturado erro amplo (evite em producao): {type(e).__name__} - {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre EAFP e LBYL em Python e quando você deve escolher cada um?"
A: "LBYL (Look Before You Leap) verifica condições antes de agir (usando 'if in', 'os.path.exists', etc.).
    EAFP (Easier to Ask Forgiveness than Permission) tenta a operação diretamente em um bloco try/except.
    Em Python, EAFP é o padrão idiomático porque:
    1. É thread-safe em operações de I/O (evita o problema TOCTOU onde o recurso desaparece entre a checagem e o uso).
    2. Em Python 3.11+, blocos try sem erro têm custo nulo (Zero-Cost Exceptions).
    Deve-se escolher LBYL apenas quando a exceção ocorre com frequência altíssima e o custo de exceções prejudica a performance."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `extrair_porta(url: str) -> int` usando a abordagem EAFP
#              para converter o trecho final da URL em int e retornar 80 como padrão caso falhe.
# Exercício 2: Crie uma classe `ContadorVotos` que implemente `__len__` e `__bool__`
#              de forma que o objeto seja considerado Truthy apenas se tiver mais de 10 votos.
# Exercício 3: Refatore um código que faz `if key in dict: return dict[key]` para uma versão
#              Pythonic resiliente usando EAFP ou `dict.get()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 18: PYTHON IDIOMÁTICO, EAFP E TRUTHINESS")
    print("==========================================================")
    demonstrar_eafp_vs_lbyl()
    demonstrar_truthiness()
    demonstrar_aplicacao_backend()
    demonstrar_internamente()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 18 executado com sucesso.")


if __name__ == "__main__":
    main()
