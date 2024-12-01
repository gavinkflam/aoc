"""Helper functions related to executing solutions from shell."""

import importlib

from aoclibs import inputs

def run_solution(year: int, star: int) -> str:
    """Run the solution for a given puzzle with the defined input parser and result printer."""
    solution_module = importlib.import_module(f'aoc{year}.solutions.star{str(star).zfill(2)}')
    input_content = inputs.input_content(year, star)
    parser, printer = solution_module.PARSER, solution_module.PRINTER

    return printer(solution_module.run(parser(input_content)))

def main(argv: list[str]) -> None:
    """Parse command line arguments and run the requested solution."""
    year, star = int(argv[1]), int(argv[2])
    print(run_solution(year, star))
