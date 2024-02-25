import pytest
from app.models.storage import users, books, passwords
from app.models.User import User
from app.models.Book import Book
from app import app

app.config['TESTING'] = True

BASE_URL = 'http://127.0.0.1:5000'


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


@pytest.fixture
def auth_token(client):
    json_payload = {'username': 'test_user1', 'password': 'password1'}

    headers = {'Content-Type': 'application/json'}

    response = client.post('/auth', json=json_payload, headers=headers)
    assert response.status_code == 200
    assert 'token' in response.json
    return response.json['token']


@pytest.fixture
def setup_mock_data():
    # Set up mock users
    user1 = User(username='test_user1', author_pseudonym='Author1')
    user2 = User(username='test_user2', author_pseudonym='Author2')
    users.extend([user1, user2])

    book1 = Book(title='Book 1', description='Description 1', author=user1, cover_image='cover1.jpg', price=19.99)
    book2 = Book(title='Book 2', description='Description 2', author=user2, cover_image='cover2.jpg', price=24.99)
    books.extend([book1, book2])

    passwords[user1.username] ='password1'
    passwords[user2.username] ='password2'

    yield

    # Teardown: Remove the mock data after the test
    users.clear()
    books.clear()
    passwords.clear()
