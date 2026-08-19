# 🐍 Python First: Repositório Educacional & Laboratório Prático de Engenharia de Software

> **Laboratório progressivo de aprendizado de Python, Engenharia de Software, Backend, Algoritmos e Inteligência Artificial Aplicada.**

Este repositório é um **guia permanente de referência técnica, laboratório executável e roadmap de evolução profissional** em Python 3.12+. Cada arquivo funciona como uma **mini aula prática autossuficiente**, contendo explicações teóricas, exemplos reais, análise de complexidade (Big O), boas práticas, antipadrões e conexões com entrevistas técnicas.

> 📖 **Guia Rápido de Execução**: Consulte o [COMO_EXECUTAR.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/COMO_EXECUTAR.md) para instruções detalhadas de como executar cada um dos 87 módulos individualmente ou em lote.
> 📅 **Cronograma Completo**: Consulte o [cronograma_estudo_python.md](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/cronograma_estudo_python.md) para a trilha de 10 semanas.

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

## 📚 Estrutura Detalhada dos Módulos (01 ao 87)

### 🔹 1. Fundamentals (Fundamentos da Linguagem)
- [`01_variaveis.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/01_variaveis.py) — Tipagem dinâmica, forte, referências de memória, Type Annotations.
- [`02_operadores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/02_operadores.py) — Operadores aritméticos, lógicos, precedência, `==` vs `is`.
- [`03_tipos_dados.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/03_tipos_dados.py) — Primitive types (`int`, `float`, `bool`, `str`, `None`), casting, truthy/falsy, mutabilidade.
- [`04_condicionais.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/04_condicionais.py) — `if`/`elif`/`else`, ternários, Early Returns, guarda de condições.
- [`05_match_case.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/05_match_case.py) — Structural Pattern Matching (Python 3.10+), wildcards, guards.
- [`06_loops.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/06_loops.py) — `for`, `while`, `break`, `continue`, e blocos `for...else` / `while...else`.
- [`07_range_enumerate_zip.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/07_range_enumerate_zip.py) — Iteração idiomática com `range()`, `enumerate()`, `zip()`.
- [`08_funcoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/08_funcoes.py) — Assinaturas, parâmetros posicionais, nomeados, responsabilidade única.
- [`09_args_kwargs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/09_args_kwargs.py) — Parâmetros variádicos `*args` e `**kwargs` e repasse de argumentos.
- [`10_escopo_legb.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/10_escopo_legb.py) — Regra LEGB (Local, Enclosing, Global, Built-in), `global` e `nonlocal`.
- [`11_lambda.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/11_lambda.py) — Funções anônimas vs `def`, uso com `sorted()`, `map()`, `filter()`.
- [`12_listas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/12_listas.py) — Operações com `list`, slicing, mutabilidade e análise Big O de operações.
- [`13_tuplas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/13_tuplas.py) — Tuplas como registros imutáveis, CPython freelist, unpacking e hashability.
- [`14_dicionarios.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/14_dicionarios.py) — Hash maps compactos em CPython, `get()`, `setdefault()`, views dinâmicas e busca $O(1)$.
- [`15_sets.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/15_sets.py) — Teoria dos conjuntos (união, interseção, diferença), membership $O(1)$, deduplicação $O(n)$ e `frozenset`.
- [`16_comprehensions.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/16_comprehensions.py) — List, Dict, Set Comprehensions, bytecode `LIST_APPEND` e Generator Expressions.
- [`17_collections.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/17_collections.py) — Módulo `collections` (`Counter`, `defaultdict`, `deque`, `namedtuple`, `ChainMap`).

---

### 🟢 2. Pythonic Python (Python Idiomático & Utilitários Nativos)
- [`18_python_idiomatico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/18_python_idiomatico.py) — Código Pythonic vs Não-Pythonic, EAFP vs LBYL, Truthiness.
- [`19_slicing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/19_slicing.py) — Fatiamento avançado `[inicio:fim:passo]`, objeto `slice()`, atribuição por slice.
- [`20_unpacking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/20_unpacking.py) — Extended Unpacking (`*resto`), desestruturação em dicionários `**`.
- [`21_any_all_sorted.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/21_any_all_sorted.py) — Avaliação de curto-circuito (`any`, `all`), ordenação Timsort com `key=`.
- [`22_itertools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/22_itertools.py) — `chain`, `combinations`, `permutations`, `product`, `groupby`.
- [`23_functools.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/23_functools.py) — `@cache`, `@lru_cache`, `partial`, `reduce`, `wraps`.
- [`24_strings.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/24_strings.py) — Imutabilidade de strings, `str.join()` em $O(n)$ e f-strings avançadas.
- [`25_arquivos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/25_arquivos.py) — Leitura e escrita segura com `with open()` e UTF-8.
- [`26_json.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/26_json.py) — Serialização (`dumps`, `loads`) e encoders customizados para objetos complexos.
- [`27_pathlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/27_pathlib.py) — Orientação a objetos em caminhos do SO com `pathlib.Path` e `/`.
- [`28_modulos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/28_modulos.py) — Sistema de imports, `sys.path`, escopo `__name__`.
- [`29_packages.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/29_packages.py) — Estrutura de pacotes (`__init__.py`), `__all__` e Namespace Packages.

---

### 🟡 3. OOP & Typing (Orientação a Objetos, Exceções & Tipagem)
- [`30_excecoes.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/30_excecoes.py) — `try`/`except`/`else`/`finally`, exceções específicas e Exception Chaining (`from e`).
- [`31_excecoes_customizadas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/31_excecoes_customizadas.py) — Exceções de domínio customizadas para backend.
- [`32_classes_objetos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/32_classes_objetos.py) — Classes, instâncias, estado e `self`.
- [`33_init_str_repr.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/33_init_str_repr.py) — Construtor `__init__`, `__str__` vs `__repr__`.
- [`34_encapsulamento.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/34_encapsulamento.py) — Visibilidade (`público`, `_protegido`, `__privado` / Name Mangling).
- [`35_property.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/35_property.py) — Encapsulamento com `@property` e `@<prop>.setter`.
- [`36_heranca.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/36_heranca.py) — Herança simples e encadeamento com `super()`.
- [`37_heranca_multipla_mro.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/37_heranca_multipla_mro.py) — Herança múltipla, algoritmo C3 Linearization, inspeção de MRO (`.mro()`).
- [`38_polimorfismo.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/38_polimorfismo.py) — Polimorfismo e Duck Typing.
- [`39_classes_abstratas.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/39_classes_abstratas.py) — Contratos abstratos com `abc.ABC` e `@abstractmethod`.
- [`40_classmethod_staticmethod.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/40_classmethod_staticmethod.py) — Métodos de instância vs `@classmethod` vs `@staticmethod`.
- [`41_dunder_methods.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/41_dunder_methods.py) — Protocolos nativos (`__len__`, `__getitem__`, `__call__`).
- [`42_dataclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/42_dataclasses.py) — `@dataclass`, `field()`, `frozen=True`, `kw_only=True`, `__post_init__`.
- [`43_enum.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/43_enum.py) — Enumerações fortemente tipadas com `Enum` e `auto()`.
- [`44_type_hints.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/44_type_hints.py) — Tipagem moderna: `list[str]`, `dict[str, int]`, `str | None`, `Callable`.
- [`45_typing_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/45_typing_avancado.py) — `Protocol` (subtipagem estrutural), `Generic[T]`, `TypeVar`, `TypedDict`.

---

### 🟠 4. Advanced Python (Iteradores, Geradores, Async, Threads & Metaprogramação)
- [`46_iteradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/46_iteradores.py) — Protocolo de iteração customizado com `__iter__` e `__next__`.
- [`47_geradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/47_geradores.py) — Funções geradoras com `yield` e `yield from`.
- [`48_decoradores.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/48_decoradores.py) — Funções de alta ordem e decoradores de funções.
- [`49_decoradores_com_argumentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/49_decoradores_com_argumentos.py) — Fábricas de decoradores parametrizados.
- [`50_context_managers.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/50_context_managers.py) — Gerenciadores de contexto com `__enter__` e `__exit__`.
- [`51_contextlib.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/51_contextlib.py) — `@contextlib.contextmanager` e `contextlib.suppress`.
- [`52_asyncio_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/52_asyncio_basico.py) — `async`/`await`, Event Loop e `asyncio.run()`.
- [`53_asyncio_tasks.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/53_asyncio_tasks.py) — Execução concorrente com `create_task()` e `gather()`.
- [`54_asyncio_avancado.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/54_asyncio_avancado.py) — Controle de concorrência com `asyncio.Semaphore` e `asyncio.Queue`.
- [`55_threads.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/55_threads.py) — Concorrência com `threading.Thread` e `threading.Lock` para I/O-bound.
- [`56_multiprocessing.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/56_multiprocessing.py) — Paralelismo real em múltiplos núcleos para tarefas CPU-bound.
- [`57_concurrent_futures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/57_concurrent_futures.py) — Pools de execução com `ThreadPoolExecutor`.
- [`58_cpu_vs_io_bound.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/58_cpu_vs_io_bound.py) — Guia de arquitetura: CPU-bound vs I/O-bound e impacto do GIL.
- [`59_logging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/59_logging.py) — Logging profissional estruturado com níveis, formatters e handlers.
- [`60_debugging.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/60_debugging.py) — Análise de tracebacks e depuração com `breakpoint()`.
- *(Módulo Opcional / Metaprogramação)*:
  - [`85_getattr_getattribute.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/85_getattr_getattribute.py) — Interceptação de atributos com `__getattr__`.
  - [`86_descriptors.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/86_descriptors.py) — Protocolo Descriptor (`__get__`, `__set__`).
  - [`87_metaclasses.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/87_metaclasses.py) — Metaclasses com `type` e `__new__`.

---

### 🧪 5. Testing & Quality (Testes Automatizados & Qualidade)
- [`61_pytest_basico.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/61_pytest_basico.py) — Introdução ao `pytest` e asserções idiomáticas.
- [`62_pytest_fixtures.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/62_pytest_fixtures.py) — Reutilização de estado de teste com `@pytest.fixture`.
- [`63_pytest_parametrize.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/63_pytest_parametrize.py) — Testes parametrizados para múltiplas entradas.
- [`64_mocking.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/64_mocking.py) — Isolamento de dependências externas com `unittest.mock.MagicMock`.
- [`65_testes_integracao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/65_testes_integracao.py) — Pirâmide de testes (Unitários vs Integração).

