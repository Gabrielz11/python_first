"""
28_modulos.py - Módulos em Python, Mecanismo de Importação e sys.path

Objetivos:
1. Compreender o conceito de Módulo em Python (todo arquivo `.py` é um módulo).
2. Entender a ordem de busca de importação gerenciada pelo `sys.path` e o cache em `sys.modules`.
3. Dominar o padrão `if __name__ == '__main__':` para separação entre código executável e biblioteca.
4. Aplicar técnicas de carregamento dinâmico de módulos utilizando `importlib`.
5. Prevenir problemas graves como Importação Circular (Circular Imports) e poluição de namespace com wildcard imports (`from module import *`).
"""

import importlib
import math
import sys
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Módulo em Python?
Um módulo é simplesmente um arquivo com extensão `.py` contendo definições de funções, classes, variáveis
e código executável. Módulos são as unidades fundamentais de organização e reutilização de código em Python.

Mecanismo de Importação (`sys.path` e `sys.modules`):
Quando você executa `import meu_modulo`:
1. O Python verifica se o módulo já foi importado anteriormente no dicionário de cache `sys.modules`.
   Se sim, retorna a referência imediatamente (custo de performance zero).
2. Se não estiver no cache, o Python busca o arquivo `.py` sequencialmente nos diretórios listados em `sys.path`:
   - 1º: O diretório do script que iniciou a execução.
   - 2º: A variável de ambiente `PYTHONPATH`.
   - 3º: Os diretórios da biblioteca padrão (Standard Library).
   - 4º: Os diretórios de pacotes instalados por terceiros (`site-packages`).
