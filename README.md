# 🐍 Python First: Repositório Educacional & Laboratório Prático de Engenharia de Software

> **Laboratório progressivo de aprendizado de Python, Engenharia de Software, Backend, Algoritmos e Inteligência Artificial Aplicada.**

Este repositório é um **guia permanente de referência técnica, laboratório executável e roadmap de evolução profissional** em Python 3.12+. Todos os 87 módulos estão organizados de forma limpa e enxuta na pasta [`conteudo/`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo). Cada arquivo funciona como uma **mini aula prática autossuficiente**, contendo explicações teóricas, exemplos reais, análise de complexidade (Big O), boas práticas, antipadrões e conexões com entrevistas técnicas.

> 📖 **Guia Rápido de Execução**: Consulte o [COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md) para instruções detalhadas de como executar cada um dos 87 módulos individualmente ou em lote.
> 📅 **Cronograma Completo**: Consulte o [cronograma_estudo_python.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/cronograma_estudo_python.md) para a trilha de 10 semanas.

---

## 📂 Estrutura do Repositório

```text
pythonfirst/
│
├── 📂 conteudo/                   # Todos os 87 módulos educacionais executáveis (01 ao 87)
│   ├── 01_variaveis.py
│   ├── ...
│   └── 87_metaclasses.py
│
├── 📄 COMO_EXECUTAR.md            # Guia passo a passo para execução e testes
├── 📄 README.md                   # Documentação principal e índice do repositório
├── 📄 cronograma_estudo_python.md # Plano pedagógico de 10 semanas
├── 📄 verify_all_87.py           # Script de verificação e auditoria em lote
├── 📄 pyproject.toml              # Configuração dos linters e formatadores (Ruff / Mypy)
├── 📄 requirements.txt           # Dependências do projeto
└── 📄 .gitignore                  # Arquivos ignorados pelo Git
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

### 🔹 1. Fundamentals (Fundamentos da Linguagem)
- [`conteudo/01_variaveis.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/01_variaveis.py) — Tipagem dinâmica, forte, referências de memória, Type Annotations.
- [`conteudo/02_operadores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/02_operadores.py) — Operadores aritméticos, lógicos, precedência, `==` vs `is`.
- [`conteudo/03_tipos_dados.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/03_tipos_dados.py) — Primitive types (`int`, `float`, `bool`, `str`, `None`), casting, truthy/falsy, mutabilidade.
- [`conteudo/04_condicionais.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/04_condicionais.py) — `if`/`elif`/`else`, ternários, Early Returns, guarda de condições.
- [`conteudo/05_match_case.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/05_match_case.py) — Structural Pattern Matching (Python 3.10+), wildcards, guards.
- [`conteudo/06_loops.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/06_loops.py) — `for`, `while`, `break`, `continue`, e blocos `for...else` / `while...else`.
- [`conteudo/07_range_enumerate_zip.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/07_range_enumerate_zip.py) — Iteração idiomática com `range()`, `enumerate()`, `zip()`.
- [`conteudo/08_funcoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/08_funcoes.py) — Assinaturas, parâmetros posicionais, nomeados, responsabilidade única.
- [`conteudo/09_args_kwargs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/09_args_kwargs.py) — Parâmetros variádicos `*args` e `**kwargs` e repasse de argumentos.
- [`conteudo/10_escopo_legb.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/10_escopo_legb.py) — Regra LEGB (Local, Enclosing, Global, Built-in), `global` e `nonlocal`.
- [`conteudo/11_lambda.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/11_lambda.py) — Funções anônimas vs `def`, uso com `sorted()`, `map()`, `filter()`.
- [`conteudo/12_listas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/12_listas.py) — Operações com `list`, slicing, mutabilidade e análise Big O de operações.
- [`conteudo/13_tuplas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/13_tuplas.py) — Tuplas como registros imutáveis, CPython freelist, unpacking e hashability.
- [`conteudo/14_dicionarios.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/14_dicionarios.py) — Hash maps compactos em CPython, `get()`, `setdefault()`, views dinâmicas e busca $O(1)$.
- [`conteudo/15_sets.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/15_sets.py) — Teoria dos conjuntos (união, interseção, diferença), membership $O(1)$, deduplicação $O(n)$ e `frozenset`.
- [`conteudo/16_comprehensions.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/16_comprehensions.py) — List, Dict, Set Comprehensions, bytecode `LIST_APPEND` e Generator Expressions.
- [`conteudo/17_collections.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/17_collections.py) — Módulo `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`, `ChainMap`).

---

