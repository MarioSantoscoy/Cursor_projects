# app.py
# 
# This is a simple Flask web application that functions as a task list manager (TODO list).
# 
# Features:
# - Displays a list of tasks, each with a completion status.
# - Allows the addition of new tasks via a form.
# - Lets users mark tasks as completed.
#
# Key Components:
# - In-memory storage: Uses a Python list (`tasks`) to hold task dictionaries.
# - Each task is represented by a dictionary with keys: 'id', 'text', and 'completed'.
# - Functions:
#     - `add_task_to_list(text)`: Adds a new task with a unique ID.
#     - `complete_task(id)`: Marks a task as completed by ID.
# - Flask routes:
#     - `/`: Shows all tasks, sorted with incomplete tasks first.
#     - `/add` (POST): Handles form submissions to add tasks.
#     - `/completed/<int:id>`: Marks a task as completed.
# - The UI is rendered using `templates/index.html`.
#
# Notes:
# - This application does not persist data; all tasks are lost when restarting the server.
# - For simplicity, it uses global variables and does not support multiple users or concurrency.

import json
import atexit
import os
from flask import Flask, request, redirect, render_template

app= Flask(__name__)

tasks = []
next_id = 1

def add_task_to_list(text):
    global next_id
    task = {'id': next_id, 'text': text, 'completed': False}
    tasks.append(task)
    next_id += 1
        

def complete_task(id):        
    for task in tasks:
        if task['id'] == id:
            task['completed'] = True
            break


@app.route('/')
def index():
    sorted_tasks = sorted(tasks, key=lambda t: t['completed'])
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task_text')

    if task_text:
        add_task_to_list(task_text)
    return redirect('/')

@app.route('/completed/<int:id>')
def completed(id):
    complete_task(id)
    return redirect('/')


TASKS_FILE = 'tasks.json'

def load_tasks():
    global tasks, next_id
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
            tasks.clear()
            tasks.extend(data.get('tasks', []))
            next_id = data.get('next_id', 1)
    else:
        tasks.clear()
        next_id = 1

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump({'tasks': tasks, 'next_id': next_id}, f)

# Cargar tareas al iniciar la app
load_tasks()

# Guardar tareas cuando la app termina
atexit.register(save_tasks)

if __name__ == '__main__':
    app.run(debug=True)





