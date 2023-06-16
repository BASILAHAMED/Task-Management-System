from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample tasks
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description 1',
        'completed': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description 2',
        'completed': False
    }
]

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Get a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'completed': False,
        'name' : data['name']
    }
    tasks.append(task)
    return jsonify({'message': 'Task created successfully'})

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task.update(data)
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'message': 'Task not found'})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'})

if __name__ == '__main__':
    app.run(debug=True)
