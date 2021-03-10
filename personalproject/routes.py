from flask import redirect, url_for, render_template, flash
from personalproject.forms import RegistrationForm, LoginForm
from personalproject.models import User, Post
from personalproject import app

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

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('blog'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '12345678901234567890':

            flash(f' {form.email.data} has been logged in!', 'success')
            return redirect(url_for('blog'))
        else: 
            flash('Login Unsuccessful. Please make sure your credantials are correct!', 'danger')
    return render_template('login.html', title='Login', form=form)