"""
06_loops.py - Estruturas de Repetição (for, while, break, continue, pass) e o Bloco else em Laços

Objetivos:
1. Dominar iterações com laços `for` e `while`.
2. Utilizar corretamente as instruções de controle `break`, `continue` e `pass`.
3. Compreender o recurso único do Python: o bloco `else` associado a laços `for` e `while`.
4. Evitar laços infinitos e compreender os custos computacionais da iteração.
"""



# ==========================================================
# 1. CONCEITO: O que é o `for ... else` e `while ... else`?
# ==========================================================
"""
O Bloco `else` em Laços de Repetição em Python:
Diferente do `else` em condicionais, o bloco `else` acoplado a um `for` ou `while` executa
APENAS E TÃO SOMENTE SE o laço for concluído NATURALMENTE (percorreu todos os itens ou a condição do while tornou-se falsa)
SEM ter encontrado uma instrução `break`!

Caso de Uso Ideal:
Mecanismos de BUSCA / PROCURA. Se você varre uma lista procurando um item e o encontra, executa `break`.
Se o item NUNCA for encontrado, o laço encerra e o bloco `else` é acionado para tratar a ausência do item.
"""


def demonstrar_for_else_busca(servidores: list[str], alvo: str) -> None:
    print(f"\n--- 1. CONCEITO: Buscando servidor '{alvo}' ---")

    # O laço for em Python é um "for-each" por padrão (itera diretamente sobre elementos da sequência)
    for servidor in servidores:
        print(f"  Checando status de: {servidor}")
        if servidor == alvo:
            print(f"  [SUCESSO] Servidor '{alvo}' encontrado e responsivo! Interrompendo laço com break.")
            break
    else:
        # Executa APENAS se o laço terminou sem nenhum break!
        print(f"  [FALHA] Varredura completa. Servidor '{alvo}' NAO foi encontrado na rede!")


# ==========================================================
# 2. EXEMPLOS: `while`, `break`, `continue` e `pass`
# ==========================================================
def demonstrar_instrucoes_controle() -> None:
    print("\n--- 2. EXEMPLOS: break, continue e pass ---")

    # 1. Uso do `continue` para pular iterações (processar apenas números pares)
    print("Processando apenas numeros pares (usando continue):")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares: list[int] = []

    for num in numeros:
        if num % 2 != 0:
            continue  # Pula o restante do bloco do laço para números ímpares
        pares.append(num)

    print(f"Numeros pares filtrados: {pares}")

    # 2. Uso do `pass` como placeholder nulo para código futuro
    for _ in range(2):
        pass  # Nenhuma operação. Mantém a sintaxe válida.

    # 3. Laço `while` com acumulador e segurança contra laço infinito
    print("\nSimulação de Retry com while loop:")
    tentativas = 0
    max_tentativas = 3
    sucesso = False

    while tentativas < max_tentativas and not sucesso:
        tentativas += 1
        print(f"  Tentativa #{tentativas} de conexão...")
        if tentativas == 2:
            sucesso = True
            print("  Conexão estabelecida com sucesso!")
    else:
        if not sucesso:
            print("  [ALERT] Todas as tentativas esgotadas!")


# ==========================================================
# 3. EXEMPLO PRÁTICO: Verificador de Saúde de Serviços (Health Checker)
# ==========================================================
def verificar_saude_microservicos(servicos: dict[str, str]) -> dict[str, list[str]]:
    print("\n--- 3. EXEMPLO PRÁTICO: Health Checker de Produção ---")

    relatorio: dict[str, list[str]] = {"online": [], "offline": []}

    for nome_servico, url in servicos.items():
        # Simulação de checagem
        if "manutencao" in url:
            print(f"  Pulando servico em manutenção: {nome_servico} (usando continue)")
            continue

        if "fail" in url:
            relatorio["offline"].append(nome_servico)
        else:
            relatorio["online"].append(nome_servico)

    return relatorio


