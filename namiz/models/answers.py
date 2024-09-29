# models/answers.py

answers = {
    'schema': {
        'question_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'quizzes',
                'field': '_id',
                'embeddable': True  # Allows embedding question details
            },
            'required': True,
        },
        'question_details': {  # Embedded question information
            'type': 'dict',
            'schema': {
                'question_text': {'type': 'string'},
                'options': {'type': 'list'},
                'correct_answer': {'type': 'string'}
            },
            'default': {}
        },
        'answer': {
            'type': 'string',
            'required': True
        }
    }
}
