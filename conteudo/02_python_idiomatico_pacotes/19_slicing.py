"""
19_slicing.py - Fatiamento Avançado de Sequências (Slicing, Stride, Objetos slice e Memória)

Objetivos:
1. Dominar a sintaxe completa de fatiamento `sequence[start:stop:step]` em Python.
2. Entender o comportamento de passos negativos (`stride` negativo) e inversão de sequências.
3. Compreender a alocação de memória: Shallow Copy vs Views com `memoryview`.
4. Utilizar o objeto nativo `slice()` para criar fatiamentos reutilizáveis e legíveis.
5. Aplicar slicing em cenários reais de paginação de dados e processamento em lotes (batching).
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Slicing?
Slicing (Fatiamento) é uma operação nativa de Python que permite extrair sub-sequências de coleções
ordenadas (listas, tuplas, strings, bytes) especificado um intervalo `[start:stop:step]`.

Características fundamentais:
1. Limites inclusivo/exclusivo: O índice `start` é INCLUSIVO, enquanto `stop` é EXCLUSIVO.
2. Segurança contra IndexError: Ao contrário do acesso direto por índice (`lista[10]`), o slicing
   é extremamente tolerante a índices fora dos limites.
3. Criação de Cópias Superficiais (Shallow Copy): O fatiamento em listas e tuplas gera uma nova
   instância contendo referências para os mesmos elementos originais.
4. Passos negativos (`step < 0`): Invertem o sentido da iteração ao longo da sequência.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS
# ==========================================================
def demonstrar_sintaxe_fundamentos() -> None:
    print("\n--- 1. FUNDAMENTOS: Sintaxe [start:stop:step] ---")
    numeros: list[int] = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Sintaxe básica: do índice 2 até o 5 (exclusivo)
    sub_lista: list[int] = numeros[2:5]
    print(f"Original: {numeros}")
    print(f"numeros[2:5] -> {sub_lista}")

    # Omitindo limites
    primeiros_tres = numeros[:3]
    ultimos_tres = numeros[-3:]
    print(f"Primeiros 3 [:3]: {primeiros_tres}")
    print(f"Ultimos 3 [-3:]: {ultimos_tres}")

    # Utilizando stride (passo)
    pares = numeros[::2]
    print(f"Elementos em índices pares [::2]: {pares}")

    # Stride negativo (Inversão)
    invertida = numeros[::-1]
    print(f"Lista totalmente invertida [::-1]: {invertida}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: OBJETOS SLICE REUTILIZÁVEIS
# ==========================================================
def demonstrar_objetos_slice() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Objeto slice() Nomenclaturado ---")

    # Em vez de hardcodar indices como dados[0:4], podemos usar objetos slice nomeados
    CABECALHO = slice(0, 2)
    CORPO_PAYLOAD = slice(2, 6)
    RODAPE = slice(6, None)

    registro_registro_bruto: list[str] = [
        "HEADER_v1", "2026-08-19", "CLIENTE_A", "R$ 1500.00", "PAGO", "BOLETO", "CHECKSUM_OK", "END"
    ]

    print(f"Cabecalho extraido: {registro_registro_bruto[CABECALHO]}")
    print(f"Corpo do registro: {registro_registro_bruto[CORPO_PAYLOAD]}")
    print(f"Rodape e metadados: {registro_registro_bruto[RODAPE]}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def paginar_resultados(dados: list[Any], pagina: int, tamanho_pagina: int) -> list[Any]:
    """Realiza paginação de lista em memória via slicing idiomático."""
    if pagina < 1 or tamanho_pagina < 1:
        return []

    inicio = (pagina - 1) * tamanho_pagina
    fim = inicio + tamanho_pagina
    return dados[inicio:fim]


def demonstrar_paginacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Paginação de Resultados em Memória ---")
    registros_banco = [f"Usuario_{i:03d}" for i in range(1, 25)]

    pagina_1 = paginar_resultados(registros_banco, pagina=1, tamanho_pagina=5)
    pagina_2 = paginar_resultados(registros_banco, pagina=2, tamanho_pagina=5)

    print(f"Pagina 1 (size 5): {pagina_1}")
    print(f"Pagina 2 (size 5): {pagina_2}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: MEMÓRIA E VIEW
# ==========================================================
"""
Como o Python executa Slicing:
1. Quando executamos `lista[a:b]`, o Python chama internamente `lista.__getitem__(slice(a, b))`.
2. Para objetos mutáveis (`list`), o fatiamento ALOCA uma nova estrutura de dados contendo
   ponteiros para os mesmos objetos (Shallow Copy). Alterar um objeto mutável dentro da sublista afetará o original!
