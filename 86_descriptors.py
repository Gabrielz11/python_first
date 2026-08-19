"""
86_descriptors.py - Descriptors em Python (`__get__`, `__set__`, `__delete__`)

Objetivos:
1. Implementar o protocolo Descriptor para reutilizar lógica de atributos (como `@property` faz por debaixo dos panos).
"""

from typing import Any


class DescriptorValidadorString:
    def __init__(self, nome_atributo: str) -> None:
        self.nome_atributo = nome_atributo

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.nome_atributo)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError(f"O atributo '{self.nome_atributo}' deve ser uma string!")
        instance.__dict__[self.nome_atributo] = value


class Perfil:
    nome = DescriptorValidadorString("nome")

    def __init__(self, nome: str) -> None:
        self.nome = nome


def main() -> None:
    print("==========================================================")
    print("  AULA 86: DESCRIPTORS PROTOCOL")
    print("==========================================================")
    p = Perfil("Gabriel")
    print(f"Nome validado pelo Descriptor: {p.nome}")
    try:
        p.nome = 123  # type: ignore
    except TypeError as e:
        print(f"[X] Validação do Descriptor barrou tipo inválido: {e}")
    print("\n[Concluido] Arquivo 86 executado com sucesso.")


if __name__ == "__main__":
    main()
