from flask import Flask, request, jsonify
import sqlite3
import jwt
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_super_secret_key"

def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header is missing"}), 401

        parts = auth_header.split()

        if len(parts) != 2 or parts[0] != "Bearer":
            return jsonify({"error": "Invalid authorization header format"}), 401

        token = parts[1]

        try:
            decoded_data = jwt.decode(
                token,
                app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )
            request.admin_user = decoded_data["username"]

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create admins table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    # Insert sample users only if table is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]

    if user_count == 0:
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Dan",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))

    conn.commit()
    conn.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    conn = get_db_connection()
    admin = conn.execute(
        "SELECT * FROM admins WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()
    conn.close()

    if not admin:
        return jsonify({"error": "Invalid username or password"}), 401

    # Token valid for 2 minutes
    expiry = datetime.utcnow() + timedelta(minutes=2)
    
    token = jwt.encode(
        {
            "username": username,
            "exp": expiry
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "token": token,
        "expires_at" : expiry.strftime("%Y-%m-%d %H:%M:%S %Z")
    })


@app.route("/users", methods=["GET"])
@token_required
def get_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return jsonify([dict(user) for user in users])

@app.route("/users/<int:user_id>", methods=["GET"])
@token_required
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    conn.close()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(dict(user))

@app.route("/users", methods=["POST"])
@token_required
def add_user():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        (data["name"],)
    )
    conn.commit()

    new_user_id = cursor.lastrowid
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (new_user_id,)
    ).fetchone()
    conn.close()

    return jsonify({
        "message": "User created successfully",
        "user": dict(user)
    }), 201

@app.route("/", methods=["GET"])
def home():
    return "Flask JWT API is running"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    
    
    
    

"""
{
  "username": "admin",
  "password": "admin123"
} 
"""

