# This is app.py, this is the main file called.
from src import app
from flask import render_template, send_from_directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service-worker.js')
def worker():
    # the directory path is relative to path where app is created
    return send_from_directory('build','service-worker.js')

@app.route('/<name>')
def others(name):
    return send_from_directory('build',name)

if __name__ == '__main__':
    app.run()
