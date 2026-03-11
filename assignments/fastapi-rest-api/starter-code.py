from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.get("/")
def read_root():
    return {"message": "FastAPI assignment is running."}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def create_book(book: Book):
    books.append(book.model_dump())
    return {"message": "Book added successfully.", "book": book}
