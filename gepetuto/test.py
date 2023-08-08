"""Add "test" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call

LOG = logging.getLogger("gepetuto.test")


def test(files, **kwargs):
    """Test python scripts."""
    python_interpreter = kwargs["python"]
    LOG.info("testing tutorial sources.")
    tp_id = int(str(files[0])[2])  # get the tp id of the first file
    check_ipynb(tp_id, python_interpreter)
    for f in files:
        LOG.debug(f"Checking {f}")
        check_call([python_interpreter, f])
        current_tp_id = int(str(f)[2])
        if tp_id != current_tp_id:
            tp_id = current_tp_id
            check_ipynb(current_tp_id, python_interpreter)
    LOG.info("test passed.")


def check_ipynb(tp_number, python_interpreter):
    """Check .ipynb files from given tp_number."""
    ipynb = next(Path().glob(f"{tp_number}_*.ipynb"))
    check_call(["jupyter", "nbconvert", "--to", "script", f"{ipynb}"])
    converted_ipynb = next(Path().glob(f"{tp_number}_*.py"))
    LOG.debug(f"Checking temporary file {converted_ipynb}")
    check_call([python_interpreter, converted_ipynb])
    Path.unlink(converted_ipynb)
