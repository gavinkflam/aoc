"""Run solutions and compare against the answers."""

import unittest

from aoclibs import executions, files


class TestSolutions(unittest.TestCase):
    """Run solutions and compare against the answers."""

    def test_solutions(self):
        """Run solutions with the defined input parser and result printer."""
        for star in range(1, 5):
            answer = files.data_file_content(2024, "star", star, path_prefix="/tests")
            self.assertEqual(answer, executions.run_solution(2024, star))
