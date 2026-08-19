"""
26_json.py - Serialização e Deserialização JSON (json module, Custom Encoders e Performance)

Objetivos:
1. Dominar o módulo nativo `json`: `dumps`/`loads` (para strings) e `dump`/`load` (para arquivos).
2. Configurar opções de formatação como `indent`, `sort_keys`, `ensure_ascii=False` e `separators`.
3. Tratar tipos não suportados nativamente (como `datetime`, `Decimal`, `UUID` e objetos de classe) com Custom Encoders.
4. Entender a diferença estrita entre o formato JSON (especificação RFC 8259) e dicionários Python.
5. Desenvolver serializadores resilientes para APIs REST e barramentos de mensagens no backend.
"""

from datetime import date, datetime
from decimal import Decimal
import json
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é JSON e como o Python lida com ele?
JSON (JavaScript Object Notation - RFC 8259) é o formato padrão da indústria para troca de dados
em APIs REST, microsserviços e configurações.

Mapeamento de Tipos Python <-> JSON:
- dict <-> Object {}
- list, tuple <-> Array []
- str <-> String "" (Sempre aspas duplas!)
- int, float <-> Number
- True, False <-> true, false
- None <-> null

Funções Principais:
- `json.dumps(obj)`: Converte objeto Python em STRING JSON (String Memory).
- `json.loads(string_json)`: Converte STRING JSON em objeto Python.
- `json.dump(obj, fp)`: Escreve o objeto Python diretamente em um ARQUIVO.
- `json.load(fp)`: Lê o arquivo contendo JSON e converte em objeto Python.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: DUMPS E LOADS
# ==========================================================
def demonstrar_dumps_e_loads() -> None:
    print("\n--- 1. FUNDAMENTOS: json.dumps e json.loads ---")

    payload_python: dict[str, Any] = {
        "usuario_id": 1001,
        "nome": "Gabriel Z",
        "ativo": True,
        "roles": ["admin", "developer"],
        "metadata": None,
    }

    # Serializando para String JSON formatada
    json_string = json.dumps(payload_python, indent=2, ensure_ascii=False)
    print("String JSON gerada:")
    print(json_string)

    # Deserializando de volta para Dicionário Python
    dicionario_reconstruido = json.loads(json_string)
    print(f"\nTipo Reconstruido: {type(dicionario_reconstruido).__name__}")
    print(f"Nome extraido: {dicionario_reconstruido['nome']}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: CUSTOM JSON ENCODER E DATETIME
# ==========================================================
class RespostaAPIEncoder(json.JSONEncoder):
    """Custom Encoder para serializar tipos Python complexos em JSON."""

    def default(self, o: Any) -> Any:
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, Decimal):
            return float(o)
        if hasattr(o, "to_dict"):
            return o.to_dict()
        return super().default(o)


