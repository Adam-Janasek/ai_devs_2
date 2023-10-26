import openai


def is_flagged(data):
    return data.get('results', [])[0].get('flagged', False)


def moderate(text):
    moderate_response = openai.Moderation.create(input=text)
    return moderate_response


def chat_completion(system_message, user_message):
    completion_response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message},
        ],
    )
    return completion_response.choices[0].message.content
