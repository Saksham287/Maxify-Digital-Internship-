import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ben",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Dan",))


conn.commit()
conn.close()

print("Database initialized successfully.")