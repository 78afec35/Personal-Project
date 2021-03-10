from personalproject import db
from personalproject.models import User, Post
from flask_sqlalchemy import SQLAlchemy

db.create_all

#Test User Creation
user_1 = User(username='Suner',email='Suner@test.com',password='passwordpassword')
db.session.add(user_1)
db.session.commit()