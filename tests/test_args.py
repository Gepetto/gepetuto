"""Unit tests for gepetuto."""
import unittest
from pathlib import Path

from gepetuto.main import get_files, parse_args


class TestGepetutoArguments(unittest.TestCase):
    """Class with all unit tests for gepetuto arguments."""

    def test_no_arg(self):
        """Check files we work on when no arguments are given."""
        arguments = parse_args()
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") in file_list[1])
        self.assertTrue(Path("tp2/cholesky.py") in file_list[2])
        self.assertTrue(Path("tp2/another_script.py") in file_list[2])

    def test_tp_id_1(self):
        """Check files we work on when we specify tp_id = 1."""
        arguments = parse_args(["1"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") in file_list[1])
        self.assertTrue(2 not in file_list.keys())

    def test_file_cholesky(self):
        """Check files we work on when we specify a file with --file."""
        arguments = parse_args(["--file", "tp1/cholesky.py"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") not in file_list[1])
        self.assertTrue(2 not in file_list.keys())

    def test_tp_id_1_file_cholesky(self):
        """Check files we work on when we specify tp_id = 1 and a file in tp1 folder."""
        arguments = parse_args(["1", "--file", "tp1/cholesky.py"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") not in file_list[1])
        self.assertTrue(2 not in file_list.keys())

    def test_no_file_matching(self):
        """Check files we work on when tp_id and --file has no files in common."""
        arguments = parse_args(["2", "--file", "tp1/cholesky.py"])
        file_list = get_files(arguments)
        self.assertTrue(1 not in file_list.keys())
        self.assertTrue(2 not in file_list.keys())

    def test_filter_cholesky(self):
        """Check files we work on with --filter cholesky argument."""
        arguments = parse_args(["--filter", "cholesky"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") not in file_list[1])
        self.assertTrue(Path("tp2/cholesky.py") in file_list[2])
        self.assertTrue(Path("tp2/another_script.py") not in file_list[2])

    def test_tp_id_1_filter_cholesky(self):
        """Check files we work on with --filter cholesky argument."""
        arguments = parse_args(["1", "--filter", "cholesky"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") not in file_list[1])
        self.assertTrue(2 not in file_list.keys())

    def test_file_cholesky_filter_cholesky(self):
        """Check files we work on with --filter cholesky and --file on cholesky file."""
        arguments = parse_args(["--file", "tp1/cholesky.py", "--filter", "cholesky"])
        file_list = get_files(arguments)
        self.assertTrue(Path("tp1/cholesky.py") in file_list[1])
        self.assertTrue(Path("tp1/example_script.py") not in file_list[1])
        self.assertTrue(2 not in file_list.keys())

    def test_no_file_matching_2(self):
        """Check files we work on when --file and --filter has no files in common."""
        arguments = parse_args(
            ["--file", "tp1/example_script.py", "--filter", "cholesky"],
        )
        file_list = get_files(arguments)
        self.assertTrue(1 not in file_list.keys())
        self.assertTrue(2 not in file_list.keys())


if __name__ == "__main__":
    unittest.main()
