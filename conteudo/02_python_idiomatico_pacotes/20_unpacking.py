"""
20_unpacking.py - Desempacotamento de Sequências e Dicionários (Extended Unpacking e Merge)

Objetivos:
1. Dominar o desempacotamento de sequências (Tuple/List Unpacking) básico e estendido (`*rest`).
2. Compreender a desestruturação e mesclagem de dicionários utilizando `**` e o operador `|` (PEP 584).
3. Aplicar o desempacotamento na passagem de argumentos dinâmicos para funções (`*args`, `**kwargs`).
4. Entender a substituição de iteráveis e manipulação de retornos múltiplos sem tuplas temporárias.
5. Evitar armadilhas comuns em desestruturação de estruturas aninhadas e valores insuficientes.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Unpacking (Desempacotamento)?
Unpacking é o mecanismo idiomático do Python para extrair elementos de uma estrutura iterável
(como tuplas, listas, conjuntos, geradores e dicionários) e atribuí-los diretamente a múltiplas
variáveis em uma única instrução limpa.

Modalidades de Unpacking:
1. Unpacking Direto: Atribuição 1-para-1 onde o número de variáveis deve corresponder exatamente
   ao número de elementos na sequência (`a, b = [10, 20]`).
2. Extended Unpacking (`*rest`): Introduzido na PEP 3132, permite capturar elementos sobressalentes
   em uma lista usando o operador asterisco (`cabeça, *cauda = lista`).
3. Dictionary Unpacking (`**` e `|`): Permite desestruturar pares chave-valor e mesclar dicionários.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: DESEMPACOTAMENTO DE SEQUÊNCIAS
# ==========================================================
def demonstrar_unpacking_sequencias() -> None:
    print("\n--- 1. FUNDAMENTOS: Sequence Unpacking & Extended Unpacking ---")

    # Unpacking simples de Tupla
    ponto: tuple[int, int, int] = (100, 200, 50)
    x, y, z = ponto
    print(f"Coordenadas desempacotadas: x={x}, y={y}, z={z}")

    # Extended Unpacking (*rest)
    valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    primeiro, segundo, *resto, ultimo = valores

    print(f"Primeiro: {primeiro} | Segundo: {segundo}")
    print(f"Elementos do meio (*resto): {resto} (tipo {type(resto).__name__})")
    print(f"Ultimo: {ultimo}")

    # Ignorando valores com o sublinhado (_) por convenção
    data_iso = "2026-08-19"
    ano, _, dia = data_iso.split("-")
    print(f"Ano extraido: {ano}, Dia extraido: {dia} (Mes ignorado via _)")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: DICIONÁRIOS E OPERADOR PIPELINE
# ==========================================================
def demonstrar_unpacking_dicionarios() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Dictionary Unpacking & Merge ---")

    config_padrao: dict[str, Any] = {"theme": "dark", "timeout": 30, "debug": False}
    config_user: dict[str, Any] = {"timeout": 60, "debug": True}

    # Forma clássica via ** (cria um novo dict)
    config_final_kwargs = {**config_padrao, **config_user}
    print(f"Configuracao mesclada (via **): {config_final_kwargs}")

    # Forma moderna Python 3.9+ via operador de união `|` (PEP 584)
    config_final_union = config_padrao | config_user
    print(f"Configuracao mesclada (via |): {config_final_union}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def despachar_evento_webhook(tipo_evento: str, url_destino: str, **payload: Any) -> None:
    """Simula um despachante de webhooks que consome kwargs dinâmicos via unpacking."""
    print(f"[Webhook] Enviando {tipo_evento} para {url_destino}")
    print("  Payload enviado:")
    for chave, valor in payload.items():
        print(f"    - {chave}: {valor}")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Event Payload Dispatcher ---")
    dados_evento = {
        "usuario_id": 9941,
        "acao": "LOGIN_SUCCESS",
        "ip_origem": "192.168.1.100",
        "user_agent": "Mozilla/5.0",
    }

    # Passagem de parâmetros via desempacotamento de dicionário **
    despachar_evento_webhook(
        "USER_ACTIVITY",
        "https://analytics.empresa.com/collect",
        **dados_evento,
    )


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE
# ==========================================================
"""
Como o Python executa o Unpacking:
1. No bytecode do CPython, o desempacotamento de tamanho fixo emite a instrução `UNPACK_SEQUENCE`.
2. O CPython verifica se a contagem de elementos do iterável corresponde exatamente à contagem de variáveis esperadas.
3. No caso de `Extended Unpacking` (`*rest`), o CPython emite `UNPACK_EX`, construindo uma lista em C
   para acomodar os elementos excedentes.
