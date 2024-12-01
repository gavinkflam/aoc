"""Run solutions and compare against the answers."""

import unittest

from aoclibs import executions

class TestSolutions(unittest.TestCase):
    """Run solutions and compare against the answers."""

    def test_solutions(self):
        """Run solutions with the defined input parser and result printer."""
        self.assertEqual('2166959', executions.run_solution(2024, 1))
        self.assertEqual('23741109', executions.run_solution(2024, 2))
