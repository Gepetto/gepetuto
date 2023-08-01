"""Add "test" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call
from typing import List

LOG = logging.getLogger("gepetuto.test")


def test(tp_id: List[int], **kwargs):
    """Test python scripts."""
    python_version = kwargs["python"]
    LOG.info("testing tutorial sources.")
    for n in tp_id:
        LOG.debug(f"Looking for tp {n}")
        folder = Path(f"tp{n}")
        for python_file in folder.glob("*.py"):
            LOG.debug(f"Checking {python_file}")
            check_call([python_version, python_file])
            check_ipynb(n, python_version)
    LOG.info("test passed.")


def check_ipynb(tp_number, python_version):
    """Check .ipynb files from given tp_number and move it in temporary folder."""
    ipynb = next(Path().glob(f"{tp_number}_*.ipynb"))
    check_call(["jupyter", "nbconvert", "--to", "script", f"{ipynb}"])
    converted_ipynb = next(Path().glob(f"{tp_number}_*.py"))
    LOG.debug(f"Checking temporary file {converted_ipynb}")
    check_call([python_version, converted_ipynb])
    Path.unlink(converted_ipynb)
