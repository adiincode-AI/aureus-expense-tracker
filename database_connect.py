import sqlite3
import os


def connect_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "aureus_database.db")
    return sqlite3.connect(db_path)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS expensesdb(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    amount REAL NOT NULL,
                    date TEXT,
                    note TEXT
                )
            """)

    conn.commit()
    conn.close()


def insert_value(category, amount, date, note, ):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT into expensesdb(category, amount, date, note) VALUES (?,?,?,?)",
        (category, amount, date, note)
    )
    conn.commit()
    conn.close()


def view_value():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expensesdb")
    rows = cursor.fetchall()
    conn.close()
    return rows

# def total_value():
#     conn = connect_db()
#     cursor = conn.cursor()

#     cursor.execute("SELECT SUM(amount) FROM expenses")
#     total = cursor.fetchall()[0]

#     conn.close()


def delete_value(expensedb_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expensesdb WHERE id = ?", (expensedb_id,))

    conn.commit()
    conn.close()
