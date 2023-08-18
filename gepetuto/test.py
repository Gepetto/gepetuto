"""Add "test" action for the "gepetuto" program."""

import logging
import tempfile
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
            check_call([python_interpreter, str(tp_file)])
    tmp_dir = tempfile.TemporaryDirectory()
    ipynbs = get_ipynbs(files)
    for tp_ipynbs in ipynbs.values():
        for tp_ipynb in tp_ipynbs:
            check_ipynb(tp_ipynb, python_interpreter, tmp_dir)
    LOG.info("test passed.")


def get_ipynbs(files):
    """Get the dictionary of ipynbs to test."""
    ipynbs = defaultdict(list)
    for ipynb in Path().glob("*.ipynb"):
        prefix = str(ipynb).split("-")[0]
        if prefix.isdecimal():
            if int(prefix) in files.keys():
                ipynbs[prefix].append(ipynb)
        else:
            ipynbs[prefix].append(ipynb)
    return ipynbs


def check_ipynb(ipynb, python_interpreter, tmp_dir):
    """Check .ipynb files from given tp_number."""
    prefix = str(ipynb).split("-")[0]
    tp_path = Path(f"tp{prefix}" if prefix.isdecimal() else prefix)
    check_call(["cp", f"{ipynb}", tmp_dir.name])
    ipynb_copy = next(Path(tmp_dir.name).glob(f"{prefix}-*.ipynb"))
    if tp_path.exists():
        generate_ipynb(ipynb_copy, tp_path, True)
    check_call(["jupyter", "nbconvert", "--to", "script", ipynb_copy])
    converted_ipynb = next(Path(tmp_dir.name).glob(f"{prefix}-*.py"))
    LOG.debug("Checking temporary file %s", converted_ipynb)
    check_call([python_interpreter, converted_ipynb])
