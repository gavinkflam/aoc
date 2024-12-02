"""Helper functions related to resource file manipulation."""

import glob
import os.path
from pathlib import Path

import cryptocode

PROJECT_DIR = os.path.abspath(str(Path(__file__).parent.absolute()) + '/..')

def encrypt_file(key: str, filepath: str) -> None:
    """Encrypt the content of a file and save it as a .enc file."""
    content = Path(filepath).read_text(encoding='utf-8')
    parent_path, filename = str(Path(filepath).parent.absolute()), Path(filepath).stem
    enc_filepath = f'{parent_path}/{filename}.enc'

    if os.path.exists(enc_filepath):
        return

    with open(enc_filepath, 'w', encoding='utf-8') as enc_file:
        print(cryptocode.encrypt(content, key), file=enc_file, end='')

def decrypt_file(key: str, filepath: str) -> None:
    """Decrypt the content of an encrypted file and save it as a new file."""
    encrypted_content = Path(filepath).read_text(encoding='utf-8')
    parent_path, filename = str(Path(filepath).parent.absolute()), Path(filepath).stem

    with open(f'{parent_path}/{filename}.txt', 'w', encoding='utf-8') as enc_file:
        decrypted_content = cryptocode.decrypt(encrypted_content, key)
        if not decrypted_content:
            raise ValueError('Incorrect encryption key.')

        print(decrypted_content, file=enc_file, end='')

def encrypt_files(key: str) -> None:
    """Encrypt all data files in the project and save them as .enc files."""
    for filepath in glob.glob(f'{PROJECT_DIR}/**/data/*.txt', recursive=True):
        encrypt_file(key, filepath)

def decrypt_files(key: str) -> None:
    """Decrypt all encrypted data files in the project and save them as .txt files."""
    for filepath in glob.glob(f'{PROJECT_DIR}/**/data/*.enc', recursive=True):
        decrypt_file(key, filepath)

def data_file_content(year: int, file_prefix: str, file_number: int, path_prefix: str = '') -> str:
    """Read the content of a data file."""
    filename = f'{file_prefix}{str(file_number).zfill(2)}.txt'
    return Path(f'{PROJECT_DIR}{path_prefix}/aoc{year}/data/{filename}').read_text(encoding='utf-8')
