# models/courses.py

courses = {
    'schema': {
        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 255,
            'required': True,
        },
        'description': {
            'type': 'string',
        },
        'instructor_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'users',
                'field': '_id',
                'embeddable': True  # Allows embedding instructor details
            },
            'required': True,
        },
        'instructor_details': {  # Embedded instructor information
            'type': 'dict',
            'schema': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'role': {'type': 'string'}
            },
            'default': {}
        },
        'modules': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'modules',
                    'field': '_id',
                    'embeddable': True  # Allows embedding module details
                },
            },
        },
        'modules_details': {  # Embedded modules information
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'title': {'type': 'string'},
                    'lectures': {'type': 'list'},
                    'quiz': {'type': 'objectid'}
                }
            },
            'default': []
        },
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    }
}
