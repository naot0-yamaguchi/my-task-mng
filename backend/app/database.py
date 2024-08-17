from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app: Flask):
    db.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
