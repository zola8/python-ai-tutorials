import hashlib
import sqlite3

conn = sqlite3.connect("userdata.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
username1, password1 = "user1", hashlib.sha256("alma".encode("utf-8")).hexdigest()
username2, password2 = "user2", hashlib.sha256("user2".encode("utf-8")).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))

conn.commit()
conn.close()
