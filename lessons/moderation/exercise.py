from openapi.utils import moderate, is_flagged

task_name = 'moderation'


def resolve(payload, **kwargs):
    sentences = payload.get('input')
    answers = []
    for sentence in sentences:
        moderate_response = moderate(sentence)
        answers.append(int(is_flagged(moderate_response)))
    return answers
