# tests/test_users.py
import pytest

def test_create_user(client):
    user_data = {
        "username": "jane_doe",
        "email": "jane@example.com",
        "role": "student"
    }
    response = client.post('/users', json=user_data)
    assert response.status_code == 201
    assert "jane_doe" in response.json['_items'][0]['username']
    assert response.json['_items'][0]['email'] == "jane@example.com"

def test_get_users(client, mongo_client):
    # Insert sample user
    db = mongo_client.get_database()
    db.users.insert_one({
        "username": "john_doe",
        "email": "john@example.com",
        "role": "instructor",
        "enrolled_courses": [],
        "completed_courses": []
    })
    
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1
    assert response.json['_items'][0]['username'] == "john_doe"

def test_get_specific_user(client, mongo_client):
    # Insert sample user
    db = mongo_client.get_database()
    user = db.users.insert_one({
        "username": "john_doe",
        "email": "john@example.com",
        "role": "instructor",
        "enrolled_courses": [],
        "completed_courses": []
    })
    user_id = str(user.inserted_id)
    
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json['username'] == "john_doe"

def test_update_user(client, mongo_client):
    # Insert sample user
    db = mongo_client.get_database()
    user = db.users.insert_one({
        "username": "john_doe",
        "email": "john@example.com",
        "role": "instructor",
        "enrolled_courses": [],
        "completed_courses": []
    })
    user_id = str(user.inserted_id)
    
    update_data = {
        "email": "john_new@example.com"
    }
    response = client.patch(f'/users/{user_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['email'] == "john_new@example.com"

def test_delete_user(client, mongo_client):
    # Insert sample user
    db = mongo_client.get_database()
    user = db.users.insert_one({
        "username": "john_doe",
        "email": "john@example.com",
        "role": "instructor",
        "enrolled_courses": [],
        "completed_courses": []
    })
    user_id = str(user.inserted_id)
    
    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.users.find_one({"_id": user.inserted_id}) is None

