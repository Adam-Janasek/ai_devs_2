def resolve(payload, **kwargs):
    message = ' '.join([
        'Tell me about yourself but replace name, surname, proffesion and city with given placeholders: %imie%,',
        '%nazwisko%, %zawod% and %miasto%,',
    ])
    return message
