import sqlite3
import os
from datetime import datetime

os.makedirs("database", exist_ok=True)

DB_PATH = "database/pusti_tusti.db"


def save_record(student, foods, nutrition):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            foods TEXT,
            calories INTEGER,
            protein INTEGER,
            date TEXT
        )
    ''')

    cur.execute('''
        INSERT INTO records
        (student_name, foods, calories, protein, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        student['name'],
        ', '.join(foods),
        nutrition['calories'],
        nutrition['protein'],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()