from flask import (
    Flask,
    request,
    redirect,
    render_template
)
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.controllers.user_controller import UserController
from app.controllers.auth_controller import AuthController
from app.controllers.task_controller import TaskController

def create_routes(app: Flask):
    # 新規ユーザー登録用の画面
    @app.get('/register')
    def show_register_page():
        return render_template('register.html')

    # 新規ユーザーを登録する。
    @app.post('/register')
    def register():
        data = request.get_json()
        user_name = data.get('user_name')
        user_pw = data.get('user_pw')
        return UserController.register(user_name, user_pw)

    # ログイン画面
    @app.get('/login')
    def show_login_page():
        return render_template('login.html')

    # ユーザーがログインする。
    @app.post('/login')
    def login():
        data = request.get_json()
        user_name = data.get('user_name')
        user_pw = data.get('user_pw')
        return AuthController.login(user_name, user_pw)

    # ユーザーがログアウトする。
    @app.post('/logout')
    @jwt_required()
    def logout():
        return AuthController.logout(get_jwt()['jti'])

    # タスク一覧表示
    @app.get('/index')
    def index():
        return render_template('index.html')

    # タスク一覧表示
    @app.get('/fecth_index_data')
    @jwt_required()
    def fecth_index_data():
        user_id = get_jwt_identity()['id']
        return TaskController.get_tasks(user_id)

    # タスク存在確認
    @app.post('/check_existence')
    @jwt_required()
    def check_existence():
        user_id = get_jwt_identity()['id']
        title = request.get_json()['title']
        return TaskController.check_existence(user_id, title)

    # タスク追加
    @app.post('/new_task')
    @jwt_required()
    def new_task():
        user_id = get_jwt_identity()['id']
        data = request.get_json()
        return TaskController.new_task(user_id, data)

    # タスク更新
    @app.patch('/update_task')
    @jwt_required()
    def update_task():
        user_id = get_jwt_identity()['id']
        data = request.get_json()
        return TaskController.update_task(user_id, data)

    # タスク削除
    @app.delete('/delete_task')
    @jwt_required()
    def delete_task():
        user_id = get_jwt_identity()['id']
        data = request.get_json()
        return TaskController.delete_task(user_id, data)
