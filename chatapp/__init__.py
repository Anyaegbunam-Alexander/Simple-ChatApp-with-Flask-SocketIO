from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .events import socketio

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "NOT SO SECURE SECRET KEY"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
    app.config["FLASK_APP"] = 'run.py'

    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    socketio.init_app(app)
    
    from .routes import main

    app.register_blueprint(main)
    
    return app
