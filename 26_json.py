"""
26_json.py - Serialização e Deserialização JSON (`json.dumps`, `json.loads`)

Objetivos:
1. Trabalhar com JSON em Python nativo (`json.dumps`, `json.loads`, `json.dump`, `json.load`).
2. Entender mapeamento de tipos Python <-> JSON.
3. Customizar encoders para tipos complexos usando `json.JSONEncoder` ou `default=`.
"""

import json
from datetime import datetime
from typing import Any


def custom_serializer(obj: Any) -> Any:
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Tipo {type(obj)} não é serializável em JSON")


def demonstrar_json() -> None:
    print("\n--- 1. SERIALIZAÇÃO E DESERIALIZAÇÃO JSON ---")

    payload = {
        "usuario_id": 101,
        "nome": "Ana Maria",
        "roles": ["admin", "developer"],
        "ativo": True,
        "criado_em": datetime.now()
    }

    # Serialização com indentação e serializer customizado para datetime
    json_str = json.dumps(payload, indent=2, default=custom_serializer, ensure_ascii=False)
    print(f"JSON Gerado:\n{json_str}")

    # Deserialização
    dados_recuperados = json.loads(json_str)
    print(f"Dados Recuperados (dict): {dados_recuperados['nome']} (ID: {dados_recuperados['usuario_id']})")


def main() -> None:
    print("==========================================================")
    print("  AULA 26: SERIALIZAÇÃO E DESERIALIZAÇÃO JSON")
    print("==========================================================")
    demonstrar_json()
    print("\n[Concluido] Arquivo 26 executado com sucesso.")


if __name__ == "__main__":
    main()