---

### 🏛️ 6. Software Engineering (Clean Code, SOLID, DI & Design Patterns)
- [`66_clean_code.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/66_clean_code.py) — Princípios de Clean Code em Python.
- [`67_solid.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/67_solid.py) — Os 5 princípios SOLID na prática.
- [`68_dependency_injection.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/68_dependency_injection.py) — Injeção de Dependências e Desacoplamento.
- [`69_design_patterns.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/69_design_patterns.py) — Strategy, Factory, Adapter, Observer em Python.
- [`70_repository_pattern.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/70_repository_pattern.py) — Implementação do Pattern Repository e Camada de Persistência.

---

### ⚡ 7. Algorithms & Data Structures (Estruturas de Dados & Análise Big O)
- [`71_big_o.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/71_big_o.py) — Análise de complexidade temporal e espacial ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$).
- [`72_arrays_lists.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/72_arrays_lists.py) — Algoritmos em Arrays: Two Pointers e Sliding Window.
- [`73_hash_maps.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/73_hash_maps.py) — Resolução do algoritmo Two Sum em $O(n)$ com Hash Map.
- [`74_stack.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/74_stack.py) — Estrutura Pilha (LIFO) e validação de parênteses.
- [`75_queue.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/75_queue.py) — Estrutura Fila (FIFO) com `collections.deque`.
- [`76_linked_list.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/76_linked_list.py) — Lista Encadeada Simples e inversão em $O(n)$.
- [`77_binary_search.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/77_binary_search.py) — Busca Binária em arrays ordenados ($O(\log n)$).
- [`78_recursao.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/78_recursao.py) — Recursão, Call Stack e caso base.
- [`79_trees.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/79_trees.py) — Árvore Binária de Busca (BST) e percursos.
- [`80_heap.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/80_heap.py) — Fila de prioridade com `heapq` e algoritmo Top-K.
- [`81_graphs.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/81_graphs.py) — Representação de Grafos e Busca em Largura (BFS).

