import unittest
import requests
import json
from urllib.parse import urljoin
from urllib.request import urlopen


def get_api_result(endpoint_url):
    response = urlopen(endpoint_url)
    json_reply = response.read()
    return json.loads(json_reply)


class MessagingServiceApiTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__server = 'http://127.0.0.1:5000/'        # localhost

    def test_create_new_message(self):
        endpoint = '/message/send_message'
        url = urljoin(self.__server, endpoint)

        parameters = {
            'sender_id': 'Stefan',
            'recipient_id': 'Niklas',
            'message_body': 'This is a new message created from api test of the endpoint',
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url=url, json=parameters, headers=headers)

        assert response.status_code == 200, 'Error: got status %d' % response.status_code

    def test_get_message_by_id(self):
        endpoint = '/message/{}'.format(1)
        url = urljoin(self.__server, endpoint)
        result = get_api_result(url)
        assert len(result) == 1, 'No message with message_id = 1 found'

    def test_get_message_by_date(self):
        endpoint = '/message/messages/?start={0}&stop={1}'.format('2021-02-02', '2021-05-02')
        url = urljoin(self.__server, endpoint)
        result = get_api_result(url)
        assert len(result) == 1, 'Expected 1 message, but got {}'.format(len(result))
