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
├── 📂 conteudo/                                # Os 87 módulos organizados em 10 subpastas
│   ├── 📁 01_fundamentos_collections/         # Módulos 01 a 17 (Variáveis, Loops, Listas, Dicts, Sets, Collections)
│   ├── 📁 02_python_idiomatico_pacotes/      # Módulos 18 a 29 (EAFP, Slicing, Itertools, Pathlib, Pacotes)
│   ├── 📁 03_excecoes_poo_typing/             # Módulos 30 a 45 (POO, ABC, Dataclasses, Protocol, Generics)
│   ├── 📁 04_iteradores_decoradores_contexto/ # Módulos 46 a 51 (Yield, Decorators, Contextlib)
│   ├── 📁 05_async_concorrencia/              # Módulos 52 a 58 (Asyncio, Threads, Multiprocessing, GIL)
│   ├── 📁 06_logging_debugging_testes/        # Módulos 59 a 65 (Logging, Debugging, Pytest, Mocks)
│   ├── 📁 07_engenharia_software/             # Módulos 66 a 70 (Clean Code, SOLID, DI, Repository Pattern)
│   ├── 📁 08_dsa_algoritmos/                  # Módulos 71 a 81 (Big O, Hash Maps, Pilhas, Árvores, Grafos)
│   ├── 📁 09_http_resiliencia/                # Módulos 82 a 84 (HTTP REST, Urllib, Retries & Backoff)
│   └── 📁 10_metaprogramacao/                 # Módulos 85 a 87 (Getattr, Descriptors, Metaclasses)
│
├── 📄 COMO_EXECUTAR.md                         # Guia detalhado de execução e testes
├── 📄 README.md                                # Documentação principal e índice do repositório
├── 📄 cronograma_estudo_python.md              # Plano pedagógico de 10 semanas
├── 📄 verify_all_87.py                        # Script de verificação e auditoria em lote
├── 📄 pyproject.toml                           # Configuração dos linters e formatadores (Ruff / Mypy)
├── 📄 requirements.txt                        # Dependências do projeto
└── 📄 .gitignore                               # Arquivos ignorados pelo Git
```

---

## 🗺️ Índice Interativo dos Módulos Educacionais (`conteudo/`)

### 📁 1. Fundamentos da Linguagem & Collections (`conteudo/01_fundamentos_collections/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **01** | [`01_variaveis.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/01_variaveis.py) | Variáveis & Referências | Tipagem dinâmica vs forte, ponteiros de memória na Heap e `id()` |
| **02** | [`02_operadores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/02_operadores.py) | Operadores & Comparação | Operadores aritméticos, lógicos, curto-circuito e a diferença entre `==` e `is` |
| **03** | [`03_tipos_dados.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/03_tipos_dados.py) | Tipos Primitivos | Inteiros, floats, booleans, mutabilidade e conversões de tipo (casting) |
| **04** | [`04_condicionais.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/04_condicionais.py) | Controle de Fluxo | Tomada de decisão, operador ternário, Early Return e cláusulas de guarda |
| **05** | [`05_match_case.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/05_match_case.py) | Pattern Matching | Structural Pattern Matching (Python 3.10+), desestruturação e guards |
| **06** | [`06_loops.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/06_loops.py) | Laços de Repetição | Iteração com `for` e `while`, `break`, `continue` e o bloco idiomático `for...else` |
| **07** | [`07_range_enumerate_zip.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/07_range_enumerate_zip.py) | Iteração Idiomática | Navegação de sequências usando `range()`, `enumerate()` e `zip(strict=True)` |
| **08** | [`08_funcoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/08_funcoes.py) | Assinaturas de Funções | Parâmetros posicionais, nomeados, Positional-Only (`/`) e Keyword-Only (`*`) |
| **09** | [`09_args_kwargs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/09_args_kwargs.py) | Parâmetros Variádicos | Empacotamento e repasse de argumentos com `*args` (tupla) e `**kwargs` (dict) |
| **10** | [`10_escopo_legb.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/10_escopo_legb.py) | Regra LEGB | Escopos Local, Enclosing, Global e Built-in, com uso de `global` e `nonlocal` |
| **11** | [`11_lambda.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/11_lambda.py) | Funções Anônimas | Uso de funções `lambda` com `sorted()`, `map()`, `filter()` e closures |
| **12** | [`12_listas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/12_listas.py) | Estrutura `list` | Array dinâmico de ponteiros no CPython, Shallow vs Deep Copy e Big O |
| **13** | [`13_tuplas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/13_tuplas.py) | Estrutura `tuple` | Sequências imutáveis, Freelist no CPython, Unpacking e Hashability |
| **14** | [`14_dicionarios.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/14_dicionarios.py) | Estrutura `dict` | Tabela Hash compacta no CPython, busca $O(1)$ média, `.get()` e views dinâmicas |
| **15** | [`15_sets.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/15_sets.py) | Estrutura `set` | Teoria dos conjuntos (união, interseção), pertenciamento $O(1)$ e `frozenset` |
| **16** | [`16_comprehensions.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/16_comprehensions.py) | Comprehensions | List, Set, Dict Comprehensions, bytecode `LIST_APPEND` e Generators |
| **17** | [`17_collections.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/17_collections.py) | Módulo `collections` | Estruturas `Counter`, `defaultdict`, `deque` ($O(1)$ popleft), `NamedTuple` e `ChainMap` |

---

### 🟢 2. Python Idiomático, Arquivos & Pacotes (`conteudo/02_python_idiomatico_pacotes/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **18** | [`18_python_idiomatico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/18_python_idiomatico.py) | Pythonic Code | Zen do Python (PEP 20), filosofia EAFP vs LBYL e verificação de Truthiness |
| **19** | [`19_slicing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/19_slicing.py) | Slicing Avançado | Fatiamento `[start:stop:step]`, objeto `slice()` e modificações in-place |
| **20** | [`20_unpacking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/20_unpacking.py) | Extended Unpacking | Desestruturação com asterisco (`*resto`) e fusão de dicionários (`**d1, **d2`) |
| **21** | [`21_any_all_sorted.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/21_any_all_sorted.py) | Built-in Functions | Curto-circuito com `any()` e `all()`, e ordenação Timsort com `sorted(key=...)` |
| **22** | [`22_itertools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/22_itertools.py) | Módulo `itertools` | Iteradores de alta performance: `chain`, `combinations`, `permutations`, `groupby` |
| **23** | [`23_functools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/23_functools.py) | Módulo `functools` | Memoization com `@cache`, `@lru_cache`, `partial()`, `reduce()` e `@wraps` |
| **24** | [`24_strings.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/24_strings.py) | String Formatting | Concatenação em $O(n)$ com `' '.join()`, f-strings avançadas e debug (`f"{x=}"`) |
| **25** | [`25_arquivos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/25_arquivos.py) | Manipulação de I/O | Escrita e leitura segura de arquivos com `with open(...)` e codificação UTF-8 |
| **26** | [`26_json.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/26_json.py) | Trabalhando com JSON | Serialização (`dumps`, `loads`) e encoders para tipos customizados (`datetime`) |
| **27** | [`27_pathlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/27_pathlib.py) | Módulo `pathlib` | Orientação a objetos em caminhos do SO com `Path` e operador `/` multiplataforma |
| **28** | [`28_modulos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/28_modulos.py) | Sistema de Imports | Como o Python localiza módulos via `sys.path` e a guarda `if __name__ == '__main__':` |
| **29** | [`29_packages.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/29_packages.py) | Estrutura de Pacotes | Organização com `__init__.py`, controle de exports com `__all__` e Namespace Packages |

---

### 🟡 3. Exceptions, POO Avançada & Typing (`conteudo/03_excecoes_poo_typing/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **30** | [`30_excecoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/30_excecoes.py) | Tratamento de Erros | Fluxo `try/except/else/finally` e Exception Chaining (`raise ... from e`) |
| **31** | [`31_excecoes_customizadas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/31_excecoes_customizadas.py) | Exceções de Domínio | Criação de exceções personalizadas com atributos para APIs Backend |
| **32** | [`32_classes_objetos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/32_classes_objetos.py) | Classes & Instâncias | Atributos de instância (`self`), atributos de classe e estado dos objetos |
| **33** | [`33_init_str_repr.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/33_init_str_repr.py) | Representação de Objetos | Construtor `__init__`, e a diferença entre `__str__` (usuário) e `__repr__` (debug) |
| **34** | [`34_encapsulamento.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/34_encapsulamento.py) | Encapsulamento | Atributos protegidos por convenção (`_`) e privados via Name Mangling (`__`) |
| **35** | [`35_property.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/35_property.py) | Getters & Setters | Encapsulamento idiomático usando os decoradores `@property` e `@setter` |
| **36** | [`36_heranca.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/36_heranca.py) | Herança Simples | Reutilização de código entre classes e repasse de construtor com `super()` |
| **37** | [`37_heranca_multipla_mro.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/37_heranca_multipla_mro.py) | Herança Múltipla & MRO | Resolução do problema do diamante e inspeção de MRO via `.mro()` (Algoritmo C3) |
| **38** | [`38_polimorfismo.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/38_polimorfismo.py) | Polimorfismo | Comportamentos dinâmicos orientados ao conceito de Duck Typing |
| **39** | [`39_classes_abstratas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/39_classes_abstratas.py) | Interfaces com ABC | Definição de contratos abstratos obrigatórios usando `abc.ABC` e `@abstractmethod` |
| **40** | [`40_classmethod_staticmethod.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/40_classmethod_staticmethod.py) | Métodos Especiais | Construtores alternativos com `@classmethod` vs utilitários com `@staticmethod` |
| **41** | [`41_dunder_methods.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/41_dunder_methods.py) | Dunder Methods | Métodos mágicos: `__len__`, `__getitem__` (indexação) e `__call__` (invocação) |
| **42** | [`42_dataclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/42_dataclasses.py) | Módulo `dataclasses` | `@dataclass`, imutabilidade com `frozen=True`, `kw_only=True` e `__post_init__` |
| **43** | [`43_enum.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/43_enum.py) | Enumerações | Modelagem de constantes de domínio fortemente tipadas com `enum.Enum` e `auto()` |
| **44** | [`44_type_hints.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/44_type_hints.py) | Tipagem Estática | Anotações modernas de tipos (PEP 484), sintaxe Union `A | B` e tipos `Callable` |
| **45** | [`45_typing_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/45_typing_avancado.py) | Typing Avançado | Subtipagem estrutural com `Protocol`, algoritmos genéricos com `Generic[T]` e `TypedDict` |

---

### 📁 4. Iterators, Generators, Decorators & Context Managers (`conteudo/04_iteradores_decoradores_contexto/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **46** | [`46_iteradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/46_iteradores.py) | Protocolo de Iteração | Implementação de iteradores customizados com `__iter__` e `__next__` |
| **47** | [`47_geradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/47_geradores.py) | Geradores & Yield | Funções geradoras com `yield`, avaliação preguiçosa e deleção via `yield from` |
| **48** | [`48_decoradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/48_decoradores.py) | Decoradores Simples | Funções de alta ordem, medição de tempo de execução e uso de `functools.wraps` |
| **49** | [`49_decoradores_com_argumentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/49_decoradores_com_argumentos.py) | Decoradores Parametrizados | Criação de fábricas de decoradores aceitando argumentos de configuração |
| **50** | [`50_context_managers.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/50_context_managers.py) | Gerenciadores de Contexto | Suporte à instrução `with` implementando os métodos `__enter__` e `__exit__` |
| **51** | [`51_contextlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/51_contextlib.py) | Módulo `contextlib` | Criação simplificada de context managers com `@contextmanager` e `contextlib.suppress` |

---

### 📁 5. Async & Concorrência (`conteudo/05_async_concorrencia/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **52** | [`52_asyncio_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/52_asyncio_basico.py) | Fundamentos do Asyncio | Programação assíncrona, Event Loop, corrotinas `async def`, `await` e `asyncio.run()` |
| **53** | [`53_asyncio_tasks.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/53_asyncio_tasks.py) | Tarefas Concorrentes | Execução paralela no Event Loop usando `asyncio.create_task()` e `asyncio.gather()` |
| **54** | [`54_asyncio_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/54_asyncio_avancado.py) | Controle Assíncrono | Limitação de requisições simultâneas com `asyncio.Semaphore` e filas com `asyncio.Queue` |
| **55** | [`55_threads.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/55_threads.py) | Multithreading | Concorrência com `threading.Thread`, prevenção de Race Conditions com `Lock` e o GIL |
| **56** | [`56_multiprocessing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/56_multiprocessing.py) | Paralelismo Multiprocesso | Paralelismo real em múltiplos núcleos do SO para cargas CPU-bound com `Process` |
| **57** | [`57_concurrent_futures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/57_concurrent_futures.py) | Executor Pools | Pools de execução de alto nível usando `ThreadPoolExecutor` e `ProcessPoolExecutor` |
| **58** | [`58_cpu_vs_io_bound.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/58_cpu_vs_io_bound.py) | Guia Arquitetural | Comparativo prático: Cargas CPU-Bound vs I/O-Bound e quando escolher Async vs Threads |

---

### 📁 6. Logging, Debugging & Testing (`conteudo/06_logging_debugging_testes/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **59** | [`59_logging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/59_logging.py) | Logging Profissional | Sistema de logs estruturado com `logging`, níveis de severidade, formatters e handlers |
| **60** | [`60_debugging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/60_debugging.py) | Depuração de Código | Técnicas de debugging usando a instrução nativa `breakpoint()` (PDB embutido) |
| **61** | [`61_pytest_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/61_pytest_basico.py) | Pytest Inicial | Fundamentos de testes unitários com Pytest, nomenclatura `test_*` e asserções |
| **62** | [`62_pytest_fixtures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/62_pytest_fixtures.py) | Pytest Fixtures | Injeção de dependências e estado de testes reutilizável usando `@pytest.fixture` |
| **63** | [`63_pytest_parametrize.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/63_pytest_parametrize.py) | Testes Parametrizados | Validação de múltiplos cenários de teste sem duplicação de código com `@parametrize` |
| **64** | [`64_mocking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/64_mocking.py) | Mocking & Isolamento | Isolamento de APIs externas e bancos de dados usando `unittest.mock.MagicMock` |
| **65** | [`65_testes_integracao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/65_testes_integracao.py) | Testes de Integração | Princípios da Pirâmide de Testes (Unitários vs Integração vs E2E) |

---

### 📁 7. Engenharia de Software (`conteudo/07_engenharia_software/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **66** | [`66_clean_code.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/66_clean_code.py) | Clean Code em Python | Código limpo, legibilidade, funções pequenas com responsabilidade única |
| **67** | [`67_solid.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/67_solid.py) | Princípios SOLID | Aplicação dos 5 princípios SOLID de forma idiomática no Python Backend |
| **68** | [`68_dependency_injection.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/68_dependency_injection.py) | Injeção de Dependência | Desacoplamento de serviços e Inversão de Controle para máxima testabilidade |
| **69** | [`69_design_patterns.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/69_design_patterns.py) | Padrões de Projeto | Implementação prática de Design Patterns (ex: Strategy com funções First-Class) |
| **70** | [`70_repository_pattern.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/70_repository_pattern.py) | Repository Pattern | Isolamento completo da camada de dados em relação à regra de negócios da aplicação |

---

### 📁 8. Algoritmos & Estruturas de Dados / DSA (`conteudo/08_dsa_algoritmos/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **71** | [`71_big_o.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/71_big_o.py) | Análise de Complexidade | Estudo formal de Big O temporal e espacial: $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$ |
| **72** | [`72_arrays_lists.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/72_arrays_lists.py) | Algoritmos em Arrays | Padrões clássicos: Dois Ponteiros (Two Pointers) e Janela Deslizante (Sliding Window) |
| **73** | [`73_hash_maps.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/73_hash_maps.py) | Hash Map Algorithms | Resolução do problema clássico **Two Sum** em $O(n)$ tempo usando Tabela Hash |
| **74** | [`74_stack.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/74_stack.py) | Estrutura Pilha (LIFO) | Implementação de Pilha e algoritmo de validação de parênteses balanceados em $O(n)$ |
| **75** | [`75_queue.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/75_queue.py) | Estrutura Fila (FIFO) | Implementação de Fila de alta performance usando `collections.deque` |
| **76** | [`76_linked_list.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/76_linked_list.py) | Lista Encadeada | Construção de Nó e Lista Simplesmente Encadeada com inversão in-place em $O(n)$ |
| **77** | [`77_binary_search.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/77_binary_search.py) | Busca Binária | Algoritmo de Busca Binária em arrays ordenados com complexidade $O(\log n)$ |
| **78** | [`78_recursao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/78_recursao.py) | Recursão & Call Stack | Análise da pilha de execução de funções recursivas e definição de Caso Base |
| **79** | [`79_trees.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/79_trees.py) | Árvore Binária (BST) | Árvore Binária de Busca e percurso em ordem (In-Order Traversal) para ordenação |
| **80** | [`80_heap.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/80_heap.py) | Min-Heap & Prioridades | Fila de prioridades com o módulo `heapq` e resolução do problema de **Top-K elementos** |
| **81** | [`81_graphs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/81_graphs.py) | Grafos & Busca BFS | Representação de Grafos via Lista de Adjacência e algoritmo Busca em Largura |

---

### 📁 9. HTTP e Resiliência (`conteudo/09_http_resiliencia/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **82** | [`82_http_fundamentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/82_http_fundamentos.py) | Protocolo HTTP | Verbos HTTP (`GET`, `POST`, `PUT`, `DELETE`), Status Codes e payload REST |
| **83** | [`83_http_client.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/83_http_client.py) | Cliente HTTP Nativo | Consumo de Web APIs REST sem bibliotecas externas usando `urllib.request` |
| **84** | [`84_retries_timeouts.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/84_retries_timeouts.py) | Resiliência HTTP | Padrões de resiliência: Reexecução com Exponential Backoff e controle de Timeouts |

---

### 📁 10. Metaprogramação (`conteudo/10_metaprogramacao/`)

| # | Módulo / Arquivo | Tópico Principal | Conteúdo & Aprendizado |
| :---: | :--- | :--- | :--- |
| **85** | [`85_getattr_getattribute.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/85_getattr_getattribute.py) | Atributos Dinâmicos | Interceptação de atributos dinâmicos com `__getattr__` vs `__getattribute__` |
| **86** | [`86_descriptors.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/86_descriptors.py) | Protocolo Descriptor | Protocolo Descriptor (`__get__`, `__set__`) para reuso de lógica em atributos |
| **87** | [`87_metaclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/87_metaclasses.py) | Metaclasses | Metaclasses customizadas estendendo `type` para interceptar declaração de classes |

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
