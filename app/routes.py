import json
from flask import request
from app import app, database


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!', 200


@app.route('/users', methods=['GET'])
def get_users():
    # x = [1, 2, 3]
    # json.dumps(x) -> '[1, 2, 3]'
    # y = {1: 'a', 'b': 'xy'}
    # json.dumps(y) -> "{1: 'a', 'b': 'xy'}"

    page = request.args.get('page', type=int)
    size = 2

    if page is not None:
        left = (page - 1) * size
        right = page * size
        return json.dumps(database[left:right]), 200
    return json.dumps(database), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    return database[user_id], 200


# POST /users/ -- создание пользователя
# PATCH /users/<int:user_id> -- Сменить имя пользователя


# GET users/
# GET users/1
