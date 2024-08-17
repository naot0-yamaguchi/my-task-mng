import logging
from flask import jsonify
from flask import current_app as app
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import Users
from ..exceptions.user_not_found_exception import UserNotFoundException

TOKEN_EXPIRATION_TIME = 86400 # 1日

class AuthService():

    @staticmethod
    def login(user_name, user_pw):
        user = Users.query.filter(Users.user_name == user_name).first()
        if user is None:
            raise UserNotFoundException()

        if check_password_hash(user.user_pw, user_pw):
            return {
                'access_token': create_access_token(identity={"id": user.id}),
                'refresh_token': create_refresh_token(identity={"id": user.id})
            }
        else:
            raise UserNotFoundException()

    @staticmethod
    def logout(jti):
        try:
            from app.__init__ import r
            r.setex(f'jti:{jti}', TOKEN_EXPIRATION_TIME, 'true')
            return jsonify({'msg': 'Successfully logged out.'}), 200
        except Exception as e:
            return jsonify({'msg': 'Logout Failed', 'error': str(e)}), 500
