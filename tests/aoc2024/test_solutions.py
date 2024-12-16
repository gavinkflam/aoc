"""Run solutions and compare against the answers."""

import timeit
import unittest

from aoclibs import executions, files


class TestSolutions(unittest.TestCase):
    """Run solutions and compare against the answers."""

    # pylint: disable=cell-var-from-loop
    def test_solutions(self):
        """Run solutions with the defined input parser and result printer."""
        for star in range(1, 33):
            answer = files.data_file_content(2024, "star", star, path_prefix="/tests")
            time = timeit.timeit(
                lambda: self.assertEqual(answer, executions.run_solution(2024, star)),
                number=1,
            )
            ms = round(time * 1000, 2)

            print(f"Solution for star {star} took {ms}ms to finish")
