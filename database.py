import sqlite3
from config import DB_NAME


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        filetype TEXT,
        tags TEXT,
        summary TEXT,
        filepath TEXT
    )
    """)
    conn.commit()
    conn.close()


def insert_file(filename, filetype, tags, summary, filepath):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO files (filename, filetype, tags, summary, filepath) VALUES (?, ?, ?, ?, ?)",
        (filename, filetype, tags, summary, filepath)
    )
    conn.commit()
    conn.close()


def search_files(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    q1 = """
        SELECT filename, filetype, tags, summary
        FROM files
        WHERE filename LIKE ?
           OR tags LIKE ?
           OR summary LIKE ?
    """
    value = f"%{keyword}%"
    cursor.execute(q1, (value, value, value))
    results = cursor.fetchall()

    if not results:
        q2 = """
            SELECT filename, filetype, tags, summary
            FROM files
            WHERE REPLACE(filename, ' ', '') LIKE REPLACE(?, ' ', '')
               OR REPLACE(tags, ' ', '') LIKE REPLACE(?, ' ', '')
               OR REPLACE(summary, ' ', '') LIKE REPLACE(?, ' ', '')
        """
        cursor.execute(q2, (value, value, value))
        results = cursor.fetchall()

    conn.close()
    return results


def get_file_detail(filename):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT filename, filetype, tags, summary, filepath FROM files WHERE filename = ?",
        (filename,)
    )
    result = cursor.fetchone()
    conn.close()
    return result


def get_file_count():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM files")
    count = cursor.fetchone()[0]
    conn.close()
    return count
