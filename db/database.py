import sys
import os
import sqlite3

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


db_path = "game.db"
db = sqlite3.connect(db_path, check_same_thread=False)
cursor = db.cursor()


def init_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            firstname TEXT
        )
    ''')
    db.commit()

def add_user_if_not_exists(user_id, username, firstname):
    print(f"Checking if user exists: {user_id}, {username}, {firstname}")
    cursor.execute('SELECT id FROM users WHERE id = ?', (user_id,))
    if cursor.fetchone() is None:
        print(f"Adding new user: {user_id}, {username}, {firstname}")
        cursor.execute('INSERT INTO users (id, username, firstname) VALUES (?, ?, ?)',
                       (user_id, username, firstname))
        db.commit()
