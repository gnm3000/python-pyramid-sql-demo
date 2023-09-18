import pytest
from webtest import TestApp

from main import main
@pytest.fixture
def app():
    return TestApp(main())

def test_hello_route(app):
    response = app.get('/')
    assert response.status_code == 200
    assert 'hello' in response.text
    
def test_genre_table_route(app):
    response = app.get('/db/Chinook/Genre/GenreId/2.html')
    assert response.status_code == 200
    assert 'Jazz' in response.text
def test_customer_table_route(app):
    response = app.get('/db/Chinook/Customer/FirstName/Helena.html')
    assert response.status_code == 200
    assert 'Helena' in response.text

    

if __name__ == '__main__':
    pytest.main()