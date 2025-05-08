from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
tasks = []
users = {}

# GET endpoints
@app.route('/')
def home():
    return jsonify({"message": "¡Bienvenido al servidor Flask!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

# POST endpoints
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    if 'title' not in task:
        return jsonify({"error": "Title is required"}), 400
    tasks.append(task)
    return jsonify({"message": "Task created", "task": task}), 201

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    if 'id' not in user or 'name' not in user:
        return jsonify({"error": "ID and name are required"}), 400
    users[user['id']] = user
    return jsonify({"message": "User created", "user": user}), 201

# PUT endpoints
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404
    task = request.json
    if 'title' not in task:
        return jsonify({"error": "Title is required"}), 400
    tasks[task_id] = task
    return jsonify({"message": "Task updated", "task": task})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    user = request.json
    if 'name' not in user:
        return jsonify({"error": "Name is required"}), 400
    users[user_id].update(user)
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE endpoints
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404
    deleted_task = tasks.pop(task_id)
    return jsonify({"message": "Task deleted", "task": deleted_task})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})

if __name__ == '__main__':
    app.run(debug=True, port=5000)