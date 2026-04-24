import mysql.connector
import bcrypt
from cryptography.fernet import Fernet

# Encryption key for username
SECRET_ENC_KEY = b'SgB_5bjMfVYLrnh0x6Xw9J6dwXmUPxO62WPddSOkwpM='
cipher = Fernet(SECRET_ENC_KEY)

# MySQL connection config
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "S@ksham287",
    "database": "auth_app"
}

def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create admins table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)

    # Check if admin already exists
    cursor.execute("SELECT id, username FROM admins")
    admins = cursor.fetchall()

    admin_exists = False
    for admin in admins:
        decrypted_username = cipher.decrypt(admin[1].encode()).decode()
        if decrypted_username == "admin":
            admin_exists = True
            break

    if not admin_exists:
        encrypted_username = cipher.encrypt("admin".encode()).decode()
        hashed_password = bcrypt.hashpw(
            "admin123".encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            "INSERT INTO admins (username, password) VALUES (%s, %s)",
            (encrypted_username, hashed_password)
        )
        print("Admin created with encrypted username and hashed password")
    else:
        print("Admin already exists")

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("INSERT INTO users (name) VALUES (%s)", ("Ben",))
        cursor.execute("INSERT INTO users (name) VALUES (%s)", ("John",))
        cursor.execute("INSERT INTO users (name) VALUES (%s)", ("Alexa",))
        print("Sample users inserted")
    else:
        print("Users already exist")

    conn.commit()
    cursor.close()
    conn.close()

    print("MySQL database initialized successfully.")

if __name__ == "__main__":
    init_db()