from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/contactme")
def contactme():
    return render_template("contactme.html")
@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)