import openai


def is_flagged(data):
    return data.get('results', [])[0].get('flagged', False)


def moderate(text):
    moderate_response = openai.Moderation.create(input=text)
    return moderate_response


def chat_completion(system_message, user_message, model='gpt-3.5-turbo'):
    completion_response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message},
        ],
    )
    return completion_response.choices[0].message.content


def image_recognize(user_message, img_url):
    completion_response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_message},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": img_url,
                        },
                    },
                ],
            }
        ],
    )
    return completion_response.choices[0].message.content


def embedding(text):
    embedding_response = openai.Embedding.create(
        input=text,
        model='text-embedding-ada-002',
    )
    return embedding_response['data'][0]['embedding']


def transcript(file):
    return openai.Audio.transcribe('whisper-1', file)
