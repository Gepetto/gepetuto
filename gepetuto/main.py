"""Gepetuto main program source code."""

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


def parse_args(args=None) -> argparse.Namespace:
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
        "-f",
        "--file",
        default=[],
        type=str,
        nargs="*",
        help="choose which files to process.",
    )
    parser.add_argument(
        "-F",
        "--filter",
        default=[],
        type=str,
        nargs="*",
        help="filter files to process.",
    )
    parser.add_argument(
        "tp_id",
        default=[],
        type=int,
        nargs="*",
        help="choose which tp to process. Default to all.",
    )
    parser.add_argument(
        "-p",
        "--python",
        default=retrieve_python_interpreter(),
        help="choose python interpreter to use.",
    )

    args = parser.parse_args(args=args)

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


def retrieve_python_interpreter():
    """Retrieve installed python interpreter."""
    try:
        check_call(["python3", "--version"])
        return "python3"
    except FileNotFoundError:
        try:
            check_call(["python", "--version"])
            return "python"
        except FileNotFoundError:
            LOG.warn(
                "Didn't found 'python3' or 'python' executable, using ",
                sys.executable,
            )
            return sys.executable


def get_file_list(args):
    """Get the list of files we use action on."""
    if args.tp_id == []:
        get_tp_id()
    if args.file != []:
        [Path(f) for f in args.file]
    file_list = []
    for n in args.tp_id:
        folder = Path(f"tp{n}")
        tp_files = folder.glob("*.py")
        if args.file != []:
            tp_files = [f for f in tp_files if f in args.file]
        if args.filter != []:
            tp_files = [
                f
                for f in tp_files
                if any(filter_str in str(f) for filter_str in args.filter)
            ]
        file_list += tp_files
    return file_list


def main():
    """Run command."""
    args = parse_args()
    files = get_file_list(args)
    if args.action == "generate":
        generate(**vars(args))
    elif args.action == "lint":
        lint(files, **vars(args))
    elif args.action == "test":
        test(files, **vars(args))
    elif args.action == "all":
        LOG.debug("no action specified, running all 3.")
        lint(files, **vars(args))
        test(files, **vars(args))
        generate(**vars(args))
