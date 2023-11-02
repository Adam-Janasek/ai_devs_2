import re

import requests

from openai_api.utils import transcript


def resolve(payload, **kwargs):
    message = payload.get('msg', '')

    url_pattern = r'https?://[^\s]+'
    url_match = re.search(url_pattern, message)
    url = url_match.group(0)

    file_path = 'files/example.mp3'
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    with open(file_path, 'rb') as audio_file:
        response = transcript(audio_file)

    return response.get('text')
