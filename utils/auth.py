from flask_login import UserMixin
from utils.db import get_connection

class User(UserMixin):
    def __init__(self, id):
        self.id = id

def get_user(username):
    """Retrieves a user from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"username": row[0], "password": row[1]}
    return None

def create_user(username, password):
    """Creates a new user in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()