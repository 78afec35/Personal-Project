from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Suner Syuleyman',
        'title': 'Blog Post 1',
        'content': 'Hey this is my blog post',
        'date_posted' : 'April 1st'
    },
    {
        'author': 'Suner Syuleyman',
        'title': 'Blog Post 2',
        'content': 'Hey this is my second blog post',
        'date_posted' : 'April 1st'
    }

]

me = [
    {
        'author': 'Suner Syuleyman',
        'title': 'Intro Page',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted' : 'April 1st'
    },

]

@app.route("/")
def home():
    return render_template("index.html",me=me)
@app.route("/blog")
def blog():
    return render_template("blog.html",posts=posts)
@app.route("/contactme")
def contactme():
    return render_template("contactme.html")
@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)