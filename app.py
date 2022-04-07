from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import commands

db = SQLAlchemy()

mg = Migrate()

def create_app():
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = 'postgresql://gustavo:1234@localhost:5432/exercitando'

    from models import Music

    db.init_app(app)

    mg.init_app(app, db)

    commands.init_app(app, db)
    
    return app




