"""
25_arquivos.py - Manipulação de Arquivos, I/O Buffering, Streams e Context Managers

Objetivos:
1. Dominar o I/O de arquivos em Python utilizando a instrução `open()` e modos de abertura (`r`, `w`, `a`, `rb`, `wb`).
2. Garantir o fechamento determinístico de recursos utilizando o Gerenciador de Contexto `with`.
3. Processar arquivos de grande porte em partes (Chunking/Streaming) mantendo uso de memória RAM O(1).
4. Trabalhar com buffers em memória usando o módulo `io` (`StringIO`, `BytesIO`).
5. Evitar vazamentos de File Descriptors no sistema operacional e erros de codificação de caracteres.
"""

import io
import os
import tempfile


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Manipulação de Arquivos (I/O) em Python?
I/O (Input/Output) de arquivos é o processo de interagir com o sistema de arquivos do Sistema Operacional
para ler ou gravar dados no disco rígido/SSD.

Modos de Abertura Principais:
- 'r' (Read): Leitura (padrão). Lança FileNotFoundError se o arquivo não existir.
- 'w' (Write): Escrita. Sobrescreve (trunca) o arquivo se ele existir ou cria um novo.
- 'a' (Append): Anexo. Escreve dados ao final do arquivo existente sem apagar seu conteúdo.
- 'b' (Binary): Modo binário. Combinado com r/w (ex: 'rb', 'wb') para imagens, PDFs e executáveis.
- '+' (Update): Permite leitura e escrita simultâneas (ex: 'r+').

