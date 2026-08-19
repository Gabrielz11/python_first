"""
05_match_case.py - Structural Pattern Matching (match / case) no Python Moderno

Objetivos:
1. Compreender o funcionamento do `match / case` introduzido no Python 3.10+.
2. Ir além do simples 'switch/case' tradicional: explorar o Pattern Matching Estrutural.
3. Utilizar padrões compostos, coringa (`_`), guardas de condição (`if`) e desestruturação de Sequências, Dicionários e Objetos.
"""

from dataclasses import dataclass
from typing import Any

# ==========================================================
# 1. CONCEITO: O que é Pattern Matching Estrutural?
# ==========================================================
"""
Em linguagens funcionais (como Scala, Rust, Elixir, Haskell), o Pattern Matching permite
desestruturar dados e tomar decisões com base no FORMATO, CONTEÚDO e TIPO da estrutura de dados.

No Python 3.10+, a instrução `match / case` trouxe esse poder para a linguagem.
Não se trata de apenas comparar valores (como o switch em C/Java); ele pode extrair dados internos
de listas, tuplas, dicionários e instâncias de classes dinamicamente.
"""


def processar_status_http(codigo_status: int) -> str:
    print(f"\n--- 1. CONCEITO: Match simples de valor status={codigo_status} ---")

    match codigo_status:
        case 200 | 201 | 204:
            return "Sucesso na Requisição (2xx)"
        case 400 | 401 | 403 | 404:
            return "Erro do Cliente (4xx)"
        case 500 | 502 | 503:
            return "Erro Interno do Servidor (5xx)"
        case _:
            return f"Codigo HTTP Desconhecido ({codigo_status})"


# ==========================================================
# 2. EXEMPLOS: Desestruturação de Coleções e Guards
# ==========================================================
def processar_comando_cli(comando: list[str]) -> str:
    """
    Desestrutura listas de tamanho e formato variáveis.
    """
    match comando:
        # Match exato de comando de parada sem argumentos
        case ["quit"] | ["exit"]:
            return "Saindo da aplicação..."

        # Match de um comando de 2 elementos ("load", filename)
        case ["load", filename]:
            return f"Carregando arquivo: '{filename}'"

        # Match com Guarda de Condição (if)
        case ["save", filename] if filename.endswith(".json"):
            return f"Salvando em formato JSON: '{filename}'"

        case ["save", filename]:
            return f"Salvando em formato genérico: '{filename}'"

        # Match com resto de elementos usando *args
        case ["process", *arquivos]:
            return f"Processando lista de {len(arquivos)} arquivo(s): {arquivos}"

        case _:
            return f"Comando não reconhecido: {comando}"


# ==========================================================
# 3. EXEMPLO PRÁTICO: Desestruturação de Dicionários e Data Classes
# ==========================================================
@dataclass
class EventoClique:
    x: int
    y: int


@dataclass
class EventoTecla:
    key: str


def processar_evento_sistema(evento: Any) -> str:
    """
    Pattern Matching Estrutural em Objetos de Domínio e Dicionários.
    """
    match evento:
        # Match de Dicionário contendo chaves específicas
        case {"tipo": "LOGIN", "user_id": uid, "sucesso": True}:
            return f"[Audit] Login bem-sucedido do usuário #{uid}"

        case {"tipo": "LOGIN", "user_id": uid, "sucesso": False}:
            return f"[ALERTA] Falha de login para o usuário #{uid}"

        # Match de Classe (extrai atributos x e y diretamente)
        case EventoClique(x=pos_x, y=pos_y) if pos_x > 100:
            return f"Clique fora da margem esquerda: (x={pos_x}, y={pos_y})"

        case EventoClique(x=pos_x, y=pos_y):
            return f"Clique na tela: (x={pos_x}, y={pos_y})"

        case EventoTecla(key=k):
            return f"Tecla pressionada: '{k}'"

        case _:
            return "Evento desconhecido ignorado"


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade do `match / case`:
- Para checagens simples de valores constantes: O(1) similar a um dicionário de salto interno no CPython.
- Para desestruturação de listas/dicionários complexos: O(k) onde k é o número de elementos inspecionados na estrutura.
"""


# ==========================================================
# 5. COMPARATIVO: IF/ELIF TRADICIONAL VS MATCH/CASE ESTRUTURAL
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    comando = ["save", "relatorio.json"]

    # [X] NÃO-PYTHONIC (if/elif manual extraindo índices de lista):
    print("[X] Nao-Pythonic (if/elif manual com len e índices):")
    if len(comando) == 2 and comando[0] == "save":
        arquivo = comando[1]
        if arquivo.endswith(".json"):
            res_if = f"Salvar JSON: {arquivo}"
        else:
            res_if = f"Salvar: {arquivo}"
    else:
        res_if = "Outro"
    print(f"Resultado if/elif: {res_if}")

    # [OK] PYTHONIC (match/case declarativo):
    print("[OK] Pythonic (match/case estrutural):")
    res_match = processar_comando_cli(comando)
    print(f"Resultado match/case: {res_match}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar usar uma variável como constante de comparação no case sem usar Enum ou ponto.
    STATUS_ESPERADO = 200

    status = 500
    match status:
        # ⚠️ Se você escrever 'case STATUS_ESPERADO:', o Python NAO compara!
        # Ele BIND (atribui) a variável STATUS_ESPERADO com o valor 500!
        # Para comparar com variáveis existentes, use um Enum ou qualifique com modulo (ex: Config.STATUS_ESPERADO).
        case 200:
            print("[OK] Match correto com literal 200")
        case _:
            print("[OK] Caiu no wildcard correto para status 500")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre o switch/case de linguagens tradicionais e o match/case do Python 3.10+?"
A: "O `match/case` do Python é um Pattern Matching Estrutural completo.
    Ele permite extrair dados (bindings), desestruturar coleções (listas, tuplas, dicts), verificar tipos de classes
    e aplicar guardas condicionais (`if`), funcionando como uma poderosa ferramenta de parsing declarativo."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função que receba uma resposta de API em formato JSON (dict) contendo dados de um usuário
#              e use `match / case` para retornar mensagens diferentes se o usuário for "ADMIN", "COMMON" ou "GUEST".
# Exercício 2: Escreva um parser de comandos matemáticos simples (ex: `["ADD", 10, 20]`, `["SUB", 50, 15]`) usando match/case.


def main() -> None:
    print("==========================================================")
    print("  AULA 05: STRUCTURAL PATTERN MATCHING (MATCH / CASE)")
    print("==========================================================")
    print(processar_status_http(200))
    print(processar_status_http(404))

    print("\nTestando Comandos CLI:")
    print(processar_comando_cli(["quit"]))
    print(processar_comando_cli(["load", "dados.csv"]))
    print(processar_comando_cli(["process", "a.txt", "b.txt", "c.txt"]))

    print("\nTestando Eventos Estruturados:")
    payload_ok = {"tipo": "LOGIN", "user_id": 101, "sucesso": True}
    payload_fail = {"tipo": "LOGIN", "user_id": 999, "sucesso": False}
    print(processar_evento_sistema(payload_ok))
    print(processar_evento_sistema(payload_fail))
    print(processar_evento_sistema(EventoClique(150, 200)))

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 05 executado com sucesso.")


if __name__ == "__main__":
    main()
