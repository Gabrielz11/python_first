# 🐍 Python First: Trilha Completa de Engenharia de Software com Python 3.12+

> **Do Básico ao Nível Engenheiro de Software Sênior: Laboratório Prático, Arquitetura, Algoritmos, Concorrência e Engenharia de Produção.**

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/M%C3%B3dulos-87%2F87%20Conclu%C3%ADdos-brightgreen.svg)]()
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

O **PythonFirst** é um ecossistema educacional completo projetado para transformar qualquer pessoa em um **Engenheiro de Software Python de nível profissional**.

Diferente de tutoriais superficiais, cada um dos **87 módulos executáveis** funciona como uma **mini aula prática e autossuficiente**, unindo teoria profunda sobre o funcionamento interno do CPython, análises formais de complexidade (**Big O temporal e espacial**), comparações idiomáticas (*Pythonic vs Non-Pythonic*), padrões de projeto, concorrência, testes automatizados e conexões diretas com **perguntas de entrevistas técnicas de Big Techs**.

---

## 📖 Guias Rápidos de Navegação

- 🚀 **[COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md)** — Instruções detalhadas de execução para cada módulo individual ou em lote.
- 📅 **[cronograma_estudo_python.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/cronograma_estudo_python.md)** — Cronograma pedagógico guiado de 10 semanas.
- 📁 **[conteudo/](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo)** — Diretório com todas as 10 categorias e 87 arquivos de estudo.

---

## 🧩 Metodologia Pedagógica (Ciclo de Aprendizado)

Cada módulo do repositório foi construído segundo o ciclo de aprendizado ativo em 7 passos:

```text
  [ 1. CONCEITO ] ──────► Entender o funcionamento interno no CPython e alocação de memória.
         │
  [ 2. SINTAXE ]  ──────► Conhecer a sintaxe moderna e Type Hints (Python 3.12+).
         │
  [ 3. EXEMPLO ]  ──────► Executar código prático e observar as saídas no console.
         │
  [ 4. COMPARATIVO ] ───► Analisar a abordagem Não-Pythonic vs Pythonic (EAFP, Truthiness, Bytecode).
         │
  [ 5. ARMADILHAS ] ────► Identificar antipadrões, vazamentos de memória e exceções de runtime.
         │
  [ 6. BIG O & PROD ] ──► Analisar a complexidade temporal/espacial e cenários reais de backend.
         │
  [ 7. EXERCÍCIOS ] ────► Fixar o conhecimento resolvendo desafios propostos ao final do arquivo.
```

---

## 📐 Estrutura do Repositório

O projeto possui uma estrutura limpa, moderna e modular:

```text
pythonfirst/
│
├── 📂 conteudo/                                # 87 Módulos práticos divididos em 10 categorias
│   ├── 📁 01_fundamentos_collections/         # Módulos 01 a 17 (Variáveis, Loops, Listas, Dicts, Sets, Collections)
│   ├── 📁 02_python_idiomatico_pacotes/      # Módulos 18 a 29 (EAFP, Slicing, Itertools, Functools, Pathlib)
│   ├── 📁 03_excecoes_poo_typing/             # Módulos 30 a 45 (POO, ABC, Dataclasses, Protocol, Generics)
│   ├── 📁 04_iteradores_decoradores_contexto/ # Módulos 46 a 51 (Yield, Decorators, Contextlib)
│   ├── 📁 05_async_concorrencia/              # Módulos 52 a 58 (Asyncio, Threads, Multiprocessing, GIL)
│   ├── 📁 06_logging_debugging_testes/        # Módulos 59 a 65 (Logging, Debugging, Pytest, Mocks)
│   ├── 📁 07_engenharia_software/             # Módulos 66 a 70 (Clean Code, SOLID, DI, Repository Pattern)
│   ├── 📁 08_dsa_algoritmos/                  # Módulos 71 a 81 (Big O, Hash Maps, Pilhas, Árvores, Grafos)
│   ├── 📁 09_http_resiliencia/                # Módulos 82 a 84 (HTTP REST, Cliente Nativo, Retries & Backoff)
│   └── 📁 10_metaprogramacao/                 # Módulos 85 a 87 (Getattr, Descriptors, Metaclasses)
│
├── 📄 COMO_EXECUTAR.md                         # Guia de comandos de execução e testes
├── 📄 README.md                                # Documentação principal e índice do repositório
├── 📄 cronograma_estudo_python.md              # Trilha pedagógica orientada no tempo
├── 📄 verify_all_87.py                        # Script de auditoria que executa e valida os 87 arquivos
├── 📄 pyproject.toml                           # Configurações do Ruff, Mypy e Pytest
├── 📄 requirements.txt                        # Dependências do projeto
└── 📄 .gitignore                               # Regras de exclusão do Git
```

