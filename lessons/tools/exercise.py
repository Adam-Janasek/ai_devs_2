# 'msg': 'Decide whether the task should be added to the ToDo list or to the calendar (if time is provided) and return the corresponding JSON',
# 'hint': 'always use YYYY-MM-DD format for dates',
# 'example for ToDo': 'Przypomnij mi, że mam kupić mleko = {"tool":"ToDo","desc":"Kup mleko" }',
# 'example for Calendar': 'Jutro mam spotkanie z Marianem = {"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2023-11-16"}',
# 'question': 'W poniedziałek mam wizytę u lekarza'
import datetime
import json

from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    question = payload.get('question')
    # todo: could be done by function calling
    system_message = ' '.join([
        'Decide whether the task should be added to the ToDo list or to the calendar (if time is provided) and return the corresponding JSON',
        'always use YYYY-MM-DD format for dates',
        f'today is {datetime.date.today()}',
        'example for ToDo: Przypomnij mi, że mam kupić mleko = {"tool":"ToDo","desc":"Kup mleko" }',
        'example for Calendar: Jutro mam spotkanie z Marianem = {"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2023-11-16"}',
    ])
    return json.loads(chat_completion(system_message, question, model='gpt-4'))
