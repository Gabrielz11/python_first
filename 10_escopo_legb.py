"""
10_escopo_legb.py - Escopo de Variáveis (Regra LEGB), global e nonlocal

Objetivos:
1. Dominar a regra de resolução de escopos LEGB em Python (Local, Enclosing, Global, Built-in).
2. Compreender a diferença entre a instrução `global` e a instrução `nonlocal`.
3. Entender por que o uso de variáveis `global` é considerado um Anti-Pattern em Engenharia de Software.
4. Explorar o conceito de Closures (funções que capturam variáveis do escopo Enclosing).
"""

import builtins
from typing import Callable

# ==========================================================
# 1. CONCEITO: A Regra LEGB de Resolução de Nomes
# ==========================================================
"""
Quando você faz referência a uma variável em Python (ex: `print(x)`), o Python busca o nome `x`
nesta ordem exata (Ordem LEGB):

1. L (Local): Dentro da função ou lambda corrente.
2. E (Enclosing): Nas funções aninhadas envolventes (do escopo externo para o interno).
3. G (Global): No nível superior (top-level) do módulo `.py` corrente.
4. B (Built-in): No módulo nativo da linguagem (ex: `len`, `range`, `ValueError`).

Se a variável não for encontrada em NENHUM desses 4 escopos, o Python lança `NameError`.
"""

# Variavel no escopo GLOBAL (G)
contador_global: int = 100


def demonstrar_legb() -> None:
    print("\n--- 1. CONCEITO: Regra LEGB em Ação ---")

    # Variavel no escopo LOCAL (L) de demonstrar_legb
    local_val: str = "Variável Local"

    def funcao_interna() -> None:
        # Variavel no escopo LOCAL de funcao_interna
        # `local_val` é acessado via escopo ENCLOSING (E) da função pai!
        print(f"  [Função Interna] Acessando Enclosing: {local_val}")
        print(f"  [Função Interna] Acessando Global: {contador_global}")
        print(f"  [Função Interna] Acessando Built-in (len): {builtins.len([1, 2, 3])}")

    funcao_interna()


# ==========================================================
# 2. EXEMPLOS: `nonlocal` (Closures) vs `global`
# ==========================================================
def criar_contador_closure(valor_inicial: int = 0) -> Callable[[], int]:
    """
    Exemplo de Closure usando `nonlocal`.
    A função interna mantém e altera o estado do escopo Enclosing sem poluir o escopo Global!
    """
    # Variavel no escopo ENCLOSING
    contador: int = valor_inicial

    def incrementar() -> int:
        # `nonlocal` avisa ao Python que a variável `contador` pertence ao escopo da função envolvente (Enclosing)!
        # Sem `nonlocal`, tentar reatribuir `contador += 1` causaria UnboundLocalError!
        nonlocal contador
        contador += 1
        return contador

    return incrementar


# ==========================================================
# 3. EXEMPLO PRÁTICO: Evitando o Anti-pattern `global`
# ==========================================================

# ❌ ABORDAGEM COM GLOBAL (Má prática de arquitetura):
estado_sistema_global = {"conectado": False, "tentativas": 0}


def conectar_sistema_global_bad() -> None:
    global estado_sistema_global
    estado_sistema_global["conectado"] = True
    # Mutação global imprevisível por qualquer parte do sistema!


# ✅ ABORDAGEM ORIENTADA A OBJETO OU CLOSURE (Clean Code):
class ConexaoSistema:
    """Encapsula o estado dentro de um objeto, eliminando dependência de variáveis globais."""

    def __init__(self) -> None:
        self.conectado: bool = False
        self.tentativas: int = 0

    def conectar(self) -> None:
        self.conectado = True


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Performance de Busca de Variáveis (LEGB):
- Acesso a variáveis Locais (L): É a busca MAIS RÁPIDA em Python! (Tabela de símbolos locais usa índices diretos no CPython bytecode `LOAD_FAST`).
- Acesso a variáveis Globais (G) ou Built-in (B): Mais lento (`LOAD_GLOBAL`), pois envolve lookup em dicionário hash.

Dica de Performance Sênior:
Se você usa uma função built-in ou global repetidamente em um laço de milhões de iterações,
atribua-a a uma variável local para acelerar a busca (ex: `local_len = len`).
"""


# ==========================================================
# 5. COMPARATIVO DE ARQUITETURA DE ESTADO
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO: Global vs Closure/Classe ---")

    # [OK] Usando Closure com nonlocal para gerenciar estado encapsulado:
    meu_contador = criar_contador_closure(10)
    print(f"Incremento 1 (Closure): {meu_contador()}")
    print(f"Incremento 2 (Closure): {meu_contador()}")
    print(f"Incremento 3 (Closure): {meu_contador()}")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    var_global = 50

    def tentar_modificar_global() -> None:
        # Armadilha: Tentar ler e atribuir sem a palavra-chave `global` gera UnboundLocalError!
        try:
            # var_global = var_global + 1 # Descomentar lança UnboundLocalError!
            pass
        except UnboundLocalError as e:
            print(f"[!] UnboundLocalError capturado: {e}")

    tentar_modificar_global()


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é uma Closure em Python e qual a diferença entre as palavras-chave `global` e `nonlocal`?"
A: "Uma Closure é uma função aninhada que 'lembra' e retém acesso às variáveis de seu escopo envolvente (Enclosing),
    mesmo após a função pai ter finalizado sua execução.
    `global` declara que a variável deve ser resolvida no módulo raiz (top-level).
    `nonlocal` declara que a variável pertence ao escopo da função aninhada mais próxima (Enclosing), excluindo o escopo Global."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `criar_gerador_id(prefixo: str)` que retorne uma Closure.
#              A cada chamada da Closure, ela deve retornar uma string no formato `"PREFIXO-001"`, `"PREFIXO-002"`, etc.
# Exercício 2: Explique o que acontece com a resolução LEGB ao tentar redefinir a função built-in `print = 123`.


def main() -> None:
    print("==========================================================")
    print("  AULA 10: ESCOPO DE VARIÁVEIS (REGRA LEGB), GLOBAL E NONLOCAL")
    print("==========================================================")
    demonstrar_legb()
    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 10 executado com sucesso.")


if __name__ == "__main__":
    main()
