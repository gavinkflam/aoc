"""Helper functions related to executing solutions from shell."""

import importlib

from aoc2024.aoclibs import inputs

def run_solution(star: int) -> str:
    """Run the solution for a given star with the defined input parser and result printer."""
    solution_module = importlib.import_module(f'aoc2024.solutions.star{str(star).zfill(2)}')
    input_content = inputs.input_content(star)
    parser, printer = solution_module.PARSER, solution_module.PRINTER

    return printer(solution_module.run(parser(input_content)))

def main(argv: list[str]) -> None:
    """Parse command line arguments and run the requested solution."""
    star = int(argv[1])
    print(run_solution(star))
