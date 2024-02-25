from datetime import datetime
from datetime import timedelta
import jwt
import xmltodict
import json

jwt_secret_key = "wookie_books_secret_key"


def encode_jwt(user):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'username': user.username,
        'exp': expiration_time
    }
    return jwt.encode(payload, jwt_secret_key, algorithm='HS256')


def decode_jwt(token):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None


def parse_payload(request):
    result = None
    content_type = request.headers.get('Content-Type', 'application/json')
    if content_type == 'application/xml':
        result = xmltodict.parse(request.get_data())['user']
    elif content_type == 'application/json':
        result = json.loads(request.get_data().decode('utf-8'))
    return result
