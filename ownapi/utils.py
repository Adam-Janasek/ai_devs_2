import openai

from ownapi.models import db, Message


def get_messages(user_id):
    return Message.query.filter_by(user_id=user_id).all()


def save_message(user_id, message_text):
    new_message = Message(user_id=user_id, message=message_text)
    db.session.add(new_message)
    db.session.commit()


def chat_completion(system_message, user_message, model='gpt-3.5-turbo'):
    completion_response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message},
        ],
    )
    return completion_response.choices[0].message.content
