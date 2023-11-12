from time import sleep

from openai_api.utils import chat_completion


def user_message(hints, bad_answer):
    return ' '.join([
        f"O kim mowa? ${' '.join(hints)}?",
        f'Podaj tylko imię i nazwisko. Jeśli nie wiesz zwróć tylko {bad_answer}',
    ])


def resolve(payload, **kwargs):
    hint = payload.get('hint')
    controller = kwargs.get('controller')

    hints = [hint]
    system_message = ' '
    bad_answer = '0'

    max_retries = 10
    retry_delay = 1

    for _ in range(max_retries):
        answer = chat_completion(system_message, user_message(hints, bad_answer))
        if answer != bad_answer:
            break

        sleep(retry_delay)
        controller.get_task_token()
        task_description = controller.get_task_description()
        hints.append(task_description.get('hint'))
    else:
        raise Exception('I dont know ;(')

    return answer
