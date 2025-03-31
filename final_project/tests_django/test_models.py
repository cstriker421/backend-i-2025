import pytest
from books.models import Book, ReadingSession

@pytest.mark.django_db
def test_book_str():
    book = Book.objects.create(
        title="Test Title",
        author="Test Author",
        genre="Test Genre",
        status="read",
        rating=4
    )
    assert str(book) == "Test Title by Test Author"

@pytest.mark.django_db
def test_reading_session_str():
    book = Book.objects.create(
        title="Test Book",
        author="Author",
        genre="Genre",
        status="reading",
        rating=3
    )
    session = ReadingSession.objects.create(
        book=book,
        duration_minutes=60,
        notes="Good session"
    )
    assert str(session) == f"{book.title} - {session.duration_minutes} min on {session.date}"
