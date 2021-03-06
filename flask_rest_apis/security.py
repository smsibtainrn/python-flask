from flask import jsonify
from werkzeug.security import safe_str_cmp

from user import User

users = [
    User(1, 'smsrn', 'smsrn')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = userid_mapping.get(username, None)
    for user in users:
        print('step 1')
        if user.username == username:
            print('step 2')
            if user.password == password:
                print('check pass: ', user.password == password)
                return user
    # if user and safe_str_cmp(user.password, password):
        # return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
