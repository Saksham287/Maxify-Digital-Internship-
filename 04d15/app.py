from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Ben"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }

    users.append(new_user)
    
    return jsonify({
        "message": "User added successfully",
        "user": new_user
    }), 201
    
if __name__ == '__main__':
    app.run(debug=True)