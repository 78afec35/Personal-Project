import secrets
import os
from PIL import Image
from flask import redirect, url_for, render_template, flash, request, abort
from personalproject.forms import RegistrationForm, LoginForm, UpdateAccount, PostForm
from personalproject.models import User, Post
from personalproject import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required

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
    posts=Post.query.all()
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

def save_pic(form_picture):
    random_name = secrets.token_hex(12)
    _, f_ext = os.path.splitext(form_picture.filename)
    pic_name = random_name + f_ext
    pic_path = os.path.join(app.root_path, 'static/img/userimages',pic_name)
    
    pic_resize=(512,512)
    i = Image.open(form_picture)
    i.thumbnail(pic_resize)
    
    i.save(pic_path)
    return pic_name

@app.route("/account/", methods = ['GET','POST'])
@login_required
def account():
    form = UpdateAccount()


    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_pic(form.picture.data)
            current_user.image_file =  picture_file

        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Account details have been updated!', 'success')
        return redirect(url_for('account'))
    pic= url_for('static', filename='/img/userimages/' + current_user.image_file)
    return render_template('account.html', title='Account', pic=pic, form=form)

@app.route("/post/new",methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been added to the blog!', 'success')
        return redirect(url_for('blog'))
    return render_template('create_post.html', title='New Post', form = form, legend="New Post")

@app.route("/post/<int:post_id>",methods = ['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post=post)

@app.route("/post/<int:post_id>/update",methods = ['GET','POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('The post has been updated' ,'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form = form, legend="Update Post")

@app.route("/post/<int:post_id>/delete",methods = ['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted!','danger')
    return redirect(url_for('blog'))