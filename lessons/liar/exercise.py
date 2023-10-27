from openapi.utils import chat_completion

task_name = 'liar'


def resolve(payload, **kwargs):
    question = 'What is capital of Poland?'
    controller = kwargs.get('controller')
    liar_answer = controller.post_task_description(question).get('answer', '')

    system_message = ' '.join([
      f'You are a validation checker: {question}'
      'Return YES/NO for the given answer.',
    ])
    return chat_completion(system_message, liar_answer)
