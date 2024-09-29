# tests/test_quizzes.py
import pytest

def test_create_quiz(client, mongo_client):
    # Insert module
    db = mongo_client.get_database()
    module = db.modules.insert_one({
        "course_id": None,
        "title": "Algorithms",
        "lectures": [],
        "quiz": None
    })
    module_id = str(module.inserted_id)
    
    quiz_data = {
        "module_id": module_id,
        "questions": [
            {
                "question_text": "What is the time complexity of binary search?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
                "correct_answer": "O(log n)"
            }
        ],
        "answers": []
    }
    response = client.post('/quizzes', json=quiz_data)
    assert response.status_code == 201
    assert response.json['_items'][0]['questions'][0]['question_text'] == "What is the time complexity of binary search?"

def test_get_quizzes(client, mongo_client):
    # Insert sample quiz
    db = mongo_client.get_database()
    db.quizzes.insert_one({
        "module_id": None,
        "questions": [],
        "answers": []
    })
    
    response = client.get('/quizzes')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1

def test_get_specific_quiz(client, mongo_client):
    # Insert sample quiz
    db = mongo_client.get_database()
    quiz = db.quizzes.insert_one({
        "module_id": None,
        "questions": [],
        "answers": []
    })
    quiz_id = str(quiz.inserted_id)
    
    response = client.get(f'/quizzes/{quiz_id}')
    assert response.status_code == 200
    assert response.json['_id'] == quiz_id

def test_update_quiz(client, mongo_client):
    # Insert sample quiz
    db = mongo_client.get_database()
    quiz = db.quizzes.insert_one({
        "module_id": None,
        "questions": [],
        "answers": []
    })
    quiz_id = str(quiz.inserted_id)
    
    update_data = {
        "questions": [
            {
                "question_text": "What is 2+2?",
                "options": ["3", "4", "5"],
                "correct_answer": "4"
            }
        ]
    }
    response = client.patch(f'/quizzes/{quiz_id}', json=update_data)
    assert response.status_code == 200
    assert len(response.json['questions']) == 1
    assert response.json['questions'][0]['question_text'] == "What is 2+2?"

def test_delete_quiz(client, mongo_client):
    # Insert sample quiz
    db = mongo_client.get_database()
    quiz = db.quizzes.insert_one({
        "module_id": None,
        "questions": [],
        "answers": []
    })
    quiz_id = str(quiz.inserted_id)
    
    response = client.delete(f'/quizzes/{quiz_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.quizzes.find_one({"_id": quiz.inserted_id}) is None

