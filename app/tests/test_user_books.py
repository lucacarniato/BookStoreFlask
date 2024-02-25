def test_user_books_resource(client, setup_mock_data, auth_token):
    url = '/user/books'
    headers = {'Authorization': auth_token, 'Content-Type': 'application/json'}

    # Test GET method
    response_get = client.get(url, headers=headers)
    assert response_get.status_code == 200
    response_dict = response_get.json
    assert 'books' in response_dict
    assert response_dict['books'][0]['title'] == 'Book 1'
    assert response_dict['books'][0]['description'] == 'Description 1'
    assert response_dict['books'][0]['author']['username'] == 'test_user1'
    assert response_dict['books'][0]['author']['author_pseudonym'] == 'Author1'
    assert response_dict['books'][0]['cover_image'] == 'cover1.jpg'
    assert response_dict['books'][0]['price'] == '19.99'

    # Test POST method
    data_post = {'title': 'Test Book', 'description': 'Test Description', 'cover_image': 'test.jpg', 'price': 19.99}
    response_post = client.post(url, json=data_post, headers=headers)
    assert response_post.status_code == 200
    response_lists = response_post.json
    assert 'message' in response_lists[0]
    assert response_lists[0]['message'] == 'Book published successfully'

    response_get = client.get(url, headers=headers)
    assert response_get.status_code == 200
    response_dict = response_get.json
    assert 'books' in response_dict


    assert response_dict['books'][1]['title'] == 'Test Book'
    assert response_dict['books'][1]['description'] == 'Test Description'
    assert response_dict['books'][1]['author']['username'] == 'test_user1'
    assert response_dict['books'][1]['author']['author_pseudonym'] == 'Author1'
    assert response_dict['books'][1]['cover_image'] == 'test.jpg'
    assert response_dict['books'][1]['price'] == '19.99'
