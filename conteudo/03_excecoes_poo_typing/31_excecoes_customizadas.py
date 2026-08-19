"""
31_excecoes_customizadas.py - Criação de Exceções de Domínio Personalizadas

Objetivos:
1. Criar classes de exceções customizadas herdando de `Exception`.
2. Adicionar atributos de contexto (ex: código de erro HTTP, payload).
3. Estruturar exceções de domínio para APIs Backend.
"""

class RegraNegocioException(Exception):
    def __init__(self, mensagem: str, status_code: int = 400) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.status_code = status_code


class SaldoInsuficienteException(RegraNegocioException):
    def __init__(self, saldo_atual: float, valor_saque: float) -> None:
        msg = f"Saldo insuficiente: R$ {saldo_atual:.2f} para saque de R$ {valor_saque:.2f}."
        super().__init__(msg, status_code=422)
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque


def realizar_saque(saldo: float, valor: float) -> float:
    if valor > saldo:
        raise SaldoInsuficienteException(saldo_atual=saldo, valor_saque=valor)
    return saldo - valor


def main() -> None:
    print("==========================================================")
    print("  AULA 31: EXCEÇÕES DE DOMÍNIO CUSTOMIZADAS")
    print("==========================================================")
    try:
        realizar_saque(100.0, 250.0)
    except SaldoInsuficienteException as e:
        print(f"[X] Capturada Exceção de Domínio: {e.mensagem}")
        print(f"    Status HTTP sugerido: {e.status_code}")
    print("\n[Concluido] Arquivo 31 executado com sucesso.")


if __name__ == "__main__":
    main()
