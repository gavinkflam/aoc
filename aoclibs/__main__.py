"""Entry point to run solutions from shell."""

import os
import sys

from aoclibs import executions, files

match sys.argv[1]:
    case 'decrypt_files':
        files.decrypt_files(os.environ['AOC_ENC_KEY'])
    case 'encrypt_files':
        files.encrypt_files(os.environ['AOC_ENC_KEY'])
    case 'run':
        year, star = int(sys.argv[2]), int(sys.argv[3])
        print(executions.run_solution(year, star))
    case _:
        print(f'Unknown command {sys.argv[1]}')
