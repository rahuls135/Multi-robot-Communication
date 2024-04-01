from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description']
    }
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'}), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    data = request.json
    task.update(data)
    return jsonify({'message': 'Task updated successfully'})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
