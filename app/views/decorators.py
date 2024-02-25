from flask import request, jsonify, Response
import xmltodict

def content_negotiation(func):
    def wrapper(*args, **kwargs):
        content_type = request.headers.get('Content-Type', 'application/json')
        if content_type == 'application/xml':
            return Response(xmltodict.unparse(func(*args, **kwargs)), content_type='application/xml')
        else:
            return jsonify(func(*args, **kwargs))
    return wrapper