from openai_api.utils import embedding


def resolve(payload, **kwargs):
    param = 'Hawaiian pizza'
    return embedding(param)
