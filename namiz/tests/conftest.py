# tests/conftest.py
import pytest
from eve import Eve
from namiz.config import get_settings
from unittest import mock

@pytest.fixture
def app():
    # Mock the Config to use a test MongoDB URI
    with mock.patch('namiz.config.get_settings') as mock_get_settings:
        mock_settings = mock.Mock()
        mock_settings.MONGO_URI = 'mongodb://localhost:27017/test_eve_playground'
        mock_settings.LOG_LEVEL = 'DEBUG'
        mock_settings.DOMAIN = get_settings().DOMAIN  # Use existing DOMAIN
        mock_get_settings.return_value = mock_settings
        
        # Initialize Eve app
        app = Eve(settings='settings.py')
        
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(scope='session')
def mongo_client():
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/test_eve_playground')
    yield client
    client.close()

@pytest.fixture(autouse=True)
def run_around_tests(mongo_client):
    # Clean up the test database before each test
    db = mongo_client.get_database()
    for collection in db.list_collection_names():
        db[collection].delete_many({})
    yield
    # Clean up after tests
    for collection in db.list_collection_names():
        db[collection].delete_many({})

