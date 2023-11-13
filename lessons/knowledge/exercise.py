import requests

from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    question = payload.get('question')
    source = {
        'currency': 'https://api.nbp.pl/api/exchangerates/tables/A/?format=json',
        'population': 'https://restcountries.com/v3.1/name/',
        'general': '',
    }

    system_message = ''
    user_message = ' '.join([
      f'You got a question: {question}'
      'Return only category of the question: currency, population or general.',
    ])
    chat_response = chat_completion(system_message, user_message)

    url = source.get(chat_response)
    response = None
    if url:
        response = requests.get(url).json()

    system_message = ' '.join([
        'Based on your knowledge or additional context, return answer for the given question.',
        f'"""{response}"""',
    ])
    user_message = ' '.join([
        f'{question}'
    ])
    return chat_completion(system_message, user_message)
