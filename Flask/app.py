# Digital Factory Assesment : ToDo Application to perform few CRUD operations
# Framework : Flask
# Database : SQLAlchemy
# Author : Omkar Pawar 

# Import required functionalites from flask and SQLAlchemy

from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure SQLALCHEMY_DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Create class ToDo and database columns as task_id[Primary Key] and content, done flag.
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Task_id
    content = db.Column(db.Text) # Task_name
    done = db.Column(db.Boolean, default=False) # Done Flag

# Initialize by a constructor
    def __init__(self, content):
        self.content = content
        self.done = False
# Return the content
    def __repr__(self):
        return '<Content %s>' % self.content

# Create database
db.create_all()

#  Endpoint1 : Main Page that shows all todo tasks entered in the database and their action.
@app.route('/')
def tasks_list():
    tasks = ToDo.query.all()
    return render_template('list.html', tasks=tasks)

# Endpoint2 : To create a todo task and post it on the page.
@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error' # Throws and error is nothing is given in task.
    # Add task to database.
    task = ToDo(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

# Endpoint3 : Delete a todo task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = ToDo.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')

# Endpoint4 : Mark a todo task as complete. Strikes the task when marked as done.
@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = ToDo.query.get(task_id)

    if not task:
        return redirect('/')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
