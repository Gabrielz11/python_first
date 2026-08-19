"""
38_polimorfismo.py - Polimorfismo, Duck Typing e Interfaces Implícitas

Objetivos:
1. Compreender o conceito de Polimorfismo em Python e como diferentes classes podem responder ao mesmo método.
2. Dominar a filosofia do Duck Typing ("Se anda como um pato e quaca como um pato, então é um pato").
3. Entender a diferença entre Polimorfismo baseado em Herança e Polimorfismo Dinâmico (Duck Typing).
4. Desenvolver sistemas extensíveis com baixo acoplamento utilizando interfaces implícitas.
5. Prevenir exceções `AttributeError` em runtime ao invocar contratos dinâmicos.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Polimorfismo e Duck Typing?
Polimorfismo significa "muitas formas". Em POO, é a capacidade de objetos de diferentes classes responderem
ao mesmo chamado de método de forma personalizada.

Em linguagens estáticas (como C++ ou Java):
Para que duas classes sejam usadas polimorficamente em uma função, elas OBRIGATORIAMENTE devem herdar da MESMA interface
ou classe pai estrita (`class Processador implements IProcessador`).

Em Python (Duck Typing / Interfaces Implícitas):
O Python NÃO exige que as classes pertençam à mesma hierarquia de herança!
Se o objeto possui o método esperado (ex: `.enviar()`), o Python simplesmente executa o método sem perguntar quem é a classe pai.
"Se anda como um pato e quaca como um pato, o Python o trata como um pato."
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: DUCK TYPING DEMONSTRADO
# ==========================================================
class ServicoEmail:
    def enviar_notificacao(self, destinatario: str, mensagem: str) -> bool:
        print(f"  [EMAIL] Enviando para {destinatario}: {mensagem}")
        return True


class ServicoSMS:
    def enviar_notificacao(self, destinatario: str, mensagem: str) -> bool:
        print(f"  [SMS] Enviando torpedo para {destinatario}: {mensagem}")
        return True


class ServicoPushNotification:
    def enviar_notificacao(self, destinatario: str, mensagem: str) -> bool:
        print(f"  [PUSH] Mobile Push para {destinatario}: {mensagem}")
        return True


# Função Polimórfica: Não se importa com o tipo exato, apenas se o objeto "sabe enviar_notificacao"
def notificar_usuario(notificador: Any, destino: str, msg: str) -> None:
    notificador.enviar_notificacao(destino, msg)


def demonstrar_fundamentos_polimorfismo() -> None:
    print("\n--- 1. FUNDAMENTOS: Duck Typing em Ação ---")

    email = ServicoEmail()
    sms = ServicoSMS()
    push = ServicoPushNotification()

    notificar_usuario(email, "gabriel@empresa.com", "Seu pedido foi despachado.")
    notificar_usuario(sms, "+5511999998888", "Seu código de acesso é 4902.")
    notificar_usuario(push, "USR-1002", "Nova mensagem recebida.")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: PROCESSADORES DE PAGAMENTO
# ==========================================================
class ProcessadorPix:
    def processar_pagamento(self, valor: float) -> str:
        return f"PIX de R$ {valor:.2f} aprovado instantaneamente."


class ProcessadorCartaoCredito:
    def processar_pagamento(self, valor: float) -> str:
        return f"Cartão de Crédito de R$ {valor:.2f} aprovado em 1x."


class ProcessadorBoleto:
    def processar_pagamento(self, valor: float) -> str:
        return f"Boleto de R$ {valor:.2f} gerado com sucesso."


def demonstrar_processadores_polimorficos() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Processamento Polimórfico ---")

    meios_pagamento: list[Any] = [
        ProcessadorPix(),
        ProcessadorCartaoCredito(),
        ProcessadorBoleto(),
    ]

    valor_compra = 150.00
    for meio in meios_pagamento:
        # Polimorfismo puro: Todos os objetos respondem a .processar_pagamento()
        resultado = meio.processar_pagamento(valor_compra)
        print(f"  Result: {resultado}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class CheckoutEngineService:
    """Motor backend desacoplado que aceita qualquer gateway polimórfico."""

    def __init__(self, gateway_pagamento: Any) -> None:
        self.gateway = gateway_pagamento

    def fechar_pedido(self, valor: float) -> None:
        print("  [CheckoutEngine] Iniciando fechamento de pedido...")
        # Confia no Duck Typing do gateway recebido via Injeção de Dependência
        status = self.gateway.processar_pagamento(valor)
        print(f"  [CheckoutEngine] Resposta do Gateway: {status}")


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Injeção de Dependência Polimórfica ---")
    gateway = ProcessadorPix()
    checkout = CheckoutEngineService(gateway)

    checkout.fechar_pedido(499.90)


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: DYNAMIC LOOKUP
# ==========================================================
"""
Como o CPython executa chamadas Polimórficas:
1. Em linguagens compiladas estaticamente, as chamadas de métodos usam vtables de ponteiros de função fixos em C++.
2. Em CPython, a chamada `objeto.método()` realiza uma busca dinâmica de atributos em tempo de execução (Dynamic Lookup).
3. O interpretador busca o nome do método no dicionário de atributos do objeto ou de sua classe (`__dict__`).
4. Se o método existir, ele é invocado diretamente. Essa flexibilidade total é a base do Duck Typing.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Chamada de Método Polimórfico em Duck Typing: Custo de busca dinâmica em dicionário CPython -> Tempo O(1).
- Espaço: O(1) de espaço adicional.
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    objeto_qualquer: Any = ServicoEmail()

    # [X] NÃO-PYTHONIC: Forçar checagem estrita de tipos com isinstance() matando o polimorfismo
    print("[X] Nao-Pythonic (Checagem rígida com isinstance):")
    if isinstance(objeto_qualquer, ServicoEmail):
        objeto_qualquer.enviar_notificacao("dest", "msg")

    # [OK] PYTHONIC: Duck Typing direto ou EAFP (Easier to Ask Forgiveness)
    print("\n[OK] Pythonic (Duck Typing / EAFP):")
    try:
        objeto_qualquer.enviar_notificacao("dest", "msg")
    except AttributeError:
        print("[!] Objeto não implementa a interface esperada!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Confie no Duck Typing para escrever código flexível e reutilizável.
2. Caso queira garantir validações de tipos estáticos sem acoplar por herança, utilize `typing.Protocol` (PEP 544).
3. Mantenha os nomes de métodos consistentes entre classes polimórficas (ex: se um envia por `.enviar()`, os outros não devem usar `.dispatch()`).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    class Invalido:
        pass

    obj_invalido = Invalido()

    # Armadilha 1: AttributeError em runtime ao passar um objeto incompatível
    try:
        notificar_usuario(obj_invalido, "dest", "msg")
    except AttributeError as e:
        print(f"[!] Armadilha 1 (AttributeError em Duck Typing): {e}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "O que é Duck Typing e como ele se diferencia do Polimorfismo por Herança de linguagens como Java?"
A: "Em linguagens como Java, para que duas classes sejam usadas polimorficamente, elas precisam compartilhar explicitamente uma interface ou superclasse declarada.
    No Duck Typing do Python, o tipo exato ou a hierarquia do objeto não importam.
    Se o objeto fornece os métodos e propriedades exigidos no momento da chamada (se ele 'quaca como um pato'),
    o Python o aceita dinamicamente, permitindo baixíssimo acoplamento entre os componentes."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie três classes (`PDFReport`, `CSVReport`, `HTMLReport`), cada uma com o método `gerar(dados: dict) -> str` e processe uma lista delas polimorficamente.
# Exercício 2: Escreva uma função polimórfica `calcular_area_total(formas: list[Any]) -> float` onde cada objeto da lista calcula sua área via `.area()`.
# Exercício 3: Utilize a abordagem EAFP com `try/except AttributeError` para chamar um método polimórfico com fallback.


def main() -> None:
    print("==========================================================")
    print("  AULA 38: POLIMORFISMO, DUCK TYPING E INTERFACES")
    print("==========================================================")
    demonstrar_fundamentos_polimorfismo()
    demonstrar_processadores_polimorficos()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 38 executado com sucesso.")


if __name__ == "__main__":
    main()
