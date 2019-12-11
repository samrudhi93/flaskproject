from flaskproject import app, db
from flaskproject.models import todo

from flask import Flask, render_template, request, redirect


@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/home')

        except:
            return 'there was an issue'
    else:
        tasks = todo.query.order_by(todo.data_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/home')

    except:
        return 'there was an error deleting row'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/home')
        except:
            return 'there is a problem in updating'
    else:
        return render_template('update.html', task=task)