3. Para dados binários/grandes buffers (`bytes`, `bytearray`), o slicing tradicional aloca novas cópias de memória.
   Para evitar isso e ter custo de cópia zero (Zero-Copy), utiliza-se o objeto nativo `memoryview`.
"""


def demonstrar_memoryview_zero_copy() -> None:
    print("\n--- 4. INTERNO: Zero-Copy com memoryview ---")
    # Criando um buffer grande de bytes (ex: imagem ou arquivo recebido na rede)
    buffer_grande = bytearray(b"HEADER_METADADOS_PAYLOAD_ASSINATURA")

    # Criando uma view sem duplicar os bytes na memória RAM
    view = memoryview(buffer_grande)
    sub_view_payload = view[17:24]

    print(f"Conteudo da subview (Zero-Copy): {sub_view_payload.tobytes().decode()}")
    print(f"Tipo da estrutura: {type(sub_view_payload).__name__}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade de Slicing:
- Tempo: O(k), onde `k` é o número de elementos fatiados (tamanho da sublista resultante).
- Espaço: O(k) de memória adicional para a nova lista/string fatiada (exceto `memoryview` que é O(1)).
- Atribuição em fatia (`lista[1:3] = [99, 100]`): O(N + K) dependendo do deslocamento dos elementos na memória.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    texto = "Python_3_12"

    # [X] NÃO-PYTHONIC: Loop manual para inverter string ou pegar os últimos caracteres
    print("[X] Nao-Pythonic (Loop manual):")
    chars_invertidos = []
    for i in range(len(texto) - 1, -1, -1):
        chars_invertidos.append(texto[i])
    texto_inv = "".join(chars_invertidos)
    print(f"  String invertida: {texto_inv}")

    # [OK] PYTHONIC: Slicing direto com stride negativo
    print("[OK] Pythonic:")
    print(f"  String invertida [::-1]: {texto[::-1]}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize `slice()` nomeado para constantes de fatiamento frequentes ou layouts fixos de arquivos posicioais.
2. Lembre-se que `lista[:]` faz uma cópia rasa (shallow copy) completa de `lista`.
3. Cuidado ao usar passos negativos com limites explícitos: `lista[5:2:-1]` exige que o inicio seja maior que o fim!
4. Para fatiar sem alterar a referência da lista original, use atribuição em fatia: `lista[:] = [1, 2, 3]`.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Confusão ao tentar fatiar com stride negativo mantendo ordem normal
    numeros = [10, 20, 30, 40, 50]
    # Tentar fatiar do 1 ao 4 com passo -1 resulta em lista vazia!
    resultado_vazio = numeros[1:4:-1]
    print(f"[!] Armadilha 1 (numeros[1:4:-1]): {resultado_vazio} (Retorna vazia porque start < stop!)")

    # Armadilha 2: Modificar objetos mutáveis dentro de uma fatia achando que é um deep copy
    matriz_original = [[1, 2], [3, 4]]
    fatia_copia = matriz_original[:1]
    fatia_copia[0][0] = 999  # Altera a sublista original!
    print(f"[!] Armadilha 2 (Shallow Copy): Matriz original afetada: {matriz_original}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença de performance entre `lista.reverse()`, `reversed(lista)` e `lista[::-1]`?"
A: "1. `lista.reverse()` altera a própria lista in-place (in-place mutation), retornando None. Tempo O(N), Espaço O(1).
    2. `reversed(lista)` retorna um ITERADOR sem copiar a lista. Tempo O(1) de criação, Espaço O(1).
    3. `lista[::-1]` cria uma NOVA LISTA contendo a cópia invertida. Tempo O(N), Espaço O(N).
    Escolha `reversed()` para apenas iterar, `.reverse()` para alterar a lista original e `[::-1]` se precisar de uma cópia independente."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função `is_palindromo(texto: str) -> bool` que verifica se uma palavra é um palíndromo
#              removendo espaços e ignorando maiúsculas/minúsculas usando slicing `[::-1]`.
# Exercício 2: Escreva uma função `trocar_primeiro_e_ultimo(lista: list[Any]) -> list[Any]` que altera o primeiro
#              e o último elemento de posição usando slicing e unpacking sem modificar a lista original.
# Exercício 3: Crie um gerador `gerar_batches(colecao: list[Any], tamanho_batch: int)` que yielding fatias da lista
#              até consumi-la totalmente.


def main() -> None:
    print("==========================================================")
    print("  AULA 19: FATIAMENTO AVANÇADO DE SEQUÊNCIAS (SLICING)")
    print("==========================================================")
    demonstrar_sintaxe_fundamentos()
    demonstrar_objetos_slice()
    demonstrar_paginacao_backend()
    demonstrar_memoryview_zero_copy()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 19 executado com sucesso.")


if __name__ == "__main__":
    main()
