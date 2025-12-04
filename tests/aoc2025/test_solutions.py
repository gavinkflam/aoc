"""Test solutions of the year 2025."""

import unittest

from tests import test_utils


class TestSolutions(unittest.TestCase):
    """Run solutions and compare against the answers."""

    def test_2025_solutions(self):
        """Run solutions and compare against the answers."""
        test_utils.test_solutions(2025, 8)
