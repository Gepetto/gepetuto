"""Add "lint" action for the "gepetuto" program."""

import logging
from subprocess import check_call

LOG = logging.getLogger("gepetuto.lint")


def lint(files, **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    for tp_files in files.values():
        for tp_file in tp_files:
            lint_file(tp_file, kwargs["check"])
    LOG.info("lint done.")


def lint_file(file, check):
    """Lint python script."""
    LOG.debug("Checking %s", file)
    if check:
        check_call(["isort", file, "--check"])
        check_call(["black", file, "--check"])
        check_call(["ruff", "--fix", file, "--exit-non-zero-on-fix"])
    else:
        check_call(["isort", file])
        check_call(["black", file])
        check_call(["ruff", "--fix", file])
