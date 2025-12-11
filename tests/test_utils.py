"""Run solutions and compare against the answers."""

import time
from typing import Iterable

from aoclibs import executions, files


def test_solutions(year: int, stars: Iterable[int]):
    """Run solutions with the defined input parser and result printer."""
    for star in stars:
        start_ns = time.time_ns()
        answer = executions.run_solution(year, star)
        took_ms = round((time.time_ns() - start_ns) / 10**6, 2)

        star_text = str(star).rjust(2, "0")
        expected = files.data_file_content(year, "star", star, path_prefix="/tests")
        assert (
            answer == expected
        ), f"{year} star {star_text}: expected {expected}, got {answer}"

        print(f"{year} star {star_text}: correct, took {took_ms}ms", flush=True)
