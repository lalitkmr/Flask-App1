from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# app.config["SESSION_PERMANENT"]=False
# app.config["SESSION_TYPE"] ="filesystem"
app.config['SECRET_KEY'] = 'e5aa6f5abe210648e25c710cb7dbfdaee5797e025075264211de92ac55aac547'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLAlchemy(app)
# Session(app)					
bcrypt = Bcrypt(app)
login_master = LoginManager(app)
login_master.login_view = 'login'
login_master.login_message_category = 'info'

from cyberworld import CWroutes


