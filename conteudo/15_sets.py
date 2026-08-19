"""
15_sets.py - Estrutura de Dados Set e Frozenset (Teoria dos Conjuntos e O(1) Lookup)

Objetivos:
1. Dominar `set` e `frozenset` em Python 3.12+: sintaxe, deduplicação e operações matemáticas de conjuntos.
2. Compreender a arquitetura interna do CPython (Hash Table sem valores).
3. Analisar a complexidade Big O temporal de pertencimento `in` e operações de conjuntos.
4. Diferenciar `set` mutável de `frozenset` imutável e hashable.
"""



# ==========================================================
# 1. CONCEITO: Como o `set` Funciona Internamente no CPython?
# ==========================================================
"""
Em CPython, um `set` é implementado como uma TABELA HASH contendo APENAS CHAVES (sem valores associados).

Características Internas no CPython:
- Elementos Únicos: Garantia matemática de ausência de duplicatas via `hash(element)` e `__eq__`.
- Sem Ordem Garantida: Diferente dos dicts (Python 3.7+), a ordem dos elementos num `set` é arbitrária.
- Imutabilidade dos Elementos: Todos os elementos inseridos em um `set` DEVEM ser hashable!

Tabela de Complexidade Temporal (Big O) do Set:
-----------------------------------------------------------------------------
Operação                      Sintaxe                  Complexidade Média (Big O)
-----------------------------------------------------------------------------
Teste de Pertencimento        `x in s`                 O(1) [Constante]
Adição de Elemento            `s.add(x)`               O(1) [Constante]
Remoção de Elemento           `s.remove(x)`            O(1) [Constante]
União de Conjuntos            `s1 | s2`                O(n + m)
Intersecção de Conjuntos      `s1 & s2`                O(min(len(s1), len(s2)))
Diferença de Conjuntos        `s1 - s2`                O(len(s1))
-----------------------------------------------------------------------------
"""


def demonstrar_operacoes_conjuntos() -> None:
    print("\n--- 1. CONCEITO: Operações Matemáticas de Teoria dos Conjuntos ---")

    devs_backend = {"Python", "PostgreSQL", "Docker", "Linux"}
    devs_frontend = {"JavaScript", "TypeScript", "React", "Docker"}

    # 1. União (|): Todos os elementos de ambos os conjuntos (sem duplicatas)
    todas_tecnologias = devs_backend | devs_frontend
    print(f"União (backend | frontend): {todas_tecnologias}")

    # 2. Intersecção (&): Apenas elementos presentes em AMBOS os conjuntos
    techs_em_comum = devs_backend & devs_frontend
    print(f"Intersecção (backend & frontend): {techs_em_comum}")

    # 3. Diferença (-): Elementos no backend que NÃO estão no frontend
    exclusivo_backend = devs_backend - devs_frontend
    print(f"Diferença (backend - frontend): {exclusivo_backend}")

    # 4. Diferença Simétrica (^): Elementos em APENAS UM dos conjuntos (exclui comuns)
    diferenca_simetrica = devs_backend ^ devs_frontend
    print(f"Diferença Simétrica (backend ^ frontend): {diferenca_simetrica}")


# ==========================================================
# 2. DEDUPLICAÇÃO DE DADOS: O(n) vs PRESERVAÇÃO DE ORDEM
# ==========================================================
def demonstrar_deduplicacao() -> None:
    print("\n--- 2. EXEMPLO: Deduplicação de Dados ---")

    logs_ip = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1"]
    print(f"Logs de IP originais (com duplicatas): {logs_ip}")

    # Deduplicação rápida usando set (NÃO preserva a ordem original)
    ips_unicos_set = list(set(logs_ip))
    print(f"Deduplicação com `set()` (Ordem arbitrária): {ips_unicos_set}")

    # Deduplicação Sênior que PRESERVA a ORDEM original (Usando dict.fromkeys() em O(n)):
    ips_unicos_ordenados = list(dict.fromkeys(logs_ip))
    print(f"Deduplicação com `dict.fromkeys()` (Preserva Ordem): {ips_unicos_ordenados}")


# ==========================================================
# 3. FROZENSET: O Conjunto Imutável e Hashable
# ==========================================================
def demonstrar_frozenset() -> None:
    print("\n--- 3. CONCEITO: Frozenset como Chave de Dicionário ---")

    # `frozenset` é a versão imutável do `set`. Como tem hash estável, pode ser elemento de outro set ou chave de dict!
    permissoes_admin = frozenset(["criar", "ler", "atualizar", "deletar"])
    permissoes_guest = frozenset(["ler"])

    perfis_acesso: dict[frozenset[str], str] = {
        permissoes_admin: "Grupo Administradores",
        permissoes_guest: "Grupo Visitantes",
    }

    consulta = frozenset(["ler"])
    grupo = perfis_acesso.get(consulta, "Perfil Desconhecido")
    print(f"Busca por grupo com frozenset {list(consulta)}: {grupo}")


# ==========================================================
# 4. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 4. ARMADILHAS E ERROS COMUNS ---")

    # [!] ARMADILHA 1: Criar set vazio com `{}` cria um DICT!
    vazio_errado = {}
    vazio_correto = set()
    print(f"Tipo de '{{}}': {type(vazio_errado)} | Tipo de 'set()': {type(vazio_correto)}")

    # [!] ARMADILHA 2: Tentar adicionar objeto mutável (unhashable) em um set
    conjunto_teste = {1, 2, 3}
    try:
        conjunto_teste.add([4, 5])  # list é unhashable!
    except TypeError as e:
        print(f"[X] TypeError ao adicionar lista em set: {e}")


# ==========================================================
# 5. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta Frequente de Entrevista:
Q: "Dado dois arrays gigantes de IDs, como você encontra os IDs presentes em ambos em O(n) tempo?"
A: "Converter um dos arrays para um `set` em O(n) tempo. Depois, iterar sobre o segundo array
    e filtrar apenas os elementos que retornarem True para `id in set_id`, que é O(1) por elemento.
    Tempo total: O(n + m), muito superior a dois loops aninhados O(n * m)."
"""


# ==========================================================
# 6. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `tem_caracteres_unicos(texto: str) -> bool` que determine se uma string
#              contém apenas caracteres totalmente distintos usando `set` (retorna True se len(set) == len(str)).
# Exercício 2: Escreva uma função `diferenca_simetrica_manual(s1: set, s2: set) -> set` que implemente a
#              diferença simétrica usando apenas os operadores de união `|`, intersecção `&` e diferença `-`.


def main() -> None:
    print("==========================================================")
    print("  AULA 15: ESTRUTURA DE DADOS SET E FROZENSET")
    print("==========================================================")
    demonstrar_operacoes_conjuntos()
    demonstrar_deduplicacao()
    demonstrar_frozenset()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 15 executado com sucesso.")


if __name__ == "__main__":
    main()
