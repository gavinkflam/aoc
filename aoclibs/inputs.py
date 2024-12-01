"""Helper functions related to input files manipulation."""

from os import path
from pathlib import Path

PROJECT_DIR = path.abspath(str(Path(__file__).parent.absolute()) + '/..')

def input_content(year: int, star: int) -> str:
    """Read the content of the input file for the given puzzle."""
    filename = f'day{str((star + 1) // 2).zfill(2)}.txt'
    return Path(f'{PROJECT_DIR}/aoc{year}/inputs/{filename}').read_text(encoding='utf-8')

def parse_int_grid(lines: str) -> list[list[int]]:
    """Parse the given string as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in lines.splitlines()]
