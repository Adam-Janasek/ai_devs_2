from openapi.utils import chat_completion, embedding


def resolve(payload, **kwargs):
    param = 'Hawaiian pizza'
    return embedding(param)