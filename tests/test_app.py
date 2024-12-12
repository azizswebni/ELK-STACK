import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_upload_logs(client):
    data = {'file': (open('test_logs.csv', 'rb'), 'test_logs.csv')}
    response = client.post('/upload', data=data)
    assert response.status_code == 200

def test_search_logs(client):
    response = client.get('/search?query=test')
    assert response.status_code == 200
    
def test_kibana_dashboard(client):
    response = client.get('/kibana_dashboard?dashboard_id=test-dashboard')
    assert response.status_code == 200