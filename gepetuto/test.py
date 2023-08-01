"""Add "test" action for the "gepetuto" program."""

import logging
import sys
from pathlib import Path
from subprocess import check_call
from typing import List

LOG = logging.getLogger("gepetuto.test")


def test(tp_id: List[int], **kwargs):
    """Test python scripts."""
    LOG.info("testing tutorial sources.")
    for n in tp_id:
        LOG.debug(f"Looking for tp {n}")
        folder = Path(f"tp{n}")
        for python_file in folder.glob("*.py"):
            LOG.debug(f"Checking {python_file}")
            check_call([sys.executable, python_file])
    LOG.info("test passed.")
