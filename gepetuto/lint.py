"""Add "lint" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call
from typing import List

LOG = logging.getLogger("gepetuto.lint")


def lint(tp_id: List[int], **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    for n in tp_id:
        LOG.debug(f"Looking for tp {n}")
        lint_tp_folder(n)
    LOG.info("lint done.")


def lint_tp_folder(tp_number):
    """Lint python scripts for a given tp_number."""
    LOG.debug(f"Looking for tp {tp_number}")
    folder = Path(f"tp{tp_number}")
    for python_file in folder.glob("*.py"):
        print(python_file)
        LOG.debug(f"Checking {python_file}")
        check_call(["isort", python_file])
        check_call(["black", python_file])
        check_call(["ruff", "--fix", python_file])
