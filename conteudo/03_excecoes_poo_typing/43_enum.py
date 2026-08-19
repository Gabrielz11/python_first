"""
43_enum.py - Enumerações com Enum, IntEnum, StrEnum e Pattern Matching

Objetivos:
1. Dominar o uso do módulo nativo `enum` (`Enum`, `IntEnum`, `StrEnum` e `auto()`).
2. Eliminar o antipadrão de "Magic Strings" e "Magic Numbers" no código de aplicação.
3. Compreender as vantagens de `StrEnum` (Python 3.11+) para interoperabilidade com JSON e APIs REST.
4. Integrar Enums com a instrução `match/case` para máquinas de estado em serviços backend.
5. Inspecionar as propriedades `.name` e `.value` de membros de enums.
"""

from enum import Enum, IntEnum, StrEnum, auto
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é um Enum em Python?
Um Enum (Enumeration / Enumeração) é um conjunto de nomes simbólicos (membros) vinculados a valores constantes e únicos.

Vantagens de Usar Enums:
1. Eliminação de Magic Strings/Numbers: Substitui strings como `"CANCELLED"` soltas por `StatusPedido.CANCELADO`.
2. Segurança de Tipos (Type Safety): Ferramentas como Mypy impedem a atribuição de estados inexistentes.
3. Imutabilidade: Membros de Enums não podem ter seus valores alterados durante a execução do programa.
4. Iterabilidade e Introspecção: Permite listar facilmente todos os estados válidos de um fluxo.

Tipos Principais:
- `Enum`: Classe base genérica para enumerações.
- `IntEnum`: Subclasse de `int`, cujos membros podem ser comparados com inteiros nativos.
- `StrEnum` (Python 3.11+): Subclasse de `str`, cujos membros são strings e serializam perfeitamente para JSON.
- `auto()`: Gera valores automaticamente sequenciais ou idênticos ao nome do membro.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: ENUM BÁSICO E AUTO()
# ==========================================================
class StatusPedido(StrEnum):
    """Enumeração de Status de Pedido usando StrEnum (Python 3.11+)."""

    RASCUNHO = auto()  # Gera 'rascunho' automaticamente em StrEnum
    PAGO = "pago"
    ENVIADO = "enviado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"


class NivelAcesso(IntEnum):
    """Enumeração de Níveis de Acesso para autorização."""

    LEITURA = 1
    ESCRITA = 2
    ADMIN = 3


