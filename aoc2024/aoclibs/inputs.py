"""Helper functions related to input files manipulation."""

from os.path import abspath
from pathlib import Path

INPUT_DIR = abspath(str(Path(__file__).parent.absolute()) + '/../inputs')

def input_content(star: int) -> str:
    """Read the content of the input file for the given puzzle."""
    return Path(f'{INPUT_DIR}/star{str(star).zfill(2)}.txt').read_text(encoding='utf-8')

def parse_int_grid(lines: str) -> list[list[int]]:
    """Parse the given string as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in lines.splitlines()]
