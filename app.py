from flask import Flask, render_template, request, redirect, url_for
from model import add_task, get_all_tasks
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        tasks = get_all_tasks()
        return render_template('index.html', tasks=tasks)
    elif request.method == 'POST':
        new_task = request.form['task']
        add_task(new_task)
        return redirect(url_for('hello_world', _method='GET'))


if __name__ == '__main__':
    app.run(debug=True)
