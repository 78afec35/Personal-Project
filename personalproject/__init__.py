from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# I know this is not supposed to be here, however security implementation is not something I am assessed on for this project.
app.config['SECRET_KEY'] = 'd4e754bef5ca6727f10a59665946bc42b07481dd9bbc66ed3dbc1a31d40e698ff18c2ebf71b8aa6163b2fc4526068e42c808bd1f8349c1197deacbb616655a1a98552b1d610d9c85ce137575ee54b2386eb67b6a23462badb05d48eee5862de07600691a89f56baed299d5ff9601e69c013ee35c609a30b82df1ec7249a6aacac0d9b3f7edffb6c3e56b3fc5341162efc5059f5f17ed35244c2e412f4fc790df86260b51bae94a21c812535e748c98d8a4af40097c640da2f4ff222da6cfaa9d19c69fffa520c3861b10893370c822742d1e4605a3ece75e76ee8403bbb5b66bccfc2762d2720e45202b1153e812c172ffc341416c2e74197140f3a3bdc3a434'
app.config['SQLALCHEMY_DATABASE_URI']=  'sqlite:///blog.db'
# end of sensitive information
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from personalproject import routes