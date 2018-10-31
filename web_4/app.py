from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/new_bike", methods=["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("new_bike2.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        print("Model: ", model)
        print("Fee: ", fee)
        print("Image: ", image)
        print("Year: ", year)
        return "gotcha"    


if __name__ == '__main__':
  app.run(debug=True)