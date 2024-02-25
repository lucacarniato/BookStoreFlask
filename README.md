# Bookstore REST API Project

## Introduction
This project aims to implement a RESTful API for a bookstore using Python with Flask framework. 
The bookstore platform is envisioned to enable Wookies, led by Lohgarra, to self-publish their adventures and sell them online. The profits generated from book sales will be utilized to procure medical supplies for an impoverished Ewok settlement.

## Tasks
- Implement the project using Python with Flask framework.
- Develop a REST API returning data in JSON or XML format based on the `Content-Type` header.
- Design a custom user model with an additional field for "author pseudonym".
- Create a book model comprising the fields: title, description, author (custom user model), cover image, and price, choosing appropriate data types.
- Provide an authentication endpoint allowing users to authenticate with the API using their username and password and return a JWT token.
- Implement REST endpoints for managing books, allowing GET operations for listing and viewing books, with optional search functionality using query parameters.
- Create REST resources for authenticated users, implementing CRUD operations and an endpoint to unpublish a book (DELETE).
- Develop API tests for all endpoints.

## Evaluation Criteria
- Adherence to Python best practices.
- Proper implementation of models, configuration, and tests, ensuring adherence to best practices with Flask framework.
- Thorough API testing for all implemented endpoints.
- Implementation ensuring users can only unpublish their own books.
- Bonus: Ensure Darth Vader is unable to publish his work on Wookie Books.
