"""Add "test" action for the "gepetuto" program."""

import logging
import os
from pathlib import Path
from subprocess import check_call

LOG = logging.getLogger("gepetuto.test")


def test(**kwargs):
    """Test python scripts."""
    LOG.info("testing tutorial sources.")
    for tp_number in range(100):
        LOG.debug(f"Looking for tp {tp_number}")
        folder = Path() / f"tp{tp_number}"
        if Path.exists(folder):
            folder_files = os.listdir(folder)
            folder_python_files = list(filter(lambda file: ".py" in file, folder_files))
            for python_file in folder_python_files:
                check_call(["python", folder / python_file])
        else:
            if tp_number == 0:
                continue
            break
    LOG.info("test passed.")
