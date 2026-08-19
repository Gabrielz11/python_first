"""
67_solid.py - Os 5 Princípios SOLID Aplicados em Python (SRP, OCP, LSP, ISP, DIP)

Objetivos:
1. Dominar os 5 princípios de design de software orientado a objetos SOLID.
2. Aplicar o Single Responsibility Principle (SRP - Princípio da Responsabilidade Única).
3. Aplicar o Open/Closed Principle (OCP - Aberto para Extensão, Fechado para Modificação) via Polimorfismo.
4. Aplicar o Liskov Substitution Principle (LSP - Substituição de Liskov).
5. Aplicar o Interface Segregation Principle (ISP) e o Dependency Inversion Principle (DIP - Inversão de Dependência).
"""

from abc import ABC, abstractmethod
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que são os Princípios SOLID?
SOLID é um acrônimo criado por Michael Feathers para 5 princípios fundamentais de design de código POO formulados por Robert C. Martin (Uncle Bob):

1. S - Single Responsibility Principle (SRP):
   Uma classe deve ter um, e apenas um, motivo para mudar. (Uma única responsabilidade).
2. O - Open/Closed Principle (OCP):
   Módulos de software devem estar Abertos para extensão, mas Fechados para modificação.
3. L - Liskov Substitution Principle (LSP):
   Subclasses devem ser substituíveis por suas classes base sem quebrar o comportamento da aplicação.
4. I - Interface Segregation Principle (ISP):
   Clientes não devem ser forçados a depender de interfaces que não utilizam (Interfaces pequenas e focadas).
5. D - Dependency Inversion Principle (DIP):
   Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: REFATORANDO SRP E OCP
# ==========================================================
# --- 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP) ---
class RelatorioFinanceiroData:
    """Responsável APENAS pelos dados do relatório."""

    def __init__(self, dados: list[float]) -> None:
        self.dados = dados

    def calcular_total(self) -> float:
        return sum(self.dados)


class RelatorioFormatter:
    """Responsável APENAS pela formatação do relatório."""

    @staticmethod
    def formatar_para_json(relatorio: RelatorioFinanceiroData) -> str:
        return f'{{"total": {relatorio.calcular_total():.2f}}}'


# --- 2. OPEN/CLOSED PRINCIPLE (OCP) ---
class DescontoStrategy(ABC):
    """Abstração para estratégias de desconto (Aberto para Extensão, Fechado para Modificação)."""

    @abstractmethod
    def calcular_desconto(self, valor: float) -> float:
        pass


class DescontoNatal(DescontoStrategy):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.15


class DescontoBlackFriday(DescontoStrategy):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.30


class CalculadoraPreco:
    def __init__(self, estrategia_desconto: DescontoStrategy) -> None:
        self.estrategia = estrategia_desconto

    def calcular_preco_final(self, valor: float) -> float:
        return valor - self.estrategia.calcular_desconto(valor)


