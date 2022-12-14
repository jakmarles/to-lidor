import json
from flask import Flask

app = Flask(__name__)

DATA = 'Database.json'
students = []


def load_json(DATA):
    try:
        with open(DATA, 'r') as file:
            return json.load(file)
    except:
        save_json(DATA,[])
        return []



def save_json(var):
    with open(DATA, 'w+') as file:
        return json.dump(students,file, indent=4)



@app.route('/search/<name>')
def search(name=""):
        students_json=load_json(DATA)
        for stud in students_json:
         if stud['name'] == name:
            return stud
        else:
           return f"{name} not found"

@app.route('/del/<name>')
def kill(name=""):
        students_json=load_json(DATA)
        for stud in students_json:
            if stud["name"] == name:
                students_json.remove(stud)
                save_json(students_json)
            return students_json 
        else:
            return f"{name} not found"



@app.route('/add/<name>/<int:age>')
def add(name='', age=0):
    SAVE = save_json(students.append({"name": name, "age": age}))
    save_json(SAVE)
    return 'The player added'


@app.route("/")
def hello_world():
    return """
    <img src="/static/media/welcome.gif"> <br><br><br>
    """

@app.route("/about/<int:id>")
def about(id):
    load_json(DATA)
    if id >= len(load_json(DATA)):
        return "<h1>The id is too big!</h1>"
    if id <= len(load_json(DATA)):
        return load_json(DATA)[id]

@app.route("/about/")
def about1():
    return load_json(DATA)




load_json(DATA)
app.run(debug=True)
