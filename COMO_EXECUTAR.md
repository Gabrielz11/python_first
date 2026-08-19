# 🚀 Guia de Execução: Módulos 01 ao 87 (PythonFirst)

Este documento fornece as instruções completas para executar, testar e auditar cada um dos **87 módulos didático-práticos** (localizados na pasta [`conteudo/`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo)) do repositório **PythonFirst**.

---

## 🛠️ Pré-requisitos e Ambiente

- **Python**: versão `3.12+` recomendada.
- **Ambiente Virtual (Venv)**:
  ```powershell
  # No Windows PowerShell:
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- **Instalação das Dependências**:
  ```powershell
  pip install -r requirements.txt
  ```

---

## ⚡ Comandos Rápidos de Auditoria e Qualidade

- **Executar todos os 87 scripts de uma vez**:
  ```powershell
  python verify_all_87.py
  ```
- **Verificação de Linting (Ruff)**:
  ```powershell
  ruff check .
  ```
- **Checagem de Tipagem Estática (Mypy)**:
  ```powershell
  mypy .
  ```
- **Suíte de Testes Automatizados (Pytest)**:
  ```powershell
  pytest
  ```

---

## 📚 Como Executar Cada Módulo Individualmente (01 ao 87)

Todos os scripts estão armazenados na pasta `conteudo/` e podem ser executados individualmente via terminal:

### 🔹 Semana 1: Fundamentos da Linguagem e Controle de Fluxo
```powershell
python conteudo/01_variaveis.py
python conteudo/02_operadores.py
python conteudo/03_tipos_dados.py
python conteudo/04_condicionais.py
python conteudo/05_match_case.py
python conteudo/06_loops.py
python conteudo/07_range_enumerate_zip.py
```

### 🟢 Semana 2: Funções, Coleções e Análise Big O Inicial
```powershell
python conteudo/08_funcoes.py
python conteudo/09_args_kwargs.py
python conteudo/10_escopo_legb.py
python conteudo/11_lambda.py
python conteudo/12_listas.py
python conteudo/13_tuplas.py
python conteudo/14_dicionarios.py
python conteudo/15_sets.py
python conteudo/16_comprehensions.py
python conteudo/17_collections.py
```

### 🟡 Semana 3: Python Idiomático, Manipulação de Arquivos e Pacotes
```powershell
python conteudo/18_python_idiomatico.py
python conteudo/19_slicing.py
python conteudo/20_unpacking.py
python conteudo/21_any_all_sorted.py
python conteudo/22_itertools.py
python conteudo/23_functools.py
python conteudo/24_strings.py
python conteudo/25_arquivos.py
python conteudo/26_json.py
python conteudo/27_pathlib.py
python conteudo/28_modulos.py
python conteudo/29_packages.py
```

### 🟠 Semana 4: Tratamento de Exceções, POO e Typing Avançado
```powershell
python conteudo/30_excecoes.py
python conteudo/31_excecoes_customizadas.py
python conteudo/32_classes_objetos.py
python conteudo/33_init_str_repr.py
python conteudo/34_encapsulamento.py
python conteudo/35_property.py
python conteudo/36_heranca.py
python conteudo/37_heranca_multipla_mro.py
python conteudo/38_polimorfismo.py
python conteudo/39_classes_abstratas.py
python conteudo/40_classmethod_staticmethod.py
python conteudo/41_dunder_methods.py
python conteudo/42_dataclasses.py
python conteudo/43_enum.py
python conteudo/44_type_hints.py
python conteudo/45_typing_avancado.py
```

### 🔴 Semana 5: Iteradores, Geradores, Decoradores e Context Managers
```powershell
python conteudo/46_iteradores.py
python conteudo/47_geradores.py
python conteudo/48_decoradores.py
python conteudo/49_decoradores_com_argumentos.py
python conteudo/50_context_managers.py
python conteudo/51_contextlib.py
```

### ⚡ Semana 6: Concorrência, Assincronismo e I/O
```powershell
python conteudo/52_asyncio_basico.py
python conteudo/53_asyncio_tasks.py
python conteudo/54_asyncio_avancado.py
python conteudo/55_threads.py
python conteudo/56_multiprocessing.py
python conteudo/57_concurrent_futures.py
python conteudo/58_cpu_vs_io_bound.py
```

### 🌌 Semana 7: Logging, Debugging e Testes Automatizados
```powershell
python conteudo/59_logging.py
python conteudo/60_debugging.py
python conteudo/61_pytest_basico.py
python conteudo/62_pytest_fixtures.py
python conteudo/63_pytest_parametrize.py
python conteudo/64_mocking.py
python conteudo/65_testes_integracao.py
```

### 🏛️ Semana 8: Clean Code, SOLID e Arquitetura de Software
```powershell
python conteudo/66_clean_code.py
python conteudo/67_solid.py
python conteudo/68_dependency_injection.py
python conteudo/69_design_patterns.py
python conteudo/70_repository_pattern.py
```

### 🔬 Semana 9: Algoritmos e Estruturas de Dados (Big O)
```powershell
python conteudo/71_big_o.py
python conteudo/72_arrays_lists.py
python conteudo/73_hash_maps.py
python conteudo/74_stack.py
python conteudo/75_queue.py
python conteudo/76_linked_list.py
python conteudo/77_binary_search.py
python conteudo/78_recursao.py
python conteudo/79_trees.py
python conteudo/80_heap.py
python conteudo/81_graphs.py
```

### 🚀 Semana 10: Comunicação HTTP e Resiliência Backend
```powershell
python conteudo/82_http_fundamentos.py
python conteudo/83_http_client.py
python conteudo/84_retries_timeouts.py
```

### 🔬 Módulo Opcional: Metaprogramação Avançada
```powershell
python conteudo/85_getattr_getattribute.py
python conteudo/86_descriptors.py
python conteudo/87_metaclasses.py
```

---

## 🎯 Dica de Estudos Sênior

Ao executar cada arquivo:
1. Observe a saída impressa no terminal.
2. Abra o arquivo fonte em `conteudo/` para analisar a implementação do CPython, explicações de **Big O** e comparações entre código não-Pythonic e Pythonic.
3. Altere os parâmetros das funções e resolva os **Exercícios Sugeridos** contidos nos comentários ao final de cada aula.
