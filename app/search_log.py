"""
Handles local logging of user flight searches using SQLite.
Creates, inserts, and retrieves search history entries from the database.
"""

import sqlite3
from datetime import datetime
import os
from flask import current_app

# Default database name; can be overridden using Flask config
DB_NAME = os.path.join("instance", "searches.db")


def initialize_db():
    """
    Initializes the SQLite database by creating the 'searches' table if it doesn't exist.
    """
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


def log_search(origin, destination, max_price):
    """
    Inserts a new flight search record into the database.

    Args:
        origin (str): IATA code of the origin city.
        destination (str): IATA code of the destination city.
        max_price (float): Maximum price for the search query.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO searches (origin, destination, max_price, date_searched)
            VALUES (?, ?, ?, ?)
        ''', (
            origin,
            destination,
            max_price,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ))
        conn.commit()


def get_all_searches():
    """
    Retrieves all logged flight search records from the database, ordered by most recent.

    Returns:
        list of tuple: Each tuple contains origin, destination, max_price, and date_searched.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT origin, destination, max_price, date_searched
            FROM searches
            ORDER BY id DESC
        ''')
        return cursor.fetchall()
