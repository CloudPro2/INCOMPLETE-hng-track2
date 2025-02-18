from fastapi import APIRouter, HTTPException
from app.models.book import Book
from app.db import db

router = APIRouter()

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((book for book in db.books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
