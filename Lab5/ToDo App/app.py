from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


class Todo():
    def __init__(self,id,text):
        self.id = id
        self.text = text
        self.complete = False

todosList = []

@app.route('/')
def index():
    return render_template('index.html', todos=todosList)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('new-todo')
    todosList.append(Todo(len(todosList),new_todo))
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    for todo in todosList:
        if todo.id == int(id):
            todo.complete = True
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    for todo in todosList:
        if todo.complete:
            todosList.remove(todo)
    return redirect(url_for('index'))

@app.route('/delete_all')
def delete_all():
    todosList.clear()
    return redirect(url_for('index'))