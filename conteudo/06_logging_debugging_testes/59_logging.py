"""
59_logging.py - Sistema de Log Estruturado em Python (`logging`)

Objetivos:
1. Substituir chamadas `print()` por logging profissional.
2. Configurar níveis de log (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
3. Personalizar formatadores de mensagem.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("PythonFirst")


def main() -> None:
    print("==========================================================")
    print("  AULA 59: LOGGING E SISTEMA DE LOGS ESTRUTURADO")
    print("==========================================================")
    logger.info("Aplicação iniciada com sucesso.")
    logger.warning("Alerta: Uso de memória acima de 70%.")
    logger.error("Erro simulado: Falha na conexão de banco.")
    print("\n[Concluido] Arquivo 59 executado com sucesso.")


if __name__ == "__main__":
    main()
