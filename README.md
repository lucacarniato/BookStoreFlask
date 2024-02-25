# Bookstore REST API Project

## Introduction
This project aims to implement a RESTful API for a bookstore using Python with Flask framework. 

## Tasks
- Implement the project using Python with Flask framework.
- Develop a REST API returning data in JSON or XML format based on the `Content-Type` header.
- Design a custom user model with an additional field for "author pseudonym".
- Create a book model comprising the fields: title, description, author (custom user model), cover image, and price, choosing appropriate data types.
- Provide an authentication endpoint allowing users to authenticate with the API using their username and password and return a JWT token.
- Implement REST endpoints for managing books, allowing GET operations for listing and viewing books, with optional search functionality using query parameters.
- Create REST resources for authenticated users, implementing CRUD operations and an endpoint to unpublish a book (DELETE).
- Develop API tests for all endpoints.