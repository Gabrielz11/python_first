# 📅 Cronograma de Estudos Python: Do Básico ao Engenheiro Sênior (10 Semanas)

> **Plano de Aprendizado Progressivo & Trilha de Evolução Profissional em Python**

---

## 🧭 Metodologia Pedagógica

Para transformar teoria em habilidade real de Engenharia de Software, cada tópico deve ser estudado segundo o ciclo:

```text
  [ CONCEITO ] ──► Entender o POR QUÊ e o funcionamento interno.
       │
  [ EXEMPLO ] ──► Analisar o código de referência fornecido.
       │
  [ ALTERAR ] ──► Modificar os parâmetros do exemplo e observar as saídas.
       │
  [ EXERCÍCIO ] ──► Resolver o exercício proposto sem olhar a solução.
       │
  [ DESAFIO ] ──► Otimizar a solução considerando Big O temporal e espacial.
       │
  [ MINIPROJETO ] ──► Integrar o conhecimento em um módulo reutilizável.
       │
  [ REVISÃO ] ──► Explicar a solução verbalmente como em uma entrevista técnica.
```

---

## 📌 Trilha Principal vs Aprofundamento Avançado (Opcional)

- **Trilha Principal (Core)**: Módulos de 01 a 84, FastAPI, Banco de Dados, IA Nativa e Projetos Práticos. Essencial para atuação como Engenheiro Backend / Python Developer.
- **Trilha de Aprofundamento Avançado (Opcional)**: Módulos 85, 86 e 87 (Metaprogramação, Descriptors e Metaclasses). Recomendado para criação de frameworks, ORMs e bibliotecas de infraestrutura.

---

## 🗓️ Cronograma Semana a Semana

### 🔹 Semana 1: Fundamentos da Linguagem & Controle de Fluxo
- **Objetivo**: Sintaxe moderna, tipagem dinâmica vs forte, mutabilidade, tomada de decisão e laços.
- **Arquivos**:
  - `01_variaveis.py`
  - `02_operadores.py`
  - `03_tipos_dados.py`
  - `04_condicionais.py`
  - `05_match_case.py`
  - `06_loops.py`
  - `07_range_enumerate_zip.py`
- **Desafio Semanal**: 3 exercícios em `exercicios/01_fundamentos/`.

---

### 🟢 Semana 2: Funções, Collections & Análise de Complexidade Inicial
- **Objetivo**: Assinaturas de funções, escopo LEGB, coleções nativas e entendimento de Big O em listas e dicionários.
- **Arquivos**:
  - `08_funcoes.py`
  - `09_args_kwargs.py`
  - `10_escopo_legb.py`
  - `11_lambda.py`
  - `12_listas.py` *(com Big O)*
  - `13_tuplas.py`
  - `14_dicionarios.py` *(com Big O O(1) médio)*
  - `15_sets.py` *(com Big O de membership vs construção)*
  - `16_comprehensions.py`
  - `17_collections.py` *(Counter, defaultdict, deque)*
- **Desafio Semanal**: 3 desafios em `desafios/` (Arrays & Hash Maps).

---

### 🟡 Semana 3: Python Idiomático, Manipulação de Arquivos & Módulos
- **Objetivo**: Escrever Python idioamático (Pythonic), manuseio de arquivos, JSON e organização de pacotes.
- **Arquivos**:
  - `18_python_idiomatico.py`
  - `19_slicing.py`
  - `20_unpacking.py`
  - `21_any_all_sorted.py`
  - `22_itertools.py`
  - `23_functools.py`
  - `24_strings.py`
  - `25_arquivos.py`
  - `26_json.py`
  - `27_pathlib.py`
  - `28_modulos.py`
  - `29_packages.py`
- **Projeto Prático**: Início do `projetos/projeto_01_cli_task_manager/`.

---