---

## 🗺️ Trilha de Aprendizado Completa (Módulos 01 ao 87)

### 🔹 1. Fundamentos da Linguagem & Collections (`conteudo/01_fundamentos_collections/`)
- [`01_variaveis.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/01_variaveis.py) — Tipagem dinâmica vs forte, ponteiros de memória Heap, `id()`, mutabilidade.
- [`02_operadores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/02_operadores.py) — Operadores aritméticos, lógicos, bitwise, curto-circuito, `==` vs `is`.
- [`03_tipos_dados.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/03_tipos_dados.py) — Primitivos (`int`, `float`, `bool`, `str`, `None`), casting explícito, Truthy/Falsy.
- [`04_condicionais.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_condicionais.py) — Tomada de decisão, operadores ternários, Early Return e cláusulas de guarda.
- [`05_match_case.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_match_case.py) — Structural Pattern Matching (Python 3.10+), desestruturação, wildcards `_` e guards.
- [`06_loops.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_loops.py) — Laços `for`, `while`, `break`, `continue`, e os blocos idiomáticos `for...else` / `while...else`.
- [`07_range_enumerate_zip.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_range_enumerate_zip.py) — Iteração performática com `range()`, `enumerate()`, `zip()` e `strict=True`.
- [`08_funcoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_funcoes.py) — Definição de funções, parâmetros posicionais, nomeados, Keyword-Only (`*`) e Positional-Only (`/`).
- [`09_args_kwargs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_args_kwargs.py) — Argumentos variádicos `*args` (tupla) e `**kwargs` (dicionário) e repasse de argumentos.
- [`10_escopo_legb.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_escopo_legb.py) — Regra LEGB (Local, Enclosing, Global, Built-in), instruções `global` e `nonlocal`.
- [`11_lambda.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/11_lambda.py) — Funções anônimas vs `def`, uso com `sorted()`, `map()`, `filter()` e closures.
- [`12_listas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/12_listas.py) — Array dinâmico de ponteiros no CPython, Shallow Copy vs Deep Copy e análise Big O de operações.
- [`13_tuplas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/13_tuplas.py) — Sequências imutáveis, CPython Freelist, Unpacking e Hashability (tuplas como chaves de dict).
- [`14_dicionarios.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/14_dicionarios.py) — Tabela Hash compacta (Python 3.6+), métodos `.get()`, `.setdefault()`, views dinâmicas e busca $O(1)$ média.
- [`15_sets.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/15_sets.py) — Teoria dos conjuntos (união `|`, interseção `&`, diferença `-`), membership $O(1)$, deduplicação e `frozenset`.
- [`16_comprehensions.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/16_comprehensions.py) — List, Set, Dict Comprehensions, bytecode C-level `LIST_APPEND` e Generator Expressions.
- [`17_collections.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/17_collections.py) — Módulo `collections`: `Counter`, `defaultdict`, `deque` ($O(1)$ `popleft`), `NamedTuple` e `ChainMap`.

---

### 🟢 2. Python Idiomático, Arquivos & Pacotes (`conteudo/02_python_idiomatico_pacotes/`)
- [`18_python_idiomatico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/18_python_idiomatico.py) — Filosofia Pythonic (Zen do Python - PEP 20), EAFP vs LBYL, Swap de variáveis sem temporários.
- [`19_slicing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/19_slicing.py) — Fatiamento avançado `[start:stop:step]`, objeto `slice()`, atribuição e deleção in-place por slice.
- [`20_unpacking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/20_unpacking.py) — Extended Unpacking (`a, *b, c`), fusão de dicionários (`**d1, **d2`) e repasse de argumentos.
- [`21_any_all_sorted.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/21_any_all_sorted.py) — Curto-circuito com `any()` e `all()`, ordenação estável Timsort $O(n \log n)$ com `sorted(key=...)`.
- [`22_itertools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/22_itertools.py) — Alta performance com `combinations`, `permutations`, `product`, `chain` e `groupby`.
- [`23_functools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/23_functools.py) — Programação funcional com `@cache`, `@lru_cache` (Memoization), `partial()`, `reduce()` e `@wraps`.
- [`24_strings.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/24_strings.py) — Concatenação performática com `' '.join()` em $O(n)$, f-strings avançadas e depuração (`f"{x=}"`).
- [`25_arquivos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/25_arquivos.py) — Leitura e escrita segura de arquivos com `with open(...)`, gerenciamento de buffers e encoding UTF-8.
- [`26_json.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/26_json.py) — Serialização e deserialização JSON (`dumps`, `loads`), tratando tipos complexos (ex: `datetime`).
- [`27_pathlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/27_pathlib.py) — Orientação a objetos no sistema de arquivos com `pathlib.Path` e o operador `/` multiplataforma.
- [`28_modulos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/28_modulos.py) — Mecanismo de importação do Python, inspeção de `sys.path` e a guarda `if __name__ == '__main__':`.
- [`29_packages.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/29_packages.py) — Organização de pacotes com `__init__.py`, controle de API pública com `__all__` e Namespace Packages.

---

### 🟡 3. Exceptions, POO Avançada & Typing (`conteudo/03_excecoes_poo_typing/`)
- [`30_excecoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/30_excecoes.py) — Tratamento de erros com `try`/`except`/`else`/`finally` e Exception Chaining (`raise ... from e`).
- [`31_excecoes_customizadas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/31_excecoes_customizadas.py) — Criação de exceções de domínio ricas com atributos de contexto (ex: status code HTTP).
- [`32_classes_objetos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/32_classes_objetos.py) — Modelagem orientada a objetos, atributos de instância vs atributos de classe e estado.
- [`33_init_str_repr.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/33_init_str_repr.py) — Construtor `__init__`, diferenciação entre `__str__` (usuário) e `__repr__` (desenvolvedor/debug).
- [`34_encapsulamento.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/34_encapsulamento.py) — Modificadores de acesso por convenção (`_protegido`) e Name Mangling (`__privado`).
- [`35_property.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/35_property.py) — Encapsulamento idiomático com decoradores `@property`, `@salario.setter` e validação.
- [`36_heranca.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/36_heranca.py) — Herança simples, reutilização de inicializadores com `super()` e sobrescrita de métodos.
- [`37_heranca_multipla_mro.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/37_heranca_multipla_mro.py) — Herança múltipla, problema do diamante e inspeção de MRO (Method Resolution Order / Algoritmo C3).
- [`38_polimorfismo.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/38_polimorfismo.py) — Polimorfismo baseado em Duck Typing ("Se anda como pato e quaca como pato...").
- [`39_classes_abstratas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/39_classes_abstratas.py) — Definição de contratos de interface com `abc.ABC` e `@abstractmethod`.
- [`40_classmethod_staticmethod.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/40_classmethod_staticmethod.py) — Fábricas de objetos com `@classmethod` vs funções utilitárias com `@staticmethod`.
- [`41_dunder_methods.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/41_dunder_methods.py) — Métodos mágicos: `__len__`, `__getitem__` (indexação) e `__call__` (tornar objeto invocável).
- [`42_dataclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/42_dataclasses.py) — Classes de dados com `@dataclass`, `frozen=True` (imutabilidade), `kw_only=True` e `__post_init__`.
- [`43_enum.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/43_enum.py) — Enumerações fortemente tipadas com `enum.Enum` e constantes automáticas `auto()`.
- [`44_type_hints.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/44_type_hints.py) — Anotações de tipos modernas (PEP 484), sintaxe Union `A | B` e tipos funcionais `Callable`.
- [`45_typing_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/45_typing_avancado.py) — Subtipagem estrutural com `Protocol`, generics com `TypeVar` e `Generic[T]`, e `TypedDict`.

---

### 📁 4. Iterators, Generators, Decorators & Context Managers (`conteudo/04_iteradores_decoradores_contexto/`)
- [`46_iteradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/46_iteradores.py) — Protocolo de iteração nativo: implementando `__iter__` e `__next__` com `StopIteration`.
- [`47_geradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/47_geradores.py) — Funções geradoras com `yield`, pausa de execução e deleção com `yield from`.
- [`48_decoradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/48_decoradores.py) — Decoradores de funções, closures e preservação de metadados com `functools.wraps`.
- [`49_decoradores_com_argumentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/49_decoradores_com_argumentos.py) — Fábricas de decoradores parametrizados (aninhamento em 3 níveis).
- [`50_context_managers.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/50_context_managers.py) — Gerenciadores de contexto com `__enter__` e `__exit__` (supressão de exceções).
- [`51_contextlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/51_contextlib.py) — Utilitários do módulo `contextlib`: decorador `@contextmanager` e `contextlib.suppress`.

---

### 📁 5. Async & Concorrência (`conteudo/05_async_concorrencia/`)
- [`52_asyncio_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/52_asyncio_basico.py) — Programação assíncrona, Event Loop, corrotinas `async def`, `await` e `asyncio.run()`.
- [`53_asyncio_tasks.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/53_asyncio_tasks.py) — Concorrência não-bloqueante com `asyncio.create_task()` e agregação de resultados com `asyncio.gather()`.
- [`54_asyncio_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/54_asyncio_avancado.py) — Primitivas de sincronização assíncrona: limite de taxa com `asyncio.Semaphore` e filas com `asyncio.Queue`.
- [`55_threads.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/55_threads.py) — Multithreading com `threading.Thread`, prevenção de Race Conditions com `threading.Lock` e o papel do GIL.
- [`56_multiprocessing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/56_multiprocessing.py) — Paralelismo real de CPU bypassando o GIL com múltiplos processos (`multiprocessing.Process`).
- [`57_concurrent_futures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/57_concurrent_futures.py) — Abstração de alto nível com Pools de Execução: `ThreadPoolExecutor` e `ProcessPoolExecutor`.
- [`58_cpu_vs_io_bound.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/58_cpu_vs_io_bound.py) — Guia definitivo de decisão arquitetural: Cargas CPU-Bound vs I/O-Bound e quando usar cada modelo.

