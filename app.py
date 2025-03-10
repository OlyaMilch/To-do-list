from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db_path = os.path.abspath("todo.db")  # Db path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # SQLAlchemy says:
# "Use SQLite as your database and store it in the file todo.db."
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabling change alerts from Flask
app.config['SECRET_KEY'] = os.urandom(24).hex()  # We generate a random key, it is needed to encrypt session data

db = SQLAlchemy(app)

# Contents inside db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)  # When the task is completed, set True by task id

# Home page (shows task list)
@app.route('/all')
def index():
    tasks = Task.query.all()  # Get all tasks
    return render_template('index.html', tasks=tasks)  # Displays HTML pages

# Add tasks page
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Task edit page
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get(id)
    if request.method == 'POST':
        task.title = request.form['title']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

# Delete task
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Mark task as completed
@app.route('/complete/<int:id>')
def complete_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed  # Toggle status from False to True
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create a db if it doesn't exist
    app.run(debug=True)
