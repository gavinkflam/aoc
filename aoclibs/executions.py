"""Helper functions related to executing solutions from shell."""

from dataclasses import dataclass
import importlib
from typing import Any, Callable

from aoclibs import files


@dataclass
class SolutionModule:
    """A data class to represent a puzzle solution."""

    run: Callable[[Any], Any]
    parser: Callable[[str], Any] = str
    printer: Callable[[Any], str] = str


def run_solution(year: int, star: int) -> str:
    """Run the solution for a given puzzle with the defined input parser and result printer."""
    module_name = f"aoc{year}.solutions.star{str(star).zfill(2)}"
    solution_module = importlib.import_module(module_name).solution

    input_content = files.data_file_content(year, "day", (star + 1) // 2)
    return solution_module.printer(
        solution_module.run(solution_module.parser(input_content))
    )
