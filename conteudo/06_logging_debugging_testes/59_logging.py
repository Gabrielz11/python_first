"""
59_logging.py - Módulo logging, Níveis de Log, Handlers e Log Estruturado em Produção

Objetivos:
1. Dominar o uso da biblioteca nativa `logging` para substituição completa de declarações `print()`.
2. Compreender a hierarquia de Níveis de Log (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
3. Configurar Loggers, Handlers (`StreamHandler`, `FileHandler`, `RotatingFileHandler`) e Formatters.
4. Aplicar a prática de passar argumentos diferidos no logging (`logger.info("Msg %s", arg)`) para economia de CPU.
5. Utilizar `logger.exception()` dentro de blocos `except` para inclusão automática do Traceback nos logs de produção.
"""

import logging
import os
import sys
import tempfile


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Por que usar o módulo logging em vez de print()?
Em aplicações comerciais de backend, o uso de `print()` é considerado um antipadrão grave.

Vantagens do Módulo logging:
1. Controle por Níveis: Permite alternar o nível de detalhamento (ex: exibir `DEBUG` em desenvolvimento e apenas `INFO`/`ERROR` em produção) sem alterar uma linha de código.
2. Roteamento Múltiplo (Handlers): Envia mensagens simultaneamente para o terminal (stdout), arquivos de texto em disco e agregadores externos (Datadog, ElasticSearch/ELK, CloudWatch).
3. Enriquecimento de Metadados (Formatters): Adiciona automaticamente timestamp, nome do arquivo, número da linha, nível do log e ID da thread.
4. Tracebacks Automáticos: O método `logger.exception()` captura e formata a exceção atual de forma estruturada.

Níveis de Log Padrão (Valores Numéricos Crescentes):
- `DEBUG` (10): Detalhes diagnósticos de baixo nível (útil para desenvolvimento).
- `INFO` (20): Confirmação de que as coisas estão funcionando como esperado em produção.
- `WARNING` (30): Indicação de algo inesperado ou problema iminente (ex: espaço em disco baixo).
- `ERROR` (40): Falha em uma função/operação específica, mas a aplicação continua rodando.
- `CRITICAL` (50): Erro grave que pode paralisar o sistema ou o serviço inteiro.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CONFIGURAÇÃO DE LOGGER
# ==========================================================
def demonstrar_fundamentos_logging() -> None:
    print("\n--- 1. FUNDAMENTOS: Níveis de Log e Logger Nomeado ---")

    # Obtém um logger nomeado específico para o módulo atual (PEP 8 Best Practice)
    logger = logging.getLogger("meu_modulo_app")
    logger.setLevel(logging.DEBUG)

    # Evita duplicação de handlers se reutilizado
    if not logger.handlers:
        handler_console = logging.StreamHandler(sys.stdout)
        formatador = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s")
        handler_console.setFormatter(formatador)
        logger.addHandler(handler_console)

    logger.debug("Mensagem de DEBUG: Detalhes internos de variáveis.")
    logger.info("Mensagem de INFO: Processamento iniciado com sucesso.")
    logger.warning("Mensagem de WARNING: Recurso consumindo mais de 80%% de RAM.")
    logger.error("Mensagem de ERROR: Falha ao comunicar com API de frete.")
    logger.critical("Mensagem de CRITICAL: Banco de dados inacessível!")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: LOGGER.EXCEPTION E FORMATAÇÃO DIFERIDA
