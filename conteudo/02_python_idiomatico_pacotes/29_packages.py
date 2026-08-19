"""
29_packages.py - Pacotes em Python, __init__.py, __all__ e Importações Relativas vs Absolutas

Objetivos:
1. Compreender a estrutura de Pacotes em Python (diretórios contendo um arquivo `__init__.py`).
2. Entender o papel do arquivo `__init__.py` na exposição de APIs públicas via `__all__`.
3. Diferenciar Importações Absolutas de Importações Relativas (`.modulo`, `..modulo_pai`).
4. Conhecer os Pacotes de Namespace Implícitos (Implicit Namespace Packages - PEP 420).
5. Estruturar a arquitetura de módulos e pacotes em aplicações corporativas escaláveis de backend.
"""

import sys
import tempfile
from pathlib import Path


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Pacote em Python?
Um pacote é simplesmente um diretório no sistema de arquivos que agrupa múltiplos módulos relacionados.
Permite organizar o código em hierarquias com notação de ponto (`pacote.subpacote.modulo`).

Componentes de um Pacote Tradicional:
1. Pasta física no disco contendo módulos `.py`.
2. Arquivo `__init__.py`: Executado automaticamente quando o pacote é importado.
   É usado para inicializar o pacote, expor classes/funções principais e definir `__all__`.

Namespace Packages (PEP 420 - Python 3.3+):
Permitem criar pacotes distribuídos em diferentes pastas no disco sem a necessidade de um arquivo `__init__.py`.
No entanto, em projetos comerciais de backend, manter o `__init__.py` é uma boa prática recomendada.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: IMPORTAÇÕES ABSOLUTAS VS RELATIVAS
# ==========================================================
"""
Sintaxe de Importações:

1. Importação Absoluta (Recomendada pela PEP 8):
   Especifica o caminho completo a partir da raiz do projeto ou site-packages.
   Exemplo: `from meu_projeto.services.auth import Autenticador`

2. Importação Relativa:
   Utiliza pontos (`.`) para referenciar o módulo atual ou módulos superiores dentro do MESMO pacote.
   - `from . import helpers` (Mesmo diretório)
   - `from ..models import Usuario` (Diretório pai)
   - `from ...config import SETTINGS` (Diretório avô)
   Nota: Importações relativas funcionam APENAS dentro de pacotes importados, nunca em scripts executados diretamente no terminal!
"""


