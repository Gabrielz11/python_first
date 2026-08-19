"""
66_clean_code.py - Princípios de Clean Code Aplicados ao Python

Objetivos:
1. Escrever código limpo, autoexplicativo e legível.
2. Manter funções pequenas com responsabilidade única.
3. Evitar comentários redundantes que apenas repetem o código.
"""

def calcular_desconto(preco: float, percentual_desconto: float) -> float:
    """Calcula o preço final após aplicar o desconto percentual."""
    if percentual_desconto <= 0:
        return preco
    fator = 1.0 - (percentual_desconto / 100.0)
    return preco * fator


def main() -> None:
    print("==========================================================")
    print("  AULA 66: PRINCÍPIOS DE CLEAN CODE EM PYTHON")
    print("==========================================================")
    preco_final = calcular_desconto(200.0, 15.0)
    print(f"Preço final com Clean Code: R$ {preco_final:.2f}")
    print("\n[Concluido] Arquivo 66 executado com sucesso.")


if __name__ == "__main__":
    main()
