"""Main gepetuto program.

This can be started with `python -m gepetuto`, or simply `gepetuto`.
"""

import argparse
import logging
import os
import pathlib
import sys

from .generate import generate
from .lint import lint
from .test import test

LOG = logging.getLogger("gepetuto")


def parse_args() -> argparse.Namespace:
    """Check what the user want."""
    # Get current interpreter
    python = pathlib.Path(sys.executable)
    if str(python.parent) in os.environ.get("PATH", "").split(os.pathsep):
        # its path is in PATH: no need for absolute path
        python = pathlib.Path(python.name)

    parser = argparse.ArgumentParser(
        prog=f"{python} -m gepetuto",
        description="gepetuto tools",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increment verbosity level",
    )

    parser.add_argument("action", choices=["lint", "test", "generate"], nargs="?")

    args = parser.parse_args()

    if args.verbose == 0:
        level = os.environ.get("GEPETUTO_LOG_LEVEL", "WARNING")
    else:
        level = 30 - 10 * args.verbose
    logging.basicConfig(level=level)

    LOG.debug("parsed arguments :%s", args)

    return args


def main():
    """Run command."""
    args = parse_args()
    if args.action == "generate":
        generate(**vars(args))
    elif args.action == "lint":
        lint(**vars(args))
    elif args.action == "test":
        test(**vars(args))
    else:
        LOG.debug("no action specified, running all 3.")
        lint(**vars(args))
        test(**vars(args))
        generate(**vars(args))


if __name__ == "__main__":
    main()
