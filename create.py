from personalproject import db
from personalproject.models import User, Post
from flask_sqlalchemy import SQLAlchemy

db.drop_all()
db.create_all()
