"""Add "lint" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call
from typing import Dict, List

LOG = logging.getLogger("gepetuto.lint")


def lint(files: Dict[int, List[Path]], **kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
    for tp_files in files.values():
        for tp_file in tp_files:
            lint_file(tp_file, kwargs["check"])
    LOG.info("lint done.")


def lint_file(file: Path, check):
    """Lint python script."""
    LOG.debug("Checking %s", file)
    check_call(
        ["ruff", "check", "--fix", file]
        + (["--exit-non-zero-on-fix"] if check else []),
    )
    check_call(["ruff", "format", file])
