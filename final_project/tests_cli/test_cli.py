import pytest
from typer.testing import CliRunner
from cli import cli
from books.models import Book, ReadingSession

runner = CliRunner()

@pytest.mark.django_db
def test_add_book():
    result = runner.invoke(cli.app, [
        "book", "add",
        "--title", "Test Title",
        "--author", "Test Author",
        "--genre", "Test Genre",
        "--status", "reading",
        "--rating", "4"
    ])
    assert result.exit_code == 0
    assert "✅ Book added successfully!" in result.output
    assert Book.objects.filter(title="Test Title").exists()


@pytest.mark.django_db
def test_list_books():
    Book.objects.create(title="Dune", author="Frank Herbert", status="read")
    result = runner.invoke(cli.app, ["book", "list"])
    assert result.exit_code == 0
    assert "Dune" in result.output


@pytest.mark.django_db
def test_mark_read():
    book = Book.objects.create(title="Test", author="A", status="reading")
    result = runner.invoke(cli.app, ["book", "mark-read", str(book.id)])
    assert result.exit_code == 0
    assert "marked as read" in result.output
    book.refresh_from_db()
    assert book.status == "read"


@pytest.mark.django_db
def test_log_reading():
    book = Book.objects.create(title="LogMe", author="Log", status="read")
    result = runner.invoke(cli.app, [
        "book", "log-reading", str(book.id), "25", "--notes", "Focused session"
    ])
    assert result.exit_code == 0
    assert "Logged 25 min" in result.output
    assert ReadingSession.objects.filter(book=book, duration_minutes=25).exists()


@pytest.mark.django_db
def test_summary_output():
    Book.objects.create(title="S", author="A", status="read")
    result = runner.invoke(cli.app, ["book", "summary"])
    assert result.exit_code == 0
    assert "📚 Reading Summary 📚" in result.output
