from app.models.storage import books

def test_user_book_detail_resource_json(client, setup_mock_data, auth_token):
    # Assuming you have a valid book_id for testing
    book_id = id(books[0])
    url = f'/user/books/{book_id}'
    headers = {'Authorization': auth_token, 'Content-Type': 'application/json'}

    # Test GET method
    response_get = client.get(url, headers=headers)

    assert response_get.status_code == 200
    response_dict = response_get.json
    assert 'book' in response_dict
    assert response_dict['book']['title'] == 'Book 1'
    assert response_dict['book']['description'] == 'Description 1'
    assert response_dict['book']['author']['username'] == 'test_user1'
    assert response_dict['book']['author']['author_pseudonym'] == 'Author1'
    assert response_dict['book']['cover_image'] == 'cover1.jpg'
    assert response_dict['book']['price'] == '19.99'

    # Test PUT method
    data_put = {'title': 'Updated Title', 'description': 'Updated Description'}
    response_put = client.put(url, json=data_put, headers=headers)
    assert response_put.status_code == 200
    response_dict = response_put.json
    assert 'message' in response_dict
    assert response_dict['message'] == 'Book updated successfully'

    response_get = client.get(url, headers=headers)
    assert response_get.status_code == 200
    response_dict = response_get.json

    assert response_dict['book']['title'] == 'Updated Title'
    assert response_dict['book']['description'] == 'Updated Description'
    assert response_dict['book']['author']['username'] == 'test_user1'
    assert response_dict['book']['author']['author_pseudonym'] == 'Author1'
    assert response_dict['book']['cover_image'] == 'cover1.jpg'
    assert response_dict['book']['price'] == '19.99'

    # Test DELETE method
    response_delete = client.delete(url, headers=headers)
    assert response_delete.status_code == 200
    response_dict = response_delete.json
    assert 'message' in response_dict
    assert response_dict['message'] =='Book unpublished successfully'

    response_get = client.get(url, headers=headers)
    assert response_get.status_code == 200
    response_dict = response_get.json
    assert 'error' in response_dict[0]
    assert response_dict[0]['error'] == 'Book not found or unauthorized'


def test_user_book_detail_resource_unauthorized_user_json(client, setup_mock_data, auth_token):
    # Assuming you have a valid book_id for testing
    book_id = id(books[1])
    url = f'/user/books/{book_id}'
    headers = {'Authorization': auth_token, 'Content-Type': 'application/json'}

    # Test GET method
    response_get = client.get(url, headers=headers)
    assert response_get.status_code == 200
    response_dict = response_get.json
    assert 'error' in response_dict[0]
    assert response_dict[0]['error'] == 'Book not found or unauthorized'

