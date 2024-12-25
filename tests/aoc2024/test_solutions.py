"""Run solutions and compare against the answers."""

import timeit
import unittest

from aoclibs import executions, files


class TestSolutions(unittest.TestCase):
    """Run solutions and compare against the answers."""

    # pylint: disable=cell-var-from-loop
    def test_2024_solutions(self):
        """Run solutions with the defined input parser and result printer."""
        for star in range(1, 51):
            answer = files.data_file_content(2024, "star", star, path_prefix="/tests")
            time = timeit.timeit(
                lambda: self.assertEqual(answer, executions.run_solution(2024, star)),
                number=1,
            )
            star_text = str(star).rjust(2, "0")
            ms = round(time * 1000, 2)

            print(f"2024 star {star_text}: {ms}ms", flush=True)
