# This is app.py, this is the main file called.
from src import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/static/<name>')
# def root(name):
#     return app.send_static_file(name)

if __name__ == '__main__':
    app.run()
