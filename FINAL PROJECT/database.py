# database.py
import sqlite3
import json
from typing import Optional, Tuple
import bcrypt

DB_PATH = "users.db"

def get_connection():
    # check_same_thread=False helps when Streamlit reruns touch the DB from same process
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db(path: str = DB_PATH):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        name TEXT,
        password_hash TEXT,
        verified INTEGER DEFAULT 0,
        verification_code TEXT,
        subscribed INTEGER DEFAULT 0,
        free_uses INTEGER DEFAULT 0
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        predicted TEXT,
        details TEXT,
        herbs TEXT,
        language TEXT,
        timestamp INTEGER
    )
    """)
    conn.commit()
    conn.close()

# -------------------------
# Password helpers (bcrypt)
# -------------------------
def hash_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False

# -------------------------
# User creation & verification
# -------------------------
def create_user(db_path: str, name: str, email: str, password: str) -> Tuple[bool, str]:
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    # create tables if they don't exist (safe)
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        name TEXT,
        password_hash TEXT,
        verified INTEGER DEFAULT 0,
        verification_code TEXT,
        subscribed INTEGER DEFAULT 0,
        free_uses INTEGER DEFAULT 0
    )
    """)
    try:
        pw_hash = hash_password(password)
        c.execute(
            "INSERT INTO users (email, name, password_hash, verified, free_uses) VALUES (?, ?, ?, 0, 0)",
            (email, name, pw_hash)
        )
        conn.commit()
        conn.close()
        return True, "Created"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "An account with that email already exists."

def verify_user_code_in_db(db_path: str, email: str, code: str):
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET verification_code = ? WHERE email = ?", (code, email))
    conn.commit()
    conn.close()

def set_verified(db_path: str, email: str, code_entered: str) -> Tuple[bool, str]:
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT verification_code FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    if not row:
        conn.close()
        return False, "No account found for that email."
    stored_code = row[0]
    if stored_code and stored_code == code_entered:
        c.execute("UPDATE users SET verified = 1, verification_code = NULL, free_uses = 2 WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        return True, "Verified"
    conn.close()
    return False, "Invalid verification code."

# -------------------------
# NEW: mark_user_verified (used by app.py verify flow)
# -------------------------
def mark_user_verified(email: str):
    """Set verified = 1 for a user after they enter the correct 4-digit code."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET verified = 1, verification_code = NULL, free_uses = 2 WHERE email = ?", (email.strip().lower(),))
    conn.commit()
    conn.close()

# -------------------------
# Login verification
# -------------------------
def verify_login(db_path: str, email: str, password: str) -> bool:
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    stored_hash = row[0]
    return verify_password(password, stored_hash)

def get_user_by_email(db_path: str, email: str) -> Optional[dict]:
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT email, name, verified, subscribed, free_uses FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    if not row:
        return None
    return {
        "email": row[0],
        "name": row[1],
        "verified": bool(row[2]),
        "subscribed": bool(row[3]),
        "free_uses": row[4]
    }

# -------------------------
# Utilities: free uses, subscription, history
# -------------------------
def update_free_uses(db_path: str, email: str, free_uses: int):
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET free_uses = ? WHERE email = ?", (int(free_uses), email))
    conn.commit()
    conn.close()

def grant_subscription(db_path: str, email: str):
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET subscribed = 1, free_uses = 999 WHERE email = ?", (email,))
    conn.commit()
    conn.close()

def add_history(db_path: str, email: str, predicted: str, details: dict, herbs: list, language: str, timestamp: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (email, predicted, details, herbs, language, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
        (email, predicted, json.dumps(details), json.dumps(herbs), language, timestamp)
    )
    conn.commit()
    conn.close()

def get_history_for_user(db_path: str, email: str, limit: int = 10):
    email = email.strip().lower()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT predicted, details, herbs, language, timestamp FROM history WHERE email = ? ORDER BY id DESC LIMIT ?", (email, limit))
    rows = c.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append({
            "predicted": r[0],
            "details": json.loads(r[1]) if r[1] else {},
            "herbs": json.loads(r[2]) if r[2] else [],
            "language": r[3],
            "timestamp": r[4]
        })
    return results
