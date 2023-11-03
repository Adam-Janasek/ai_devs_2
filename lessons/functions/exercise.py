def resolve(payload, **kwargs):
    return {
        'name': 'addUser',
        'description': 'add user to the database',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'provide name of the user',
                },
                'surname': {
                    'type': 'string',
                    'description': 'provide surname of the user',
                },
                'year': {
                    'type': 'integer',
                    'description': 'provide year of born of the user',
                },
            },
        },
    }
