# 🚀 Guia de Execução: Módulos 01 ao 87 (PythonFirst)

Este documento fornece as instruções completas para executar, testar e auditar cada um dos **87 módulos didático-práticos** organizados nas 10 subpastas da diretoria [`conteudo/`](file:///c:/Users/gabri/Documents/PROJECTS/pythonfirst/conteudo).

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

- **Executar todos os 87 scripts de uma vez (Varredura de Subpastas)**:
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

## 📚 Execução por Categoria de Conhecimento

### 📁 1. Fundamentos e Collections (`conteudo/01_fundamentos_collections/`)
```powershell
python conteudo/01_fundamentos_collections/01_variaveis.py
python conteudo/01_fundamentos_collections/02_operadores.py
python conteudo/01_fundamentos_collections/03_tipos_dados.py
python conteudo/01_fundamentos_collections/04_condicionais.py
python conteudo/01_fundamentos_collections/05_match_case.py
python conteudo/01_fundamentos_collections/06_loops.py
python conteudo/01_fundamentos_collections/07_range_enumerate_zip.py
python conteudo/01_fundamentos_collections/08_funcoes.py
python conteudo/01_fundamentos_collections/09_args_kwargs.py
python conteudo/01_fundamentos_collections/10_escopo_legb.py
python conteudo/01_fundamentos_collections/11_lambda.py
python conteudo/01_fundamentos_collections/12_listas.py
python conteudo/01_fundamentos_collections/13_tuplas.py
python conteudo/01_fundamentos_collections/14_dicionarios.py
python conteudo/01_fundamentos_collections/15_sets.py
python conteudo/01_fundamentos_collections/16_comprehensions.py
python conteudo/01_fundamentos_collections/17_collections.py
```

### 📁 2. Python Idiomático, Arquivos e Packages (`conteudo/02_python_idiomatico_pacotes/`)
```powershell
python conteudo/02_python_idiomatico_pacotes/18_python_idiomatico.py
python conteudo/02_python_idiomatico_pacotes/19_slicing.py
python conteudo/02_python_idiomatico_pacotes/20_unpacking.py
python conteudo/02_python_idiomatico_pacotes/21_any_all_sorted.py
python conteudo/02_python_idiomatico_pacotes/22_itertools.py
python conteudo/02_python_idiomatico_pacotes/23_functools.py
python conteudo/02_python_idiomatico_pacotes/24_strings.py
python conteudo/02_python_idiomatico_pacotes/25_arquivos.py
python conteudo/02_python_idiomatico_pacotes/26_json.py
python conteudo/02_python_idiomatico_pacotes/27_pathlib.py
python conteudo/02_python_idiomatico_pacotes/28_modulos.py
python conteudo/02_python_idiomatico_pacotes/29_packages.py
```

### 📁 3. Exceptions, POO e Typing (`conteudo/03_excecoes_poo_typing/`)
```powershell
python conteudo/03_excecoes_poo_typing/30_excecoes.py
python conteudo/03_excecoes_poo_typing/31_excecoes_customizadas.py
python conteudo/03_excecoes_poo_typing/32_classes_objetos.py
python conteudo/03_excecoes_poo_typing/33_init_str_repr.py
python conteudo/03_excecoes_poo_typing/34_encapsulamento.py
python conteudo/03_excecoes_poo_typing/35_property.py
python conteudo/03_excecoes_poo_typing/36_heranca.py
python conteudo/03_excecoes_poo_typing/37_heranca_multipla_mro.py
python conteudo/03_excecoes_poo_typing/38_polimorfismo.py
python conteudo/03_excecoes_poo_typing/39_classes_abstratas.py
python conteudo/03_excecoes_poo_typing/40_classmethod_staticmethod.py
python conteudo/03_excecoes_poo_typing/41_dunder_methods.py
python conteudo/03_excecoes_poo_typing/42_dataclasses.py
python conteudo/03_excecoes_poo_typing/43_enum.py
python conteudo/03_excecoes_poo_typing/44_type_hints.py
python conteudo/03_excecoes_poo_typing/45_typing_avancado.py
```

### 📁 4. Iterators, Generators, Decorators e Context Managers (`conteudo/04_iteradores_decoradores_contexto/`)
```powershell
python conteudo/04_iteradores_decoradores_contexto/46_iteradores.py
python conteudo/04_iteradores_decoradores_contexto/47_geradores.py
python conteudo/04_iteradores_decoradores_contexto/48_decoradores.py
python conteudo/04_iteradores_decoradores_contexto/49_decoradores_com_argumentos.py
python conteudo/04_iteradores_decoradores_contexto/50_context_managers.py
python conteudo/04_iteradores_decoradores_contexto/51_contextlib.py
```

### 📁 5. Async e Concorrência (`conteudo/05_async_concorrencia/`)
```powershell
python conteudo/05_async_concorrencia/52_asyncio_basico.py
python conteudo/05_async_concorrencia/53_asyncio_tasks.py
python conteudo/05_async_concorrencia/54_asyncio_avancado.py
python conteudo/05_async_concorrencia/55_threads.py
python conteudo/05_async_concorrencia/56_multiprocessing.py
python conteudo/05_async_concorrencia/57_concurrent_futures.py
python conteudo/05_async_concorrencia/58_cpu_vs_io_bound.py
```

### 📁 6. Logging, Debugging e Testing (`conteudo/06_logging_debugging_testes/`)
```powershell
python conteudo/06_logging_debugging_testes/59_logging.py
python conteudo/06_logging_debugging_testes/60_debugging.py
python conteudo/06_logging_debugging_testes/61_pytest_basico.py
python conteudo/06_logging_debugging_testes/62_pytest_fixtures.py
python conteudo/06_logging_debugging_testes/63_pytest_parametrize.py
python conteudo/06_logging_debugging_testes/64_mocking.py
python conteudo/06_logging_debugging_testes/65_testes_integracao.py
```

### 📁 7. Engenharia de Software (`conteudo/07_engenharia_software/`)
```powershell
python conteudo/07_engenharia_software/66_clean_code.py
python conteudo/07_engenharia_software/67_solid.py
python conteudo/07_engenharia_software/68_dependency_injection.py
python conteudo/07_engenharia_software/69_design_patterns.py
python conteudo/07_engenharia_software/70_repository_pattern.py
```

### 📁 8. DSA / Entrevistas (`conteudo/08_dsa_algoritmos/`)
```powershell
python conteudo/08_dsa_algoritmos/71_big_o.py
python conteudo/08_dsa_algoritmos/72_arrays_lists.py
python conteudo/08_dsa_algoritmos/73_hash_maps.py
python conteudo/08_dsa_algoritmos/74_stack.py
python conteudo/08_dsa_algoritmos/75_queue.py
python conteudo/08_dsa_algoritmos/76_linked_list.py
python conteudo/08_dsa_algoritmos/77_binary_search.py
python conteudo/08_dsa_algoritmos/78_recursao.py
python conteudo/08_dsa_algoritmos/79_trees.py
python conteudo/08_dsa_algoritmos/80_heap.py
python conteudo/08_dsa_algoritmos/81_graphs.py
```

### 📁 9. HTTP e Resiliência (`conteudo/09_http_resiliencia/`)
```powershell
python conteudo/09_http_resiliencia/82_http_fundamentos.py
python conteudo/09_http_resiliencia/83_http_client.py
python conteudo/09_http_resiliencia/84_retries_timeouts.py
```

### 📁 10. Metaprogramação (`conteudo/10_metaprogramacao/`)
```powershell
python conteudo/10_metaprogramacao/85_getattr_getattribute.py
python conteudo/10_metaprogramacao/86_descriptors.py
python conteudo/10_metaprogramacao/87_metaclasses.py
```
