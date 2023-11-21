import os


def resolve(payload, **kwargs):
    return os.getenv('OWNAPI_URL')
