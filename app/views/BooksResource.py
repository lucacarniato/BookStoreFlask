from flask import request
from flask_restful import Resource
from .decorators import content_negotiation
from ..models import books


class BooksResource(Resource):
    @content_negotiation
    def get(self):
        query = request.args.get('query')
        if query:
            filtered_books = [book.serialize() for book in books if query.lower() in book.title.lower()]
        else:
            filtered_books = [book.serialize() for book in books]
        return {'filtered_books': {'books': filtered_books}}
