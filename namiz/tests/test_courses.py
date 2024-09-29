# tests/test_courses.py
import pytest

def test_create_course(client, mongo_client):
    # Insert instructor
    db = mongo_client.get_database()
    instructor = db.users.insert_one({
        "username": "instructor1",
        "email": "instructor1@example.com",
        "role": "instructor",
        "enrolled_courses": [],
        "completed_courses": []
    })
    instructor_id = str(instructor.inserted_id)
    
    course_data = {
        "title": "Advanced Python",
        "description": "Deep dive into Python.",
        "instructor_id": instructor_id,
        "modules": []
    }
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201
    assert response.json['_items'][0]['title'] == "Advanced Python"

def test_get_courses(client, mongo_client):
    # Insert sample course
    db = mongo_client.get_database()
    db.courses.insert_one({
        "title": "Data Science 101",
        "description": "Introduction to Data Science.",
        "instructor_id": None,
        "modules": []
    })
    
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1
    assert response.json['_items'][0]['title'] == "Data Science 101"

def test_get_specific_course(client, mongo_client):
    # Insert sample course
    db = mongo_client.get_database()
    course = db.courses.insert_one({
        "title": "Machine Learning",
        "description": "Learn machine learning concepts.",
        "instructor_id": None,
        "modules": []
    })
    course_id = str(course.inserted_id)
    
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    assert response.json['title'] == "Machine Learning"

def test_update_course(client, mongo_client):
    # Insert sample course
    db = mongo_client.get_database()
    course = db.courses.insert_one({
        "title": "Machine Learning",
        "description": "Learn machine learning concepts.",
        "instructor_id": None,
        "modules": []
    })
    course_id = str(course.inserted_id)
    
    update_data = {
        "description": "Updated description for Machine Learning."
    }
    response = client.patch(f'/courses/{course_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['description'] == "Updated description for Machine Learning."

def test_delete_course(client, mongo_client):
    # Insert sample course
    db = mongo_client.get_database()
    course = db.courses.insert_one({
        "title": "Machine Learning",
        "description": "Learn machine learning concepts.",
        "instructor_id": None,
        "modules": []
    })
    course_id = str(course.inserted_id)
    
    response = client.delete(f'/courses/{course_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.courses.find_one({"_id": course.inserted_id}) is None

