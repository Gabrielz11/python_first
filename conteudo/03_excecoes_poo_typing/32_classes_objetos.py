"""
32_classes_objetos.py - Classes, Objetos, Atributos de Instância vs Classe e Ciclo de Vida

Objetivos:
1. Dominar a fundamentação da Programação Orientada a Objetos (POO) em Python 3.
2. Diferenciar Atributos de Instância (específicos de cada objeto) de Atributos de Classe (compartilhados).
3. Compreender o papel do parâmetro `self` nos métodos de instância.
4. Entender o ciclo de vida de um objeto no CPython (Alocação com `__new__` e Inicialização com `__init__`).
5. Modelar Entidades de Domínio e evitar a armadilha clássica de atributos de classe mutáveis.
"""

from typing import Any


# ==========================================================
# 1. CONCEITO
# ==========================================================
"""
O que é uma Classe e um Objeto em Python?
- Classe: É o "molde" ou "blueprint" que define a estrutura (atributos) e os comportamentos (métodos)
  de um determinado tipo de dado. Em Python, a classe também é um objeto de primeira classe na memória RAM!
- Objeto (Instância): É a concretização do molde reservada na memória Heap.

Atributos de Instância vs Atributos de Classe:
- Atributos de Instância (`self.nome = valor`): Pertencem exclusivamente àquela instância específica do objeto.
- Atributos de Classe (`versao = "1.0"`): Pertencem à classe e são COMPARTILHADOS por TODAS as instâncias daquela classe.
"""


# ==========================================================
# 2. SINTAXE E FUNDAMENTOS: CRIAÇÃO DE CLASSES E INSTÂNCIAS
# ==========================================================
class ServidorBackend:
    # Atributo de Classe (Compartilhado por todas as instâncias)
    SISTEMA_OPERACIONAL: str = "Linux Ubuntu 24.04 LTS"
    total_servidores_criados: int = 0

    def __init__(self, hostname: str, ip: str, memoria_gb: int) -> None:
        # Atributos de Instância (Únicos por objeto)
        self.hostname: str = hostname
        self.ip: str = ip
        self.memoria_gb: int = memoria_gb
        self.ativo: bool = True

        # Incrementa o contador global da classe
        ServidorBackend.total_servidores_criados += 1

    def desativar(self) -> None:
        """Método de instância que altera o estado do servidor."""
        self.ativo = False
        print(f"  [Servidor {self.hostname}] foi desativado.")


def demonstrar_fundamentos_classes() -> None:
    print("\n--- 1. FUNDAMENTOS: Instâncias e Atributos de Classe ---")

    s1 = ServidorBackend("srv-web-01", "192.168.1.10", 16)
    s2 = ServidorBackend("srv-db-01", "192.168.1.20", 64)

    print(f"Servidor 1: {s1.hostname} | RAM: {s1.memoria_gb}GB | SO: {s1.SISTEMA_OPERACIONAL}")
    print(f"Servidor 2: {s2.hostname} | RAM: {s2.memoria_gb}GB | SO: {s2.SISTEMA_OPERACIONAL}")
    print(f"Total de Servidores Instanciados: {ServidorBackend.total_servidores_criados}")

    s1.desativar()
    print(f"Status s1.ativo: {s1.ativo} | Status s2.ativo: {s2.ativo}")


# ==========================================================
# 3. EXEMPLOS PROGRESSIVOS: CICLO DE VIDA (__NEW__ E __INIT__)
# ==========================================================
class ExemploCicloVida:
    def __new__(cls, *args: Any, **kwargs: Any) -> "ExemploCicloVida":
        print("  1. __new__ chamado: Alocando memória para a nova instância no CPython...")
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome: str) -> None:
        print("  2. __init__ chamado: Inicializando os atributos da instância criada...")
        self.nome = nome


def demonstrar_ciclo_vida() -> None:
    print("\n--- 2. EXEMPLOS PROGRESSIVOS: Ciclo de Vida (__new__ vs __init__) ---")
    obj = ExemploCicloVida("Demonstração")
    print(f"Objeto instanciado com sucesso: {obj.nome}")


# ==========================================================
# 4. EXEMPLO PRÁTICO / BACKEND / PRODUÇÃO
# ==========================================================
class UsuarioDomain:
    """Entidade de Domínio representando um Usuário em um sistema backend."""

    def __init__(self, user_id: int, email: str, perfil: str = "usuario") -> None:
        self.user_id = user_id
        self.email = email
        self.perfil = perfil
        self._tentativas_login_invalidas: int = 0

    def registrar_falha_login(self) -> None:
        self._tentativas_login_invalidas += 1
        if self._tentativas_login_invalidas >= 3:
            print(f"  [Alerta Seguranca] Usuario {self.email} bloqueado por multiplas falhas!")

    def resetar_falhas(self) -> None:
        self._tentativas_login_invalidas = 0


def demonstrar_aplicacao_backend() -> None:
    print("\n--- 3. APLICAÇÃO BACKEND: Entidade de Domínio Usuario ---")
    user = UsuarioDomain(user_id=105, email="gabriel@empresa.com")

    print(f"Usuario criado: ID {user.user_id} | Email: {user.email}")
    user.registrar_falha_login()
    user.registrar_falha_login()
    user.registrar_falha_login()