# ==========================================================
def demonstrar_logger_exception() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: logger.exception() e Formatação Diferida ---")

    logger = logging.getLogger("servico_pagamento")
    logger.setLevel(logging.INFO)

    # 1. Formatação Diferida (Lazy Formatting):
    # Passe argumentos separadamente em vez de f-strings para que a interpolação ocorra APENAS se o nível de log estiver ativo!
    user_id = 9941
    logger.info("Usuário %s autenticado com sucesso.", user_id)  # [OK] Diferido!

    # 2. Captura automática de Traceback em exceções
    try:
        _ = 10 / 0
    except ZeroDivisionError:
        logger.exception("Falha ao calcular taxa de divisão para o usuário %s:", user_id)


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ApplicationLoggerConfig:
    """Configurador central de logs de produção com saída em arquivo e console."""

    @staticmethod
    def setup_logger(nome: str, arquivo_log: str) -> logging.Logger:
        logger = logging.getLogger(nome)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            # Formato Estruturado
            fmt = logging.Formatter(
                '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(name)s", "message": "%(message)s"}'
            )

            # Handler para Arquivo
            file_handler = logging.FileHandler(arquivo_log, encoding="utf-8")
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)

        return logger


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Logging Estruturado em Arquivo ---")
    path_log = os.path.join(tempfile.gettempdir(), "app_prod.log")

    log_prod = ApplicationLoggerConfig.setup_logger("api_gateway", path_log)
    log_prod.info("Serviço inicializado na porta 8080")

    print(f"Log gravado no arquivo: {path_log}")
    if os.path.exists(path_log):
        with open(path_log, "r", encoding="utf-8") as f:
            print(f"Conteúdo lido: {f.read().strip()}")
        # Libera o FileHandler para fechar o arquivo antes do remove no Windows
        for h in log_prod.handlers[:]:
            h.close()
            log_prod.removeHandler(h)
        os.remove(path_log)


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ARVORE DE HIERARQUIA DE LOGGERS
# ==========================================================
"""
Como o módulo logging funciona internamente:
1. Hierarquia com Notação de Ponto: Os Loggers são organizados em uma estrutura de árvore pai/filho.
   `logging.getLogger("app.services.user")` é filho de `logging.getLogger("app.services")` que é filho de `logging.getLogger("app")`.
2. Propagação (`logger.propagate = True`): Por padrão, quando um log é emitido por um logger filho,
   ele é propagado para cima na árvore até atingir os Handlers do Root Logger.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Chamada de Log desativada (`logger.debug(...)` quando o nível é `INFO`): Tempo O(1) [Verificação de flag inteira], Espaço O(1).
- Chamada de Log ativa: Tempo O(N) onde N é o número de Handlers registrados.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar print() para registrar erros ou f-strings caras no logger
    print("[X] Nao-Pythonic:")
    print("  print(f'Erro no usuario {user_id}')  # Sem timestamp, sem nível, sem controle de saída!")

    # [OK] PYTHONIC: Usar logger.info() com formatação diferida %s
    print("\n[OK] Pythonic:")
    print("  logger.info('Processando usuario %s', user_id)  # Estruturado e eficiente!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Obtenha sempre o logger nomeado do módulo atual via `logger = logging.getLogger(__name__)`.
2. Dentro de blocos `except`, utilize `logger.exception("Mensagem")` em vez de `logger.error()`. O `exception()` inclui automaticamente o Traceback completo.
3. Utilize formatação por porcentagem (`logger.info("Dado %s", valor)`) em vez de f-strings. Se o nível de log estiver desativado, o Python economiza CPU não formatando a string.
4. NUNCA utilize `print()` em código de produção de microsserviços.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Usar `logger.exception()` FORA de um bloco except
    # Lança erro ou imprime 'NoneType: None' no Traceback porque não existe exceção ativa!
    logger = logging.getLogger("test_trap")
    print("[!] Armadilha 1: Chamar logger.exception() fora de um bloco 'except' gera log confuso com NoneType no Traceback!")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Por que devemos preferir a sintaxe `logger.info("Usuário %s", user_id)` em vez de `logger.info(f"Usuário {user_id}")`?"
A: "Por uma questão de otimização de performance (Lazy String Formatting).
    Na sintaxe f-string `f"Usuário {user_id}"`, a concatenação de strings é executada IMEDIATAMENTE no momento em que a linha é lida, mesmo que o nível de log esteja configurado para `ERROR` (desativando o `INFO`).
    Na sintaxe com `%s`, a interpolação da string só é processada internamente se o nível de log `INFO` estiver realmente ativo no Logger, evitando desperdício de ciclo de CPU e alocação de memória RAM em produção."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Configure um logger que grave mensagens de nível `ERROR` em um arquivo de log e exiba `INFO` no terminal.
# Exercício 2: Escreva uma função que simule a leitura de um arquivo inexistente e registre o erro usando `logger.exception()`.
# Exercício 3: Crie um Formatter customizado que converta todas as mensagens de log para o formato JSON.


def main() -> None:
    print("==========================================================")
    print("  AULA 59: MÓDULO LOGGING, HANDLERS E LOG ESTRUTURADO")
    print("==========================================================")
    demonstrar_fundamentos_logging()
    demonstrar_logger_exception()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 59 executado com sucesso.")


if __name__ == "__main__":
    main()
