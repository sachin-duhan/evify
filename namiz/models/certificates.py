# models/certificates.py

certificates = {
    'schema': {
        'student_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'users',
                'field': '_id',
                'embeddable': True  # Allows embedding student details
            },
            'required': True,
        },
        'student_details': {  # Embedded student information
            'type': 'dict',
            'schema': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'role': {'type': 'string'}
            },
            'default': {}
        },
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
        'date': {
            'type': 'datetime',
            'required': True,
        }
    },
    'additional_lookup': {
        'url': 'regex("[\\w]+")',
        'field': 'student_id'
    }
}
