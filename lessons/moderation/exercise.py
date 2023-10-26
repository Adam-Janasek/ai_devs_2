from openapi.utils import moderate

task_name = 'moderation'


def resolve(payload):
    sentences = payload.get('input')
    answers = []
    for sentence in sentences:
        answers.append(int(moderate(sentence)))
    return answers
