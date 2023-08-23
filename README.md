# Gepetuto

[![PyPI version](https://badge.fury.io/py/gepetuto.svg)](https://pypi.org/project/gepetuto)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gepetto/gepetuto/main.svg)](https://results.pre-commit.ci/latest/github/gepetto/gepetuto/main)
[![Tests](https://github.com/gepetto/gepetuto/actions/workflows/tests.yml/badge.svg)](https://github.com/gepetto/gepetuto/actions/workflows/tests.yml)
[![Release](https://github.com/gepetto/gepetuto/actions/workflows/release.yml/badge.svg)](https://github.com/gepetto/gepetuto/actions/workflows/release.yml)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

## Tutorial edition framework

This project contains some tools to help authoring and maintaing python tutorials presented on notebooks.

## Install

Add `gepetuto` in your pip / PyPI dependencies

## Usage

1. create a (eg. `tp1`) directory (`tp0` can be used to check prerequisites)
2. write python scripts (eg. `example_script.py`) in this directory
3. delimit snippets inside those scripts between `# %jupyter_snippet example_snippet` and `# %end_jupyter_snippet`
4. create a (eg. `1-example_notebook.ipynb`) notebook, containing `import gepetuto.magic`
5. run `gepetuto -a generate`: this will create a `tp{i}/generated` directory with eg. `example_script_example_snippet`
6. cells can contain either eg. `%load tp1/generated/example_script_example_snippet` to display some code to students,
   or their `%do_not_load` version to let the student write the code themself
7. run `gepetuto -a test` to check all python scripts in tp directories
8. run `gepetuto -a lint` to ensure the coding standards are respected in all python scripts in tp directories
9. add `gepetuto -a test` in your CI, and `gepetuto -a lint` + `gepetuto -a generate` in your pre-commit

### Command line

```
$ gepetuto -h
usage: gepetuto [-h] [-v] [-a [{lint,test,generate,all}]] [-f [FILE [FILE ...]]] [-F [FILTER [FILTER ...]]]
                [-p PYTHON] [-c] [-C DIRECTORY] [--version] [tp_id [tp_id ...]]

Tutorial edition framework

positional arguments:
  tp_id                 choose which tp to process. Default to all.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increment verbosity level
  -a [{lint,test,generate,all}], --action [{lint,test,generate,all}]
                        choose what to do. Default to 'generate'.
  -f [FILE [FILE ...]], --file [FILE [FILE ...]]
                        choose which files to process.
  -F [FILTER [FILTER ...]], --filter [FILTER [FILTER ...]]
                        filter files to process.
  -p PYTHON, --python PYTHON
                        choose python interpreter to use.
  -c, --check           check if linters change files.
  -C DIRECTORY, --directory DIRECTORY
                        choose directory to run action on.
  --version             Get gepetuto version.
```

## CI Example

example of CI using all gepetuto actions on tests folder here :
- https://github.com/Gepetto/gepetuto/blob/main/.github/workflows/tests.yml

## Pre commit example

```
- repo: https://github.com/Gepetto/gepetuto
  rev: v1.2.0
  hooks:
  - id: generate-action
  - id: lint-action
  - id: test-action
```


## Examples

- https://github.com/gepetto/supaero2023
- https://github.com/nmansard/jnrh2023
