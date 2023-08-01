"""Add "lint" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call
from typing import List

LOG = logging.getLogger("gepetuto.lint")


def lint(tp_id: List[int], **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    if tp_id:
        for n in tp_id:
            lint_tp_folder(n)
    else:
        for tp_number in range(100):
            LOG.debug(f"Looking for tp {tp_number}")
            try:
                lint_tp_folder(tp_number)
            except StopIteration:
                if tp_number == 0:
                    continue
                break
    LOG.info("lint done.")


def lint_tp_folder(tp_number):
    """Lint python scripts for a given tp_number."""
    LOG.debug(f"Looking for tp {tp_number}")
    folder = Path(f"tp{tp_number}")
    if folder.exists():
        for python_file in folder.glob("*.py"):
            print(python_file)
            LOG.debug(f"Checking {python_file}")
            check_call(["isort", python_file])
            check_call(["black", python_file])
            check_call(["ruff", "--fix", python_file])
    else:
        raise StopIteration
