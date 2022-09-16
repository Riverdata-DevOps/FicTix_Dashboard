# Bibliotecas para a WEB API
from libraries import *

# Função para download do banco de dados como pdf
def create_download_link(path, filename):
    with open(path, 'rb') as f:
        val = f.read()
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Fazer Download do Arquivo</a>'


# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
