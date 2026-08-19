# 🐍 Python First: Repositório Educacional & Laboratório Prático de Engenharia de Software

> **Laboratório progressivo de aprendizado de Python, Engenharia de Software, Backend, Algoritmos e Inteligência Artificial Aplicada.**

Este repositório é um **guia permanente de referência técnica, laboratório executável e roadmap de evolução profissional** em Python 3.12+. Todos os 87 módulos estão organizados de forma limpa na pasta [`conteudo/`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo), divididos em **10 categorias fundamentais de conhecimento**. Cada arquivo funciona como uma **mini aula prática autossuficiente**, contendo explicações teóricas, exemplos reais, análise de complexidade (Big O), boas práticas, antipadrões e conexões com entrevistas técnicas.

> 📖 **Guia Rápido de Execução**: Consulte o [COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md) para instruções detalhadas de como executar cada um dos 87 módulos individualmente ou em lote.
> 📅 **Cronograma Completo**: Consulte o [cronograma_estudo_python.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/cronograma_estudo_python.md) para a trilha de 10 semanas.

---

## 📂 Estrutura do Repositório

```text
pythonfirst/
│
├── 📂 conteudo/                                # Os 87 módulos organizados em 10 subpastas
│   ├── 📁 01_fundamentos_collections/         # Módulos 01 a 17 (Variaveis, Tipos, Dicts, Sets, Collections)
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

## 🎯 Categorização dos Módulos por Nível & Nível de Domínio

```text
       [ 1. Fundamentals ] ──► Sintaxe, Tipagem, Controle de Fluxo
               │
       [ 2. Pythonic Python ] ──► Idiomas, Slicing, Itertools, Functools
               │
       [ 3. OOP & Typing ] ──► Classes, Dunder Methods, Dataclasses, Protocol
               │
       [ 4. Advanced Python ] ──► Iteradores, Geradores, Decoradores, Async
               │
       [ 5. Testing & Quality ] ──► Pytest, Fixtures, Mocks, Integration Tests
               │
       [ 6. Software Engineering ] ──► Clean Code, SOLID, DI, Design Patterns
               │
       [ 7. Algorithms & Data Structs ] ──► Big O, Hash Maps, Trees, Graphs
               │
       [ 8. HTTP & Web APIs ] ──► Protocollos, Clientes HTTP, Resiliência
               │
       [ 9. FastAPI Framework ] ──► Rotas, Pydantic, DI, Arquitetura Hexagonal
               │
       [ 10. Database Engineering ] ──► SQL, PostgreSQL, ACID, Repositories, ORM
               │
       [ 11. AI Engineering ] ──► Embeddings, Vector Search, RAG, Agentes (Sem Frameworks)
               │
       [ 12. Interview Preparation ] ──► Desafios com Análise Temporal e Espacial
