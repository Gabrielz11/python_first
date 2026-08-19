"""
34_encapsulamento.py - Encapsulamento, Atributos Privados e Name Mangling em Python

Objetivos:
1. Dominar o conceito de Encapsulamento em Python e a filosofia "We are all consenting adults here".
2. Compreender as três convenções de visibilidade: Público (`nome`), Protegido (`_protegido`) e Privado (`__privado`).
3. Entender o mecanismo de Name Mangling (`_NomeDaClasse__atributo`) aplicado pelo CPython em atributos com duplo sublinhado.
4. Aplicar técnicas de proteção de estado interno e invariantes em entidades de negócio.
5. Evitar a armadilha de achar que o Name Mangling é uma barreira de segurança criptográfica impenetrável.
"""


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é Encapsulamento em Python?
Encapsulamento é o princípio de POO que oculta os detalhes de implementação interna de um objeto
e restringe o acesso direto ao seu estado, permitindo alterações apenas através de métodos públicos autorizados.

Filosofia do Python ("Consenting Adults"):
Em linguagens como Java ou C++, existem palavras-chave rígidas do compilador (`private`, `protected`, `public`).
Em Python, NÃO existem modificadores de acesso rígidos. O controle é baseado em convenções e Name Mangling:

1. Atributo Público (`self.nome`): Acessível e modificável livremente de qualquer lugar.
2. Atributo Protegido (`self._saldo`): Prefixo de UM sublinhado (`_`). Convenção da PEP 8 que indica:
   "Este atributo é interno da classe ou suas subclasses. Não altere diretamente por fora!".
3. Atributo Privado (`self.__chave_secreta`): Prefixo de DOIS sublinhados (`__`). O CPython ativa o
   mecanismo de Name Mangling para evitar colisões acidentais de nomes em herança.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: NAME MANGLING DEMONSTRADO
# ==========================================================
class CofreSeguranca:
    def __init__(self, titular: str, codigo_pin: str, saldo_inicial: float) -> None:
        self.titular: str = titular  # Público
        self._codigo_pin: str = codigo_pin  # Protegido (Convenção)
        self.__saldo: float = saldo_inicial  # Privado (Name Mangling)

    def consultar_saldo(self, pin_informado: str) -> float:
        """Método público para acesso controlado ao saldo privado."""
        if pin_informado != self._codigo_pin:
            raise PermissionError("PIN de seguranca incorreto!")
        return self.__saldo


