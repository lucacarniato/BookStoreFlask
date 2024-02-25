import xmltodict

def test_authenticate_endpoint_json(client, setup_mock_data):
    json_payload = {'username': 'test_user1', 'password': 'password1'}

    headers = {'Content-Type': 'application/json'}

    response = client.post('/auth', json=json_payload, headers=headers)
    assert response.status_code == 200
    assert 'token' in response.json


def test_authenticate_endpoint_xml(client, setup_mock_data):
    xml_payload = """
    <user>
        <username>test_user1</username>
        <password>password1</password>
    </user>
    """
    headers = {'Content-Type': 'application/xml'}

    response = client.post('/auth', data=xml_payload, headers=headers)
    assert response.status_code == 200
    response_dict = xmltodict.parse(response.get_data())
    assert 'token' in response_dict