```

---

## 📚 Índice dos Módulos Educacionais (`conteudo/`)

### 📁 1. Fundamentos e Collections (`conteudo/01_fundamentos_collections/`)
- [`01_variaveis.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/01_variaveis.py) — Tipagem dinâmica, forte, referências de memória, Type Annotations.
- [`02_operadores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/02_operadores.py) — Operadores aritméticos, lógicos, precedência, `==` vs `is`.
- [`03_tipos_dados.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/03_tipos_dados.py) — Primitive types (`int`, `float`, `bool`, `str`, `None`), casting, truthy/falsy, mutabilidade.
- [`04_condicionais.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/04_condicionais.py) — `if`/`elif`/`else`, ternários, Early Returns, guarda de condições.
- [`05_match_case.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/05_match_case.py) — Structural Pattern Matching (Python 3.10+), wildcards, guards.
- [`06_loops.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/06_loops.py) — `for`, `while`, `break`, `continue`, e blocos `for...else` / `while...else`.
- [`07_range_enumerate_zip.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/07_range_enumerate_zip.py) — Iteração idiomática com `range()`, `enumerate()`, `zip()`.
- [`08_funcoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/08_funcoes.py) — Assinaturas, parâmetros posicionais, nomeados, responsabilidade única.
- [`09_args_kwargs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/09_args_kwargs.py) — Parâmetros variádicos `*args` e `**kwargs` e repasse de argumentos.
- [`10_escopo_legb.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/10_escopo_legb.py) — Regra LEGB (Local, Enclosing, Global, Built-in), `global` e `nonlocal`.
- [`11_lambda.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/11_lambda.py) — Funções anônimas vs `def`, uso com `sorted()`, `map()`, `filter()`.
- [`12_listas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/12_listas.py) — Operações com `list`, slicing, mutabilidade e análise Big O de operações.
- [`13_tuplas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/13_tuplas.py) — Tuplas como registros imutáveis, CPython freelist, unpacking e hashability.
- [`14_dicionarios.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/14_dicionarios.py) — Hash maps compactos em CPython, `get()`, `setdefault()`, views dinâmicas e busca $O(1)$.
- [`15_sets.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/15_sets.py) — Teoria dos conjuntos (união, interseção, diferença), membership $O(1)$, deduplicação $O(n)$ e `frozenset`.
- [`16_comprehensions.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/16_comprehensions.py) — List, Dict, Set Comprehensions, bytecode `LIST_APPEND` e Generator Expressions.
- [`17_collections.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_fundamentos_collections/17_collections.py) — Módulo `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`, `ChainMap`).

---

### 📁 2. Python Idiomático, Arquivos e Packages (`conteudo/02_python_idiomatico_pacotes/`)
- [`18_python_idiomatico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/18_python_idiomatico.py) — Código Pythonic vs Não-Pythonic, EAFP vs LBYL, Truthiness.
- [`19_slicing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/19_slicing.py) — Fatiamento avançado `[inicio:fim:passo]`, objeto `slice()`, atribuição por slice.
- [`20_unpacking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/20_unpacking.py) — Extended Unpacking (`*resto`), desestruturação em dicionários `**`.
- [`21_any_all_sorted.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/21_any_all_sorted.py) — Avaliação de curto-circuito (`any`, `all`), ordenação Timsort com `key=`.
- [`22_itertools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/22_itertools.py) — `chain`, `combinations`, `permutations`, `product`, `groupby`.
- [`23_functools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/23_functools.py) — `@cache`, `@lru_cache`, `partial`, `reduce`, `wraps`.
- [`24_strings.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/24_strings.py) — Imutabilidade de strings, `str.join()` em $O(n)$ e f-strings avançadas.
- [`25_arquivos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/25_arquivos.py) — Leitura e escrita segura com `with open()` e UTF-8.
- [`26_json.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/26_json.py) — Serialização (`dumps`, `loads`) e encoders customizados para objetos complexos.
- [`27_pathlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/27_pathlib.py) — Orientação a objetos em caminhos do SO com `pathlib.Path` e `/`.
- [`28_modulos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/28_modulos.py) — Sistema de imports, `sys.path`, escopo `__name__`.
- [`29_packages.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_python_idiomatico_pacotes/29_packages.py) — Estrutura de pacotes (`__init__.py`), `__all__` e Namespace Packages.

---