### 🟠 Semana 4: Trata de Exceções, POO Fundamentos e Avançada
- **Objetivo**: Modelagem de domínio orientada a objetos, encapsulamento, herança, polimorfismo e dunder methods.
- **Arquivos**:
  - `30_excecoes.py`
  - `31_excecoes_customizadas.py`
  - `32_classes_objetos.py`
  - `33_init_str_repr.py`
  - `34_encapsulamento.py`
  - `35_property.py`
  - `36_heranca.py`
  - `37_heranca_multipla_mro.py`
  - `38_polimorfismo.py`
  - `39_classes_abstratas.py`
  - `40_classmethod_staticmethod.py`
  - `41_dunder_methods.py`
  - `42_dataclasses.py`
  - `43_enum.py`
  - `44_type_hints.py`
  - `45_typing_avancado.py`

---

### 🔴 Semana 5: Iteradores, Geradores, Decoradores & Context Managers
- **Objetivo**: Manipulação eficiente de memória, geradores (`yield`), metaprogramação leve com decoradores e `with`.
- **Arquivos**:
  - `46_iteradores.py`
  - `47_geradores.py`
  - `48_decoradores.py`
  - `49_decoradores_com_argumentos.py`
  - `50_context_managers.py`
  - `51_contextlib.py`

---

### ⚡ Semana 6: Testes Automatizados, Logging & Debugging
- **Objetivo**: Suíte de testes com Pytest, fixtures, parametrização, mocks e qualidade de código com Ruff/Mypy.
- **Arquivos**:
  - `59_logging.py`
  - `60_debugging.py`
  - `61_pytest_basico.py`
  - `62_pytest_fixtures.py`
  - `63_pytest_parametrize.py`
  - `64_mocking.py`
  - `65_testes_integracao.py`
  - Execução da suíte real em `tests/`.

---

### 🌌 Semana 7: Concorrência, Assincronismo & HTTP
- **Objetivo**: Entender a fundo `asyncio`, Event Loop, Threads vs Processos vs Corrotinas, resiliência HTTP.
- **Arquivos**:
  - `52_asyncio_basico.py`
  - `53_asyncio_tasks.py`
  - `54_asyncio_avancado.py`
  - `55_threads.py`
  - `56_multiprocessing.py`
  - `57_concurrent_futures.py`
  - `58_cpu_vs_io_bound.py`
  - `82_http_fundamentos.py`
  - `83_http_client.py`
  - `84_retries_timeouts.py`

---

### 🏛️ Semana 8: Clean Code, Arquitetura de Software & Algoritmos
- **Objetivo**: Princípios SOLID, Dependency Injection, Repository Pattern, Estruturas de Dados e Busca em Grafos.
- **Arquivos**:
  - `66_clean_code.py` a `70_repository_pattern.py`
  - `71_big_o.py` a `81_graphs.py`
- **Projeto Prático**: `projetos/projeto_02_api_task_manager/`.

---

### 🚀 Semana 9: Backend Profissional com FastAPI & PostgreSQL
- **Objetivo**: APIs REST prontas para produção, Pydantic v2, injeção de dependência, transações ACID e ORM.
- **Pastas**:
  - `fastapi_estudos/`
  - `database_estudos/`
- **Projeto Prático**: `projetos/projeto_03_user_management_api/`.

---

### 🤖 Semana 10: IA Engineering, RAG & Agentes Autônomos (Sem Frameworks)
- **Objetivo**: Criar pipelines de IA, embeddings, busca por cosseno, RAG e agentes autônomos do zero em Python puro.
- **Pasta**:
  - `ia_estudos/`
- **Projetos Práticos**:
  - `projetos/projeto_04_document_qa/`
  - `projetos/projeto_05_rag_api/`
  - `projetos/projeto_06_agent/`
  - `projetos/projeto_07_automacao/`

---

## 🔬 Módulo Opcional de Aprofundamento Avançado (Metaprogramação)
- `85_getattr_getattribute.py`
- `86_descriptors.py`
- `87_metaclasses.py`

*(Recomendado realizar após a Semana 10 para consolidar conhecimentos de infraestrutura).*
