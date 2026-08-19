"""
01_variaveis.py - Variáveis, Referências de Memória e Sistema de Tipagem em Python

Objetivos:
1. Compreender a criação e gerenciamento de variáveis em Python 3.12+.
2. Diferenciar Tipagem Dinâmica de Tipagem Forte (e por que Python possui ambas).
3. Entender a alocação de memória: em Python, variáveis são RÓTULOS (ponteiros/referências) para objetos.
4. Aplicar convenções de nomenclatura (PEP 8), constantes por convenção, Type Annotations (PEP 526) e Unpacking.
"""


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma variável em Python?
Em linguagens estáticas (como C ou Java tradicional), uma variável é um "contêiner" de memória
com um tipo fixo reservado na compilação.
Em Python, TUDO é um objeto na Heap. Uma variável NÃO guarda o valor diretamente;
ela guarda UMA REFERÊNCIA (um ponteiro para o endereço de memória onde o objeto reside).

Tipagem Dinâmica vs Tipagem Forte:
- Tipagem Dinâmica: O tipo pertence ao OBJETO na memória, não à variável.
  A mesma variável pode apontar para um int e depois para uma str.
- Tipagem Forte: O Python NÃO realiza coerção silenciosa de tipos incompatíveis em operações.
  Exemplo: "34" + 1 lança TypeError (diferente de JavaScript ou PHP).
"""


def demonstrar_conceito_referencia() -> None:
    print("\n--- 1. CONCEITO: Referencias de Memoria e id() ---")

    # Ambas as variáveis a e b passam a apontar para o MESMO objeto inteiro na memória
    a = 1000
    b = a

    print(f"Valor de a: {a} | Endereco de memoria id(a): {id(a)}")
    print(f"Valor de b: {b} | Endereco de memoria id(b): {id(b)}")
    print(f"a e b apontam para o mesmo objeto? {a is b}")

    # Reatribuindo a: a passa a apontar para um NOVO objeto int(2000). b continua apontando para 1000.
    a = 2000
    print("\nApos reatribuir a = 2000:")
    print(f"Valor de a: {a} | Novo id(a): {id(a)}")
    print(f"Valor de b: {b} | Mantem id(b): {id(b)}")
    print(f"a e b ainda apontam para o mesmo objeto? {a is b}")


# ==========================================================
# 2. EXEMPLOS: Sintaxe, Convenções e Type Annotations
# ==========================================================
def demonstrar_sintaxe_e_tipagem() -> None:
    print("\n--- 2. EXEMPLOS: Declaracao, Type Hints e Unpacking ---")

    # Convenção PEP 8: snake_case para variáveis e funções
    nome_usuario: str = "Gabriel"
    idade_usuario: int = 34
    taxa_sucesso: float = 99.8
    ativo: bool = True

    # Constantes em Python são definidas por convenção utilizando UPPER_SNAKE_CASE
    TIMEOUT_PADRAO_SEGUNDOS: int = 30
    URL_BASE_API: str = "https://api.empresa.com/v1"

    print(f"Usuario: {nome_usuario} ({type(nome_usuario).__name__})")
    print(f"Idade: {idade_usuario} ({type(idade_usuario).__name__})")
    print(f"Constante URL: {URL_BASE_API}")

    # Múltipla atribuição e Unpacking (Desempacotamento de Sequências)
    largura, altura, profundidade = 1920, 1080, 60
    print(f"Dimensoes desempacotadas: {largura}x{altura}x{profundidade}")

    # Troca elegante de variáveis sem necessidade de variável temporária (temp)
    x, y = 10, 20
    x, y = y, x
    print(f"Troca de valores (swap): x={x}, y={y}")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Cenário Real de Engenharia Backend
# ==========================================================
def demonstrar_exemplo_real() -> None:
    print("\n--- 3. EXEMPLO PRATICO: Configuracao de Sessao de Usuario ---")

    # DTO (Data Transfer Object) conceitual usando variáveis tipadas
    user_id: int = 10452
    user_email: str = "gabriel@empresa.com.br"
    is_admin: bool = False
    permissions: list[str] = ["read:reports", "write:tickets"]

    # Exemplo de verificação com tipagem forte garantida
    if is_admin:
        role_label = "Administrador"
    else:
        role_label = "Usuario Comum"

    print(f"[Sessao Criada] ID={user_id} | Email={user_email} | Perfil={role_label}")
    print(f"Permissoes atribuidas ({len(permissions)}): {', '.join(permissions)}")


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade Temporal e Espacial de Atribuição de Variáveis em Python:
- Criar/Atribuir uma variável (a = 10):
  - Complexidade Temporal: O(1) [Constante]. É apenas a criação de uma referência no escopo local.
  - Complexidade Espacial: O(1) de espaço adicional para o ponteiro na tabela de símbolos local.

Curiosidade de Implementação (CPython - Interning):
- Para otimizar memória e tempo, o CPython faz 'interning' de pequenos inteiros no intervalo [-5, 256].
- Em tempo de compilação de código dentro do mesmo bloco/módulo, constantes literais iguais podem ser otimizadas pelo compilador bytecode.
"""