# ==========================================================
# 4. ANÁLISE DE DESEMPENHO E COMPLEXIDADE (BIG O)
# ==========================================================
"""
Complexidade de Laços de Repetição:
- Laço Simples (`for x in lista`): O(n) Temporal, onde n é o tamanho da lista.
- Laços Aninhados (`for x in lista1: for y in lista2`): O(n * m) Temporal. Se n == m, torna-se O(n²).

Atenção ao custo O(n²):
Em grandes volumes de dados (ex: 100.000 itens), um laço aninhado $O(n^2)$ fará 10.000.000.000 de iterações!
Substitua laços aninhados por dicionários ou conjuntos para reduzir a busca interna de O(n) para O(1).
"""


# ==========================================================
# 5. COMPARATIVO: CÓDIGO NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    servidores = ["srv-prod-1", "srv-prod-2", "srv-db-1"]

    # [X] NÃO-PYTHONIC (Flag booleana manual para checar se item foi encontrado):
    print("[X] Nao-Pythonic (Usando flag manual 'encontrado = False'):")
    encontrado = False
    for s in servidores:
        if s == "srv-db-1":
            encontrado = True
            break
    if not encontrado:
        print("  Servidor nao encontrado.")
    else:
        print("  Servidor encontrado com sucesso!")

    # [OK] PYTHONIC (Aproveitando o bloco `for ... else` sem flags):
    print("[OK] Pythonic (Usando for ... else nativo):")
    for s in servidores:
        if s == "srv-db-1":
            print("  Servidor encontrado com sucesso!")
            break
    else:
        print("  Servidor nao encontrado.")


# ==========================================================
# 6. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Modificar a própria lista ENQUANTO itera sobre ela!
    # Isso altera os índices internos do iterador e pula elementos!
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista original antes do laço mutável: {numeros}")

    # ❌ ERRADO:
    # for num in numeros:
    #     if num % 2 == 0:
    #         numeros.remove(num) # CUIDADO! Altera o tamanho da lista em tempo de execução!

    # ✅ CORRETO (Criar uma nova lista filtrada ou iterar sobre uma cópia `numeros[:]`):
    numeros_filtrados = [n for n in numeros if n % 2 != 0]
    print(f"Lista filtrada corretamente (sem mutacao durante iteracao): {numeros_filtrados}")


# ==========================================================
# 7. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Quando o bloco `else` acoplado a um laço `for` ou `while` é executado em Python?"
A: "O bloco `else` do laço executa APENAS quando o laço termina sua iteração completa por exaustão da sequência
    ou quando a condição do `while` se torna falsa. Se o laço for interrompido prematuramente por um `break`,
    o bloco `else` é completamente IGNORADO."
"""


# ==========================================================
# 8. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um programa que varra uma lista de transações bancárias. Se encontrar uma transação suspeita
#              (valor > 10.000), exiba um alerta e use `break`. Se nenhuma for suspeita, use o bloco `else` para exibir "Nenhuma anomalia detectada".
# Exercício 2: Escreva um laço `while` que simule a contagem regressiva de um lançamento, pulando o número 5 usando `continue`.


def main() -> None:
    print("==========================================================")
    print("  AULA 06: ESTRUTURAS DE REPETIÇÃO E O BLOCO ELSE EM LAÇOS")
    print("==========================================================")

    servidores_rede = ["srv-web-01", "srv-web-02", "srv-db-primary"]
    demonstrar_for_else_busca(servidores_rede, "srv-db-primary")  # Encontra
    demonstrar_for_else_busca(servidores_rede, "srv-cache-01")   # Não encontra (aciona else)

    demonstrar_instrucoes_controle()

    servicos_api = {
        "Auth": "https://auth.empresa.com",
        "Billing": "https://billing-manutencao.empresa.com",
        "Legacy": "https://fail-legacy.empresa.com",
    }
    res_health = verificar_saude_microservicos(servicos_api)
    print(f"Relatório de Saúde: {res_health}")

    demonstrar_comparativo()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 06 executado com sucesso.")


if __name__ == "__main__":
    main()
