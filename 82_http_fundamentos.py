"""
82_http_fundamentos.py - Fundamentos do Protocolo HTTP e REST APIs

Objetivos:
1. Compreender métodos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
2. Entender Status Codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Server Error`).
"""

def simular_requisicao_http(metodo: str, endpoint: str) -> tuple[int, str]:
    if metodo == "GET" and endpoint == "/api/status":
        return 200, '{"status": "online"}'
    elif metodo == "POST" and endpoint == "/api/usuarios":
        return 201, '{"id": 101, "mensagem": "Criado com sucesso"}'
    return 404, '{"erro": "Não encontrado"}'


def main() -> None:
    print("==========================================================")
    print("  AULA 82: FUNDAMENTOS HTTP E ARQUITETURA REST")
    print("==========================================================")
    status, payload = simular_requisicao_http("GET", "/api/status")
    print(f"Resposta HTTP [Status {status}]: {payload}")
    print("\n[Concluido] Arquivo 82 executado com sucesso.")


if __name__ == "__main__":
    main()
