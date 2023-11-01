from openapi.utils import chat_completion, embedding

task_name = 'embedding'


def resolve(payload, **kwargs):
    param = 'Hawaiian pizza'
    return embedding(param)
