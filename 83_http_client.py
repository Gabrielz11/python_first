"""
83_http_client.py - Requisições HTTP com Cliente Nativo (`urllib.request`)

Objetivos:
1. Realizar requisições HTTP sem dependências externas utilizando o módulo nativo `urllib.request`.
"""

import json
from urllib.request import Request, urlopen


def buscar_post_simulado() -> None:
    # Usando JSONPlaceholder público para exemplo nativo
    url = "https://jsonplaceholder.typicode.com/posts/1"
    req = Request(url, headers={"User-Agent": "PythonFirstClient/1.0"})
    try:
        with urlopen(req, timeout=3.0) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))
            print(f"[HTTP] Post retornado com sucesso: Título='{dados['title'][:30]}...'")
    except Exception as e:
        print(f"[!] Simulação de chamada externa fallback: {e}")


def main() -> None:
    print("==========================================================")
    print("  AULA 83: CLIENTE HTTP NATIVO COM URLLIB.REQUEST")
    print("==========================================================")
    buscar_post_simulado()
    print("\n[Concluido] Arquivo 83 executado com sucesso.")


if __name__ == "__main__":
    main()
