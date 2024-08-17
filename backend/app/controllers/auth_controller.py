from flask import make_response, jsonify, url_for
from ..services.auth_service import AuthService
from ..exceptions.user_not_found_exception import UserNotFoundException

# 認証にかかわる処理をまとめるコントローラー
class AuthController():

    # ユーザーがログインする。
    @staticmethod
    def login(user_name, user_pw):
         try:
             tokens = AuthService.login(user_name, user_pw)
             response = make_response({'message': 'Login Successful', 'jwt_token': tokens['access_token']})
             response.set_cookie(
                 'refresh_token',
                 tokens['refresh_token'],
                 httponly = True, # JSからのアクセスを防ぐ
                 secure = False, # TODO : Trueに変える
                 samesite = 'Strict',
                 max_age = 1 * 24 * 60 * 60 # 有効期限を1日にする
             )
             response.headers['Location'] = url_for('index')
             return response
         except UserNotFoundException as e:
             return jsonify({'error': str(e)}), 404

    # ユーザーがログアウトする。
    @staticmethod
    def logout(jti):
         return AuthService.logout(jti)
