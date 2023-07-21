from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '912c0ed68bfc61f67ec05b59'
app.app_context().push()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes