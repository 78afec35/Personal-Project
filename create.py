from personalproject import db

db.create(all)

from personalproject import User, Post
user_1 = User(username='Suner',email='Suner@test.com',password='passwordpassword')
db.session.add(user_1)
db.session.commit()