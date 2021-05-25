from flask import Flask
from flask_restx import Api
import threading


def create_flask_app():
    # create and configure the app
    _app = Flask(__name__)
    _app.debug = True
    return _app


def create_swagger_app(flask_app):
    swagger_app = Api(app=flask_app,
                      version='Beta',
                      title='Messaging Service',
                      description='Server endpoints for sending, recieving and deleting messages',
                      doc='/',
                      default='Endpoints',
                      )
    return swagger_app


if __name__ == '__main__':
    app = create_app()
    app.run()

