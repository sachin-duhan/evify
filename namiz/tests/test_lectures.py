# tests/test_lectures.py
import pytest

def test_create_lecture(client, mongo_client):
    # Insert module
    db = mongo_client.get_database()
    module = db.modules.insert_one({
        "course_id": None,
        "title": "Data Structures",
        "lectures": [],
        "quiz": None
    })
    module_id = str(module.inserted_id)
    
    lecture_data = {
        "module_id": module_id,
        "title": "Arrays and Lists",
        "video_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/arrays_and_lists.mp4",
        "notes_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/arrays_and_lists_notes.pdf"
    }
    response = client.post('/lectures', json=lecture_data)
    assert response.status_code == 201
    assert response.json['_items'][0]['title'] == "Arrays and Lists"

def test_get_lectures(client, mongo_client):
    # Insert sample lecture
    db = mongo_client.get_database()
    db.lectures.insert_one({
        "module_id": None,
        "title": "Linked Lists",
        "video_url": "",
        "notes_url": ""
    })
    
    response = client.get('/lectures')
    assert response.status_code == 200
    assert len(response.json['_items']) == 1
    assert response.json['_items'][0]['title'] == "Linked Lists"

def test_get_specific_lecture(client, mongo_client):
    # Insert sample lecture
    db = mongo_client.get_database()
    lecture = db.lectures.insert_one({
        "module_id": None,
        "title": "Trees",
        "video_url": "",
        "notes_url": ""
    })
    lecture_id = str(lecture.inserted_id)
    
    response = client.get(f'/lectures/{lecture_id}')
    assert response.status_code == 200
    assert response.json['title'] == "Trees"

def test_update_lecture(client, mongo_client):
    # Insert sample lecture
    db = mongo_client.get_database()
    lecture = db.lectures.insert_one({
        "module_id": None,
        "title": "Trees",
        "video_url": "",
        "notes_url": ""
    })
    lecture_id = str(lecture.inserted_id)
    
    update_data = {
        "title": "Advanced Trees"
    }
    response = client.patch(f'/lectures/{lecture_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['title'] == "Advanced Trees"

def test_delete_lecture(client, mongo_client):
    # Insert sample lecture
    db = mongo_client.get_database()
    lecture = db.lectures.insert_one({
        "module_id": None,
        "title": "Trees",
        "video_url": "",
        "notes_url": ""
    })
    lecture_id = str(lecture.inserted_id)
    
    response = client.delete(f'/lectures/{lecture_id}')
    assert response.status_code == 204
    
    # Verify deletion
    assert db.lectures.find_one({"_id": lecture.inserted_id}) is None

