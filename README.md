# 🎄 Advent of Code

My solutions of the [Advent of Code](https://adventofcode.com/) coding puzzles.

## Setup

1. Install Python 3 using [asdf](https://asdf-vm.com/guide/getting-started.html), or using your favorite package manager / version management system.
2. Install virtualenv, e.g. `pip install virtualenv`.
3. Create virtualenv, e.g. `virtualenv .venv`.
4. Activate virtualenv, e.g. `source .venv/bin/activiate`.
5. Install dependencies.
    - `pip install -r requirements.txt`
    - `pip install -r requirements-dev.txt`.

## Data files

Input and answer files are encrypted because Advent of Code states that inputs should not be shared.

### Decrypt data files

1. Export encryption key, e.g. `export AOC_ENC_KEY='hello_world'`.
2. Decrypt all data files using `python -m aoclibs decrypt_files`

### Encrypt data files

1. Export encryption key, e.g. `export AOC_ENC_KEY='hello_world'`.
2. Encrypt all data files using `python -m aoclibs encrypt_files`

## Run

Example: `python -m aoclibs run 2024 1`

## Development

### Tests

`python -m unittest`

### Formatting

Use [Black](https://github.com/psf/black) to auto-format code.

`black $(git ls-files '*.py')`

### Linting

`pylint $(git ls-files '*.py')`

## License

MIT
