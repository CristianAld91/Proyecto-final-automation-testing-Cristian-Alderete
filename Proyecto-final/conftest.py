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
        "id": "11",
        "name": "Ash ketchum",
        "username": "ashketchum",
        "email": "ashketchum@gmail.com"
    }
    
def pytest_html_report_title(report):
    report.title = "API JSONPLACEHOLDER - POST"