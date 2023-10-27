task_name = 'helloapi'


def resolve(payload, **kwargs):
    return payload.get('cookie')
