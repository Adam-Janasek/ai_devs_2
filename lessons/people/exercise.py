import json

from openai_api.utils import chat_completion


def resolve(payload, **kwargs):
    question = payload.get('question')

    system_message = ''
    user_message = f'zwróć tylko pełnę imię i nazwisko w mianowniku z tego pytania: {question}'
    name = chat_completion(system_message, user_message)

    with open('lessons/people/people.json', 'r') as file:
        data = json.load(file)

    person_info = None
    for person in data:
        if person['imie'] in name and person['nazwisko'] in name:
            person_info = person
            break

    user_message = f'na podstawie: {person_info}, odpowiedz na pytanie: {question}'
    return chat_completion(system_message, user_message)
