import xmltodict


def test_get_books_endpoint_json(client, setup_mock_data, auth_token):
    headers = {'Authorization': auth_token, 'Content-Type': 'application/json'}
    response = client.get('/books', headers=headers)
    assert response.status_code == 200
    response_dict = response.json
    assert 'filtered_books' in response_dict
    assert 'books' in response_dict['filtered_books']
    books = response_dict['filtered_books']['books']
    assert len(books) == 2

    # Assertions for the first book (index 0)
    assert books[0]['title'] == 'Book 1'
    assert books[0]['description'] == 'Description 1'
    assert books[0]['author']['username'] == 'test_user1'
    assert books[0]['author']['author_pseudonym'] == 'Author1'
    assert books[0]['cover_image'] == 'cover1.jpg'
    assert books[0]['price'] == '19.99'

    # Assertions for the second book (index 1)
    assert books[1]['title'] == 'Book 2'
    assert books[1]['description'] == 'Description 2'
    assert books[1]['author']['username'] == 'test_user2'
    assert books[1]['author']['author_pseudonym'] == 'Author2'
    assert books[1]['cover_image'] == 'cover2.jpg'
    assert books[1]['price'] == '24.99'


def test_get_books_endpoint_xml(client, setup_mock_data, auth_token):
    headers = {'Authorization': auth_token, 'Content-Type': 'application/xml'}
    response = client.get('/books', headers=headers)
    assert response.status_code == 200
    response_dict = xmltodict.parse(response.get_data())
    assert 'filtered_books' in response_dict
    assert 'books' in response_dict['filtered_books']
    books = response_dict['filtered_books']['books']
    assert len(books) == 2

    # Assertions for the first book (index 0)
    assert books[0]['title'] == 'Book 1'
    assert books[0]['description'] == 'Description 1'
    assert books[0]['author']['username'] == 'test_user1'
    assert books[0]['author']['author_pseudonym'] == 'Author1'
    assert books[0]['cover_image'] == 'cover1.jpg'
    assert books[0]['price'] == '19.99'

    # Assertions for the second book (index 1)
    assert books[1]['title'] == 'Book 2'
    assert books[1]['description'] == 'Description 2'
    assert books[1]['author']['username'] == 'test_user2'
    assert books[1]['author']['author_pseudonym'] == 'Author2'
    assert books[1]['cover_image'] == 'cover2.jpg'
    assert books[1]['price'] == '24.99'
