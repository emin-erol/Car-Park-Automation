import sqlite3

def veriTabaniOlustur():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

def kullaniciEkle():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('emin', '1234'))

    conn.commit()
    conn.close()

def sensorsTablosunuOlustur():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            sensor_id INTEGER PRIMARY KEY,
            cameraId TEXT,
            t_leftX INTEGER,
            t_leftY INTEGER,
            t_rightX INTEGER,
            t_rightY INTEGER,
            b_leftX INTEGER,
            b_leftY INTEGER,
            b_rightX INTEGER,
            b_rightY INTEGER,
            situation INTEGER DEFAULT 0,
            FOREIGN KEY(cameraId) REFERENCES cameras(id)
        )
    ''')

    cursor.execute("UPDATE sensors SET situation = 0 WHERE situation = ?", (1,))

    conn.commit()
    conn.close()

def camerasTablosunuOlustur():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cameras (
            id INTEGER PRIMARY KEY,
            camera_id TEXT,
            port TEXT
        )
    ''')

    conn.commit()
    conn.close()
