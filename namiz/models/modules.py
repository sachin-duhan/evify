# models/modules.py

modules = {
    'schema': {
        'course_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'courses',
                'field': '_id',
                'embeddable': True  # Allows embedding course details
            },
            'required': True,
        },
        'course_details': {  # Embedded course information
            'type': 'dict',
            'schema': {
                'title': {'type': 'string'},
                'description': {'type': 'string'}
            },
            'default': {}
        },
        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 255,
            'required': True,
        },
        'lectures': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'lectures',
                    'field': '_id',
                    'embeddable': True  # Allows embedding lecture details
                }
            }
        },
        'lectures_details': {  # Embedded lectures information
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'title': {'type': 'string'},
                    'video_url': {'type': 'string'},
                    'notes_url': {'type': 'string'}
                }
            },
            'default': []
        },
        'quiz': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'quizzes',
                'field': '_id',
                'embeddable': True  # Allows embedding quiz details
            }
        },
        'quiz_details': {  # Embedded quiz information
            'type': 'dict',
            'schema': {
                'questions': {'type': 'list'},
                'answers': {'type': 'list'}
            },
            'default': {}
        }
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    }
}