---

### 📁 6. Logging, Debugging & Testing (`conteudo/06_logging_debugging_testes/`)
- [`59_logging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/59_logging.py) — Logging profissional estruturado (`logging`), níveis de severidade, formatters e handlers.
- [`60_debugging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/60_debugging.py) — Técnicas de depuração nativa utilizando `breakpoint()` (PDB embutido no Python 3.7+).
- [`61_pytest_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/61_pytest_basico.py) — Fundamentos do `pytest`, convenções de nomenclatura `test_*` e asserções idiomáticas.
- [`62_pytest_fixtures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/62_pytest_fixtures.py) — Preparação e limpeza de estado de testes reutilizáveis usando `@pytest.fixture`.
- [`63_pytest_parametrize.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/63_pytest_parametrize.py) — Testes parametrizados para validação de múltiplos casos de borda em uma única função.
- [`64_mocking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/64_mocking.py) — Isolamento de serviços externos com Mocks (`unittest.mock.MagicMock` e asserções de chamadas).
- [`65_testes_integracao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/65_testes_integracao.py) — Conceitos da Pirâmide de Testes (Unitários vs Integração vs E2E).

---

### 📁 7. Engenharia de Software (`conteudo/07_engenharia_software/`)
- [`66_clean_code.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/66_clean_code.py) — Princípios de código limpo: funções com responsabilidade única, nomes expressivos e redução de aninhamento.
- [`67_solid.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/67_solid.py) — Os 5 princípios SOLID aplicados de forma idiomática ao Python (SRP, OCP, LSP, ISP, DIP).
- [`68_dependency_injection.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/68_dependency_injection.py) — Padrão Injeção de Dependências para desacoplamento de serviços e testabilidade.
- [`69_design_patterns.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/69_design_patterns.py) — Design Patterns orientados a objetos e funcionais (Strategy Pattern usando funções como First-Class Citizens).
- [`70_repository_pattern.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/70_repository_pattern.py) — Pattern Repositório e Camada de Persistência isolada do domínio da aplicação.

