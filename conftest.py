import pytest

@pytest.fixture
def posts_data():
    return {
        "title": "Mi primer post",
        "body": "Mi primer post de prueba",
        "userId": 1
    }
    
@pytest.fixture
def users_data():
    return {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@gmail.com"
    }    