"""
40_classmethod_staticmethod.py - Métodos de Classe, Métodos Estáticos e Factory Methods

Objetivos:
1. Dominar as diferenças entre Métodos de Instância (`self`), Métodos de Classe (`@classmethod`) e Métodos Estáticos (`@staticmethod`).
2. Utilizar `@classmethod` para implementar o Padrão de Projeto Factory Method (Construtores Alternativos).
3. Utilizar `@staticmethod` para organizar funções utilitárias que pertencem ao namespace da classe.
4. Compreender a resolução do parâmetro `cls` na herança com `@classmethod`.
5. Desenvolver instanciadores resilientes de DTOs e entidades a partir de payloads JSON/CSV em serviços backend.
"""

from datetime import date
import json
from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
Diferença entre os três tipos de métodos em Python:

1. Métodos de Instância:
   - Recebem `self` como primeiro argumento.
   - Têm acesso ao estado da instância (`self.atributo`) e da classe (`self.__class__`).

2. Métodos de Classe (`@classmethod`):
   - Recebem `cls` (a própria classe) como primeiro argumento.
   - Não têm acesso aos atributos de uma instância específica.
   - Uso principal: Factory Methods (construtores alternativos) e manipulação de estado de classe.
   - Suportam polimorfismo em herança (o `cls` aponta para a subclasse que chamou o método).

3. Métodos Estáticos (`@staticmethod`):
   - Não recebem nem `self` nem `cls` automaticamente.
   - Comportam-se como funções normais, mas ficam agrupadas dentro do namespace da classe por razões organizacionais.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: FACTORY METHOD COM CLASSMETHOD
# ==========================================================
class UsuarioDTO:
    def __init__(self, id_usuario: int, nome: str, email: str, data_cadastro: date) -> None:
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.data_cadastro = data_cadastro

    def __repr__(self) -> str:
        return f"UsuarioDTO(id={self.id_usuario}, nome={self.nome!r}, email={self.email!r})"

    # Factory Method 1: Construtor Alternativo a partir de um Dicionário
    @classmethod
    def from_dict(cls, dados: dict[str, Any]) -> "UsuarioDTO":
        """Instancia UsuarioDTO a partir de um dict."""
        return cls(
            id_usuario=int(dados["id"]),
            nome=str(dados["nome"]),
            email=str(dados["email"]),
            data_cadastro=date.fromisoformat(dados.get("data", "2026-01-01")),
        )

    # Factory Method 2: Construtor Alternativo a partir de uma String JSON
    @classmethod
    def from_json(cls, json_str: str) -> "UsuarioDTO":
        """Instancia UsuarioDTO a partir de um JSON."""
        dados = json.loads(json_str)
        return cls.from_dict(dados)

    # Método Estático Utilidade: Não precisa da instância nem da classe
    @staticmethod
    def validar_email(email: str) -> bool:
        """Utilitario de validacao de formato de email."""
        return "@" in email and "." in email