---

### 📁 8. Algoritmos & Estruturas de Dados / DSA (`conteudo/08_dsa_algoritmos/`)
- [`71_big_o.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/71_big_o.py) — Análise rigorosa de complexidade Big O: $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$.
- [`72_arrays_lists.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/72_arrays_lists.py) — Padrões clássicos em Arrays: Two Pointers (Dois Ponteiros) e Sliding Window.
- [`73_hash_maps.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/73_hash_maps.py) — Resolução do algoritmo clássico **Two Sum** em $O(n)$ tempo usando Hash Map.
- [`74_stack.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/74_stack.py) — Estrutura de dados Pilha (Stack LIFO) e algoritmo de validação de parênteses/chaves balanceadas em $O(n)$.
- [`75_queue.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/75_queue.py) — Estrutura de dados Fila (Queue FIFO) de alta performance usando `collections.deque`.
- [`76_linked_list.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/76_linked_list.py) — Implementação de Lista Simplesmente Encadeada e algoritmo de inversão de ponteiros in-place em $O(n)$.
- [`77_binary_search.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/77_binary_search.py) — Algoritmo de Busca Binária em arrays ordenados com redução de espaço de busca em $O(\log n)$.
- [`78_recursao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/78_recursao.py) — Recursão, análise da Call Stack e importância do Caso Base para evitar estouro de pilha.
- [`79_trees.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/79_trees.py) — Árvore Binária de Busca (BST) e percursos em ordem (In-Order Traversal) para obter dados ordenados.
- [`80_heap.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/80_heap.py) — Fila de Prioridades com Min-Heap utilizando `heapq` e resolução do problema dos **Top-K elementos**.
- [`81_graphs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/81_graphs.py) — Representação de Grafos via Lista de Adjacência e algoritmo de Busca em Largura (BFS).

---

### 📁 9. HTTP & Resiliência (`conteudo/09_http_resiliencia/`)
- [`82_http_fundamentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/82_http_fundamentos.py) — Verbos HTTP (`GET`, `POST`, `PUT`, `DELETE`), Status Codes REST (`200`, `201`, `400`, `404`, `500`).
- [`83_http_client.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/83_http_client.py) — Consumo de APIs REST sem dependências externas utilizando `urllib.request` nativo.
- [`84_retries_timeouts.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/84_retries_timeouts.py) — Padrão de resiliência em sistemas distribuídos: Retries com Exponential Backoff e Timeouts.