def demonstrar_fundamentos_encapsulamento() -> None:
    print("\n--- 1. FUNDAMENTOS: Name Mangling e Níveis de Acesso ---")

    cofre = CofreSeguranca("Gabriel", "1234", 15000.0)

    # Acesso Público: OK
    print(f"Titular (Publico): {cofre.titular}")

    # Acesso Protegido: Funciona, mas viola a convenção PEP 8
    print(f"PIN (Protegido via _): {cofre._codigo_pin}")

    # Acesso ao Saldo via Método Autorizado
    print(f"Saldo via consultar_saldo(): R$ {cofre.consultar_saldo('1234'):.2f}")

    # Tentativa de acesso direto ao atributo privado __saldo
    try:
        _ = cofre.__saldo  # type: ignore # Lança AttributeError!
    except AttributeError as e:
        print(f"[!] Tentativa de acesso a cofre.__saldo falhou (AttributeError): {e}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: COMO BURLAR O NAME MANGLING
# ==========================================================
def demonstrar_internamente_name_mangling() -> None:
    print("\n--- 2. INTERNO: Inspecionando o Name Mangling no __dict__ ---")

    cofre = CofreSeguranca("Gabriel", "1234", 15000.0)

    # O CPython renomeou __saldo para _CofreSeguranca__saldo!
    print("Dicionario de atributos da instancia (cofre.__dict__):")
    for chave, valor in cofre.__dict__.items():
        print(f"  - Chave: {chave!r} | Valor: {valor!r}")

    # Burlando o Name Mangling (Demostra que não é segurança absoluta em CPython)
    saldo_burlado = getattr(cofre, "_CofreSeguranca__saldo")
    print(f"\nAcessando via _CofreSeguranca__saldo (Burlado): R$ {saldo_burlado:.2f}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class GatewayPagamentoService:
    """Serviço backend com encapsulamento estrito de tokens e credenciais de API."""

    def __init__(self, api_key: str, secret_key: str) -> None:
        self._api_key = api_key
        self.__secret_key = secret_key
        self._contador_requisicoes = 0

    def processar_transacao(self, valor: float) -> bool:
        self._incrementar_contador()
        # Utiliza o secret privado internamente sem expor na API
        auth_header = f"Bearer {self._api_key}:{self.__secret_key}"
        print(f"  [Gateway] Processando R$ {valor:.2f} com Auth Header: {auth_header[:25]}...")
        return True

    def _incrementar_contador(self) -> None:
        """Método protegido interno."""
        self._contador_requisicoes += 1


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Gateway de Pagamentos ---")
    gateway = GatewayPagamentoService(api_key="pk_live_998877", secret_key="sk_live_11223344")
    gateway.processar_transacao(250.0)


# ==========================================================
# 5. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Name Mangling: Ocorre inteiramente durante a FASE DE COMPILAÇÃO de bytecode do CPython.
- Tempo: O(1) [Custo nulo de execução em runtime].
- Espaço: O(1) de memória (apenas altera o nome da chave string no dicionário `__dict__`).
"""


# ==========================================================
# 6. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Entupir a classe com getters e setters explícitos estilo Java (get_saldo/set_saldo)
    print("[X] Nao-Pythonic (Getters/Setters manuais estilo Java):")
    print("  class Conta: def get_saldo(self): return self._saldo")

    # [OK] PYTHONIC: Atributos públicos por padrão, usando _ para indicação interna ou @property se precisar de validação
    print("\n[OK] Pythonic:")
    print("  Em Python, use atributos públicos diretos. Se precisar de lógica ao acessar, migre para @property!")


# ==========================================================
# 7. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Utilize um único sublinhado `_atributo` por padrão para métodos e dados que devem ser tratados como internos.
2. Utilize dois sublinhados `__atributo` (Name Mangling) APENAS para evitar colisões de nomes em classes projetadas para Herança Profunda.
3. Lembre-se que em Python o encapsulamento é uma convenção cultural e de arquitetura, não uma trava de segurança militar.
"""


# ==========================================================
# 8. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Achar que Name Mangling impede o acesso ou modifica o valor por completo
    class Base:
        def __init__(self) -> None:
            self.__segredo = "Base"

    class Derivada(Base):
        def __init__(self) -> None:
            super().__init__()
            self.__segredo = "Derivada"  # Não sobrescreve _Base__segredo, cria _Derivada__segredo!

    d = Derivada()
    print(f"[!] Name mangling evita sobrescrita indesejada em herança: {d.__dict__}")


# ==========================================================
# 9. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Como funciona o Name Mangling em Python e por que ele é utilizado?"
A: "O Name Mangling é o processo pelo qual o CPython reescreve identificadores que começam com dois ou mais sublinhados (`__atributo`),
    acrescentando o prefixo `_NomeDaClasse` (ex: `_Conta__saldo`).
    Seu principal objetivo NÃO é a segurança contra acesso externo, mas sim prevenir a sobrescrita acidental
    de atributos internos quando uma subclasse herda de uma classe pai (evitando Name Collisions em herança)."
"""


# ==========================================================
# 10. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `ContaBancaria` com atributo protegido `_saldo` e métodos `depositar` e `sacar` com validação.
# Exercício 2: Inspecione a chave de um atributo `__senha` no dicionário `__dict__` de uma classe criada por você.
# Exercício 3: Escreva uma subclasse que herde de uma classe pai com atributo `__id` e comprove que o atributo da pai não foi sobrescrito.


def main() -> None:
    print("==========================================================")
    print("  AULA 34: ENCAPSULAMENTO E NAME MANGLING EM PYTHON")
    print("==========================================================")
    demonstrar_fundamentos_encapsulamento()
    demonstrar_internamente_name_mangling()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 34 executado com sucesso.")


if __name__ == "__main__":
    main()
