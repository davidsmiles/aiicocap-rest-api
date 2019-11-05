from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import *

from libs.strings import gettext
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()


class User(Resource):
    def get(self, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            return user_schema.dump(user)
        else:
            return {"message": gettext("user_not_found")}, 404


class UserRegister(Resource):
    def post(self):
        payload = user_schema.load(request.get_json())
        user = UserModel.find_by_email(payload.email)
        if user:
            return {"message": gettext("user_email_exists")}, 409

        payload.save_to_db()
        # UserModel.send_mail()
        return jsonify(user_schema.dump(payload))


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_payload = user_schema.load(request.get_json(), partial=("firstname", "lastname"))
        user = UserModel.find_by_email(user_payload.email)
        if user and safe_str_cmp(user.email, user_payload.email):
            access_token = create_access_token(identity=user.email, fresh=True)
            refresh_token = create_refresh_token(identity=user.email)

            return jsonify(access_token=access_token, refresh_token=refresh_token, logged_in_user=user_schema.dump(user))
        return {"message": gettext("user_invalid_credentials")}
