from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tasks = []

class Task:
    def __init__(self, id, title, description, due_date, priority, assignee, completed):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.assignee = assignee
        self.completed = completed

class TaskResource(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            return task.__dict__, 200
        else:
            return {'message': 'Task not found'}, 404

    def put(self, task_id):
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            data = request.get_json()
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.due_date = data.get('due_date', task.due_date)
            task.priority = data.get('priority', task.priority)
            task.assignee = data.get('assignee', task.assignee)
            task.completed = data.get('completed', task.completed)
            return task.__dict__, 200
        else:
            return {'message': 'Task not found'}, 404

api.add_resource(TaskResource, '/api/tasks/<int:task_id>')

# Add sample tasks
tasks.append(Task(1, 'Task 1', 'Description 1', '2023-06-30', 'High', 'John Doe', False))
tasks.append(Task(2, 'Task 2', 'Description 2', '2023-07-15', 'Medium', 'Jane Smith', False))


if __name__ == '__main__':
    app.run(debug=True)