---

### 🌐 8. HTTP & Web APIs
- [`82_http_fundamentos.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/82_http_fundamentos.py) — Verbos HTTP, headers, status codes e payloads REST.
- [`83_http_client.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/83_http_client.py) — Consumo de APIs REST com cliente nativo `urllib.request`.
- [`84_retries_timeouts.py`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/84_retries_timeouts.py) — Padrões de resiliência: Retries com Exponential Backoff.

---

### 🚀 9. FastAPI Framework (`fastapi_estudos/`)
- Módulo completo de APIs REST modernas com Pydantic, Injeção de Dependências nativa, rotas assíncronas e arquitetura limpa.

---

### 🗄️ 10. Database Engineering (`database_estudos/`)
- Integração SQL nativa, PostgreSQL, gerenciamento de transações ACID, Connection Pools e ORMs.

---

### 🤖 11. AI Engineering (`ia_estudos/`)
- Implementação de Embeddings, Busca Vetorial, RAG e Agentes autônomos em **Python puro e APIs REST diretas**, sem caixa preta de frameworks.

---

### 🎯 12. Interview Preparation & Projects (`desafios/` & `projetos/`)
- Trilha paralela de questões técnicas resolvidas com análise Big O temporal/espacial e 7 projetos práticos completos de Engenharia de Software.

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

# 3. Executar qualquer módulo individual
python 01_variaveis.py
python 52_asyncio_basico.py

# 4. Executar TODOS os 87 scripts em lote (Auditoria Automática)
python verify_all_87.py

# 5. Executar os testes automatizados e checagem de tipos
pytest
mypy .
ruff check .
```