def demonstrar_custom_encoder() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Custom JSON Encoder ---")

    dados_complexos = {
        "transacao_id": "TX-9988",
        "data_hora": datetime(2026, 8, 19, 14, 30, 0),
        "valor_total": Decimal("1500.50"),
    }

    # Forma 1: Usando parâmetro default= com função lambda
    json_lambda = json.dumps(
        dados_complexos,
        default=lambda x: x.isoformat() if isinstance(x, (datetime, date)) else str(x),
    )
    print(f"Serializacao via lambda: {json_lambda}")

    # Forma 2: Usando a classe Custom JSONEncoder (Mais robusta e reutilizável)
    json_custom_class = json.dumps(dados_complexos, cls=RespostaAPIEncoder, indent=2)
    print("\nSerializacao via RespostaAPIEncoder (cls=):")
    print(json_custom_class)


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class PipelineSerializerService:
    """Simula um middleware backend que valida e serializa payloads de resposta HTTP."""

    @staticmethod
    def processar_payload_resposta(dados_brutos: dict[str, Any]) -> str:
        try:
            return json.dumps(
                dados_brutos,
                cls=RespostaAPIEncoder,
                ensure_ascii=False,
                separators=(",", ":"),  # Compacto sem espaços desnecessários (ideal para rede)
            )
        except TypeError as e:
            # Fallback de erro de serialização
            return json.dumps({"status": 500, "erro": f"Erro de serializacao: {e}"})


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Middleware Serializador de Resposta ---")

    resposta_dto = {
        "status": 200,
        "timestamp": datetime.now(),
        "dados": {
            "cliente": "Empresa XPTO",
            "saldo_disponivel": Decimal("84500.00"),
        },
    }

    json_compacto = PipelineSerializerService.processar_payload_resposta(resposta_dto)
    print(f"Payload JSON compacto enviado na rede:\n{json_compacto}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: C-EXTENSION _JSON
# ==========================================================
"""
Como o módulo json funciona por baixo dos panos (CPython):
1. O CPython possui uma extensão escrita diretamente em C (`_json.c`) para realizar o parsing
   de strings JSON e a conversão de objetos em ultra-alta velocidade.
2. Se a extensão C não estiver disponível, o Python utiliza um fallback escrito em Python puro.
3. Diferença entre Aspas: A especificação JSON exige EXCLUSIVAMENTE aspas duplas (`"chave"`).
   Tentar usar aspas simples (`'chave'`) resulta em `json.decoder.JSONDecodeError`.
"""


def demonstrar_internamente_parse() -> None:
    print("\n--- 4. INTERNO: Validacao Estrita de Aspas Duplas ---")

    json_valido = '{"status": "sucesso"}'
    json_invalido = "{'status': 'sucesso'}"  # Aspas simples sao invalidas em JSON!

    print(f"JSON Valido parsed: {json.loads(json_valido)}")

    try:
        json.loads(json_invalido)
    except json.JSONDecodeError as e:
        print(f"[!] Erro no JSON Invalido (JSONDecodeError): {e.msg} na linha {e.lineno} col {e.colno}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- `json.dumps(obj)`: Tempo O(N), Espaço O(N), onde N é a quantidade total de nós/atributos na árvore do objeto.
- `json.loads(json_str)`: Tempo O(N), Espaço O(N), onde N é o número de caracteres da string JSON.
- Consumo de Memória: Para JSONs massivos (> 100 MB), recomenda-se usar streamingparsers como `ijson` em vez de `json.loads()`.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    data_evento = datetime(2026, 8, 19)

    # [X] NÃO-PYTHONIC: Converter campos manualmente um a um para string antes do dumps
    print("[X] Nao-Pythonic (Conversao manual pre-dumps):")
    dados_manuais = {
        "evento": "REUNIAO",
        "data": str(data_evento),  # Converte manualmente
    }
    print(f"  Result: {json.dumps(dados_manuais)}")

    # [OK] PYTHONIC: Utilizar Custom Encoder ou o parâmetro `default=`
    print("\n[OK] Pythonic (usando default=str no dumps):")
    dados_originais = {"evento": "REUNIAO", "data": data_evento}
    print(f"  Result (default=str): {json.dumps(dados_originais, default=str)}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre utilize `ensure_ascii=False` ao serializar textos em português para evitar que caracteres acentuados virem escapes Unicode `\u00e7\u00e3`.
2. Para tráfego de rede em produção, utilize `separators=(',', ':')` no `dumps` para eliminar espaços e reduzir o tamanho dos bytes transferidos.
3. Utilize `indent=2` apenas em logs ou ambientes de desenvolvimento/debug.
4. Para lidar com valores financeiros (`Decimal`), converta para `str` ou `float` de forma explícita no Custom Encoder para evitar arredondamentos indesejados.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: TypeError: Object of type datetime is not JSON serializable
    try:
        json.dumps({"data": datetime.now()})  # Sem custom encoder
    except TypeError as e:
        print(f"[!] Armadilha 1 (TypeError): {e}")

    # Armadilha 2: Confundir json.loads (String) com json.load (Arquivo)
    try:
        # Tentar passar uma string para json.load em vez de json.loads
        json.load('{"a": 1}')  # AttributeError: 'str' object has no attribute 'read'
    except AttributeError as e:
        print(f"[!] Armadilha 2 (Confundir load com loads): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre um Dicionário Python e uma String JSON, e por que não podemos usar `eval()` para ler JSON?"
A: "1. Dicionário Python é uma estrutura de dados na memória RAM (Tabela Hash com suporte a qualquer objeto). 
       JSON é um formato de texto estrito (RFC 8259) usado para intercâmbio de dados.
    2. NUNCA se deve usar `eval()` para interpretar strings JSON. O `eval()` executa qualquer código Python arbitrário,
       abrindo uma vulnerabilidade gravíssima de Injeção de Código (Remote Code Execution - RCE). 
       Sempre utilize o parser seguro `json.loads()`."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma função `salvar_json_config(caminho: str, dados: dict)` que grave um dicionário formatado com 4 espaços de indentação.
# Exercício 2: Escreva um Custom JSONEncoder que consiga serializar objetos do tipo `set` (convertendo para `list`) e objetos `UUID`.
# Exercício 3: Escreva uma função que leia um arquivo JSON contendo uma lista de produtos, filtre os produtos com preço maior que R$ 100 e retorne uma nova string JSON compacta.


def main() -> None:
    print("==========================================================")
    print("  AULA 26: SERIALIZAÇÃO E DESERIALIZAÇÃO JSON")
    print("==========================================================")
    demonstrar_dumps_e_loads()
    demonstrar_custom_encoder()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_parse()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 26 executado com sucesso.")


if __name__ == "__main__":
    main()
