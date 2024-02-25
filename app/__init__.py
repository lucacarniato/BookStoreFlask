from flask import Flask
from flask_restful import Api
from app.views.AuthResource import AuthResource
from app.views.BooksResource import BooksResource
from app.views.UserBooksResource import UserBooksResource
from app.views.UserBookDetailResource import UserBookDetailResource

app = Flask(__name__)
api = Api(app)

api.add_resource(AuthResource, '/auth')
api.add_resource(BooksResource, '/books')
api.add_resource(UserBooksResource, '/user/books')
api.add_resource(UserBookDetailResource, '/user/books/<int:book_id>')
