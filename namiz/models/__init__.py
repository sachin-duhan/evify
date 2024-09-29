# models/__init__.py
from namiz.models.users import users
from namiz.models.courses import courses
from namiz.models.modules import modules
from namiz.models.lectures import lectures
from namiz.models.quizzes import quizzes
from namiz.models.certificates import certificates
from namiz.models.answers import answers

DOMAIN = {
    'users': users,
    'courses': courses,
    'modules': modules,
    'lectures': lectures,
    'quizzes': quizzes,
    'certificates': certificates,
    'answers': answers
}
