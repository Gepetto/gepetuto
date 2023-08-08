"""Add "lint" action for the "gepetuto" program."""

import logging
from subprocess import check_call

LOG = logging.getLogger("gepetuto.lint")


def lint(files, **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    for f in files:
        lint_file(f)
    LOG.info("lint done.")


def lint_file(file):
    """Lint python script."""
    LOG.debug(f"Checking {file}")
    check_call(["isort", file])
    check_call(["black", file])
    check_call(["ruff", "--fix", file])
