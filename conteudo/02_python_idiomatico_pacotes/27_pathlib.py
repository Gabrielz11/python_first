"""
27_pathlib.py - Manipulação Orientada a Objetos do Sistema de Arquivos com pathlib

Objetivos:
1. Dominar o uso da classe `pathlib.Path` para manipulação de caminhos POO (PEP 428).
2. Substituir métodos legados do módulo `os.path` pelo uso idiomático do operador `/`.
3. Explorar propriedades essenciais de caminhos (`name`, `stem`, `suffix`, `parent`, `parts`).
4. Utilizar métodos utilitários de I/O rápido (`read_text`, `write_text`, `mkdir`, `glob`, `rglob`).
5. Desenvolver varredores de diretórios e organizadores de uploads para serviços backend.
"""

import os
from pathlib import Path
import tempfile


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é o módulo pathlib?
Introduzido na PEP 428 (Python 3.4), o `pathlib` fornece uma abordagem orientada a objetos para interagir
com caminhos do sistema de arquivos, substituindo o uso manual de strings e funções do módulo `os.path`.

Vantagens Principais:
1. Multiplataforma Automática: Abstrai diferenças de separadores entre Windows (`\`) e POSIX/Linux/macOS (`/`).
2. Operador `/` Sobregregado: Permite construir caminhos de forma elegante (`Path("/tmp") / "pasta" / "arquivo.txt"`).
3. Métodos Integrados de I/O: Permite ler e escrever arquivos sem a necessidade explícita de `open()`.
4. Tipagem Segura: Elimina bugs de manipulação incorreta de strings ao concatenar caminhos.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: PATH, OPERADOR / E PROPRIEDADES
# ==========================================================
def demonstrar_sintaxe_e_propriedades() -> None:
    print("\n--- 1. FUNDAMENTOS: pathlib.Path e Propriedades ---")

    # Construção de caminho com o operador /
    base_dir = Path(tempfile.gettempdir())
    caminho_arquivo = base_dir / "projeto_python" / "relatorios" / "financeiro_2026.csv"

    print(f"Caminho Completo: {caminho_arquivo}")
    print(f"Nome do arquivo (.name): {caminho_arquivo.name}")
    print(f"Nome sem extensao (.stem): {caminho_arquivo.stem}")
    print(f"Extensao do arquivo (.suffix): {caminho_arquivo.suffix}")
    print(f"Diretorio Pai (.parent): {caminho_arquivo.parent}")
    print(f"Partes do caminho (.parts): {caminho_arquivo.parts[-3:]}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: MKDIR, WRITE_TEXT, GLOB
# ==========================================================
def demonstrar_operacoes_diretorio() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Criacao, Leitura e Globbing ---")

    dir_teste = Path(tempfile.gettempdir()) / "pathlib_demo_dir"

    # 1. Criar diretórios (parents=True cria pais inexistentes, exist_ok=True evita erro se já existir)
    dir_teste.mkdir(parents=True, exist_ok=True)

    # 2. Escrita e Leitura Rápida de Texto (Zero Boilerplate)
    arquivo_a = dir_teste / "config.json"
    arquivo_b = dir_teste / "dados.csv"
    subfolder_log = dir_teste / "logs"
    subfolder_log.mkdir(exist_ok=True)
    arquivo_c = subfolder_log / "app.log"

    arquivo_a.write_text('{"status": "ok"}', encoding="utf-8")
    arquivo_b.write_text("id,nome\n1,Gabriel", encoding="utf-8")
    arquivo_c.write_text("[INFO] Log de teste", encoding="utf-8")

    print(f"Conteudo de config.json lido via read_text(): {arquivo_a.read_text(encoding='utf-8')}")

    # 3. Busca Recursiva com rglob()
    print("\nVarredura recursiva de arquivos com rglob('*.*'):")
    for item in dir_teste.rglob("*.*"):
        print(f"  Encontrado: {item.relative_to(dir_teste)}")

    # Cleanup
    for item in sorted(dir_teste.rglob("*"), reverse=True):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            item.rmdir()
    dir_teste.rmdir()


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class FileStorageService:
    """Serviço de armazenamento e organização de uploads de usuários em microsserviços."""

    def __init__(self, root_dir: str | Path) -> None:
        self.root_path = Path(root_dir)
        self.root_path.mkdir(parents=True, exist_ok=True)

    def salvar_upload(self, user_id: int, nome_arquivo: str, conteudo: bytes) -> Path:
        # Organiza por pastas de usuário: root/user_1001/nome_arquivo.png
        user_dir = self.root_path / f"user_{user_id}"
        user_dir.mkdir(exist_ok=True)

        target_file = user_dir / nome_arquivo
        target_file.write_bytes(conteudo)
        return target_file


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: File Storage Service ---")
    base_storage = Path(tempfile.gettempdir()) / "storage_uploads"
    storage = FileStorageService(base_storage)

    caminho_salvo = storage.salvar_upload(
        user_id=1042,
        nome_arquivo="avatar.png",
        conteudo=b"\x89PNG\r\n\x1a\n\x00_MOCK_BYTES",
    )

    print(f"Upload salvo com sucesso em: {caminho_salvo}")
    print(f"Tamanho do arquivo: {caminho_salvo.stat().st_size} bytes")

    # Cleanup
    caminho_salvo.unlink()
    caminho_salvo.parent.rmdir()
    base_storage.rmdir()


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: POSIXPATH VS WINDOWSPATH
# ==========================================================
"""
Como o pathlib é estruturado internamente (Hierarquia de Classes):
1. `PurePath`: Classe base que realiza apenas manipulação pura de strings de caminho sem acessar o disco (I/O).
   - `PurePosixPath`: Regras de caminhos no estilo Linux/macOS.
   - `PureWindowsPath`: Regras de caminhos no estilo Windows (`C:\...`).
2. `Path`: Classe concreta herdada de `PurePath` que adiciona métodos de chamada de sistema (I/O) como `.exists()`, `.mkdir()`, `.unlink()`.
   Em tempo de execução, ao instanciar `Path()`, o Python retorna uma instância de `PosixPath` ou `WindowsPath` conforme o SO.
"""


def demonstrar_internamente_pure_path() -> None:
    print("\n--- 4. INTERNO: Manipulação Pura de Caminhos de Outros SOs ---")
    from pathlib import PurePosixPath, PureWindowsPath

    win_path = PureWindowsPath("C:/Users/Gabriel/Documents/projeto/app.py")
    posix_path = PurePosixPath("/home/gabriel/projeto/app.py")

    print(f"Windows Path representado: {win_path}")
    print(f"Drive: {win_path.drive} | Partes: {win_path.parts}")
    print(f"POSIX Path representado: {posix_path}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Criação e concatenação de Path (`base / "sub"`): Tempo O(1), Espaço O(1).
- `.exists()`, `.is_file()`, `.stat()`: Chamada de sistema (syscall stat) -> Tempo O(1), Espaço O(1).
- `.glob("*.py")`: Tempo O(N) onde N é a quantidade de arquivos na pasta, Espaço O(N) para armazenar a lista de Paths.
- `.rglob("*")`: Varredura de árvore de diretórios -> Tempo O(V + E) (similar a DFS no sistema de arquivos).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    dir_base = tempfile.gettempdir()
    sub_pasta = "minha_aplicacao"
    nome_arq = "config.ini"

    # [X] NÃO-PYTHONIC: os.path.join manual e checagem via os.path.exists
    print("[X] Nao-Pythonic (modulo os.path legado):")
    caminho_legado = os.path.join(dir_base, sub_pasta, nome_arq)
    existe_legado = os.path.exists(caminho_legado)
    print(f"  Caminho string: {caminho_legado} | Existe: {existe_legado}")

    # [OK] PYTHONIC: pathlib.Path com operador /
    print("\n[OK] Pythonic (pathlib.Path):")
    caminho_py = Path(dir_base) / sub_pasta / nome_arq
    existe_py = caminho_py.exists()
    print(f"  Caminho Path: {caminho_py} | Existe: {existe_py}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre prefira `pathlib.Path` a funções do módulo `os.path` em novos projetos Python 3.
2. Utilize `parents=True` e `exist_ok=True` ao chamar `.mkdir()` para evitar exceções `FileExistsError` ou `FileNotFoundError`.
3. Lembre-se que instâncias de `Path` funcionam nativamente na maioria das funções da biblioteca padrão (`open(path)`, `json.dump(..., path)`).
4. Para obter a representação absoluta e canonicalizada de um caminho, utilize `path.resolve()`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    p = Path(tempfile.gettempdir()) / "pasta_inexistente_123" / "arquivo.txt"

    # Armadilha 1: Tentar criar arquivo em pasta pai inexistente lança FileNotFoundError
    try:
        p.write_text("teste", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"[!] Armadilha 1 (FileNotFoundError sem mkdir): {e}")

    # Armadilha 2: Tentar usar unlink() (apagar) em um diretório lança IsADirectoryError / PermissionError
    temp_dir = Path(tempfile.gettempdir()) / "demo_dir_trap"
    temp_dir.mkdir(exist_ok=True)
    try:
        temp_dir.unlink()  # unlink serve APENAS para arquivos!
    except Exception as e:
        print(f"[!] Armadilha 2 ({type(e).__name__} ao usar unlink em diretorio): {e}")
    
    temp_dir.rmdir()


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que a biblioteca `pathlib` é considerada superior ao uso tradicional de `os.path` em Python?"
A: "1. Orientação a Objetos: Trata caminhos como objetos ricos com métodos como `.read_text()`, `.suffix`, `.stat()` em vez de strings genéricas.
    2. Operador `/`: Torna a construção de subdiretórios intuitiva e imune a erros de barra invertida em diferentes sistemas operacionais.
    3. Legibilidade e Manutenibilidade: Elimina a necessidade de aninhar chamadas como `os.path.dirname(os.path.abspath(__file__))`,
       substituindo por `Path(__file__).resolve().parent`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `obter_tamanho_diretorio(caminho: Path) -> int` que percorra recursivamente um diretório usando `rglob` e retorne a soma do tamanho dos arquivos em bytes.
# Exercício 2: Escreva um programa que localize todos os arquivos `.log` em uma pasta temporária e mude a extensão de cada um para `.log.bak`.
# Exercício 3: Escreva uma função que leia um arquivo de texto via `Path.read_text()`, remova linhas em branco e salve o resultado em um novo arquivo usando `Path.write_text()`.


def main() -> None:
    print("==========================================================")
    print("  AULA 27: MANIPULAÇÃO DE CAMINHOS COM PATHLIB")
    print("==========================================================")
    demonstrar_sintaxe_e_propriedades()
    demonstrar_operacoes_diretorio()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_pure_path()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 27 executado com sucesso.")


if __name__ == "__main__":
    main()
