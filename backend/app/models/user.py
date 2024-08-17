from sqlalchemy.orm import relationship
from ..database import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    user_pw = db.Column(db.String, nullable=False)
    task = relationship("Tasks")
