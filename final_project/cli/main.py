import typer
import os
import django

# Django Environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktracker.settings")
django.setup()

from books.models import Book, ReadingSessions
app = typer.Typer(help="📚 Book Tracker CLI 📚")

@app.command()
def add_book(
    title: str = typer.Option(..., help="Title of the book"),
    author: str = typer.Option(..., help="Author of the book"),
    genre: str = typer.Option("", help="Genre of the book"),
    status: str = typer.Option("to_read", help="Status: to_read, reading, or read"),
    rating: int = typer.Option(None, help="Optional rating (1 through 5)")
):
    """Add a new book to your reading list."""
    book = Book.objects.create(
        title=title,
        author=author,
        genre=genre,
        status=status,
        rating=rating,
    )
    typer.echo(f"✅ Added book: {book.title} by {book.author}")

if __name__ == "__main__":
    app()