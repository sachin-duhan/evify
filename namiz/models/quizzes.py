# models/quizzes.py

quizzes = {
    'schema': {
        'module_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'modules',
                'field': '_id',
                'embeddable': True  # Allows embedding module details
            },
            'required': True,
        },
        'module_details': {  # Embedded module information
            'type': 'dict',
            'schema': {
                'title': {'type': 'string'},
                'course_id': {'type': 'objectid'}
            },
            'default': {}
        },
        'questions': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'question_text': {'type': 'string', 'required': True},
                    'options': {'type': 'list', 'schema': {'type': 'string'}, 'required': True},
                    'correct_answer': {'type': 'string', 'required': True}
                }
            }
        },
        'answers': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'question_id': {'type': 'objectid'},
                    'answer': {'type': 'string'}
                }
            }
        }
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'module_id'
    }
}
