from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"name": "Alice", "balance": 5000},
    2: {"name": "Bob", "balance": 3000},
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/users/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    amount = request.json.get("amount")
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    users[user_id]["balance"] += amount
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    amount = request.json.get("amount")
    if not amount or amount <= 0 or amount > users[user_id]["balance"]:
        return jsonify({"error": "Invalid withdrawal"}), 400
    users[user_id]["balance"] -= amount
    return jsonify(users[user_id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)