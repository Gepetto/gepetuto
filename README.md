# Gepetuto

## Tutorial edition framework

This project contains some tools to help authoring and maintaing python tutorials presented on notebooks.

## Install

Until the first release of this package, here is the recommended installation procedure:
```
pipx install -e .
```

## Usage

1. create a (eg. `tp1`) directory (`tp0` can be used to check prerequisites)
2. write python scripts (eg. `example_script.py`) in this directory
3. delimit snippets inside those scripts between `# %jupyter_snippet example_snippet` and `# %end_jupyter_snippet`
4. create a (eg. `1_example_notebook.ipynb`) notebook, containing `import gepetuto.magic`
5. run `gepetuto -a generate`: this will create a `tp{i}/generated` directory with eg. `example_script_example_snippet`
6. cells can contain either eg. `%load tp1/generated/example_script_example_snippet` to display some code to students,
   or their `%do_not_load` version to let the student write the code themself
7. run `gepetuto -a test` to check all python scripts in tp directories
8. run `gepetuto -a lint` to ensure the coding standards are respected in all python scripts in tp directories
9. add `gepetuto -a test` in your CI, and `gepetuto -a lint` + `gepetuto -a generate` in your pre-commit

## CI Example

example of CI using all gepetuto actions on tests folder here :
- https://github.com/Gepetto/gepetuto/blob/main/.github/workflows/python-app.yml

## Examples

- https://github.com/gepetto/supaero2023
- https://github.com/nmansard/jnrh2023