### 🟢 2. Pythonic Python (Python Idiomático & Utilitários Nativos)
- [`conteudo/18_python_idiomatico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/18_python_idiomatico.py) — Código Pythonic vs Não-Pythonic, EAFP vs LBYL, Truthiness.
- [`conteudo/19_slicing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/19_slicing.py) — Fatiamento avançado `[inicio:fim:passo]`, objeto `slice()`, atribuição por slice.
- [`conteudo/20_unpacking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/20_unpacking.py) — Extended Unpacking (`*resto`), desestruturação em dicionários `**`.
- [`conteudo/21_any_all_sorted.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/21_any_all_sorted.py) — Avaliação de curto-circuito (`any`, `all`), ordenação Timsort com `key=`.
- [`conteudo/22_itertools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/22_itertools.py) — `chain`, `combinations`, `permutations`, `product`, `groupby`.
- [`conteudo/23_functools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/23_functools.py) — `@cache`, `@lru_cache`, `partial`, `reduce`, `wraps`.
- [`conteudo/24_strings.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/24_strings.py) — Imutabilidade de strings, `str.join()` em $O(n)$ e f-strings avançadas.
- [`conteudo/25_arquivos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/25_arquivos.py) — Leitura e escrita segura com `with open()` e UTF-8.
- [`conteudo/26_json.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/26_json.py) — Serialização (`dumps`, `loads`) e encoders customizados para objetos complexos.
- [`conteudo/27_pathlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/27_pathlib.py) — Orientação a objetos em caminhos do SO com `pathlib.Path` e `/`.
- [`conteudo/28_modulos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/28_modulos.py) — Sistema de imports, `sys.path`, escopo `__name__`.
- [`conteudo/29_packages.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/29_packages.py) — Estrutura de pacotes (`__init__.py`), `__all__` e Namespace Packages.

---

### 🟡 3. OOP & Typing (Orientação a Objetos, Exceções & Tipagem)
- [`conteudo/30_excecoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/30_excecoes.py) — `try`/`except`/`else`/`finally`, exceções específicas e Exception Chaining (`from e`).
- [`conteudo/31_excecoes_customizadas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/31_excecoes_customizadas.py) — Exceções de domínio customizadas para backend.
- [`conteudo/32_classes_objetos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/32_classes_objetos.py) — Classes, instâncias, estado e `self`.
- [`conteudo/33_init_str_repr.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/33_init_str_repr.py) — Construtor `__init__`, `__str__` vs `__repr__`.
- [`conteudo/34_encapsulamento.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/34_encapsulamento.py) — Visibilidade (`público`, `_protegido`, `__privado` / Name Mangling).
- [`conteudo/35_property.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/35_property.py) — Encapsulamento com `@property` e `@<prop>.setter`.
- [`conteudo/36_heranca.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/36_heranca.py) — Herança simples e encadeamento com `super()`.
- [`conteudo/37_heranca_multipla_mro.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/37_heranca_multipla_mro.py) — Herança múltipla, algoritmo C3 Linearization, inspeção de MRO (`.mro()`).
- [`conteudo/38_polimorfismo.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/38_polimorfismo.py) — Polimorfismo e Duck Typing.
- [`conteudo/39_classes_abstratas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/39_classes_abstratas.py) — Contratos abstratos com `abc.ABC` e `@abstractmethod`.
- [`conteudo/40_classmethod_staticmethod.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/40_classmethod_staticmethod.py) — Métodos de instância vs `@classmethod` vs `@staticmethod`.
- [`conteudo/41_dunder_methods.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/41_dunder_methods.py) — Protocolos nativos (`__len__`, `__getitem__`, `__call__`).
- [`conteudo/42_dataclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/42_dataclasses.py) — `@dataclass`, `field()`, `frozen=True`, `kw_only=True`, `__post_init__`.
- [`conteudo/43_enum.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/43_enum.py) — Enumerações fortemente tipadas com `Enum` e `auto()`.
- [`conteudo/44_type_hints.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/44_type_hints.py) — Tipagem moderna: `list[str]`, `dict[str, int]`, `str | None`, `Callable`.
- [`conteudo/45_typing_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/45_typing_avancado.py) — `Protocol` (subtipagem estrutural), `Generic[T]`, `TypeVar`, `TypedDict`.

---

