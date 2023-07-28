"""Add "test" action for the "gepetuto" program."""

import logging
import sys
from pathlib import Path
from subprocess import check_call

LOG = logging.getLogger("gepetuto.test")


def test(**kwargs):
    """Test python scripts."""
    LOG.info("testing tutorial sources.")
    for tp_number in range(100):
        LOG.debug(f"Looking for tp {tp_number}")
        folder = Path(f"tp{tp_number}")
        if folder.exists():
            for python_file in folder.glob("*.py"):
                check_call([sys.executable, python_file])
        else:
            if tp_number == 0:
                continue
            break
    LOG.info("test passed.")
