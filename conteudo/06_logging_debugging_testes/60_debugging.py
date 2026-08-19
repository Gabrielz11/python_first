"""
60_debugging.py - Depuração de Código, breakpoint(), pdb e Inspeção de Stack Traces

Objetivos:
1. Dominar o uso da função built-in `breakpoint()` (PEP 553 - Python 3.7+) para depuração interativa.
2. Compreender os comandos principais do depurador interativo `pdb` (`n`, `s`, `c`, `p`, `l`, `w`, `q`).
3. Extrair e formatar stack traces programaticamente utilizando o módulo nativo `traceback`.
4. Utilizar a variável de ambiente `PYTHONBREAKPOINT=0` para desativar breakpoints em produção.
5. Inspecionar frames de execução e variáveis locais dinamicamente com `sys._getframe()`.
"""

import sys
import traceback
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Debugging em Python?
Debugging (Depuração) é o processo de inspecionar o estado interno da memória, variáveis e fluxo de controle
de um programa em tempo de execução para identificar a causa raiz de comportamentos incorretos ou exceções.

Ferramentas de Depuração Nativas:
1. `breakpoint()`: Função built-in (PEP 553) que invoca automaticamente o depurador configurado (por padrão, `pdb`).
2. `pdb` (Python Debugger): O depurador interativo da linha de comando da biblioteca padrão.
3. `traceback`: Módulo para extrair, formatar e imprimir o relatório completo da pilha de chamadas (Stack Trace).

Principais Comandos do pdb:
- `p expressão` ou `pp expressão`: Imprime o valor de uma expressão ou variável (pretty print).
- `n` (next): Executa a linha atual e passa para a próxima linha no mesmo escopo.
- `s` (step): Entra na função que está prestes a ser executada (Step Into).
- `c` (continue): Retoma a execução normal até encontrar o próximo breakpoint ou o fim do programa.
- `l` (list): Exibe as linhas de código ao redor da posição atual.
- `w` (where): Imprime a pilha de chamadas (Stack Trace) completa de onde a execução está pausada.
- `q` (quit): Aborta a execução do programa imediatamente.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: MÓDULO TRACEBACK
# ==========================================================
def funcao_nivel_3() -> None:
    # Simula uma falha em profundidade na pilha de chamadas
    raise ValueError("Erro simulado no nivel 3 da call stack")


def funcao_nivel_2() -> None:
    funcao_nivel_3()


def funcao_nivel_1() -> None:
    funcao_nivel_2()


def demonstrar_fundamentos_traceback() -> None:
    print("\n--- 1. FUNDAMENTOS: Inspeção de Stack Trace com traceback ---")

    try:
        funcao_nivel_1()
    except ValueError:
        print("Capturada excecao. Extraindo Stack Trace formatado via traceback.format_exc():\n")
        stack_str = traceback.format_exc()
        print(stack_str)


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: INSPEÇÃO DE FRAMES COM SYS._GETFRAME
# ==========================================================
def inspecionar_caller_info() -> dict[str, Any]:
    """Inspeciona o frame de quem chamou esta função (Caller Introspection)."""
    # Frame 0 e a propria funcao inspecionar_caller_info
    # Frame 1 e a funcao que chamou esta funcao
    frame_pai = sys._getframe(1)
    return {
        "funcao_pai": frame_pai.f_code.co_name,
        "arquivo": frame_pai.f_code.co_filename,
        "linha": frame_pai.f_lineno,
        "variaveis_locais_pai": frame_pai.f_locals,
    }


def minha_funcao_negocio() -> None:
    id_transacao = "TX-998811"
    valor = 250.0
    info = inspecionar_caller_info()

    print("\nInformações do Caller capturadas dinamicamente:")
    print(f"  Função Chamadora: {info['funcao_pai']}")
    print(f"  Linha da Chamada: {info['linha']}")
    print(f"  Variáveis Locais no Pai: {info['variaveis_locais_pai']}")


