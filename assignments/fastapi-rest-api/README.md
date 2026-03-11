# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice route creation, request handling, and JSON responses. By the end of this assignment, students will have a working API with both read and write endpoints.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application and implement endpoints that return data about books. Start with a health check route and a route that returns a list of books.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome or status message.
- Add a `GET /books` endpoint that returns a JSON list of at least three books.

### 🛠️ Add Data Submission and Validation

#### Description
Extend the API by allowing users to add a new book. Use a Pydantic model to validate incoming data before adding it to the in-memory list.

#### Requirements
Completed program should:

- Define a `Book` Pydantic model with `id`, `title`, and `author` fields.
- Add a `POST /books` endpoint that accepts a new book and appends it to the list.
- Return a clear success response containing the created book.
- Keep data in memory (no database required for this assignment).