3. O código do módulo é EXECUTADO do início ao fim e compilado em bytecode na pasta `__pycache__/`.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: MODOS DE IMPORTAÇÃO
# ==========================================================
def demonstrar_importacoes_e_sys_path() -> None:
    print("\n--- 1. FUNDAMENTOS: Importações e sys.path ---")

    # Utilizando módulo nativo
    print(f"Raiz quadrada via math.sqrt(25): {math.sqrt(25)}")

    # Inspecionando o cache sys.modules
    print(f"O modulo 'math' esta em sys.modules? {'math' in sys.modules}")

    # Exibindo os 3 primeiros caminhos do sys.path
    print("\nPrimeiros 3 diretórios de busca no sys.path:")
    for idx, path in enumerate(sys.path[:3], start=1):
        print(f"  {idx}. {path}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: IMPORTLIB E RELOAD
# ==========================================================
def demonstrar_carregamento_dinamico() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Importação Dinâmica com importlib ---")

    # Importação dinâmica por nome de string
    nome_modulo = "json"
    modulo_carregado: Any = importlib.import_module(nome_modulo)

    dados = {"status": "sucesso", "origem": "importlib"}
    json_str = modulo_carregado.dumps(dados)
    print(f"Módulo '{nome_modulo}' importado dinamicamente!")
    print(f"Resultado do dumps: {json_str}")

    # Recarregar módulo em tempo de execução (Recomendado apenas para REPL ou Plugins)
    importlib.reload(modulo_carregado)
    print("Módulo 'json' recarregado em runtime com importlib.reload().")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class PluginLoaderEngine:
    """Motor backend para carregamento dinâmico de plugins de pagamento."""

    @staticmethod
    def carregar_e_executar_driver(nome_driver: str) -> str:
        try:
            # Tenta importar dinamicamente o driver de pagamento
            modulo = importlib.import_module(nome_driver)
            return f"Driver '{nome_driver}' carregado do arquivo {getattr(modulo, '__file__', 'builtin')}"
        except ImportError as e:
            return f"[!] Erro ao carregar plugin de pagamento '{nome_driver}': {e}"


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Plugin Loader ---")
    engine = PluginLoaderEngine()

    print(engine.carregar_e_executar_driver("sqlite3"))
    print(engine.carregar_e_executar_driver("driver_inexistente_xpto"))


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: __PYCACHE__ E CACHING
# ==========================================================
"""
Como o CPython gerencia Módulos:
1. Arquivos `.pyc`: Ao importar um módulo, o CPython gera um arquivo compilado em bytecode localizado
   na pasta `__pycache__/modulo.cpython-312.pyc`.
2. Verificação de Modificação: O CPython compara a data de modificação (timestamp) do `.py` com o `.pyc`.
   Se o arquivo fonte não mudou, o CPython pula a fase de compilação e carrega o bytecode direto.
3. Execução Única: Mesmo que você escreva `import meu_modulo` em 10 arquivos diferentes do seu projeto,
   o arquivo `meu_modulo.py` é EXECUTADO apenas UMA VEZ durante o ciclo de vida do processo.
"""


def demonstrar_internamente_sys_modules() -> None:
    print("\n--- 4. INTERNO: sys.modules Caching ---")
    mod_math_1 = sys.modules["math"]
    import math as mod_math_2

    print(f"Ambas as importações apontam para o mesmo objeto na memória? {mod_math_1 is mod_math_2}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- 1ª Importação de um Módulo (`import X`): Tempo O(N) para ler arquivo, compilar bytecode e executar o código global do módulo.
- Importações Subsequentes: Tempo O(1) de busca na tabela Hash `sys.modules`.
- Adicionar caminhos ao `sys.path`: `sys.path.append('/caminho')` -> Aumenta a busca linear de módulos inexistentes.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Wildcard Imports (from os import *)
    # Polui o namespace atual, sobrescrevendo variáveis locais sem aviso prévio.
    print("[X] Nao-Pythonic (Wildcard Imports):")
    print("  Evite: 'from os import *' -> Polui namespace e dificulta análise estática (Mypy/Ruff).")

    # [OK] PYTHONIC: Importações explícitas ou alias de módulo
    print("\n[OK] Pythonic:")
    import os as sistema_operacional
    print(f"  Importacao explicita com alias: {sistema_operacional.name}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Organização dos Imports (PEP 8): Coloque todos os imports no topo do arquivo divididos em 3 blocos:
   - 1º Bloco: Biblioteca Padrão (Standard Library) -> ex: `import sys`, `import math`.
   - 2º Bloco: Pacotes de Terceiros (Third-Party) -> ex: `import requests`, `import fastapi`.
   - 3º Bloco: Módulos Locais da sua Aplicação -> ex: `from minha_app.services import ...`.
2. NUNCA utilize wildcard imports (`from modulo import *`).
3. Sempre envolva o código de teste executável do módulo no bloco `if __name__ == '__main__':`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Criar arquivos locais com o mesmo nome de módulos nativos (Nome Shadowing)
    # Criar um arquivo chamado `random.py` ou `json.py` no seu projeto fará o Python importar o SEU arquivo em vez do nativo!

    # Armadilha 2: Circular Import (Importação Circular)
    # Módulo A importa Módulo B que por sua vez tenta importar Módulo A antes de sua conclusão.
    print("[!] Armadilha: Importacao Circular ocorre quando o Modulo A importa B e B importa A simultaneamente.")
    print("    Solucao: Refatore a dependencia comum para um 3º modulo ou mova o import para dentro da funcao.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que acontece exatamente quando você executa um arquivo Python e qual o papel de `__name__ == '__main__'`?"
A: "1. O interpretador atribui a string `'__main__'` à variável especial `__name__` do arquivo que foi passado como ponto de entrada no terminal (`python arquivo.py`).
    2. Quando um arquivo é importado por outro módulo (`import arquivo`), a variável `__name__` do módulo importado recebe o próprio NOME do módulo (`'arquivo'`).
    3. A condição `if __name__ == '__main__':` garante que determinado bloco de código só seja executado quando o arquivo for chamado diretamente no terminal,
       evitando que scripts de teste rodem acidentalmente quando o módulo for importado por outros componentes."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `verificar_modulo_instalado(nome_modulo: str) -> bool` que consulte `sys.modules` ou utilize `importlib.util.find_spec`.
# Exercício 2: Escreva um script com a estrutura `if __name__ == '__main__':` contendo funções utilitárias que possam ser reutilizadas por outros arquivos.
# Exercício 3: Imprima o caminho do diretório no sistema de arquivos onde o módulo `math` e o módulo `json` estão instalados usando o atributo `__file__`.


def main() -> None:
    print("==========================================================")
    print("  AULA 28: MÓDULOS, IMPORTAÇÕES E SYS.PATH ENGINES")
    print("==========================================================")
    demonstrar_importacoes_e_sys_path()
    demonstrar_carregamento_dinamico()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_sys_modules()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 28 executado com sucesso.")


if __name__ == "__main__":
    main()