4. Qualquer objeto que implemente o protocolo de iteração (`__iter__`) pode ser desempacotado!
"""


def demonstrar_unpacking_iterador_customizado() -> None:
    print("\n--- 4. INTERNO: Unpacking de Iteradores Customizados ---")

    def gerador_sequencia():
        yield "Alfa"
        yield "Beta"
        yield "Gama"

    # Desempacotando diretamente de uma função geradora (sem lista intermediária na memória)
    a, b, c = gerador_sequencia()
    print(f"Gerador desempacotado diretamente: a={a}, b={b}, c={c}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Desempacotamento Simples (`a, b, c = (1, 2, 3)`): O(1) de tempo e O(1) de espaço.
- Extended Unpacking (`first, *rest = lista`):
  - Tempo: O(N), pois percorre a sequência para alocar o `*rest`.
  - Espaço: O(N) para armazenar os N-1 elementos na nova lista de `rest`.
- Dictionary Merge (`dict1 | dict2`): Tempo O(N + M), Espaço O(N + M).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    registros = ["ID-99", "2026-08-19", "CANCELADO", "MOTIVO: TIMEOUT", "REVISE: OK"]

    # [X] NÃO-PYTHONIC: Acesso por índices mágicos manuais
    print("[X] Nao-Pythonic:")
    id_reg = registros[0]
    data_reg = registros[1]
    status_reg = registros[2]
    detalhes_reg = registros[3:]
    print(f"  ID: {id_reg}, Status: {status_reg}, Detalhes: {detalhes_reg}")

    # [OK] PYTHONIC: Extended Unpacking idiomático
    print("\n[OK] Pythonic:")
    id_py, data_py, status_py, *detalhes_py = registros
    print(f"  ID: {id_py}, Status: {status_py}, Detalhes: {detalhes_py}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize sublinhado `_` para ignorar elementos que você não pretende utilizar.
2. Utilize `_` duplo `__` se precisar ignorar múltiplos elementos ou `*_` para ignorar o restante.
3. Prefira o operador `|` (Python 3.9+) para fusão de dicionários por ser mais legível do que `{**d1, **d2}`.
4. Ao trocar variáveis (swap), use `a, b = b, a` em vez de criar variáveis temporárias manuais.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: ValueError por incompatibilidade no número de elementos
    try:
        a, b = [10, 20, 30]  # Espera 2, recebe 3
    except ValueError as e:
        print(f"[!] Armadilha 1 (ValueError too many values to unpack): {e}")

    try:
        x, y, z = [1]  # Espera 3, recebe 1
    except ValueError as e:
        print(f"[!] Armadilha 1 (ValueError not enough values to unpack): {e}")

    # Armadilha 2: Tentar usar múltiplos wildcards * na mesma instrução de unpacking
    # sintaxe_invalida = "a, *b, *c = [1, 2, 3, 4]" -> SyntaxError: two starred expressions in assignment


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como funciona a troca de variáveis `a, b = b, a` em Python sob o ponto de vista de memória?"
A: "Em Python, o lado direito `b, a` é primeiramente avaliado criando uma tupla implícita na memória (stack da CPython)
    contendo as referências originais de `b` e `a`.
    Em seguida, a instrução de desempacotamento (UNPACK_SEQUENCE) atribui os ponteiros para `a` e `b` respectivamente.
    Isso garante que a troca ocorra de forma atômica e segura sem corromper os valores ou precisar de variável temporária explícita."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Dada a lista `linha_csv = ["Gabriel", "34", "Desenvolvedor", "Brasil", "Ativo"]`,
#              desempacote nome e idade nas duas primeiras variáveis e junte o restante em `metadados`.
# Exercício 2: Escreva uma função `mesclar_configs(*configs: dict[str, Any]) -> dict[str, Any]` que recebe
#              N dicionários de configuração e os mescla em ordem usando o operador `|`.
# Exercício 3: Escreva uma função que receba uma lista de números e retorne o primeiro elemento,
#              o último elemento e a média dos elementos do meio utilizando extended unpacking.


def main() -> None:
    print("==========================================================")
    print("  AULA 20: DESEMPACOTAMENTO DE SEQUÊNCIAS E DICIONÁRIOS")
    print("==========================================================")
    demonstrar_unpacking_sequencias()
    demonstrar_unpacking_dicionarios()
    demonstrar_aplicacao_backend()
    demonstrar_unpacking_iterador_customizado()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 20 executado com sucesso.")


if __name__ == "__main__":
    main()
