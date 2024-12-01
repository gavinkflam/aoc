"""Helper functions related to executing solutions from shell."""

from aoclibs import inputs
from solutions import star01, star02

SOLUTIONS = {
    1: star01,
    2: star02,
}

PARSERS = {
    1: inputs.parse_int_grid,
    2: inputs.parse_int_grid,
}

PRINTERS = {
    1: str,
    2: str,
}

def run_solution(star: int) -> str:
    """Run the solution for a given star with the defined input parser and result printer."""
    input_content = inputs.input_for_star(star)
    solution, parser, printer = SOLUTIONS[star], PARSERS[star], PRINTERS[star]
    return printer(solution.run(parser(input_content)))

def main(argv: list[str]) -> None:
    """Parse command line arguments and run the requested solution."""
    star = int(argv[1])
    print(run_solution(star))
