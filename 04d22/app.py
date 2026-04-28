from flask import Flask, request, jsonify
import mysql.connector
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from cryptography.fernet import Fernet
from functools import wraps

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_super_secret_key"

SECRET_ENC_KEY = b'SgB_5bjMfVYLrnh0x6Xw9J6dwXmUPxO62WPddSOkwpM='
cipher = Fernet(SECRET_ENC_KEY)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "My_pswrd",
    "database": "auth_app"
}

# Database Connection
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "").strip()

        if not auth_header:
            return jsonify({"error": "Authorization header is missing"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({
                "error": "Invalid authorization header format. Expected: Bearer <token>"
            }), 401

        token = auth_header.replace("Bearer ", "", 1).strip()

        try:
            decoded = jwt.decode(
                token,
                app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )
            request.admin_user = decoded["username"]

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated

# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    username_input = data.get("username")
    password_input = data.get("password")

    if not username_input or not password_input:
        return jsonify({"error": "Username and password are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM admins")
    admins = cursor.fetchall()

    cursor.close()
    conn.close()

    matched_admin = None

    for admin in admins:
        decrypted_username = cipher.decrypt(admin["username"].encode()).decode()
        if decrypted_username == username_input:
            matched_admin = admin
            break

    if not matched_admin:
        return jsonify({"error": "Invalid username or password"}), 401

    if not bcrypt.checkpw(
        password_input.encode("utf-8"),
        matched_admin["password"].encode("utf-8")
    ):
        return jsonify({"error": "Invalid username or password"}), 401

    expiry_utc = datetime.now(timezone.utc) + timedelta(minutes=2)
    expiry_local = expiry_utc.astimezone(ZoneInfo("America/New_York"))

    token = jwt.encode(
        {
            "username": username_input,
            "exp": expiry_utc
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "token": token,
        "expires_at_utc": expiry_utc.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "expires_at_local": expiry_local.strftime("%Y-%m-%d %H:%M:%S %Z")
    })

# Get all users
@app.route("/users", methods=["GET"])
@token_required
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)

# Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
@token_required
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)

# Add User
@app.route("/users", methods=["POST"])
@token_required
def add_user():
    data = request.get_json()

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("INSERT INTO users (name) VALUES (%s)", (data["name"],))
    conn.commit()

    new_id = cursor.lastrowid

    cursor.execute("SELECT * FROM users WHERE id = %s", (new_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User created successfully",
        "user": user
    }), 201

@app.route("/")
def home():
    return "Flask JWT MySQL API is running"

if __name__ == "__main__":
    app.run(debug=True)
