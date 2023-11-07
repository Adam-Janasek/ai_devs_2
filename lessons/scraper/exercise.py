from time import sleep

import requests

from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    file_url = payload.get('input')
    question = payload.get('question')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    max_retries = 3
    retry_delay = 1
    timeout = 30

    for i in range(max_retries):
        response = requests.get(file_url, headers=headers, timeout=timeout)
        if response.ok:
            break
        sleep(retry_delay)
    else:
        raise Exception('Failed to download file')

    context = response.text
    system_message = ' '.join([
        context,
        '\nReturn short answer from given question based on the given context in Polish language.',
    ])
    return chat_completion(system_message, question)
