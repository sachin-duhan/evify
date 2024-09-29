# models/lectures.py

lectures = {
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
        'title': {
            'type': 'string',  # URL to S3 video
            'minlength': 1,
            'maxlength': 255,
            'required': True,
        },
        'video_url': {
            'type': 'string',  # URL to S3 video
        },
        'notes_url': {
            'type': 'string',  # URL to S3 notes
        }
    },
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'title'
    }
}
