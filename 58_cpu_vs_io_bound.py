"""
58_cpu_vs_io_bound.py - Análise Comparativa: CPU-Bound vs I/O-Bound e Impacto do GIL

Objetivos:
1. Identificar quando utilizar Asyncio, Threads ou Multiprocessing baseando-se na natureza da carga de trabalho (I/O vs CPU).
2. Compreender a influência do Global Interpreter Lock (GIL) em execuções paralelas.
"""

def main() -> None:
    print("==========================================================")
    print("  AULA 58: CPU-BOUND VS I/O-BOUND E GUIA DE ARQUITETURA")
    print("==========================================================")
    print("Guia de Escolha Arquitetural:")
    print(" 1. Operações I/O-Bound (Requisições HTTP, Banco de Dados, Leitura de Arquivo):")
    print("    -> Use Asyncio (para máxima escala) ou ThreadPoolExecutor.")
    print(" 2. Operações CPU-Bound (Cálculos matemáticos intensivos, Processamento de Imagens):")
    print("    -> Use Multiprocessing ou ProcessPoolExecutor (Bypassa o GIL usando múltiplos núcleos).")
    print("\n[Concluido] Arquivo 58 executado com sucesso.")


if __name__ == "__main__":
    main()
