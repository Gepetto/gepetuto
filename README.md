# Gepetuto

## Tutorial edition framework

This project contains some tools to help authoring and maintaing python tutorials presented on notebooks.

## Usage

1. create a (eg. `tp1`) directory (`tp0` can be used to check prerequisites)
2. write python scripts (eg. `cholesky.py`) in this directory
3. delimit snippets inside those scripts between `# %jupyter_snippet some_name` and `# %end_jupyter_snippet`
4. run `gepetuto generate`: this will create a `tp{i}/generated` directory with eg. `cholesky_some_name` snippet
5. create a (eg. `1_factorisation.ipynb`) notebook, containing `import gepetuto.magic`
6. cells can contain either eg. `%load tp1/generated/choleskey_some_name` to display some code to the student, or their
   `%do_not_load` version to let the student write the code themself
7. run `gepetuto test` to check all python scripts in tp directories
8. run `gepetuto lint` to ensure the coding standards are respected in all python scripts in tp directories
9. add `gepetuto test` in your CI, and `gepetuto lint` + `gepetuto generate` in your pre-commit

## Examples

- https://github.com/gepetto/supaero2023
- https://github.com/nmansard/jnrh2023
