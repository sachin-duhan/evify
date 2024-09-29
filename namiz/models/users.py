# models/users.py

users = {
    'schema': {
        'username': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 32,
            'required': True,
            'unique': True,
        },
        'email': {
            'type': 'string',
            'minlength': 6,
            'maxlength': 255,
            'required': True,
            'unique': True,
        },
        'role': {
            'type': 'string',
            'allowed': ['student', 'instructor'],
            'required': True
        },
        'enrolled_courses': {
            'type': 'list',
            'schema': {'type': 'objectid', 'data_relation': {'resource': 'courses', 'field': '_id', 'embeddable': True}},
            'default': []
        },
        'enrolled_courses_details': {  # Embedded enrolled courses information
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'}
                }
            },
            'default': []
        },
        'completed_courses': {
            'type': 'list',
            'schema': {'type': 'objectid', 'data_relation': {'resource': 'courses', 'field': '_id', 'embeddable': True}},
            'default': []
        },
        'completed_courses_details': {  # Embedded completed courses information
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'completion_date': {'type': 'datetime'}
                }
            },
            'default': []
        },
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    }
}
