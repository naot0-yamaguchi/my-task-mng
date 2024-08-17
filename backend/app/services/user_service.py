from flask import abort
from werkzeug.security import generate_password_hash
from ..exceptions.user_already_exists_exception import UserAlreadyExistsException
from ..models.user import Users
from ..database import db

class UserService():

    @staticmethod
    def register(user_name, user_pw):
        same_name_user = Users.query.filter(Users.user_name == user_name).first()
        if same_name_user is not None:
            raise UserAlreadyExistsException('User Already Exists.')

        user = Users(user_name=user_name, user_pw=generate_password_hash(user_pw))
        db.session.add(user)
        db.session.commit()
