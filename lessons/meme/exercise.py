import json
import os

import requests


def resolve(payload, **kwargs):
    image = payload.get('image')
    text = payload.get('text')

    response = requests.post(
        'https://get.renderform.io/api/v2/render',
        headers={
            'Content-Type': 'application/json',
            'X-API-KEY': os.getenv('RENDER_FORM_API_KEY'),
        },
        data=json.dumps({
            'template': os.getenv('RENDER_FORM_TEMPLATE_ID'),
            'data': {
                'text.text': text,
                'image.src': image,
            }
        })
    )
    return response.json().get('href')
