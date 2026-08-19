# 🚀 Guia de Execução: Módulos 01 ao 87 (PythonFirst)

Este documento fornece as instruções completas para executar, testar e auditar cada um dos **87 módulos didático-práticos** do repositório **PythonFirst**.

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

Cada arquivo foi projetado para ser autossuficiente e executado diretamente via terminal.

### 🔹 Semana 1: Fundamentos da Linguagem e Controle de Fluxo
```powershell
python 01_variaveis.py
python 02_operadores.py
python 03_tipos_dados.py
python 04_condicionais.py
python 05_match_case.py
python 06_loops.py
python 07_range_enumerate_zip.py
```

### 🟢 Semana 2: Funções, Coleções e Análise Big O Inicial
```powershell
python 08_funcoes.py
python 09_args_kwargs.py
python 10_escopo_legb.py
python 11_lambda.py
python 12_listas.py
python 13_tuplas.py
python 14_dicionarios.py
python 15_sets.py
python 16_comprehensions.py
python 17_collections.py
```

### 🟡 Semana 3: Python Idiomático, Manipulação de Arquivos e Pacotes
```powershell
python 18_python_idiomatico.py
python 19_slicing.py
python 20_unpacking.py
python 21_any_all_sorted.py
python 22_itertools.py
python 23_functools.py
python 24_strings.py
python 25_arquivos.py
python 26_json.py
python 27_pathlib.py
python 28_modulos.py
python 29_packages.py
```

### 🟠 Semana 4: Tratamento de Exceções, POO e Typing Avançado
```powershell
python 30_excecoes.py
python 31_excecoes_customizadas.py
python 32_classes_objetos.py
python 33_init_str_repr.py
python 34_encapsulamento.py
python 35_property.py
python 36_heranca.py
python 37_heranca_multipla_mro.py
python 38_polimorfismo.py
python 39_classes_abstratas.py
python 40_classmethod_staticmethod.py
python 41_dunder_methods.py
python 42_dataclasses.py
python 43_enum.py
python 44_type_hints.py
python 45_typing_avancado.py
```

### 🔴 Semana 5: Iteradores, Geradores, Decoradores e Context Managers
```powershell
python 46_iteradores.py
python 47_geradores.py
python 48_decoradores.py
python 49_decoradores_com_argumentos.py
python 50_context_managers.py
python 51_contextlib.py
```

### ⚡ Semana 6: Concorrência, Assincronismo e I/O
```powershell
python 52_asyncio_basico.py
python 53_asyncio_tasks.py
python 54_asyncio_avancado.py
python 55_threads.py
python 56_multiprocessing.py
python 57_concurrent_futures.py
python 58_cpu_vs_io_bound.py
```

### 🌌 Semana 7: Logging, Debugging e Testes Automatizados
```powershell
python 59_logging.py
python 60_debugging.py
python 61_pytest_basico.py
python 62_pytest_fixtures.py
python 63_pytest_parametrize.py
python 64_mocking.py
python 65_testes_integracao.py
```

### 🏛️ Semana 8: Clean Code, SOLID e Arquitetura de Software
```powershell
python 66_clean_code.py
python 67_solid.py
python 68_dependency_injection.py
python 69_design_patterns.py
python 70_repository_pattern.py
```

### 🔬 Semana 9: Algoritmos e Estruturas de Dados (Big O)
```powershell
python 71_big_o.py
python 72_arrays_lists.py
python 73_hash_maps.py
python 74_stack.py
python 75_queue.py
python 76_linked_list.py
python 77_binary_search.py
python 78_recursao.py
python 79_trees.py
python 80_heap.py
python 81_graphs.py
```

### 🚀 Semana 10: Comunicação HTTP e Resiliência Backend
```powershell
python 82_http_fundamentos.py
python 83_http_client.py
python 84_retries_timeouts.py
```

### 🔬 Módulo Opcional: Metaprogramação Avançada
```powershell
python 85_getattr_getattribute.py
python 86_descriptors.py
python 87_metaclasses.py
```

---

## 🎯 Dica de Estudos Sênior

Ao executar cada arquivo:
1. Observe a saída impressa no terminal.
2. Abra o arquivo fonte para analisar a implementação do CPython, explicações de **Big O** e comparações entre código não-Pythonic e Pythonic.
3. Altere os parâmetros das funções e resolva os **Exercícios Sugeridos** contidos nos comentários ao final de cada aula.
