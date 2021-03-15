from flask import redirect, url_for, render_template, flash, request
from personalproject.forms import RegistrationForm, LoginForm
from personalproject.models import User, Post
from personalproject import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect (next_page) if next_page else redirect(url_for('blog'))

        else: 
            flash('Login Unsuccessful. Please make sure your credantials are correct!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
    
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')