def demonstrar_fundamentos_factory() -> None:
    print("\n--- 1. FUNDAMENTOS: Factory Methods com @classmethod ---")

    # Instanciação padrão via __init__
    u1 = UsuarioDTO(1, "Gabriel", "gabriel@empresa.com", date(2026, 8, 19))
    print(f"Padrão __init__: {u1}")

    # Instanciação via Factory Method from_dict
    payload_dict = {"id": 2, "nome": "Ana Silva", "email": "ana@empresa.com", "data": "2026-08-19"}
    u2 = UsuarioDTO.from_dict(payload_dict)
    print(f"Factory from_dict: {u2}")

    # Instanciação via Factory Method from_json
    payload_json = '{"id": 3, "nome": "Carlos", "email": "carlos@empresa.com"}'
    u3 = UsuarioDTO.from_json(payload_json)
    print(f"Factory from_json: {u3}")

    # Uso do @staticmethod
    valido = UsuarioDTO.validar_email("teste@empresa.com")
    print(f"Email e valido (via @staticmethod)? {valido}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: POLIMORFISMO COM CLS EM HERANÇA
# ==========================================================
class DocumentoBase:
    def __init__(self, titulo: str) -> None:
        self.titulo = titulo

    @classmethod
    def criar_padrao(cls, titulo: str) -> "DocumentoBase":
        # O cls garante que a SUBCLASSE correta seja instanciada!
        return cls(titulo=f"[PADRAO] {titulo}")


class RelatorioFinanceiro(DocumentoBase):
    pass


def demonstrar_polimorfismo_cls() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Polimorfismo do cls em Herança ---")

    doc = DocumentoBase.criar_padrao("Contrato")
    relatorio = RelatorioFinanceiro.criar_padrao("Balanço 2026")

    print(f"Tipo do doc: {type(doc).__name__} | Titulo: {doc.titulo}")
    print(f"Tipo do relatorio (Respeitou a subclasse!): {type(relatorio).__name__} | Titulo: {relatorio.titulo}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class ConfiguracaoServicoBackend:
    """Carregador de configurações de microsserviços via Factory Methods."""

    def __init__(self, host: str, porta: int, debug: bool) -> None:
        self.host = host
        self.porta = porta
        self.debug = debug

    @classmethod
    def para_desenvolvimento(cls) -> "ConfiguracaoServicoBackend":
        return cls(host="localhost", porta=8080, debug=True)

    @classmethod
    def para_producao(cls) -> "ConfiguracaoServicoBackend":
        return cls(host="api.empresa.com", porta=443, debug=False)


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Presets de Configuração ---")
    config_dev = ConfiguracaoServicoBackend.para_desenvolvimento()
    config_prod = ConfiguracaoServicoBackend.para_producao()

    print(f"DEV  -> Host: {config_dev.host}:{config_dev.porta} | Debug: {config_dev.debug}")
    print(f"PROD -> Host: {config_prod.host}:{config_prod.porta} | Debug: {config_prod.debug}")


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: DESCRITORES
# ==========================================================
"""
Como o CPython executa @classmethod e @staticmethod:
1. Ambos são implementados através do Protocolo de Descritores (Descriptors).
2. O descritor `classmethod` intercepta a chamada e passa a classe atual como primeiro argumento posicional (`cls`).
3. O descritor `staticmethod` intercepta a chamada e impede a injeção do primeiro parâmetro (`self` ou `cls`),
   chamando a função pura diretamente.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Invocação de `@classmethod` ou `@staticmethod`: Custo de interpolação do descriptor em CPython -> Tempo O(1), Espaço O(1).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 4. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Sobregar o __init__ com checagem de tipos flexíveis ou múltiplos ifs
    print("[X] Nao-Pythonic (Um unico __init__ tentando parsear dict, string ou int):")
    print("  def __init__(self, dados): if isinstance(dados, str): ...  # Código poluído!")

    # [OK] PYTHONIC: Utilizar Factory Methods nomeados expressivos (@classmethod)
    print("\n[OK] Pythonic:")
    print("  Objeto.from_dict(d) | Objeto.from_json(s)  # Factory Methods limpos e autodocumentáveis!")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Nomeie os Factory Methods com o prefixo `from_` (ex: `from_dict`, `from_env`, `from_tuple`).
2. Utilize `@classmethod` em vez de `@staticmethod` para construtores alternativos, pois o `@classmethod` respeita subclasses em herança (`cls`).
3. Utilize `@staticmethod` APENAS para funções utilitárias puras que não leem nem alteram o estado da classe ou instância.
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 5. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Tentar acessar atributos de instância (self) dentro de um @classmethod ou @staticmethod
    class ArmadilhaClass:
        def __init__(self) -> None:
            self.valor = 100

        @classmethod
        def tentar_acessar(cls) -> None:
            try:
                _ = cls.valor  # type: ignore # Lança AttributeError!
            except AttributeError as e:
                print(f"[!] Armadilha 1 (cls não possui atributos de instância): {e}")

    ArmadilhaClass.tentar_acessar()


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre `@classmethod` e `@staticmethod` em Python e quando você deve usar cada um?"
A: "1. `@classmethod` recebe a CLASSE (`cls`) como primeiro parâmetro. É usado principalmente para implementar Factory Methods
       (construtores alternativos) e métodos que manipulam o estado da classe. Ele suporta polimorfismo na herança.
    2. `@staticmethod` NÃO recebe nem a instância (`self`) nem a classe (`cls`). Funciona como uma função pura isolada,
       mantida dentro da classe apenas por conveniência de namespace e organização do código."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Data` com atributos `dia`, `mes`, `ano` e um Factory Method `from_string("19/08/2026")` que parseie a string.
# Exercício 2: Escreva um `@staticmethod` chamado `is_valida(dia, mes, ano)` que valide se a data é coerente.
# Exercício 3: Implemente uma hierarquia onde a superclasse possui um `@classmethod` fábrica e comprove que a subclasse retorna instâncias do seu próprio tipo.


def main() -> None:
    print("==========================================================")
    print("  AULA 40: MÉTODOS DE CLASSE, ESTÁTICOS E FACTORY METHODS")
    print("==========================================================")
    demonstrar_fundamentos_factory()
    demonstrar_polimorfismo_cls()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 40 executado com sucesso.")


if __name__ == "__main__":
    main()
