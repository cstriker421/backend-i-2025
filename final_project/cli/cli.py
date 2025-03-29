import os
import sys
import typer
import django
import logging

from datetime import date
from django.db import models

# Logging Setup
logger = logging.getLogger(__name__)

# Django Environment
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booktracker.settings")
django.setup()

from books.models import Book, ReadingSession

# CLI Setup
app = typer.Typer(help="📚 Book Tracker CLI 📚")
book_app = typer.Typer(help="📖 Manage your books 📖")
app.add_typer(book_app, name="book")

# Styling Helper
def styled(text, color=typer.colors.WHITE, bold=False):
    return typer.style(text, fg=color, bold=bold)

# Global Callback (for --verbose)
@app.callback()
def main(verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logs")):
    log_level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format="[{asctime}] {levelname} {name}: {message}",
        style="{"
    )
    logger.debug("Verbose mode enabled")

# CLI Commands
@book_app.command("add") # Adds book with args for title, author, genre, reading status, and optional rating
def add_book(
    title: str = typer.Option(..., help="Title of the book"),
    author: str = typer.Option(..., help="Author of the book"),
    genre: str = typer.Option("", help="Genre of the book"),
    status: str = typer.Option("to_read", help="Status: to_read, reading, or read"),
    rating: int = typer.Option(None, help="Optional rating (1 through 5)")
):
    """    
    Add a new book to your reading list.
    """
    book = Book.objects.create(
        title=title,
        author=author,
        genre=genre,
        status=status,
        rating=rating,
    )
    logger.info(f"Added book: {book.title} by {book.author}")
    typer.echo(styled("✅ Book added successfully!", typer.colors.GREEN, bold=True))
    typer.echo(f"📘 {styled(book.title, typer.colors.CYAN)} by {book.author}")

@book_app.command("list") # Lists books with optional args to filter by reading status
def list_books(status: str = typer.Option(None, help="Filter books by status (to_read, reading, read)")):
    """    
    List all books. Optionally filter by reading status.
    """
    if status:
        books = Book.objects.filter(status=status)
        logger.debug(f"Filtering books by status: {status}")
    else:
        books = Book.objects.all()

    if not books.exists():
        typer.echo(styled("📭 No books found.", typer.colors.RED, bold=True))
        return

    for book in books:
        status_color = {
            "to_read": typer.colors.MAGENTA,
            "reading": typer.colors.BLUE,
            "read": typer.colors.GREEN
        }.get(book.status, typer.colors.WHITE)

        typer.echo(
            f"[{book.id}] {styled(book.title, typer.colors.CYAN, True)} by {book.author} — "
            f"Status: {styled(book.get_status_disply(), status_color)} | "
            f"Genre: {book.genre or 'N/A'}"
        )

@book_app.command("mark-read")
def mark_read(book_id: int = typer.Argument(..., help="ID of the book to mark as read")):
    """
    Mark a book's status as 'read'.
    """
    try:
        book = Book.objects.get(id=book_id)
        logger.debug(f"Found book with ID {book_id}")
    except Book.DoesNotExist:
        typer.echo(styled(f"❌ Book with ID {book_id} not found.", typer.colors.RED, True))
        logger.warning(f"Book with ID {book_id} not found.")
        raise typer.Exit(code=1)

    if book.status == "read":
        typer.echo(styled(f"✅ '{book.title}' is already marked as read.", typer.colors.YELLOW))
        logger.info(f"Book '{book.title}' already marked as read.")
        return

    book.status = "read"
    book.save()
    typer.echo(styled(f"📘 '{book.title}' marked as read. ✅", typer.colors.GREEN, True))
    logger.info(f"Book '{book.title}' marked as read.")

@book_app.command("log-reading") # Adds a reading log by minutes with date and optional notes
def log_reading(
    book_id: int = typer.Argument(..., help="ID of the book you read"),
    minutes: int = typer.Argument(..., help="Duration in minutes"),
    notes: str = typer.Option("", help="Optional notes about the session"),
):
    """
    Log a reading session for a book.
    """
    try:
        book = Book.objects.get(id=book_id)
        logger.debug(f"Found book with ID {book_id}")
    except Book.DoesNotExist:
        typer.echo(styled(f"❌ Book with ID {book_id} not found.", typer.colors.RED, True))
        logger.warning(f"Book with ID {book_id} not found.")
        raise typer.Exit(code=1)

    session = ReadingSession.objects.create(
        book=book,
        duration_minutes=minutes,
        notes=notes,
        date=date.today()
    )

    typer.echo(styled(f"🕒 Logged {minutes} min for '{book.title}' on {session.date}.", typer.colors.GREEN))
    if notes:
        typer.echo(f"📝 Notes: {styled(notes, typer.colors.BLUE)}")
    logger.info(f"Logged {minutes} minutes for '{book.title}'.")

@book_app.command("summary") # Shows a summary of total books, breaking down by status and showcasing total read time in mins
def summary():
    """
    Show a summary of your reading activity.
    """
    total_books = Book.objects.count()
    read_count = Book.objects.filter(status="read").count()
    reading_count = Book.objects.filter(status="reading").count()
    to_read_count = Book.objects.filter(status="to_read").count()

    total_minutes = ReadingSession.objects.aggregate(
        total=models.Sum("duration_minutes")
    )["total"] or 0

    typer.echo(styled("📚 Reading Summary 📚", typer.colors.YELLOW, True))
    typer.echo(styled("-" * 35, typer.colors.BRIGHT_BLACK))

    def line(label, value, color=typer.colors.WHITE):
        typer.echo(f"{label}: {styled(str(value), color, bold=True)}")

    line("📖 Total books", total_books)
    line("✅ Read", read_count, typer.colors.GREEN)
    line("📘 Reading", reading_count, typer.colors.BLUE)
    line("📥 To Read", to_read_count, typer.colors.MAGENTA)
    line("⏱️  Total time spent reading", f"{total_minutes} minutes", typer.colors.YELLOW)
    logger.info("Displayed reading summary.")

# Entry Point
def main():
    app()

if __name__ == "__main__":
    main()