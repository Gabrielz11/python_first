"""
09_args_kwargs.py - Argumentos Variádicos (*args e **kwargs) e Unpacking

Objetivos:
1. Compreender o funcionamento interno de `*args` (posicionais variádicos) e `**kwargs` (nomeados variádicos).
2. Entender o desempacotamento (unpacking) de iteráveis em chamadas de função.
3. Aplicar o repasse seguro de argumentos em wrappers, decorators e padrões de proxy/middleware.
"""

from typing import Any

# ==========================================================
# 1. CONCEITO: O que são *args e **kwargs?
# ==========================================================
"""
Em Python, os operadores de desempacotamento `*` (tupla) e `**` (dicionário) na assinatura de uma função
permitem aceitar um número arbitrário (desconhecido a priori) de argumentos.

1. `*args`: Empacota todos os argumentos posicionais excedentes em uma TUPLA imutável chamada `args`.
2. `**kwargs`: Empacota todos os argumentos nomeados (keyword) excedentes em um DICIONÁRIO chamado `kwargs`.

Ordem Obrigatória dos Parâmetros na Assinatura:
def funcao(posicionais_normais, *args, nomeados_normais=val, **kwargs):
"""


def registrar_log(nivel: str, *mensagens: str, **metadados: Any) -> None:
    print(f"\n--- 1. CONCEITO: Log [{nivel.upper()}] ---")

    # `mensagens` é uma TUPLA contendo todos os argumentos posicionais extras
    texto_unificado = " | ".join(mensagens)
    print(f"  Mensagem: {texto_unificado}")

    # `metadados` é um DICIONÁRIO contendo todos os chave=valor adicionais
    if metadados:
        print("  Metadados associados:")
        for chave, valor in metadados.items():
            print(f"    - {chave}: {valor}")


# ==========================================================
# 2. EXEMPLOS: Unpacking em Chamadas de Função
# ==========================================================
def calcular_area_retangulo(largura: float, altura: float) -> float:
    return largura * altura


def demonstrar_unpacking_chamada() -> None:
    print("\n--- 2. EXEMPLOS: Unpacking de Sequências e Dicts em Chamadas ---")

    # Desempacotando uma tupla/lista com `*` em uma função com parâmetros nomeados
    dimensões = (15.5, 10.0)
    area = calcular_area_retangulo(*dimensões)  # Equivalente a calcular_area_retangulo(15.5, 10.0)
    print(f"Área com unpacking de tupla (*dimensões): {area}")

    # Desempacotando um dicionário com `**`
    config_params = {"largura": 20.0, "altura": 5.0}
    area_dict = calcular_area_retangulo(**config_params)  # Equivalente a calcular_area_retangulo(largura=20.0, altura=5.0)
    print(f"Área com unpacking de dict (**config_params): {area_dict}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Wrapper/Middleware de Monitoramento
# ==========================================================
def executar_com_auditoria(funcao_alvo: Any, *args: Any, **kwargs: Any) -> Any:
    """
    Função de infraestrutura / proxy que intercepta a execução de qualquer função,
    registra os argumentos recebidos e repassa tudo transparentemente (*args, **kwargs).
    """
    print(f"\n--- 3. EXEMPLO PRÁTICO: Repasse Transparente para '{funcao_alvo.__name__}' ---")
    print(f"  [Interceptador] Argumentos posicionais: {args}")
    print(f"  [Interceptador] Argumentos nomeados: {kwargs}")

    # Repassa exatamente os mesmos argumentos usando *args e **kwargs
    resultado = funcao_alvo(*args, **kwargs)

    print(f"  [Interceptador] Execução concluída com sucesso. Retorno: {resultado}")
    return resultado


def processar_pagamento(usuario_id: int, valor: float, moeda: str = "BRL") -> str:
    return f"Transação de R$ {valor} {moeda} aprovada para usuário #{usuario_id}"


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de *args e **kwargs:
- Empacotamento de *args: O(k) Temporal e Espacial, onde k é o número de argumentos posicionais passados (criação de tupla).
- Empacotamento de **kwargs: O(m) Temporal e Espacial, onde m é o número de argumentos nomeados passados (criação de dict).
"""


# ==========================================================
# 5. COMPARATIVO: CÓDIGO RÍGIDO VS FLEXÍVEL (VARIÁDICO)
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE ARQUITETURA ---")

    # [X] NÃO-PYTHONIC (Forçar o cliente a empacotar manualmente em uma lista/dict antes de chamar):
    # registrar_log_antigo("INFO", ["msg1", "msg2"], {"env": "prod"})

    # [OK] PYTHONIC (API limpa aceitando variádicos naturais):
    registrar_log("INFO", "Iniciando servico", "Conexão estabelecida", ambiente="producao", versao="2.1.0")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Conflito de nomes ao repassar **kwargs para funções com argumentos nomeados fixos.
    params = {"largura": 10.0, "altura": 5.0, "cor": "azul"}
    try:
        # Lança TypeError: calcular_area_retangulo() got an unexpected keyword argument 'cor'
        calcular_area_retangulo(**params)
    except TypeError as e:
        print(f"[!] Armadilha de Kwargs Inesperados: {e}")
        print("  -> Solução: filtre o dicionário antes de desempacotar ou aceite **kwargs na função destino.")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como implementar um decorador genérico em Python que possa envolver qualquer função sem alterar sua assinatura?"
A: "Utilizando a assinatura `def wrapper(*args, **kwargs):` no decorador interno e repassando os argumentos com `return func(*args, **kwargs)`."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `multiplicar_todos(*numeros: float) -> float` que retorne a multiplicação de todos os números passados.
# Exercício 2: Escreva uma função `criar_tag_html(tag_name: str, conteudo: str, **atributos: str) -> str`
#              que gere uma string HTML formatada (ex: `criar_tag_html("a", "Clique Aqui", href="https://site.com", id="btn")`).


def main() -> None:
    print("==========================================================")
    print("  AULA 09: ARGUMENTOS VARIÁDICOS (*ARGS E **KWARGS)")
    print("==========================================================")

    demonstrar_unpacking_chamada()

    res = executar_com_auditoria(processar_pagamento, 1084, 250.75, moeda="BRL")

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 09 executado com sucesso.")


if __name__ == "__main__":
    main()
