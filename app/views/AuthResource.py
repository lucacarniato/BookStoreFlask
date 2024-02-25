import json

from flask import request
from flask_restful import Resource
from .decorators import content_negotiation
from .utils import encode_jwt, parse_payload
from ..models import users
from ..models.storage import passwords
import xmltodict


class AuthResource(Resource):
    @content_negotiation
    def post(self):

        data = parse_payload(request)

        if not data:
            return {'error': 'Invalid payload, json or xml payload expected'}, 400

        username = data.get('username')
        password = data.get('password')

        user = next((u for u in users if u.username == username), None)

        if user and user.username in passwords and passwords[user.username] == password:
            token = encode_jwt(user)
            return {'token': token}
        else:
            return {'error': 'Invalid credentials'}, 401