def demonstrar_interning() -> None:
    print("\n--- 4. COMPLEXIDADE & INTERNING (CPython) ---")
    x = 100
    y = 100
    print(f"x = 100, y = 100 => x is y? {x is y} (CPython reutiliza o objeto de memoria)")


# ==========================================================
# 5. COMPARATIVO: NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CODIGO ---")

    # [X] NÃO-PYTHONIC (Estilo C/Java antigo):
    print("[X] Nao-Pythonic (Troca de variaveis com temp):")
    a = 5
    b = 10
    temp = a
    a = b
    b = temp
    print(f"Resultado temp: a={a}, b={b}")

    # [OK] PYTHONIC:
    print("[OK] Pythonic (Tuple Unpacking & Type Annotations):")
    c, d = 5, 10
    c, d = d, c
    print(f"Resultado tuple unpacking: c={c}, d={d}")


# ==========================================================
# 6. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Use nomes expressivos e autodocumentáveis (`tempo_decorrido_segundos` em vez de `td`).
2. Siga a PEP 8: variáveis e funções em `snake_case`, constantes em `UPPER_SNAKE_CASE`.
3. Utilize Type Annotations (`nome: str = 'valor'`) para que ferramentas estáticas (Mypy) e IDEs ajudem a evitar bugs.
4. Evite variáveis globais soltas. Prefira escopo de função ou objetos.
"""


# ==========================================================
# 7. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 7. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Achar que Python faz coerção implícita de tipos (como JS: '5' + 1 = '51')
    try:
        resultado = "5" + 1  # Lança TypeError
    except TypeError as e:
        print(f"[!] Armadilha 1 (TypeError): Nao e possivel somar str com int -> {e}")

    # Armadilha 2: Confundir igualdade de valor (==) com igualdade de identidade (is)
    lista_a = [1, 2, 3]
    lista_b = [1, 2, 3]
    print(f"lista_a == lista_b: {lista_a == lista_b} (Mesmo CONTEUDO)")
    print(f"lista_a is lista_b: {lista_a is lista_b} (OBJETOS DIFERENTES na memoria)")


# ==========================================================
# 8. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta frequente em entrevistas de Python Sênior:
Q: "Em Python, os argumentos são passados por Valor ou por Referência?"
A: "Em Python, o mecanismo é chamado de 'Pass-by-Assignment' ou 'Pass-by-Object-Reference'.
    Se você passa um objeto mutável (como lista/dict), a função pode alterar o objeto interno.
    Se passa um objeto imutável (como int/str/tuple), a reatribuição dentro da função apenas
    faz a variável local apontar para outro objeto, sem alterar o valor original do chamador."
"""


# ==========================================================
# 9. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie 3 variáveis representando os dados de um produto (nome, preco, em_estoque).
#              Adicione anotações de tipo e imprima uma frase formatada usando f-string.
# Exercício 2: Dados x = 10, y = 20, z = 30, faça a rotação dos valores de forma que x receba z,
#              y receba x, e z receba y em UMA ÚNICA LINHA (usando tuple unpacking).
# Exercício 3: Teste o id() de duas strings idênticas pequenas vs duas strings construídas dinamicamente
#              e explique o comportamento.


def main() -> None:
    print("==========================================================")
    print("  AULA 01: VARIAVEIS, REFERENCIAS E TIPAGEM EM PYTHON")
    print("==========================================================")
    demonstrar_conceito_referencia()
    demonstrar_sintaxe_e_tipagem()
    demonstrar_exemplo_real()
    demonstrar_interning()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 01 executado com sucesso.")


if __name__ == "__main__":
    main()
