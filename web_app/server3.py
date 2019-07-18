from flask import *
import json
import os
import sqlite3

app = Flask(__name__)

def create_table():
    print("Creating table...")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todos (item text);")
    conn.commit()

def get_todos_from_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT item FROM todos;")
    return list(map(lambda row: row[0], c.fetchall()))

def add_todo_to_db(item):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos VALUES ('" + item + "');")
    conn.commit()

@app.route('/')
def index():
    items = get_todos_from_db()
    return render_template('form2.html', items=items)

@app.route('/add_todo')
def add_todo():
    item = request.args.get('item')
    print(item)
    add_todo_to_db(item)
    return redirect("/", code=302)

@app.route('/get_todos')
def get_todos():
    items = get_todos_from_db()
    resp = Response(json.dumps(items))
    resp.headers['Content-Type'] = 'application/json'
    return resp
 
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    create_table()
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)
