# tests/test_books.py
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app
from app import db #Import the db

client = TestClient(app)

def test_get_book_exists():
    # Assuming you have a book with ID 1 in your fake database
    book_id = 1
    response = client.get(f"/api/v1/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    # Add more assertions to check other fields of the book

def test_get_book_not_exists():
    # Assuming you don't have a book with ID 999
    book_id = 999
    response = client.get(f"/api/v1/books/{book_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"} # the book id is not found.

def test_get_all_books():
    response = client.get(f"/api/v1/books")
    assert response.status_code == 200
    assert len(response.json()) == len(db.books)
    # assert response.json() == db.books # this is more robust, but db.books needs to be json serializable.
