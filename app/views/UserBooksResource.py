# Authenticated user endpoints
from flask import request
from flask_restful import Resource
from .decorators import content_negotiation
from .utils import decode_jwt
from ..models.Book import Book
from ..models import users, books

class UserBooksResource(Resource):
    @content_negotiation
    def get(self):
        token = request.headers.get('Authorization')
        decoded_token = decode_jwt(token)

        if decoded_token:
            username = decoded_token.get('username')

            user_books = [book.serialize() for book in books if book.author.username == username]
            return {'books': user_books}
        else:
            return {'error': 'Unauthorized'}, 401

    @content_negotiation
    def post(self):
        token = request.headers.get('Authorization')
        decoded_token = decode_jwt(token)

        if decoded_token:
            username = decoded_token.get('username')
            data = request.get_json()

            new_book = Book(
                title=data.get('title'),
                description=data.get('description'),
                author=next((user for user in users if user.username == username), None),
                cover_image=data.get('cover_image'),
                price=data.get('price')
            )

            books.append(new_book)
            return {'message': 'Book published successfully'}, 201
        else:
            return {'error': 'Unauthorized'}, 401

