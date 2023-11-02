from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    answers = []
    system_message = ' '.join([
      'Jestes pisarzem, ktory pisze blog.'
      'Napisz krotki akapit o tym co mowi podany punkt.'
      'Jesli mozna postaraj sie opisac kolejne kroki.',
    ])
    for topic in payload.get('blog'):
        answers.append(chat_completion(system_message, topic))
    return answers
