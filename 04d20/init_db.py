import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Admins table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute("SELECT * FROM admins WHERE username = ?", ("admin",))
    admin = cursor.fetchone()

    if not admin:
        cursor.execute(
            "INSERT INTO admins (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )
        print("Admin user created: username=admin, password=admin123")
    else:
        print("Admin already exists")

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Saksham",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
        print("Sample users inserted")
    else:
        print("Users already exist")

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


# Run script
if __name__ == "__main__":
    init_db()