import hashlib
import json
import os
import re
import secrets
import sqlite3
import subprocess
import requests
import yaml
DB_PASSWORD = os.environ.get("DB_PASSWORD")
def get_user(username):
    conn = sqlite3.connect("app.db")
    return conn.execute("SELECT * FROM users WHERE name = ?", (username,)).fetchall()

def ping(host):
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        raise ValueError("Invalid host format")
    return subprocess.run(["ping", "-c", "1", host], check=False)
def hash_password(password, salt=None):
    salt = salt or os.urandom(16)
    digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
    return salt, digest
def make_reset_token():
    return secrets.token_urlsafe(32)
def load_config(text):
    return yaml.safe_load(text)
def load_session(data):
    return json.loads(data)
def fetch(url):
    return requests.get(url, timeout=10)
