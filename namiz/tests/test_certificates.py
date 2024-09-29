# tests/test_certificates.py
import pytest

def test_create_certificate(client, mongo_client):
    # Insert user and course
    db = mongo_client.get_database()
    user = db.users.insert_one({
        "username": "student1",
        "email": "student1@example.com",
        "role": "student",
        "enrolled_courses": [],
        "completed_courses": []
    })
    course = db.courses.insert_one({
        "title": "Python for Data Science",
        "description": "Learn Python in Data Science context.",
        "instructor_id": None,
        "modules": []
    })
    
    certificate_data = {
        "student_id": str(user.inserted_id),
        "course_id": str(course.inserted_id),
        "date": "2023-01-01T00:00:00Z"
    }
    response = client.post('/certificates', json=certificate_data)
    assert response.status_code == 201
    assert response.json['_items'][0]['student_id'] == str(user.inserted_id)

def test_get_certificates(client, mongo_client):
    # Insert sample certificate
    db = mongo_client.get_database()
    db.certificates.insert_one({
        "student_id": None,
        "course_id": None,
        "date": "2023-01-01T00:00:00Z"
    })
    
    response = client.get('/certificates')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1

def test_get_specific_certificate(client, mongo_client):
    # Insert sample certificate
    db = mongo_client.get_database()
    certificate = db.certificates.insert_one({
        "student_id": None,
        "course_id": None,
        "date": "2023-01-01T00:00:00Z"
    })
    certificate_id = str(certificate.inserted_id)
    
    response = client.get(f'/certificates/{certificate_id}')
    assert response.status_code == 200
    assert response.json['date'] == "2023-01-01T00:00:00Z"

def test_update_certificate(client, mongo_client):
    # Insert sample certificate
    db = mongo_client.get_database()
    certificate = db.certificates.insert_one({
        "student_id": None,
        "course_id": None,
        "date": "2023-01-01T00:00:00Z"
    })
    certificate_id = str(certificate.inserted_id)
    
    update_data = {
        "date": "2023-02-01T00:00:00Z"
    }
    response = client.patch(f'/certificates/{certificate_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['date'] == "2023-02-01T00:00:00Z"

def test_delete_certificate(client, mongo_client):
    # Insert sample certificate
    db = mongo_client.get_database()
    certificate = db.certificates.insert_one({
        "student_id": None,
        "course_id": None,
        "date": "2023-01-01T00:00:00Z"
    })
    certificate_id = str(certificate.inserted_id)
    
    response = client.delete(f'/certificates/{certificate_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.certificates.find_one({"_id": certificate.inserted_id}) is None

