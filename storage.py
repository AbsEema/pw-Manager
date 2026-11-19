import json
import os

DATA_FILE = "passwords.json"

def load_passwords():
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_passwords(passwords):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(passwords, f, indent=2, ensure_ascii=False)

def add_passwords(site, username, password):
    passwords = load_passwords()
    passwords.append({
        "site": site,
        "username": username,
        "password": password
    })
    save_passwords(passwords)