Regra Crítica: Sempre especifique o parâmetro `encoding='utf-8'` ao trabalhar com arquivos de texto
para evitar inconsistências entre Windows, Linux e macOS.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: GERENCIADOR DE CONTEXTO
# ==========================================================
def demonstrar_leitura_escrita_basica() -> None:
    print("\n--- 1. FUNDAMENTOS: Abertura com Gerenciador de Contexto 'with' ---")

    caminho_temp = os.path.join(tempfile.gettempdir(), "exemplo_arquivo_test.txt")

    # 1. Escrita de Arquivo
    with open(caminho_temp, mode="w", encoding="utf-8") as arquivo:
        arquivo.write("Linha 1: Introducao ao I/O em Python\n")
        arquivo.write("Linha 2: Manipulacao segura com 'with'\n")
        arquivo.write("Linha 3: Suporte total a caracteres UTF-8: Acentuação [OK]\n")

    print(f"Arquivo temporario criado em: {caminho_temp}")

    # 2. Leitura Completa de Arquivo
    with open(caminho_temp, mode="r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print("\nConteudo lido do arquivo:")
    print(conteudo)

    # Cleanup do arquivo de teste
    if os.path.exists(caminho_temp):
        os.remove(caminho_temp)


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: LEITURA EM CHUNKS E IO EM MEMÓRIA
# ==========================================================
def demonstrar_chunks_e_stringio() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Processamento em Chunks & StringIO ---")

    # 1. Leitura de Grandes Arquivos em Chunks de Bytes/Caracteres
    caminho_temp = os.path.join(tempfile.gettempdir(), "dados_grande_test.txt")
    with open(caminho_temp, "w", encoding="utf-8") as f:
        f.write("A" * 100 + "\n" + "B" * 100)

    print("Lendo arquivo em blocos (Chunks de 32 bytes):")
    with open(caminho_temp, "r", encoding="utf-8") as f:
        while chunk := f.read(32):  # Walrus operator :=
            print(f"  [Chunk {len(chunk)} chars]: {chunk[:10]}...")

    os.remove(caminho_temp)

    # 2. StringIO: Simulação de Arquivos em Memória RAM (Essencial para Testes Unitários)
    buffer_memoria = io.StringIO()
    buffer_memoria.write("Coluna1,Coluna2,Coluna3\n")
    buffer_memoria.write("Valor1,100,True\n")
    buffer_memoria.seek(0)  # Rebobina o ponteiro para o início

    print("\nConteudo do Buffer StringIO em memoria:")
    print(buffer_memoria.read())


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class LogAggregatorService:
    """Serviço backend de processamento streaming de arquivos de log sem carregar na RAM."""

    @staticmethod
    def filtrar_erros_log(caminho_origem: str, caminho_destino: str) -> int:
        contagem_erros = 0

        with open(caminho_origem, "r", encoding="utf-8") as f_in:
            with open(caminho_destino, "w", encoding="utf-8") as f_out:
                # O próprio objeto de arquivo 'f_in' é um iterador linha-a-linha (Memory O(1))
                for linha in f_in:
                    if "[ERROR]" in linha or "[CRITICAL]" in linha:
                        f_out.write(linha)
                        contagem_erros += 1

        return contagem_erros


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Log Aggregator Streaming ---")

    dir_temp = tempfile.gettempdir()
    path_in = os.path.join(dir_temp, "app_logs_in.log")
    path_out = os.path.join(dir_temp, "app_errors_out.log")

    # Criando mock de log
    with open(path_in, "w", encoding="utf-8") as f:
        f.write("[INFO] Servidor iniciado\n")
        f.write("[ERROR] Falha ao conectar no Banco de Dados Postgres\n")
        f.write("[INFO] Requisicao recebida GET /users\n")
        f.write("[CRITICAL] Memoria RAM acima de 95%\n")

    erros_encontrados = LogAggregatorService.filtrar_erros_log(path_in, path_out)
    print(f"Processamento concluído. {erros_encontrados} registros de erro salvos.")

    # Exibindo resultado
    with open(path_out, "r", encoding="utf-8") as f:
        print(f.read().strip())

    # Cleanup
    os.remove(path_in)
    os.remove(path_out)


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE
# ==========================================================
"""
Como o I/O de Arquivos funciona no CPython e OS:
1. Quando `open()` é chamado, o CPython solicita uma chamada de sistema (syscall `open()` no Unix / `CreateFile()` no Windows)
   retornando um File Descriptor (um número inteiro que representa a tabela de arquivos do processo).
2. Gerenciador de Contexto (`with`): Ao sair do bloco `with`, o método dunder `__exit__` é chamado automaticamente,
   invocando `arquivo.close()`. Isso garante a liberação imediata do File Descriptor mesmo se ocorra uma exceção.
3. Buffering: O CPython gerencia buffers de leitura/escrita em C (geralmente blocos de 4KB u 8KB)
   para minimizar a quantidade de acessos físicos ao disco rígido.
"""


def demonstrar_internamente_file_descriptor() -> None:
    print("\n--- 4. INTERNO: Inspeção de File Descriptors ---")
    caminho_temp = os.path.join(tempfile.gettempdir(), "fd_test.txt")

    with open(caminho_temp, "w", encoding="utf-8") as f:
        print(f"File Descriptor ativo no SO: {f.fileno()}")
        print(f"Arquivo fechado dentro do with? {f.closed}")

    print(f"Arquivo fechado fora do with? {f.closed}")
    os.remove(caminho_temp)


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Leitura Completa (`arquivo.read()`): Tempo O(N), Espaço O(N) onde N é o tamanho do arquivo em bytes. Perigoso para arquivos de múltiplos GB!
- Leitura Linha a Linha (`for linha in arquivo:`): Tempo O(N), Espaço O(M) onde M é o tamanho da maior linha (praticamente O(1)).
- Leitura por Chunks (`arquivo.read(chunk_size)`): Tempo O(N), Espaço O(chunk_size) -> O(1) constante.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    caminho_temp = os.path.join(tempfile.gettempdir(), "comp_test.txt")
    with open(caminho_temp, "w", encoding="utf-8") as f:
        f.write("Linha 1: Configuração do Sistema [SUCCESS]\n")

    # [X] NÃO-PYTHONIC: Abertura manual sem with e readlines() desnecessário
    print("[X] Nao-Pythonic (sem with, perigo de vazamento de arquivo):")
    f_manual = open(caminho_temp, "r", encoding="utf-8")
    linhas_manual = f_manual.readlines()  # Carrega todas as linhas em uma lista na RAM
    for l in linhas_manual:
        _ = l.strip()
    f_manual.close()

    # [OK] PYTHONIC: Gerenciador de Contexto 'with' e iteração direta no arquivo
    print("\n[OK] Pythonic:")
    with open(caminho_temp, "r", encoding="utf-8") as f_py:
        for linha in f_py:  # Iteração streaming (Memory O(1))
            print(f"  Linha: {linha.strip()}")

    os.remove(caminho_temp)


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. NUNCA abra arquivos sem utilizar a instrução `with open(...)`. Ela previne que o arquivo permaneça bloqueado no sistema operacional.
2. Sempre passe o parâmetro `encoding='utf-8'` explicitamente. O padrão no Windows pode variar para 'cp1252', causando erros.
3. Para arquivos muito grandes (> 500 MB), nunca use `f.read()` nem `f.readlines()`. Utilize `for linha in f:` ou `f.read(chunk_size)`.
4. Ao escrever dados sensíveis, garanta a descarga do buffer usando `f.flush()` ou `os.fsync(f.fileno())`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: FileNotFoundError ao tentar ler arquivo inexistente
    try:
        with open("caminho_fantasma_12345.txt", "r", encoding="utf-8") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print(f"[!] Armadilha 1 (FileNotFoundError): {e}")

    # Armadilha 2: Tentar escrever em um arquivo aberto em modo de apenas leitura ('r')
    caminho_temp = os.path.join(tempfile.gettempdir(), "read_only_test.txt")
    with open(caminho_temp, "w", encoding="utf-8") as f:
        f.write("teste")

    try:
        with open(caminho_temp, "r", encoding="utf-8") as f:
            f.write("novo conteudo")  # Lança UnsupportedOperation
    except Exception as e:
        print(f"[!] Armadilha 2 ({type(e).__name__}): Nao e possivel escrever em modo 'r' -> {e}")

    os.remove(caminho_temp)


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como você faria para processar um arquivo de log de 50 GB em uma máquina que possui apenas 4 GB de memória RAM em Python?"
A: "Utilizaria a abordagem de I/O em streaming. Em Python, o objeto retornado por `open()` é um iterador.
    Ao iterar linha a linha (`for linha in arquivo:`) ou utilizar `arquivo.read(chunk_size)`, o Python lê pequenos
    blocos mantidos no buffer interno sem carregar o arquivo inteiro na memória RAM.
    Isso mantém a complexidade de espaço constante O(1), permitindo processar arquivos de qualquer tamanho sem estouro de memória (Out of Memory - OOM)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um programa que conte a quantidade total de linhas e caracteres de um arquivo de texto.
# Exercício 2: Escreva uma função `copiar_arquivo_binario(origem: str, destino: str)` que copie uma imagem usando o modo `'rb'` e `'wb'` em chunks de 4096 bytes.
# Exercício 3: Implemente uma função que leia um arquivo de configuração `.env` no formato `CHAVE=VALOR` e retorne um dicionário Python.


def main() -> None:
    print("==========================================================")
    print("  AULA 25: MANIPULAÇÃO DE ARQUIVOS E STREAMING I/O")
    print("==========================================================")
    demonstrar_leitura_escrita_basica()
    demonstrar_chunks_e_stringio()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_file_descriptor()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 25 executado com sucesso.")


if __name__ == "__main__":
    main()
