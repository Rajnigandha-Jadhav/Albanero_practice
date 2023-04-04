from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def welcome():
    name = "Vishal"
    l1 = ["Abdul", "Mahesh", "Manjusha"]
    return render_template("main.html",name=name, l1=l1)

@app.route("/friend")
def friend():
    return "This is my friends page"

@app.route("/friends/<name>",method=["POST"])
def friendsList(name):
    return render_template("home2.html",name=name)


if __name__ == "__main__":
    app.run(debug=True)