### 📁 3. Exceptions, POO e Typing (`conteudo/03_excecoes_poo_typing/`)
- [`30_excecoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/30_excecoes.py) — `try`/`except`/`else`/`finally`, exceções específicas e Exception Chaining (`from e`).
- [`31_excecoes_customizadas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/31_excecoes_customizadas.py) — Exceções de domínio customizadas para backend.
- [`32_classes_objetos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/32_classes_objetos.py) — Classes, instâncias, estado e `self`.
- [`33_init_str_repr.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/33_init_str_repr.py) — Construtor `__init__`, `__str__` vs `__repr__`.
- [`34_encapsulamento.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/34_encapsulamento.py) — Visibilidade (`público`, `_protegido`, `__privado` / Name Mangling).
- [`35_property.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/35_property.py) — Encapsulamento com `@property` e `@<prop>.setter`.
- [`36_heranca.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/36_heranca.py) — Herança simples e encadeamento com `super()`.
- [`37_heranca_multipla_mro.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/37_heranca_multipla_mro.py) — Herança múltipla, algoritmo C3 Linearization, inspeção de MRO (`.mro()`).
- [`38_polimorfismo.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/38_polimorfismo.py) — Polimorfismo e Duck Typing.
- [`39_classes_abstratas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/39_classes_abstratas.py) — Contratos abstratos com `abc.ABC` e `@abstractmethod`.
- [`40_classmethod_staticmethod.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/40_classmethod_staticmethod.py) — Métodos de instância vs `@classmethod` vs `@staticmethod`.
- [`41_dunder_methods.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/41_dunder_methods.py) — Protocolos nativos (`__len__`, `__getitem__`, `__call__`).
- [`42_dataclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/42_dataclasses.py) — `@dataclass`, `field()`, `frozen=True`, `kw_only=True`, `__post_init__`.
- [`43_enum.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/43_enum.py) — Enumerações fortemente tipadas com `Enum` e `auto()`.
- [`44_type_hints.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/44_type_hints.py) — Tipagem moderna: `list[str]`, `dict[str, int]`, `str | None`, `Callable`.
- [`45_typing_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_excecoes_poo_typing/45_typing_avancado.py) — `Protocol` (subtipagem estrutural), `Generic[T]`, `TypeVar`, `TypedDict`.

---

### 📁 4. Iterators, Generators, Decorators e Context Managers (`conteudo/04_iteradores_decoradores_contexto/`)
- [`46_iteradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/46_iteradores.py) — Protocolo de iteração customizado com `__iter__` e `__next__`.
- [`47_geradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/47_geradores.py) — Funções geradoras com `yield` e `yield from`.
- [`48_decoradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/48_decoradores.py) — Funções de alta ordem e decoradores de funções.
- [`49_decoradores_com_argumentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/49_decoradores_com_argumentos.py) — Fábricas de decoradores parametrizados.
- [`50_context_managers.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/50_context_managers.py) — Gerenciadores de contexto com `__enter__` e `__exit__`.
- [`51_contextlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_iteradores_decoradores_contexto/51_contextlib.py) — `@contextlib.contextmanager` e `contextlib.suppress`.

---

### 📁 5. Async e Concorrência (`conteudo/05_async_concorrencia/`)
- [`52_asyncio_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/52_asyncio_basico.py) — `async`/`await`, Event Loop e `asyncio.run()`.
- [`53_asyncio_tasks.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/53_asyncio_tasks.py) — Execução concorrente com `create_task()` e `gather()`.
- [`54_asyncio_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/54_asyncio_avancado.py) — Controle de concorrência com `asyncio.Semaphore` e `asyncio.Queue`.
- [`55_threads.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/55_threads.py) — Concorrência com `threading.Thread` e `threading.Lock` para I/O-bound.
- [`56_multiprocessing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/56_multiprocessing.py) — Paralelismo real em múltiplos núcleos para tarefas CPU-bound.
- [`57_concurrent_futures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/57_concurrent_futures.py) — Pools de execução com `ThreadPoolExecutor`.
- [`58_cpu_vs_io_bound.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_async_concorrencia/58_cpu_vs_io_bound.py) — Guia de arquitetura: CPU-bound vs I/O-bound e impacto do GIL.

---

### 📁 6. Logging, Debugging e Testing (`conteudo/06_logging_debugging_testes/`)
- [`59_logging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/59_logging.py) — Logging profissional estruturado com níveis, formatters e handlers.
- [`60_debugging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/60_debugging.py) — Análise de tracebacks e depuração com `breakpoint()`.
- [`61_pytest_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/61_pytest_basico.py) — Introdução ao `pytest` e asserções idiomáticas.
- [`62_pytest_fixtures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/62_pytest_fixtures.py) — Reutilização de estado de teste com `@pytest.fixture`.
- [`63_pytest_parametrize.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/63_pytest_parametrize.py) — Testes parametrizados para múltiplas entradas.
- [`64_mocking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/64_mocking.py) — Isolamento de dependências externas com `unittest.mock.MagicMock`.
- [`65_testes_integracao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_logging_debugging_testes/65_testes_integracao.py) — Pirâmide de testes (Unitários vs Integração).

