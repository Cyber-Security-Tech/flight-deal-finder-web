import sqlite3
from datetime import datetime

DB_NAME = "searches.db"

# Create the database and table if not exist
def initialize_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                max_price REAL NOT NULL,
                date_searched TEXT NOT NULL
            )
        ''')
        conn.commit()

# Add a new search entry
def log_search(origin, destination, max_price):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO searches (origin, destination, max_price, date_searched)
            VALUES (?, ?, ?, ?)
        ''', (origin, destination, max_price, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
def get_all_searches():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT origin, destination, max_price, date_searched FROM searches ORDER BY id DESC")
        return cursor.fetchall()
