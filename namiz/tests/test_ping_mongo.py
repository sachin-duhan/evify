# tests/test_ping_mongo.py
def test_ping_mongo(client, mongo_client):
    response = client.get('/ping-mongo')
    assert response.status_code == 200
    assert response.json['mongo_status'] == "OK"

