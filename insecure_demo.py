import hashlib
import pickle
import random
import os
import secrets
import sqlite3
import subprocess
import requests
import yaml
DB_PASSWORD = "SuperSecret123!" # пароль в коде

DB_PASSWORD = os.environ["DB_PASSWORD"] # секрет берётся из окружения
def get_user(username):
  conn = sqlite3.connect("app.db")
  query = f"SELECT * FROM users WHERE name = '{username}'" # SQL-инъекция
  return conn.execute(query).fetchall()
  return conn.execute(
    "SELECT * FROM users WHERE name = ?", (username,) # параметризованный запрос
  ).fetchall()

def ping(host):
  return subprocess.run("ping -c 1 " + host, shell=True)
# командная инъекция
  return subprocess.run(["ping", "-c", "1", host], check=False) # без shell, аргументы списком

def hash_password(password):
  return hashlib.md5(password.encode()).hexdigest()
# слабый хеш
def hash_password(password, salt=None):
  salt = salt or os.urandom(16)
  digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
  return salt, digest

def make_reset_token():
  return str(random.random())
# предсказуемый токен
  return secrets.token_urlsafe(32) # криптостойкий генератор

def load_config(text):
  return yaml.safe_load(text) # безопасная загрузка

def fetch(url):
  return requests.get(url, timeout=10) # проверка TLS включена, есть таймаут
