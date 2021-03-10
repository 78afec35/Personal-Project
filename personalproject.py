from datetime import datetime
from flask import Flask, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd4e754bef5ca6727f10a59665946bc42b07481dd9bbc66ed3dbc1a31d40e698ff18c2ebf71b8aa6163b2fc4526068e42c808bd1f8349c1197deacbb616655a1a98552b1d610d9c85ce137575ee54b2386eb67b6a23462badb05d48eee5862de07600691a89f56baed299d5ff9601e69c013ee35c609a30b82df1ec7249a6aacac0d9b3f7edffb6c3e56b3fc5341162efc5059f5f17ed35244c2e412f4fc790df86260b51bae94a21c812535e748c98d8a4af40097c640da2f4ff222da6cfaa9d19c69fffa520c3861b10893370c822742d1e4605a3ece75e76ee8403bbb5b66bccfc2762d2720e45202b1153e812c172ffc341416c2e74197140f3a3bdc3a434'
app.config['SQLALCHEMY_DATABASE_URI']=  'sqlite:///blog.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique= True, nullable = False)
    email = db.Column(db.String(120), unique= True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpeg' )
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(150), nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    content = db.Column(db.Text, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.dateposted}')"

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

if __name__ == "__main__":
    app.run(debug=True)