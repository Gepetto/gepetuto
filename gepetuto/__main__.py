"""Main gepetuto program.

This can be started with `python -m gepetuto`, or simply `gepetuto`.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from subprocess import check_call

from .generate import generate
from .lint import lint
from .test import test

LOG = logging.getLogger("gepetuto")


def parse_args() -> argparse.Namespace:
    """Check what the user want."""
    parser = argparse.ArgumentParser(prog="gepetuto", description="gepetuto tools")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increment verbosity level",
    )
    parser.add_argument(
        "-a",
        "--action",
        default="generate",
        choices=["lint", "test", "generate", "all"],
        nargs="?",
        help="choose what to do. Default to 'generate'.",
    )
    parser.add_argument(
        "tp_id",
        default=get_tp_id(),
        type=int,
        nargs="*",
        help="choose which tp to process. Default to all.",
    )
    parser.add_argument(
        "-p",
        "--python",
        default=retrieve_python_version(),
        help="choose python version to use.",
    )

    args = parser.parse_args()

    if args.verbose == 0:
        level = os.environ.get("GEPETUTO_LOG_LEVEL", "WARNING")
    else:
        level = 30 - 10 * args.verbose
    logging.basicConfig(level=level)

    LOG.debug("parsed arguments: %s", args)

    return args


def get_tp_id():
    """Find tp to process."""
    tp_id = []
    current_tp_id = 0
    while True:
        folder = Path(f"tp{current_tp_id}")
        if folder.exists():
            tp_id.append(current_tp_id)
        elif current_tp_id != 0:
            return tp_id
        current_tp_id += 1


def retrieve_python_version():
    """Retrieve installed python version."""
    try:
        check_call(["python3", "--version"])
        return "python3"
    except FileNotFoundError:
        try:
            check_call(["python", "--version"])
            return "python"
        except FileNotFoundError:
            LOG.warn("Didn't found python executable, using ", sys.executable)
            return sys.executable


def main():
    """Run command."""
    args = parse_args()
    if args.action == "generate":
        generate(**vars(args))
    elif args.action == "lint":
        lint(**vars(args))
    elif args.action == "test":
        test(**vars(args))
    elif args.action == "all":
        LOG.debug("no action specified, running all 3.")
        lint(**vars(args))
        test(**vars(args))
        generate(**vars(args))


if __name__ == "__main__":
    main()
