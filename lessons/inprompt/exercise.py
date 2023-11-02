from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    lesson_input = payload.get('input')
    question = payload.get('question')

    system_message = ' '.join([
      'Return only name of the person from given question.',
    ])
    name = chat_completion(system_message, question)

    info = ' '.join(list(filter(lambda phrase: name in phrase, lesson_input)))
    print(info)
    system_message = ' '.join([
      f'You know this about {name}: {info}.'
      'Return answer for the given question in Polish language.',
    ])

    return chat_completion(system_message, question)
