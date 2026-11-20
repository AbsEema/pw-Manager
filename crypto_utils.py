from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

SALT_FILE = "salt.bin"

def get_or_create_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt

def derive_key(master_password: str) -> bytes:
    """Deriva una clave Fernet a partir de la Password Maestra"""
    salt = get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def encrypt_data(data: str, master_password: str)-> bytes:
    key = derive_key(master_password)
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(encrypted: bytes, master_password: str)-> str:
    key = derive_key(master_password)
    f = Fernet(key)
    return f.decrypt(encrypted).decode() 