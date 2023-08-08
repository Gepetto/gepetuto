"""Add "lint" action for the "gepetuto" program."""

import logging
from subprocess import check_call

LOG = logging.getLogger("gepetuto.lint")


def lint(files, **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    for f in files:
        lint_folder(f)
    LOG.info("lint done.")


def lint_folder(file):
    """Lint python scripts in folder."""
    LOG.debug(f"Checking {file}")
    check_call(["isort", file])
    check_call(["black", file])
    check_call(["ruff", "--fix", file])