---

### 📁 10. Metaprogramação Avançada (`conteudo/10_metaprogramacao/`)
- [`85_getattr_getattribute.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/85_getattr_getattribute.py) — Metaprogramação: Interceptação de atributos dinâmicos com `__getattr__` vs `__getattribute__`.
- [`86_descriptors.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/86_descriptors.py) — Protocolo Descriptor (`__get__`, `__set__`) para reutilização de lógica de atributos em frameworks.
- [`87_metaclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/87_metaclasses.py) — Metaclasses customizadas estendendo `type` para interceptação e validação na declaração de classes.

---

## ⚡ Como Configurar e Executar

Para um guia visual passo a passo completo, acesse o documento dedicado:
📖 **[COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md)**

### 1. Clonar o Repositório e Configurar o Ambiente Virtual

```powershell
# Clonar o repositório
git clone https://github.com/Gabrielz11/python_first.git
cd pythonfirst

# Criar e ativar o ambiente virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar as dependências do projeto
pip install -r requirements.txt
```

### 2. Executar um Módulo Individualmente

```powershell
python conteudo/01_fundamentos_collections/01_variaveis.py
python conteudo/05_async_concorrencia/52_asyncio_basico.py
python conteudo/08_dsa_algoritmos/73_hash_maps.py
```

### 3. Executar o Script de Auditoria em Lote (Todos os 87 Módulos)

O repositório possui um script automatizado que varre as 10 subpastas e executa todos os 87 arquivos garantindo que o código de saída seja 0:

```powershell
python verify_all_87.py
```

### 4. Executar os Linters e Ferramentas de Qualidade

```powershell
# Checagem de Estilo e Linting rápido com Ruff
ruff check .

# Checagem de Tipagem Estática com Mypy
mypy .

# Suíte de Testes com Pytest
pytest
```

---

## 🤝 Contribuição e Licença

Contribuições com novas melhorias didáticas, correções ou novos exercícios são sempre bem-vindas!

Este projeto está sob a licença [MIT](LICENSE).

---
<p align="center">
  Desenvolvido com 🐍 e foco em <b>Engenharia de Software de Alta Performance</b>.
</p>