### 🟠 4. Advanced Python (Iteradores, Geradores, Async, Threads & Metaprogramação)
- [`conteudo/46_iteradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/46_iteradores.py) — Protocolo de iteração customizado com `__iter__` e `__next__`.
- [`conteudo/47_geradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/47_geradores.py) — Funções geradoras com `yield` e `yield from`.
- [`conteudo/48_decoradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/48_decoradores.py) — Funções de alta ordem e decoradores de funções.
- [`conteudo/49_decoradores_com_argumentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/49_decoradores_com_argumentos.py) — Fábricas de decoradores parametrizados.
- [`conteudo/50_context_managers.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/50_context_managers.py) — Gerenciadores de contexto com `__enter__` e `__exit__`.
- [`conteudo/51_contextlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/51_contextlib.py) — `@contextlib.contextmanager` e `contextlib.suppress`.
- [`conteudo/52_asyncio_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/52_asyncio_basico.py) — `async`/`await`, Event Loop e `asyncio.run()`.
- [`conteudo/53_asyncio_tasks.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/53_asyncio_tasks.py) — Execução concorrente com `create_task()` e `gather()`.
- [`conteudo/54_asyncio_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/54_asyncio_avancado.py) — Controle de concorrência com `asyncio.Semaphore` e `asyncio.Queue`.
- [`conteudo/55_threads.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/55_threads.py) — Concorrência com `threading.Thread` e `threading.Lock` para I/O-bound.
- [`conteudo/56_multiprocessing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/56_multiprocessing.py) — Paralelismo real em múltiplos núcleos para tarefas CPU-bound.
- [`conteudo/57_concurrent_futures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/57_concurrent_futures.py) — Pools de execução com `ThreadPoolExecutor`.
- [`conteudo/58_cpu_vs_io_bound.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/58_cpu_vs_io_bound.py) — Guia de arquitetura: CPU-bound vs I/O-bound e impacto do GIL.
- [`conteudo/59_logging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/59_logging.py) — Logging profissional estruturado com níveis, formatters e handlers.
- [`conteudo/60_debugging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/60_debugging.py) — Análise de tracebacks e depuração com `breakpoint()`.
- *(Módulo Opcional / Metaprogramação)*:
  - [`conteudo/85_getattr_getattribute.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/85_getattr_getattribute.py) — Interceptação de atributos com `__getattr__`.
  - [`conteudo/86_descriptors.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/86_descriptors.py) — Protocolo Descriptor (`__get__`, `__set__`).
  - [`conteudo/87_metaclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/87_metaclasses.py) — Metaclasses com `type` e `__new__`.

---

### 🧪 5. Testing & Quality (Testes Automatizados & Qualidade)
- [`conteudo/61_pytest_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/61_pytest_basico.py) — Introdução ao `pytest` e asserções idiomáticas.
- [`conteudo/62_pytest_fixtures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/62_pytest_fixtures.py) — Reutilização de estado de teste com `@pytest.fixture`.
- [`conteudo/63_pytest_parametrize.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/63_pytest_parametrize.py) — Testes parametrizados para múltiplas entradas.
- [`conteudo/64_mocking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/64_mocking.py) — Isolamento de dependências externas com `unittest.mock.MagicMock`.
- [`conteudo/65_testes_integracao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/65_testes_integracao.py) — Pirâmide de testes (Unitários vs Integração).

---

### 🏛️ 6. Software Engineering (Clean Code, SOLID, DI & Design Patterns)
- [`conteudo/66_clean_code.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/66_clean_code.py) — Princípios de Clean Code em Python.
- [`conteudo/67_solid.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/67_solid.py) — Os 5 princípios SOLID na prática.
- [`conteudo/68_dependency_injection.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/68_dependency_injection.py) — Injeção de Dependências e Desacoplamento.
- [`conteudo/69_design_patterns.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/69_design_patterns.py) — Strategy, Factory, Adapter, Observer em Python.
- [`conteudo/70_repository_pattern.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/70_repository_pattern.py) — Implementação do Pattern Repository e Camada de Persistência.

---

### ⚡ 7. Algorithms & Data Structures (Estruturas de Dados & Análise Big O)
- [`conteudo/71_big_o.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/71_big_o.py) — Análise de complexidade temporal e espacial ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$).
- [`conteudo/72_arrays_lists.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/72_arrays_lists.py) — Algoritmos em Arrays: Two Pointers e Sliding Window.
- [`conteudo/73_hash_maps.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/73_hash_maps.py) — Resolução do algoritmo Two Sum em $O(n)$ com Hash Map.
- [`conteudo/74_stack.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/74_stack.py) — Estrutura Pilha (LIFO) e validação de parênteses.
- [`conteudo/75_queue.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/75_queue.py) — Estrutura Fila (FIFO) com `collections.deque`.
- [`conteudo/76_linked_list.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/76_linked_list.py) — Lista Encadeada Simples e inversão em $O(n)$.
- [`conteudo/77_binary_search.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/77_binary_search.py) — Busca Binária em arrays ordenados ($O(\log n)$).
- [`conteudo/78_recursao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/78_recursao.py) — Recursão, Call Stack e caso base.
- [`conteudo/79_trees.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/79_trees.py) — Árvore Binária de Busca (BST) e percursos.
- [`conteudo/80_heap.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/80_heap.py) — Fila de prioridade com `heapq` e algoritmo Top-K.
- [`conteudo/81_graphs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/81_graphs.py) — Representação de Grafos e Busca em Largura (BFS).

---

### 🌐 8. HTTP & Web APIs
- [`conteudo/82_http_fundamentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/82_http_fundamentos.py) — Verbos HTTP, headers, status codes e payloads REST.
- [`conteudo/83_http_client.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/83_http_client.py) — Consumo de APIs REST com cliente nativo `urllib.request`.
- [`conteudo/84_retries_timeouts.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo/84_retries_timeouts.py) — Padrões de resiliência: Retries com Exponential Backoff.

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
python conteudo/01_variaveis.py
python conteudo/52_asyncio_basico.py

# 4. Executar TODOS os 87 scripts em lote (Auditoria Automática)
python verify_all_87.py

# 5. Executar os testes automatizados e checagem de tipos
pytest
mypy .
ruff check .
```
