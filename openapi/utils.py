import openai


def is_flagged(data):
    return data.get('results', [])[0].get('flagged', False)


def moderate(text):
    moderate_response = openai.Moderation.create(input=text)
    return is_flagged(moderate_response)
