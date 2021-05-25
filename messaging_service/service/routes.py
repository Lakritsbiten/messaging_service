import datetime
import json
import flask
from flask_restx import fields, Api, Resource, reqparse     # For automatic Swagger documentation

from messaging_service.service.flask_application import create_flask_app, create_swagger_app
from messaging_service.data_access.persistence import MessageDatabase
from messaging_service.utils.single_queue import WorkQueue
from messaging_service.utils.queued_call import redirect


flask_app = create_flask_app()
swagger_api = create_swagger_app(flask_app)


@swagger_api.route('/message/<int:message_id>')
class ExistingMessageEndpoint(Resource):

    def delete(self, message_id):
        def delete_message_binder():
            return MessageDatabase().delete_message(message_id)

        return redirect(delete_message_binder)

    def get(self, message_id):
        def get_message_binder():
            return MessageDatabase().get_message_by_id(message_id)

        return redirect(get_message_binder)

    @swagger_api.doc('Set read flag')
    def post(self, message_id):
        def set_read_message_binder():
            return MessageDatabase().set_read_message(message_id)

        return redirect(set_read_message_binder)


@swagger_api.route('/message/send_message')
class NewMessageEndpoint(Resource):

    def post(self):
        json_data = flask.request.get_json(force=True)
        sender_id = json_data['sender_id']
        recipient_id = json_data['recipient_id']
        message_body = json_data['message_body']

        def create_message_binder():
            return MessageDatabase().insert_message(sender_id=sender_id, recipient_id=recipient_id, message_body=message_body)

        return redirect(create_message_binder)


@swagger_api.route('/message/messages/', methods=['GET'])
@swagger_api.doc(params={
    'start': {
        'required': True,
        'type': 'string',
        'description': 'format YYYY-mm-dd',
        'default': '2020-01-01'},
    'stop': {
        'required': False,
        'type': 'string',
        'description': 'format YYYY-mm-dd'},
})
class GetMessagesEndpoint(Resource):

    def get(self):
        start = flask.request.args.get('start')
        stop = flask.request.args.get('stop', None)

        def get_messages_binder():
            return MessageDatabase().get_messages_by_date(start=start, stop=stop)

        return redirect(get_messages_binder)


if __name__ == '__main__':
    flask_app.run()