def demonstrar_fundamentos_enum() -> None:
    print("\n--- 1. FUNDAMENTOS: Enum, StrEnum e Propriedades ---")

    status = StatusPedido.PAGO

    print(f"Membro do Enum: {status}")
    print(f"Propriedade .name: {status.name}")
    print(f"Propriedade .value: {status.value}")

    # StrEnum e comparável diretamente com strings!
    print(f"status == 'pago'? {status == 'pago'}")

    # IntEnum e comparável diretamente com inteiros!
    print(f"NivelAcesso.ADMIN > NivelAcesso.LEITURA? {NivelAcesso.ADMIN > NivelAcesso.LEITURA}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PATTERN MATCHING COM ENUMS
# ==========================================================
def processar_transicao_estado(status_atual: StatusPedido) -> str:
    """Utiliza Pattern Matching (match/case) para transição de estados."""
    match status_atual:
        case StatusPedido.RASCUNHO:
            return "Aguardando pagamento do cliente."
        case StatusPedido.PAGO:
            return "Pagamento confirmado. Separando produtos no estoque."
        case StatusPedido.ENVIADO:
            return "Pedido em trânsito com a transportadora."
        case StatusPedido.ENTREGUE:
            return "Pedido entregue com sucesso."
        case StatusPedido.CANCELADO:
            return "Pedido cancelado. Reembolso processado."


def demonstrar_pattern_matching_enum() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Pattern Matching com Enums ---")

    print(f"RASCUNHO -> {processar_transicao_estado(StatusPedido.RASCUNHO)}")
    print(f"PAGO     -> {processar_transicao_estado(StatusPedido.PAGO)}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class GatewayPagamentoEnum(StrEnum):
    STRIPE = "stripe"
    PAGSEGURO = "pagseguro"
    MERCADOPAGO = "mercadopago"


class ProcessadorPagamentoService:
    @staticmethod
    def executar_transacao(gateway: GatewayPagamentoEnum, valor: float) -> dict[str, Any]:
        return {
            "gateway_utilizado": gateway.value,
            "valor_processado": valor,
            "status": "APROVADO",
        }


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Processador de Pagamento com Enum ---")

    resultado = ProcessadorPagamentoService.executar_transacao(
        gateway=GatewayPagamentoEnum.STRIPE,
        valor=1250.00,
    )
    print(f"Resultado Backend: {resultado}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: ENUMMETA METACLASS
# ==========================================================
"""
Como o Enum funciona no CPython:
1. As classes Enum utilizam a metaclasse `EnumMeta`.
2. A metaclasse `EnumMeta` intercepta a criação da classe e transforma cada atributo de classe
   em uma instância da própria classe Enum (Singleton per membro).
3. Tentativas de alterar o valor de um membro em runtime (`StatusPedido.PAGO = "novo"`) disparam `AttributeError`.
"""


def demonstrar_internamente_enummeta() -> None:
    print("\n--- 4. INTERNO: Imutabilidade dos Membros do Enum ---")

    try:
        StatusPedido.PAGO = "novo_valor"  # type: ignore # Lança AttributeError
    except AttributeError as e:
        print(f"[!] Alteração de membro de Enum bloqueada pelo CPython: {e}")


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Busca de membro por Nome (`StatusPedido['PAGO']`): Custo de tabela Hash CPython -> Tempo O(1).
- Busca de membro por Valor (`StatusPedido('pago')`): Custo de tabela Hash CPython -> Tempo O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Magic Strings espalhadas no código
    print("[X] Nao-Pythonic (Magic Strings):")
    print("  if status == 'PAGO_COM_SUCESSO_FINAL': ...  # Propenso a erros de digitação!")

    # [OK] PYTHONIC: Utilizar Enums fortemente tipados
    print("\n[OK] Pythonic:")
    print("  if status == StatusPedido.PAGO: ...  # Autodocumentável e checado pelo Mypy!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize `StrEnum` (Python 3.11+) para constantes de texto que precisam ser serializadas para JSON em APIs REST.
2. Utilize Nomes de Membros do Enum em MAIÚSCULAS (`PAGO`, `ENVIADO`) conforme PEP 8.
3. Utilize `auto()` para gerar valores automaticamente quando o valor exato for irrelevante.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar instanciar membro com valor inexistente dispara ValueError
    try:
        _ = StatusPedido("status_invalido_xyz")
    except ValueError as e:
        print(f"[!] Armadilha 1 (ValueError ao buscar valor inexistente): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre `Enum`, `IntEnum` e `StrEnum` em Python?"
A: "1. `Enum`: Classe base. Seus membros NÃO são instâncias de int ou str, exigindo o uso de `.value` para passar em bibliotecas externas.
    2. `IntEnum`: Seus membros herdam de `int`. Podem ser comparados e usados diretamente em operações matemáticas com inteiros.
    3. `StrEnum` (Python 3.11+): Seus membros herdam de `str`. Podem ser comparados diretamente com strings e serializados para JSON sem adaptadores."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie um `StrEnum` chamado `TipoChavePix` contendo `CPF`, `EMAIL`, `TELEFONE` e `ALEATORIA`.
# Exercício 2: Escreva uma função que receba `TipoChavePix` e valide o valor correspondente usando `match/case`.
# Exercício 3: Crie um `IntEnum` contendo prioridades de tarefas (`BAIXA=1`, `MEDIA=2`, `ALTA=3`) e ordene uma lista de tarefas por prioridade.


def main() -> None:
    print("==========================================================")
    print("  AULA 43: ENUMERAÇÕES, STRENUM E PATTERN MATCHING")
    print("==========================================================")
    demonstrar_fundamentos_enum()
    demonstrar_pattern_matching_enum()
    demonstrar_aplicacao_backend()
    demonstrar_internamente_enummeta()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 43 executado com sucesso.")


if __name__ == "__main__":
    main()
