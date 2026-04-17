from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return "Flask API with SQLite is running!"


@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    users_list = [dict(user) for user in users]
    return jsonify(users_list)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(dict(user))


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if 'name' not in data or not data['name'].strip():
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (name) VALUES (?)', (data['name'],))
    conn.commit()

    new_user_id = cursor.lastrowid

    user = conn.execute('SELECT * FROM users WHERE id = ?', (new_user_id,)).fetchone()
    conn.close()

    return jsonify({
        "message": "User added successfully",
        "user": dict(user)
    }), 201


if __name__ == '__main__':
    app.run(debug=True)