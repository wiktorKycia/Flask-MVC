from flask import Flask, render_template
from model import add_task, get_all_tasks
app = Flask(__name__)


@app.route('/')
def hello_world():
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run()
