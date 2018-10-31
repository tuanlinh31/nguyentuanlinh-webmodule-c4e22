from flask import *
app = Flask (__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        x = form['name']
        y = form['yob']
        z = form['email']
        return x + y + z



    

if __name__ == '__main__':
  app.run(debug=True)

