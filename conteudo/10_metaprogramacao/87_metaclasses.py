"""
87_metaclasses.py - Metaclasses e Criação Dinâmica de Classes (`type`)

Objetivos:
1. Compreender que em Python classes são instâncias de Metaclasses (a metaclasse padrão é `type`).
2. Criar uma Metaclass customizada herdando de `type` para interceptar a criação de novas classes.
"""

from typing import Any


class MetaclassValidacao(type):
    def __new__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> type:
        # Garante que todas as subclasses tenham um atributo ou método específico
        if name != "BaseModel" and "validar" not in namespace:
            raise TypeError(f"A classe '{name}' deve implementar o método 'validar()'!")
        return super().__new__(cls, name, bases, namespace)


class BaseModel(metaclass=MetaclassValidacao):
    pass


class ModeloUsuario(BaseModel):
    def validar(self) -> bool:
        return True


def main() -> None:
    print("==========================================================")
    print("  AULA 87: METACLASSES E INTERCEPTAÇÃO DE DECLAÇÃO DE CLASSES")
    print("==========================================================")
    u = ModeloUsuario()
    print(f"Validação do modelo: {u.validar()}")

    try:
        # Tentar declarar classe sem método validar lança TypeError na COMPILAÇÃO da classe!
        class ModeloInvalido(BaseModel):
            pass
    except TypeError as e:
        print(f"[X] Metaclass barrou classe inválida na criação: {e}")
    print("\n[Concluido] Arquivo 87 executado com sucesso.")


if __name__ == "__main__":
    main()