# ==========================================================
# 5. COMO FUNCIONA INTERNAMENTE: __DICT__ E NAMESPACE
# ==========================================================
"""
Como o Python armazena Atributos de Objetos na Memória (CPython):
1. Dicionário `__dict__`: Por padrão, toda instância de classe possui um dicionário interno
   chamado `__dict__` onde armazena seus atributos de instância como pares chave-valor.
2. Resolução de Atributos (Lookup Order): Quando você acessa `objeto.atributo`:
   - 1º O CPython busca a chave `atributo` no `objeto.__dict__`.
   - 2º Se não encontrar, busca no `Classe.__dict__`.
   - 3º Se não encontrar, busca nas classes pai (MRO).
   - 4º Se não encontrar em nenhuma lugar, dispara `AttributeError`.
"""


# ==========================================================
# 6. COMPLEXIDADE TEMPORAL E ESPACIAL
# ==========================================================
"""
Análise de Complexidade:
- Instanciação de Objeto (`Objeto()`): Tempo O(1), Espaço O(1).
- Acesso a Atributos (`obj.atributo`): Custo de busca em tabela Hash CPython -> Tempo médio O(1).
- Overhead de Memória: Cada objeto consome memória para o dicionário `__dict__` (pode ser otimizado via `__slots__`).
"""


# ==========================================================
# 7. NÃO-PYTHONIC VS PYTHONIC
# ==========================================================
def demonstrar_comparativo_pythonic() -> None:
    print("\n--- 5. COMPARATIVO DE CÓDIGO ---")

    # [X] NÃO-PYTHONIC: Usar dicionários soltos para representar entidades complexas com comportamento
    print("[X] Nao-Pythonic (Dicionarios anônimos para lógica de negócio):")
    usr_dict = {"id": 1, "status": "ativo"}
    # Lógica espalhada fora da entidade
    usr_dict["status"] = "inativo"
    print(f"  Resultado dict: {usr_dict}")

    # [OK] PYTHONIC: Encapsular estado e comportamento dentro de uma Classe dedicada
    print("\n[OK] Pythonic (Entidade de Classe):")

    class UsuarioModel:
        def __init__(self, id_u: int) -> None:
            self.id_u = id_u
            self.status = "ativo"

        def inativar(self) -> None:
            self.status = "inativo"

    u = UsuarioModel(1)
    u.inativar()
    print(f"  Resultado classe: ID {u.id_u} Status {u.status}")


# ==========================================================
# 8. BOAS PRÁTICAS E REGRAS DE OURO
# ==========================================================
"""
1. Sempre inicialize todos os atributos de instância dentro do método `__init__`.
2. Evite a armadilha de definir listas ou dicionários mutáveis como Atributos de Classe (serão compartilhados entre todas as instâncias!).
3. Utilize nomes de classes em `PascalCase` e atributos/métodos em `snake_case` (PEP 8).
"""


# ==========================================================
# 9. ARMADILHAS E ERROS COMUNS
# ==========================================================
def demonstrar_armadilhas() -> None:
    print("\n--- 6. ARMADILHAS E ERROS COMUNS ---")

    # Armadilha 1: Atributo de Classe Mutável Compartilhado
    class ServicoComArmadilha:
        # [!] PERIGO: Atributo de classe mutável!
        historico_requisicoes: list[str] = []

        def adicionar_log(self, msg: str) -> None:
            self.historico_requisicoes.append(msg)

    s1 = ServicoComArmadilha()
    s2 = ServicoComArmadilha()

    s1.adicionar_log("Req 1 do Servidor A")
    print(f"[!] Armadilha (Atributo Mutavel de Classe): s2 enxerga os logs de s1 -> {s2.historico_requisicoes}")


# ==========================================================
# 10. CONEXÃO COM ENTREVISTAS TÉCNICAS
# ==========================================================
"""
Pergunta de Entrevista:
Q: "Qual a diferença entre o método `__new__` e o método `__init__` em Python?"
A: "1. `__new__` é o VERDADEIRO construtor da classe. É um método estático que aloca o espaço de memória no CPython
       e retorna a nova instância criada do objeto.
    2. `__init__` é o inicializador da instância. Ele recebe a instância recém-criada através do primeiro parâmetro (`self`)
       e define os seus atributos iniciais. O `__init__` não deve retornar nenhum valor (deve retornar `None`)."
"""


# ==========================================================
# 11. EXERCÍCIOS SUGERIDOS
# ==========================================================
# Exercício 1: Crie uma classe `Carro` com atributos `marca`, `modelo` e `velocidade_atual` e um método `acelerar(incremento: int)`.
# Exercício 2: Crie uma classe `ContadorInstancias` que mantenha um atributo de classe contando quantas instâncias foram criadas.
# Exercício 3: Inspecione o `__dict__` de uma instância criada e de sua classe utilizando o atributo dunder `.__dict__`.


def main() -> None:
    print("==========================================================")
    print("  AULA 32: CLASSES, OBJETOS E CICLO DE VIDA EM POO")
    print("==========================================================")
    demonstrar_fundamentos_classes()
    demonstrar_ciclo_vida()
    demonstrar_aplicacao_backend()
    demonstrar_comparativo_pythonic()
    demonstrar_armadilhas()
    print("\n[Concluido] Arquivo 32 executado com sucesso.")


if __name__ == "__main__":
    main()
