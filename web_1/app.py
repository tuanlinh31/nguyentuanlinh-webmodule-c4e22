from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def homepage():
    return "Welcome to C4E Web module,enjoy"



@app.route("/linh")
def hello_linh():
    return "Hello linh"

@app.route("/praise/linh")
def praise_linh():
    return "linh is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a + b
    return str(s)

@app.route("/question")
def show_question():
    return render_template('question.html')



if __name__ == "__main__":
    app.run(debug=True)