---

### 📁 7. Engenharia de Software (`conteudo/07_engenharia_software/`)
- [`66_clean_code.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/66_clean_code.py) — Princípios de Clean Code em Python.
- [`67_solid.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/67_solid.py) — Os 5 princípios SOLID na prática.
- [`68_dependency_injection.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/68_dependency_injection.py) — Injeção de Dependências e Desacoplamento.
- [`69_design_patterns.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/69_design_patterns.py) — Strategy, Factory, Adapter, Observer em Python.
- [`70_repository_pattern.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_engenharia_software/70_repository_pattern.py) — Implementação do Pattern Repository e Camada de Persistência.

---

### 📁 8. DSA / Entrevistas (`conteudo/08_dsa_algoritmos/`)
- [`71_big_o.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/71_big_o.py) — Análise de complexidade temporal e espacial ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$).
- [`72_arrays_lists.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/72_arrays_lists.py) — Algoritmos em Arrays: Two Pointers e Sliding Window.
- [`73_hash_maps.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/73_hash_maps.py) — Resolução do algoritmo Two Sum em $O(n)$ com Hash Map.
- [`74_stack.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/74_stack.py) — Estrutura Pilha (LIFO) e validação de parênteses.
- [`75_queue.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/75_queue.py) — Estrutura Fila (FIFO) com `collections.deque`.
- [`76_linked_list.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/76_linked_list.py) — Lista Encadeada Simples e inversão em $O(n)$.
- [`77_binary_search.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/77_binary_search.py) — Busca Binária em arrays ordenados ($O(\log n)$).
- [`78_recursao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/78_recursao.py) — Recursão, Call Stack e caso base.
- [`79_trees.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/79_trees.py) — Árvore Binária de Busca (BST) e percursos.
- [`80_heap.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/80_heap.py) — Fila de prioridade com `heapq` e algoritmo Top-K.
- [`81_graphs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_dsa_algoritmos/81_graphs.py) — Representação de Grafos e Busca em Largura (BFS).

---

### 📁 9. HTTP e Resiliência (`conteudo/09_http_resiliencia/`)
- [`82_http_fundamentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/82_http_fundamentos.py) — Verbos HTTP, headers, status codes e payloads REST.
- [`83_http_client.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/83_http_client.py) — Consumo de APIs REST com cliente nativo `urllib.request`.
- [`84_retries_timeouts.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_http_resiliencia/84_retries_timeouts.py) — Padrões de resiliência: Retries com Exponential Backoff.

---

### 📁 10. Metaprogramação (`conteudo/10_metaprogramacao/`)
- [`85_getattr_getattribute.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/85_getattr_getattribute.py) — Interceptação de atributos com `__getattr__`.
- [`86_descriptors.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/86_descriptors.py) — Protocolo Descriptor (`__get__`, `__set__`).
- [`87_metaclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_metaprogramacao/87_metaclasses.py) — Metaclasses com `type` e `__new__`.

---

## 🛠️ Como Executar e Configurar o Ambiente

Para instruções completas de execução detalhada de **cada um dos 87 módulos**, consulte o documento exclusivo:
📖 **[COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md)**

### Comandos Rápidos:

```powershell
# 1. Ativar o ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar qualquer módulo individual em conteudo/
python conteudo/01_fundamentos_collections/01_variaveis.py
python conteudo/05_async_concorrencia/52_asyncio_basico.py

# 4. Executar TODOS os 87 scripts em lote (Auditoria Automática)
python verify_all_87.py

# 5. Executar os testes automatizados e checagem de tipos
pytest
mypy .
ruff check .
```