def demonstrar_conceito_pacotes() -> None:
    print("\n--- 1. FUNDAMENTOS: Estrutura de Pacotes ---")
    print("Estrutura recomendada de um pacote backend:")
    print("""
    meu_pacote/
    |-- __init__.py
    |-- modulo_a.py
    |-- modulo_b.py
    +-- subpacote/
        |-- __init__.py
        +-- payment_service.py  # usa: from ..core.database import db
        +-- payment_service.py
    """)


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: CRIANDO UM PACOTE DINÂMICO
# ==========================================================
def demonstrar_criacao_pacote_dinamico() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Pacote Dinâmico com __init__.py e __all__ ---")

    dir_temp = Path(tempfile.gettempdir()) / "meu_pacote_demo"
    dir_temp.mkdir(exist_ok=True)

    # 1. Criar __init__.py definindo a API pública
    init_file = dir_temp / "__init__.py"
    init_file.write_text(
        'from .calculadora import somar\n__all__ = ["somar"]\n', encoding="utf-8"
    )

    # 2. Criar modulo interno
    calc_file = dir_temp / "calculadora.py"
    calc_file.write_text(
        "def somar(a: int, b: int) -> int:\n    return a + b\n\ndef _privado(): pass\n",
        encoding="utf-8",
    )

    # Adicionar diretório temporário ao sys.path para testar import
    if str(dir_temp.parent) not in sys.path:
        sys.path.insert(0, str(dir_temp.parent))

    # Importando o pacote dinâmico
    import meu_pacote_demo

    print(f"Pacote importado: {meu_pacote_demo}")
    print(f"Funcao exposta via __init__.py: {meu_pacote_demo.somar(10, 20)}")
    print(f"Simbolos expostos em __all__: {getattr(meu_pacote_demo, '__all__', [])}")

    # Cleanup
    init_file.unlink()
    import shutil
    if dir_temp.exists():
        shutil.rmtree(dir_temp)


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class PackageRegistryService:
    """Simula inspeção de metadados de pacotes instalados no ambiente de produção."""

    @staticmethod
    def inspecionar_pacote(modulo_objeto: Any) -> dict[str, Any]:
        return {
            "nome": getattr(modulo_objeto, "__name__", "desconhecido"),
            "arquivo_init": getattr(modulo_objeto, "__file__", "namespace_package"),
            "subcaminhos": list(getattr(modulo_objeto, "__path__", [])),
            "simbolos_publicos": getattr(modulo_objeto, "__all__", "Não especificado"),
        }


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Inspecionando Pacotes em Produção ---")
    import json

    metadados = PackageRegistryService.inspecionar_pacote(json)
    print("Metadados do pacote nativo 'json':")
    for k, v in metadados.items():
        print(f"  {k}: {v}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: O ATRIBUTO __PATH__
# ==========================================================
"""
Como o CPython diferencia um Módulo de um Pacote:
1. Módulos simples possuem o atributo `__file__`, mas NÃO possuem o atributo `__path__`.
2. Pacotes possuem a propriedade especial `__path__` (uma lista contendo o caminho do diretório do pacote no disco).
3. Ao encontrar `__path__`, o CPython sabe que pode continuar a busca de sub-módulos dentro daquele diretório.
"""


def demonstrar_internamente_path_atributo() -> None:
    print("\n--- 4. INTERNO: Diferença entre Módulo e Pacote (__path__) ---")
    import math  # Módulo simples em C
    import urllib  # Pacote contendo sub-módulos (request, parse, etc)

    has_path_math = hasattr(math, "__path__")
    has_path_urllib = hasattr(urllib, "__path__")

    print(f"O modulo 'math' possui __path__? {has_path_math} (É um Módulo simples)")
    print(f"O modulo 'urllib' possui __path__? {has_path_urllib} (É um Pacote!)")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Importação de Pacote com sub-módulos: O(K) de tempo na primeira chamada (onde K é o tempo de execução do `__init__.py` e dos submódulos).
- Resolução de Namespace: Busca em `sys.modules` com custo O(1) [Tabela Hash].
- `__all__`: Filtra quais símbolos são importados em `from pacote import *`, reduzindo poluição de memória.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Importações relativas profundas difíceis de rastrear
    print("[X] Nao-Pythonic (Relative Imports excessivos):")
    print("  from .....core.utils.helpers import formatar_data  # Antipadrão! Quebra fácil ao mover arquivos.")

    # [OK] PYTHONIC: Importações Absolutas a partir do diretório raiz
    print("\n[OK] Pythonic (Absolute Imports - PEP 8):")
    print("  from meu_projeto.core.utils.helpers import formatar_data  # Limpo e autodocumentável!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Prefira SEMPRE Importações Absolutas (`from meu_app.models import User`) em vez de relativas (`from ..models import User`).
2. Utilize `__all__` no `__init__.py` do seu pacote para controlar o que é público e ocultar detalhes internos de implementação.
3. Mantenha os arquivos `__init__.py` o mais enxutos possível. Evite colocar regras de negócio pesadas dentro do `__init__.py`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: ImportError ao tentar executar arquivo com import relativo diretamente
    # `python meu_pacote/submodulo.py`
    print("[!] Armadilha 1: Executar um sub-módulo contendo import relativo diretamente no terminal resulta em:")
    print("    ImportError: attempted relative import with no known parent package")
    print("    Solução: Execute a partir do diretório raiz usando o argumento de módulo: python -m meu_pacote.submodulo")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a finalidade do atributo `__all__` em um pacote Python e qual seu comportamento no `from pacote import *`?"
A: "O atributo `__all__` é uma lista de strings definida no `__init__.py` (ou em qualquer módulo) que declara quais
    símbolos (funções, classes, variáveis) são exportados publicamente.
    Quando alguém executa `from pacote import *`, APENAS os elementos listados em `__all__` serão importados.
    Se `__all__` não estiver definido, o `import *` importa todos os nomes que não comecem com underline (`_`)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma estrutura de diretórios temporária representando um pacote `ecommerce` com subpacotes `pedidos` e `produtos`.
# Exercício 2: Escreva o arquivo `__init__.py` do pacote `ecommerce` usando `__all__` para expor apenas a classe `Pedido`.
# Exercício 3: Escreva uma função que receba a referência de um pacote importado e liste todos os seus submódulos disponíveis.


def main() -> None:
    print("==========================================================")
    print("  AULA 29: PACOTES EM PYTHON, __INIT__.PY E IMPORTAÇÕES")
    print("==========================================================")
    demonstrar_conceito_pacotes()
    demonstrar_criacao_pacote_dinamico()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_path_atributo()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 29 executado com sucesso.")


if __name__ == "__main__":
    main()
