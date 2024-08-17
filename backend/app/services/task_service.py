from flask import abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..database import db
from ..models.task import Tasks

class TaskService():

    @staticmethod
    def get_tasks(user_id):
        return Tasks.query.filter(Tasks.user_id == user_id).all()

    @staticmethod
    def check_existence(user_id, title):
        same_title_task = Tasks.query.filter(Tasks.user_id == user_id, Tasks.title == title).first()
        if same_title_task is None:
            return jsonify({'task_id': ''})
        else:
            return jsonify({'task_id': same_title_task.id})

    @staticmethod
    def new_task(user_id, input_data):
        task = Tasks.query.filter(Tasks.user_id == user_id, Tasks.title == input_data['title']).first()
        if task is not None:
            update_tasks(user_id, input_data)
        
        task = Tasks(
            title = input_data['title'],
            user_id = user_id,
            details = input_data['details'],
            deadline = input_data['deadline'],
            status = input_data['status']
        )
        db.session.add(task)
        db.session.commit()

    @staticmethod
    def update_task(user_id, input_data):
        task = Tasks.query.filter(Tasks.id == input_data['id']).first()
        if task is None:
            abort(f'The Task(id = {input_data['id']}) does not exist.', 404)

        task.title = input_data['title']
        task.user_id = user_id
        task.details = input_data['details']
        task.deadline = input_data['deadline']
        task.status = input_data['status']

        db.session.commit()

    @staticmethod
    def delete_task(data):
        task = Tasks.query.filter(Tasks.id == data['id']).first()
        if task is None:
            abort(f'The Task(id = {data['id']}) does not exist.', 404)

        db.session.delete(task)
        db.session.commit()
