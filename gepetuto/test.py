"""Add "test" action for the "gepetuto" program."""

import logging
from pathlib import Path
from subprocess import check_call

LOG = logging.getLogger("gepetuto.test")


def test(files, **kwargs):
    """Test python scripts."""
    python_interpreter = kwargs["python"]
    LOG.info("testing tutorial sources.")
    ipynbs = get_ipynbs(files)
    for tp_number in files.keys():
        for tp_file in files[tp_number]:
            LOG.debug(f"Checking {tp_file}")
            check_call([python_interpreter, tp_file])
    for ipynb_key in ipynbs.keys():
        for ipynb in ipynbs[ipynb_key]:
            check_ipynb(ipynb, ipynb_key, python_interpreter)
    LOG.info("test passed.")


def get_ipynbs(files):
    """Get the dictionary of ipynbs to test."""
    ipynbs = {}
    for ipynb in Path().glob("*.ipynb"):
        if str(ipynb)[0].isdigit():
            tp_number = int(str(ipynb)[0])
            if tp_number in files.keys():
                if tp_number not in ipynbs.keys():
                    ipynbs[tp_number] = [ipynb]
                else:
                    ipynbs[tp_number].append(ipynb)
        else:
            if "appendix" not in ipynbs.keys():
                ipynbs["appendix"] = [ipynb]
            else:
                ipynbs["appendix"].append(ipynb)
    return ipynbs


def check_ipynb(ipynb, ipynb_key, python_interpreter):
    """Check .ipynb files from given tp_number."""
    check_call(["jupyter", "nbconvert", "--to", "script", f"{ipynb}"])
    converted_ipynb = next(Path().glob(f"{ipynb_key}_*.py"))
    LOG.debug(f"Checking temporary file {converted_ipynb}")
    check_call([python_interpreter, converted_ipynb])
    Path.unlink(converted_ipynb)
