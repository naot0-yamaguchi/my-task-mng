from flask import jsonify
from ..services.task_service import TaskService

class TaskController():

    @staticmethod
    def get_tasks(user_id):
        task_list = [task.to_dict() for task in TaskService.get_tasks(user_id)]
        return jsonify({'tasks': task_list})

    @staticmethod
    def new_task(user_id, data):
        TaskService.new_task(user_id, data)
        return TaskController.get_tasks(user_id)

    @staticmethod
    def update_task(user_id, data):
        TaskService.update_task(user_id, data)
        return TaskController.get_tasks(user_id)

    @staticmethod
    def delete_task(user_id, data):
        TaskService.delete_task(data)
        return TaskController.get_tasks(user_id)

    @staticmethod
    def check_existence(user_id, title):
        return TaskService.check_existence(user_id, title)
