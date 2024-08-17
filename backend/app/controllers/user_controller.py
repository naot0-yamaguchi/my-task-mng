from flask import redirect, jsonify, url_for
from ..services.user_service import UserService
from ..exceptions.user_already_exists_exception import UserAlreadyExistsException

# ユーザーにかかわる処理をまとめるコントローラー
class UserController():

    # 新規ユーザーを登録する。
    @staticmethod
    def register(user_name, user_pw):
         try:
             UserService.register(user_name, user_pw)
             response = jsonify({'message': 'User Created Successfully'})
             response.status_code = 201
             response.headers['location'] = url_for('login')
             return response
         except UserAlreadyExistsException as e:
             return jsonify({'error': str(e)}), 400
