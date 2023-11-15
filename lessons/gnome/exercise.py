from openai_api.utils import image_recognize


def resolve(payload, **kwargs):
    url = payload.get('url')
    user_message = ' '.join([
        'I will give you a drawing of a gnome with a hat on his head.'
        'Return only color of hat in POLISH. If any errors occur, return "ERROR" as answer',
    ])
    return image_recognize(user_message, url)
