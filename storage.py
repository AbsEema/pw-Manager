import json
import os
from crypto_utils import encrypt_data, decrypt_data

ENCRYPTED_FILE = "password.enc"

def load_passwords(master_password: str):
    if not os.path.exists(ENCRYPTED_FILE):
        return[]
    with open(ENCRYPTED_FILE, "rb") as f:
        encrypted= f.read()
    try:
        decrypted = decrypt_data(encrypted, master_password)
        return json.loads(decrypted)
    except Exception:
        return None #Password erronia

def save_passwords(passwords, master_password: str):
    data = json.dumps(passwords, ensure_ascii=False)
    encrypted = encrypt_data(data, master_password)
    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted)

def add_passwords(site, username, password, master_password):
    passwords = load_passwords(master_password) or []
    passwords.append({
        "site": site,
        "username": username,
        "password": password
    })
    save_passwords(passwords, master_password)