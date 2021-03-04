import sqlite3
import pymysql
import pymysql.cursors
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# DROP TABLE IF EXISTS user;
# DROP TABLE IF EXISTS post;

# CREATE TABLE user (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   username TEXT UNIQUE NOT NULL,
#   password TEXT NOT NULL
# );
class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30),nullable=False)
# CREATE TABLE post (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   author_id INTEGER NOT NULL,
#   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   title TEXT NOT NULL,
#   body TEXT NOT NULL,
#   FOREIGN KEY (author_id) REFERENCES user (id)
# );
class Post (db.Model):
    id =db.Column(db.Integer,primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable= False)





