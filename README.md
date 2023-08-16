# Gepetuto

[![PyPI version](https://badge.fury.io/py/gepetuto.svg)](https://pypi.org/project/gepetuto)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gepetto/gepetuto/main.svg)](https://results.pre-commit.ci/latest/github/gepetto/gepetuto/main)
[![Tests](https://github.com/gepetto/gepetuto/actions/workflows/tests.yml/badge.svg)](https://github.com/gepetto/gepetuto/actions/workflows/tests.yml)
[![Release](https://github.com/gepetto/gepetuto/actions/workflows/release.yml/badge.svg)](https://github.com/gepetto/gepetuto/actions/workflows/release.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

## Tutorial edition framework

This project contains some tools to help authoring and maintaing python tutorials presented on notebooks.

## Install

You are strongly encouraged to use a virtual env or similar.
```
python -m pip install gepetuto
```

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

## CI Example

example of CI using all gepetuto actions on tests folder here :
- https://github.com/Gepetto/gepetuto/blob/main/.github/workflows/tests.yml

## Examples

- https://github.com/gepetto/supaero2023
- https://github.com/nmansard/jnrh2023
