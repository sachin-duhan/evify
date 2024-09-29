# tests/test_modules.py
import pytest

def test_create_module(client, mongo_client):
    # Insert course
    db = mongo_client.get_database()
    course = db.courses.insert_one({
        "title": "Web Development",
        "description": "Learn to build web applications.",
        "instructor_id": None,
        "modules": []
    })
    course_id = str(course.inserted_id)
    
    module_data = {
        "course_id": course_id,
        "title": "Frontend Development",
        "lectures": [],
        "quiz": None
    }
    response = client.post('/modules', json=module_data)
    assert response.status_code == 201
    assert response.json['_items'][0]['title'] == "Frontend Development"

def test_get_modules(client, mongo_client):
    # Insert sample module
    db = mongo_client.get_database()
    db.modules.insert_one({
        "course_id": None,
        "title": "Backend Development",
        "lectures": [],
        "quiz": None
    })
    
    response = client.get('/modules')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1
    assert response.json['_items'][0]['title'] == "Backend Development"

def test_get_specific_module(client, mongo_client):
    # Insert sample module
    db = mongo_client.get_database()
    module = db.modules.insert_one({
        "course_id": None,
        "title": "Database Design",
        "lectures": [],
        "quiz": None
    })
    module_id = str(module.inserted_id)
    
    response = client.get(f'/modules/{module_id}')
    assert response.status_code == 200
    assert response.json['title'] == "Database Design"

def test_update_module(client, mongo_client):
    # Insert sample module
    db = mongo_client.get_database()
    module = db.modules.insert_one({
        "course_id": None,
        "title": "Database Design",
        "lectures": [],
        "quiz": None
    })
    module_id = str(module.inserted_id)
    
    update_data = {
        "title": "Advanced Database Design"
    }
    response = client.patch(f'/modules/{module_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['title'] == "Advanced Database Design"

def test_delete_module(client, mongo_client):
    # Insert sample module
    db = mongo_client.get_database()
    module = db.modules.insert_one({
        "course_id": None,
        "title": "Database Design",
        "lectures": [],
        "quiz": None
    })
    module_id = str(module.inserted_id)
    
    response = client.delete(f'/modules/{module_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.modules.find_one({"_id": module.inserted_id}) is None

