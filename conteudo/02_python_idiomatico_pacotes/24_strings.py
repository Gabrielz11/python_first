"""
24_strings.py - Strings, Formatação Avançada, Encodings UTF-8/Bytes e Imutabilidade

Objetivos:
1. Compreender a imutabilidade das strings em Python e os impactos no gerenciamento de memória.
2. Dominar a sintaxe avançada de f-strings (alinhamento, precisão numérica, especificação de data e `{var=}`).
3. Diferenciar o tipo `str` (Unicode textual) do tipo `bytes` (sequência de octetos) e converter via `.encode()` / `.decode()`.
4. Utilizar os métodos nativos mais performáticos de manipulação de strings (`partition`, `join`, `split`).
5. Desenvolver parsers de logs e higienizadores de payloads em aplicações de backend.
"""

from datetime import datetime


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma String em Python?
Em Python 3, o tipo `str` representa uma sequência IMUTÁVEL de caracteres Unicode (padrão UTF-8 por convenção).
Como objetos `str` são imutáveis, qualquer operação de modificação (como `.replace()`, `.upper()`, concatenação `+`)
NÃO altera a string original, mas sim gera uma NOVA instância de string na memória Heap.

Tipos em Destaque:
- `str`: Texto legível composto por code points Unicode (ex: "Python 🐍").
- `bytes`: Sequência bruta de bytes de 8 bits (0-255) usada para I/O de arquivos, soquetes de rede e criptografia (ex: b"Python").
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: F-STRINGS AVANÇADAS
# ==========================================================
def demonstrar_fstrings_avancadas() -> None:
    print("\n--- 1. FUNDAMENTOS: f-strings Avançadas (Python 3.8+) ---")

    nome = "gabriel"
    valor_transacao = 15450.758
    data_atual = datetime(2026, 8, 19, 14, 30, 0)

    # 1. Alinhamento e Preenchimento (Padding)
    # ^ centralizado, > a direita, < a esquerda com caractere de preenchimento
    print(f"Alinhado a direita: {'[OK]':>15}")
    print(f"Preenchimento com tracos: {nome.capitalize():-^20}")

    # 2. Formatação Numérica (Moeda e Separador de milhar)
    print(f"Valor Formatado: R$ {valor_transacao:,.2f}")

    # 3. Formatação de Datas
    print(f"Data Formatada: {data_atual:%d/%m/%Y às %H:%h}")

    # 4. Self-Documenting Expression {var=} (Essencial para Debugging)
    largura = 1920
    altura = 1080
    print(f"Debug: {largura=} | {altura=} | {largura * altura=}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: UNICODE VS BYTES & MÉTODOS
# ==========================================================
def demonstrar_bytes_e_metodos() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: str vs bytes & partition ---")

    # Conversão de Unicode para Bytes (Encode) e Bytes para Unicode (Decode)
    texto_original = "  Python 3.12 [ROCKET] High Performance  "
    bytes_utf8 = texto_original.encode("utf-8")
    texto_decodificado = bytes_utf8.decode("utf-8")

    print(f"String original ({len(texto_original)} chars): {texto_original}")
    print(f"Bytes UTF-8 ({len(bytes_utf8)} bytes): {bytes_utf8}")
    print(f"Decodificado com sucesso: {texto_decodificado}")

    # Método partition() em vez de split()[0] (Mais rápido e seguro)
    header_raw = "Authorization: Bearer eyJhbGciOiJIUzI1NiIn..."
    chave, separador, valor = header_raw.partition(": ")
    print(f"\npartition() -> Header Chave: '{chave}', Valor: '{valor[:20]}...'")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ParserLogProducao:
    """Parser de alta performance para registros de logs em formato NGINX/Apache."""

    @staticmethod
    def sanitizar_linha_log(linha_bruta: str) -> dict[str, str]:
        # Exemplo: "2026-08-19 18:30:00 | INFO | /api/v1/users | 200 OK"
        partes = [p.strip() for p in linha_bruta.split("|")]
        if len(partes) < 4:
            return {"status": "INVALIDO"}

        data_hora, nivel, endpoint, status_http = partes
        return {
            "timestamp": data_hora,
            "nivel": nivel.upper(),
            "endpoint": endpoint.lower(),
            "status_http": status_http,
        }


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Parser de Logs ---")
    log_exemplo = "  2026-08-19 18:30:00 | info | /API/v1/USERS | 200 OK  "
    log_processado = ParserLogProducao.sanitizar_linha_log(log_exemplo)

    print("Log Sanitizado:")
    for k, v in log_processado.items():
        print(f"  {k}: {v}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: STRING INTERNING E BENCHMARK
# ==========================================================
"""
Como o Python gerencia Strings na Memória (CPython):
1. String Interning: O CPython reutiliza automaticamente instâncias de strings pequenas e imutáveis
   que pareçam identificadores (contendo letras, números e underlines) para economizar RAM.
2. Layout C-Struct (PEP 393): CPython armazena strings de forma compacta adaptável na memória:
   - ASCII (1 byte por caractere).
   - UCS-2 (2 bytes por caractere).
   - UCS-4 (4 bytes por caractere para emojis e caracteres complexos).
3. Concatenação em Loop: O uso de `s += 'texto'` dentro de um loop for força o CPython a realocar
   e copiar a string repetidamente, resultando em complexidade temporal quadrática O(N²).
"""


def demonstrar_interning_e_concat() -> None:
    print("\n--- 4. INTERNO: String Interning e Concatenação O(N) ---")

    # String Interning
    s1 = "python_code"
    s2 = "python_code"
    print(f"s1 is s2? {s1 is s2} (CPython reutilizou o mesmo id de memoria)")

    # Forma O(N) correta de concatenar strings: Lista + join()
    palavras = ["Python", "é", "uma", "linguagem", "excelente."]
    frase = " ".join(palavras)  # O(N) de tempo e O(N) de espaço
    print(f"Resultado do join(): {frase}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Concatenação em loop `s += char`: Tempo O(N²), Espaço O(N). antipadrão grave!
- Concatenação via `"".join(lista_de_strings)`: Tempo O(N), Espaço O(N).
- Busca de substrings (`"texto" in frase` ou `frase.find()`): Algoritmo Boyer-Moore-Horspool em CPython -> Tempo médio O(N).
- Fatiamento de String (`s[a:b]`): Tempo O(K), Espaço O(K).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    tokens = ["usr", "1049", "auth", "granted"]

    # [X] NÃO-PYTHONIC: Concatenação de string em loop usando +
    print("[X] Nao-Pythonic (s += token em loop):")
    resultado_manual = ""
    for t in tokens:
        resultado_manual += t + "/"
    print(f"  Resultado: {resultado_manual}")

    # [OK] PYTHONIC: str.join()
    print("\n[OK] Pythonic (str.join):")
    resultado_py = "/".join(tokens) + "/"
    print(f"  Resultado (join): {resultado_py}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Nunca acumule strings dentro de loops com o operador `+`. Adicione as partes em uma lista e use `"".join(lista)`.
2. Prefira `str.startswith()` e `str.endswith()` em vez de fatiamento `s[:3] == 'abc'` para checar prefixos/sufixos.
3. Use `str.partition()` em vez de `str.split()` quando precisar apenas da primeira ocorrência de um separador.
4. Lembre-se sempre de tratar encodings explicitamente (`encoding='utf-8'`) ao ler/escrever arquivos ou enviar bytes pela rede.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: UnicodeDecodeError / UnicodeEncodeError ao misturar bytes e str
    dado_binario = b"Caf\xe9"  # ISO-8859-1 (Latin-1)

    try:
        # Tentar decodificar bytes Latin-1 usando UTF-8 pode falhar
        _ = dado_binario.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"[!] Armadilha 1 (UnicodeDecodeError): {e}")

    # Decodificação correta especificando o encoding correto
    print(f"[OK] Decodificacao correta com latin-1: {dado_binario.decode('latin-1')}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que a concatenação de strings usando `+=` dentro de um loop de 100.000 iterações é extremamente lenta em Python?"
A: "Como as strings em Python são IMUTÁVEIS, cada operação `s += novo_texto` precisa alocar um novo bloco de memória RAM
    e copiar todo o conteúdo da string anterior mais o novo trecho.
    Para N iterações, isso exige 1 + 2 + 3 + ... + N cópias de caracteres, resultando em complexidade de tempo O(N²).
    A solução é usar uma lista `.append()` (complexidade O(1) amortizada) e ao final invocar `"".join(lista)`, rodando em O(N)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função `formatar_moeda(valor: float) -> str` que retorne o valor formatado no padrão brasileiro (ex: R$ 1.250,50) usando f-strings.
# Exercício 2: Crie um higienizador de nome de arquivo `sanitizar_nome_arquivo(nome: str) -> str` que remova espaços nas pontas, substitua espaços internos por sublinhados e converta para minúsculas.
# Exercício 3: Escreva um programa que receba uma frase e conte a frequência de cada palavra ignorando pontuação e diferenças entre maiúsculas e minúsculas.


def main() -> None:
    print("==========================================================")
    print("  AULA 24: STRINGS, FORMATAÇÃO AVANÇADA E ENCODINGS")
    print("==========================================================")
    demonstrar_fstrings_avancadas()
    demonstrar_bytes_e_metodos()
    demonstrar_aplicacao_backend()
    demonstrar_interning_e_concat()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 24 executado com sucesso.")


if __name__ == "__main__":
    main()
