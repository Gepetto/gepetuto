"""Add "test" action for the "gepetuto" program."""

import logging
from collections import defaultdict
from pathlib import Path
from subprocess import check_call

from .generate import generate_ipynb

LOG = logging.getLogger("gepetuto.test")


def test(files, **kwargs):
    """Test python scripts."""
    python_interpreter = kwargs["python"]
    LOG.info("testing tutorial sources.")
    for tp_files in files.values():
        for tp_file in tp_files:
            LOG.debug("Checking %s", tp_file)
            check_call([python_interpreter, tp_file])
    ipynbs = get_ipynbs(files, kwargs["directory"])
    for tp_ipynbs in ipynbs.values():
        for tp_ipynb in tp_ipynbs:
            check_ipynb(tp_ipynb, python_interpreter, kwargs["directory"])
    LOG.info("test passed.")


def get_ipynbs(files, directory):
    """Get the dictionary of ipynbs to test."""
    ipynbs = defaultdict(list)
    for ipynb in Path(directory).glob("*.ipynb"):
        prefix = ipynb.name.split("-")[0]
        if prefix.isdecimal():
            if int(prefix) in files.keys():
                ipynbs[prefix].append(ipynb)
        else:
            ipynbs[prefix].append(ipynb)
    return ipynbs


def check_ipynb(ipynb, python_interpreter, directory):
    """Check .ipynb files from given tp_number."""
    prefix = ipynb.name.split("-")[0]
    tp_path = Path(directory)
    tp_path = tp_path / f"tp{prefix}" if prefix.isdecimal() else tp_path / prefix
    if tp_path.exists():
        generate_ipynb(ipynb, tp_path, True)
    check_call(["jupyter", "nbconvert", "--to", "script", f"{ipynb}"])
    converted_ipynb = next(Path(directory).glob(f"{prefix}-*.py"))
    LOG.debug("Checking temporary file %s", converted_ipynb)
    check_call([python_interpreter, converted_ipynb])
    Path.unlink(converted_ipynb)
