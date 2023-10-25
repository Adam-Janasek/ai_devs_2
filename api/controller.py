import logging
import os

import requests


class APIController(object):
    def __init__(self, task_name):
        self._api_key = os.getenv('AI_DEVS_API_KEY')
        self._api_path = os.getenv('AI_DEVS_URL')
        self._task_name = task_name
        self._task_token = None

    def url(self, path):
        return f'{self._api_path}/{path}'

    def get_task_token(self):
        response = requests.post(self.url(f'token/{self._task_name}'), json={'apikey': self._api_key})
        self._task_token = response.json().get('token')

    def get_task_description(self):
        response = requests.get(self.url(f'task/{self._task_token}'))
        return response.json()

    def post_answer(self, answer):
        response = requests.post(self.url(f'answer/{self._task_token}'), json={'answer': answer})
        logging.debug(response.json())


def run_task(task_name, resolve):
    controller = APIController(task_name)
    controller.get_task_token()
    task_description = controller.get_task_description()
    logging.debug(task_description)
    answer = resolve(task_description)
    logging.debug(answer)
    controller.post_answer(answer)
