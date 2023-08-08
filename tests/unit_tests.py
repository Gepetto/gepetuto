"""Unit tests for gepetuto."""
import unittest
from pathlib import Path

from gepetuto.main import get_file_list, parse_args


class TestGepetutoArguments(unittest.TestCase):
    """Class with all unit tests for gepetuto arguments."""

    def test_no_arg(self):
        """Check files we work on when no arguments are given."""
        arguments = parse_args()
        file_list = get_file_list(arguments.tp_id, arguments.file)
        self.assertTrue(Path("tp1/cholesky.py") in file_list)
        self.assertTrue(Path("tp1/example_script.py") in file_list)
        self.assertTrue(Path("tp2/cholesky.py") in file_list)
        self.assertTrue(Path("tp2/another_script.py") in file_list)

    def test_tp_id_1(self):
        """Check files we work on when we specify tp_id = 1."""
        arguments = parse_args(["1"])
        file_list = get_file_list(arguments.tp_id, arguments.file)
        self.assertTrue(Path("tp1/cholesky.py") in file_list)
        self.assertTrue(Path("tp1/example_script.py") in file_list)
        self.assertTrue(Path("tp2/cholesky.py") not in file_list)
        self.assertTrue(Path("tp2/another_script.py") not in file_list)

    def test_file_cholesky(self):
        """Check files we work on when we specify a file with --file."""
        arguments = parse_args(["--file", "tp1/cholesky.py"])
        file_list = get_file_list(arguments.tp_id, arguments.file)
        self.assertTrue(Path("tp1/cholesky.py") in file_list)
        self.assertTrue(Path("tp1/example_script.py") not in file_list)
        self.assertTrue(Path("tp2/cholesky.py") not in file_list)
        self.assertTrue(Path("tp2/another_script.py") not in file_list)

    def test_tp_id_1_file_cholesky(self):
        """Check files we work on when we specify tp_id = 1 and a file in tp1 folder."""
        arguments = parse_args(["1", "--file", "tp1/cholesky.py"])
        file_list = get_file_list(arguments.tp_id, arguments.file)
        self.assertTrue(Path("tp1/cholesky.py") in file_list)
        self.assertTrue(Path("tp1/example_script.py") not in file_list)
        self.assertTrue(Path("tp2/cholesky.py") not in file_list)
        self.assertTrue(Path("tp2/another_script.py") not in file_list)

    def test_no_file_matching(self):
        """Check files we work on when tp_id and --file has no files in common."""
        arguments = parse_args(["2", "--file", "tp1/cholesky.py"])
        file_list = get_file_list(arguments.tp_id, arguments.file)
        self.assertTrue(Path("tp1/cholesky.py") not in file_list)
        self.assertTrue(Path("tp1/example_script.py") not in file_list)
        self.assertTrue(Path("tp2/cholesky.py") not in file_list)
        self.assertTrue(Path("tp2/another_script.py") not in file_list)


if __name__ == "__main__":
    unittest.main()
