import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "todos.json")

# Asegurarse que la carpeta exista
os.makedirs(DATA_DIR, exist_ok=True)

def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

@app.route("/todos", methods=["GET"])
def get_todos():
    todos = load_todos()
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    todos = load_todos()
    data = request.get_json()
    if not data or "task" not in data or not data["task"].strip():
        return jsonify({"error": "Tarea inválida"}), 400

    new_todo = {
        "id": len(todos) + 1,
        "task": data["task"].strip()
    }
    todos.append(new_todo)
    save_todos(todos)
    return jsonify({"message": "Tarea agregada", "todo": new_todo}), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todos = load_todos()
    updated_todos = [todo for todo in todos if todo["id"] != todo_id]

    if len(updated_todos) == len(todos):
        return jsonify({"error": "Tarea no encontrada"}), 404

    save_todos(updated_todos)
    return jsonify({"message": "Tarea eliminada"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
