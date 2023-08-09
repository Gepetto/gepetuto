"""Add "test" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call

LOG = logging.getLogger("gepetuto.test")


def test(files, **kwargs):
    """Test python scripts."""
    python_interpreter = kwargs["python"]
    LOG.info("testing tutorial sources.")
    for tp_number in files.keys():
        for tp_file in files[tp_number]:
            LOG.debug(f"Checking {tp_file}")
            check_call([python_interpreter, tp_file])
        check_ipynb(tp_number, python_interpreter)
    LOG.info("test passed.")


def check_ipynb(tp_number, python_interpreter):
    """Check .ipynb files from given tp_number."""
    ipynb = next(Path().glob(f"{tp_number}_*.ipynb"))
    check_call(["jupyter", "nbconvert", "--to", "script", f"{ipynb}"])
    converted_ipynb = next(Path().glob(f"{tp_number}_*.py"))
    LOG.debug(f"Checking temporary file {converted_ipynb}")
    check_call([python_interpreter, converted_ipynb])
    Path.unlink(converted_ipynb)