def demonstrar_inspecao_frames() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Inspeção de Frame de Execução ---")
    minha_funcao_negocio()


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class SafeDebuggerBackendService:
    """Serviço backend de depuração que captura stack traces para observabilidade."""

    @staticmethod
    def executar_operacao_segura(func: Any, *args: Any) -> dict[str, Any]:
        try:
            res = func(*args)
            return {"status": "SUCCESS", "result": res}
        except Exception as e:
            # Captura a pilha de chamadas em formato de lista de strings para JSON/APM
            tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
            return {
                "status": "ERROR",
                "error_type": type(e).__name__,
                "error_message": str(e),
                "stack_trace_clean": [line.strip() for line in tb_lines],
            }


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Safe Debugger Payload ---")

    relatorio_erro = SafeDebuggerBackendService.executar_operacao_segura(funcao_nivel_1)
    print(f"Status da resposta: {relatorio_erro['status']}")
    print(f"Tipo do erro: {relatorio_erro['error_type']}")
    print(f"Linhas do Stack Trace capturadas: {len(relatorio_erro['stack_trace_clean'])}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: PEP 553 E PYTHONBREAKPOINT
# ==========================================================
"""
Como o breakpoint() funciona no CPython (PEP 553):
1. A função `breakpoint()` consulta a variável de ambiente `PYTHONBREAKPOINT`.
2. Se `PYTHONBREAKPOINT=0`, a função `breakpoint()` retorna IMEDIATAMENTE sem fazer nada (Zero-Cost em produção!).
3. Se `PYTHONBREAKPOINT` for omitida, ela invoca `sys.breakpointhook()`, que por padrão carrega `pdb.set_trace()`.
4. Se `PYTHONBREAKPOINT=ipdb.set_trace`, ela invoca dinamicamente o depurador IPDB.
"""


def demonstrar_internamente_breakpoint_config() -> None:
    print("\n--- 4. INTERNO: Variável de Ambiente PYTHONBREAKPOINT ---")
    hook_atual = sys.breakpointhook
    print(f"Hook de breakpoint atual do sistema: {hook_atual}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `traceback.format_exc()`: Tempo O(D), Espaço O(D), onde D é a profundidade de frames na pilha de chamadas (Call Stack).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar `import pdb; pdb.set_trace()` legado
    print("[X] Nao-Pythonic (Sintaxe antiga):")
    print("  import pdb; pdb.set_trace()  # Sintaxe antiga pré-Python 3.7!")

    # [OK] PYTHONIC: Usar a função nativa built-in breakpoint()
    print("\n[OK] Pythonic (PEP 553):")
    print("  breakpoint()  # Limpo, nativo e configurável via ambiente!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize a função built-in `breakpoint()` em vez do legado `import pdb; pdb.set_trace()`.
2. NUNCA suba para o repositório principal (Git) arquivos contendo instruções `breakpoint()` ativas.
3. Configure `PYTHONBREAKPOINT=0` nas suas variáveis de ambiente de produção para garantir que nenhum breakpoint ativo trave o servidor web.
4. Utilize `traceback.format_exc()` para registrar detalhes completos de erros em logs de backend.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Deixar um breakpoint() esquecido em uma API web de produção
    print("[!] Armadilha 1: Um breakpoint() esquecido em produção pode travar a thread da API esperando input do terminal stdin!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como você desativa todos os `breakpoint()` de uma aplicação Python em ambiente de produção sem precisar editar os arquivos fonte?"
A: "Configurando a variável de ambiente `PYTHONBREAKPOINT=0` no container ou servidor de produção.
    A partir do Python 3.7 (PEP 553), quando `PYTHONBREAKPOINT` está definida como `"0"`, o interpretador CPython ignora completamente todas as chamadas `breakpoint()`,
    retornando imediatamente sem invocar o depurador interativo nem travar o processo."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Escreva uma função que simule uma exceção e utilize `traceback.print_exc()` para imprimir o erro formatado.
# Exercício 2: Escreva uma função que utilize `sys._getframe()` para descobrir qual a linha e o arquivo de onde ela foi chamada.
# Exercício 3: Teste a execução de um script com a variável de ambiente `PYTHONBREAKPOINT=0` e verifique que o breakpoint é ignorado.


def main() -> None:
    print("==========================================================")
    print("  AULA 60: DEPURAÇÃO DE CÓDIGO, BREAKPOINT() E TRACEBACK")
    print("==========================================================")
    demonstrar_fundamentos_traceback()
    demonstrar_inspecao_frames()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_breakpoint_config()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 60 executado com sucesso.")


if __name__ == "__main__":
    main()
