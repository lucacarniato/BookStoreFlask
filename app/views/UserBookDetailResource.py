# Authenticated user endpoints
from flask import request
from flask_restful import Resource
from .decorators import content_negotiation
from .utils import decode_jwt
from ..models import books
from ..models import users, Book

class UserBookDetailResource(Resource):
    @content_negotiation
    def get(self, book_id):
        token = request.headers.get('Authorization')
        decoded_token = decode_jwt(token)

        if decoded_token:
            username = decoded_token.get('username')
            user_book = next((book for book in books if book.author.username == username and book_id == id(book)), None)

            if user_book:
                return {'book': user_book.serialize()}
            else:
                return {'error': 'Book not found or unauthorized'}, 404
        else:
            return {'error': 'Unauthorized'}, 401

    @content_negotiation
    def put(self, book_id):
        token = request.headers.get('Authorization')
        decoded_token = decode_jwt(token)

        if decoded_token:
            username = decoded_token.get('username')
            user_book = next((book for book in books if book.author.username == username and book_id == id(book)), None)

            if user_book:
                data = request.get_json()
                user_book.title = data.get('title', user_book.title)
                user_book.description = data.get('description', user_book.description)
                user_book.cover_image = data.get('cover_image', user_book.cover_image)
                user_book.price = data.get('price', user_book.price)
                return {'message': 'Book updated successfully'}
            else:
                return {'error': 'Book not found or unauthorized'}, 404
        else:
            return {'error': 'Unauthorized'}, 401

    @content_negotiation
    def delete(self, book_id):
        token = request.headers.get('Authorization')
        decoded_token = decode_jwt(token)

        if decoded_token:
            username = decoded_token.get('username')
            user_book = next((book for book in books if book.author.username == username and book_id == id(book)), None)

            if user_book:
                books.remove(user_book)
                return {'message': 'Book unpublished successfully'}
            else:
                return {'error': 'Book not found or unauthorized'}, 404
        else:
            return {'error': 'Unauthorized'}, 401