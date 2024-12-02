"""Helper functions related to executing solutions from shell."""

import importlib

from aoclibs import files

def run_solution(year: int, star: int) -> str:
    """Run the solution for a given puzzle with the defined input parser and result printer."""
    solution_module = importlib.import_module(f'aoc{year}.solutions.star{str(star).zfill(2)}')
    input_content = files.data_file_content(year, 'day', (star + 1) // 2)
    parser, printer = solution_module.PARSER, solution_module.PRINTER

    return printer(solution_module.run(parser(input_content)))
