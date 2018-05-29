from flask import Flask, render_template
import sqlite3
import config

app = Flask(__name__)


# Routes


@app.route('/')
def hello_world():
    return 'This is the index page!'


@app.route('/hello')
@app.route('/hello/<name>')
def hello_from_the_other_side(name=None):
    return render_template('index.html', name=name)


@app.route('/hello/database')
def hello_from_database(name=None):
    return render_template('index.html', name=fetch_username())

# Utils


def fetch_username():
    connection = sqlite3.connect(config.Config.DATABASE_URI)
    cursor = connection.cursor()
    cursor.execute('SELECT NAME FROM USER WHERE ID = 1')
    return cursor.fetchone()[0]


# Main
if __name__ == '__main__':
    app.run()
