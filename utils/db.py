import sqlite3
import os

DB_NAME = "database.db"

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initializes the database and creating fresh tables if they don't exist."""
    
    conn = get_connection()
    cursor = conn.cursor()

    # Create the business_data table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS business_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        date TEXT,
        revenue REAL,
        expenses REAL,
        inventory_cost REAL,
        category TEXT
    )
    """)

    # Create the users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_record(user_id, date, revenue, expenses, inventory_cost, category="General"):
    """Inserts a new financial record into the database."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO business_data (user_id, date, revenue, expenses, inventory_cost, category)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, date, revenue, expenses, inventory_cost, category))

    conn.commit()
    conn.close()

def get_all_records(user_id):
    """Retrieves all records for a specific user from the database."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT date, revenue, expenses, inventory_cost, category FROM business_data WHERE user_id = ? ORDER BY date ASC", (user_id,))
    rows = cur.fetchall()

    conn.close()
    return rows

# Create/Initialize table automatically when the module is imported
init_db()