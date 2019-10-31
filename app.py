from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from marshmallow import ValidationError

from resources.user import User, UserRegister, UserLogin

app = Flask(__name__)
api = Api(app)

# set configuration for app
# load_dotenv(".env")
app.config.from_pyfile("config.py")

# add all resources here
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/signup')
api.add_resource(UserLogin, '/login')


@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages)


if __name__ == '__main__':
    # init sqlalchemy instance
    from db import db
    db.init_app(app)

    # init marshmallow instance
    from ma import ma
    ma.init_app(app)

    app.run()
