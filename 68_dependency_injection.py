"""
68_dependency_injection.py - Injeção de Dependências e Desacoplamento

Objetivos:
1. Desacoplar serviços injetando dependências no construtor em vez de instanciá-las internamente.
"""

from abc import ABC, abstractmethod


class ProvedorStorage(ABC):
    @abstractmethod
    def salvar_arquivo(self, nome: str, conteudo: bytes) -> str:
        pass


class StorageS3Simulado(ProvedorStorage):
    def salvar_arquivo(self, nome: str, conteudo: bytes) -> str:
        print(f"[S3] Upload simulado de '{nome}' no bucket AWS.")
        return f"https://s3.amazonaws.com/bucket/{nome}"


class ServicoUpload:
    def __init__(self, storage: ProvedorStorage) -> None:
        self.storage = storage

    def upload_foto_perfil(self, usuario_id: int, dados_foto: bytes) -> str:
        filename = f"avatar_user_{usuario_id}.jpg"
        return self.storage.salvar_arquivo(filename, dados_foto)


def main() -> None:
    print("==========================================================")
    print("  AULA 68: INJEÇÃO DE DEPENDÊNCIAS")
    print("==========================================================")
    storage = StorageS3Simulado()
    servico = ServicoUpload(storage=storage)
    url = servico.upload_foto_perfil(101, b"header_fake_bytes")
    print(f"URL gerada: {url}")
    print("\n[Concluido] Arquivo 68 executado com sucesso.")


if __name__ == "__main__":
    main()