def demonstrar_fundamentos_srp_ocp() -> None:
    print("\n--- 1. FUNDAMENTOS: SRP e OCP ---")

    relatorio = RelatorioFinanceiroData([100.0, 200.0, 50.0])
    json_output = RelatorioFormatter.formatar_para_json(relatorio)
    print(f"SRP (Relatorio Formatted): {json_output}")

    calc_bf = CalculadoraPreco(DescontoBlackFriday())
    print(f"OCP (Preço com BlackFriday 30%): R$ {calc_bf.calcular_preco_final(100.0):.2f}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: ISP E DIP
# ==========================================================
# --- 4. INTERFACE SEGREGATION PRINCIPLE (ISP) ---
class Impressora(ABC):
    @abstractmethod
    def imprimir(self, doc: str) -> None: pass


class Escanear(ABC):
    @abstractmethod
    def escanear(self) -> str: pass


class ImpressoraSimples(Impressora):
    """Não é forçada a implementar escanear()!"""

    def imprimir(self, doc: str) -> None:
        print(f"  [Impressora] Imprimindo: {doc}")


# --- 5. DEPENDENCY INVERSION PRINCIPLE (DIP) ---
class NotificadorService(ABC):
    @abstractmethod
    def enviar_mensagem(self, msg: str) -> None: pass


class EmailService(NotificadorService):
    def enviar_mensagem(self, msg: str) -> None:
        print(f"  [DIP - Email] Enviado: {msg}")


class SMSNotifier(NotificadorService):
    def enviar_mensagem(self, msg: str) -> None:
        print(f"  [DIP - SMS] Enviado: {msg}")


class ControllerNotificacao:
    """Módulo de alto nível depende da Abstração NotificadorService, não do concreto!"""

    def __init__(self, servico_notificador: NotificadorService) -> None:
        self.notificador = servico_notificador

    def executar(self, texto: str) -> None:
        self.notificador.enviar_mensagem(texto)


def demonstrar_isp_e_dip() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: ISP e DIP ---")

    controller_email = ControllerNotificacao(EmailService())
    controller_sms = ControllerNotificacao(SMSNotifier())

    controller_email.executar("Seu código é 1234")
    controller_sms.executar("Seu código é 1234")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Arquitetura SOLID Completa ---")
    imp = ImpressoraSimples()
    imp.imprimir("Relatório de Vendas")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: SOLID EM LINGUAGENS DINÂMICAS
# ==========================================================
"""
Como o SOLID é aplicado em Python:
1. O Python não exige a verborragia de interfaces como Java; o DIP e o OCP podem ser satisfeitos tanto via `abc.ABC` quanto via `typing.Protocol` (Duck Typing).
2. O importante dos princípios SOLID é a Arquitetura Lógica e o Desacoplamento de Componentes, não o uso excessivo de arquivos.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Injeção de Dependências (DIP) e Strategy (OCP): Chamadas polimórficas O(1) de tempo, Espaço O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Violando DIP (Instanciar dependência concreta dentro da classe)
    print("[X] Nao-Pythonic (Violando DIP):")
    print("  class Controller: def __init__(self): self.email = EmailService()  # Acoplamento rígido!")

    # [OK] PYTHONIC: Aplicar Inversão de Dependência via Injeção no __init__
    print("\n[OK] Pythonic:")
    print("  class Controller: def __init__(self, servico: NotificadorService): self.servico = servico")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. SRP: Se uma classe precisa de bibliotecas de banco de dados E bibliotecas de formato HTML, ela provavelmente está violando o SRP.
2. OCP: Sempre que se ver adicionando um `if/elif/else` gigante para checar o tipo de objeto, refatore para OCP via Polimorfismo.
3. DIP: Passe abstrações para o construtor das suas classes de domínio.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Over-engineering (Criar 20 interfaces abstratas para um script de 30 linhas)
    print("[!] Armadilha 1: Aplicar SOLID sem necessidade em scripts pequenos resulta em Over-Engineering desnecessário.")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre o Open/Closed Principle (OCP) e o Dependency Inversion Principle (DIP)?"
A: "1. OCP (Open/Closed): É sobre COMO ESTENDER código sem alterá-lo. Foca na adição de novos comportamentos através de polimorfismo/herança sem editar o código existente.
    2. DIP (Dependency Inversion): É sobre COMO DESACOPLAR módulos. Foca em garantir que classes de alto nível não dependam de implementações concretas de baixo nível, mas sim de abstrações (Interfaces/ABCs/Protocols)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Identifique a violação de SRP em uma classe `Usuario` que contém dados de usuário e método `salvar_no_banco_sql()`. Refatore.
# Exercício 2: Crie um sistema de cálculo de frete que respeite o OCP permitindo adicionar novas transportadoras sem alterar a classe principal.
# Exercício 3: Escreva uma classe controller que receba uma abstração de Logger via DIP.


def main() -> None:
    print("==========================================================")
    print("  AULA 67: OS 5 PRINCÍPIOS SOLID EM PYTHON")
    print("==========================================================")
    demonstrar_fundamentos_srp_ocp()
    demonstrar_isp_e_dip()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 67 executado com sucesso.")


if __name__ == "__main__":
    main()
