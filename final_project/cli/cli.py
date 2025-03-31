import pytest
import json
from typer.testing import CliRunner
from django.contrib.auth.models import User
from cli import cli
from books.models import Book, ReadingSession

runner = CliRunner()

@pytest.fixture
def test_user(tmp_path):
    """Creates a test user and writes CLI session"""
    user = User.objects.create_user(username="cliuser", password="clipass")
    session_file = tmp_path / ".cli_session"
    session_file.write_text(json.dumps({"user_id": user.id}))
    return user, session_file

@pytest.mark.django_db
def test_register_and_login():
    # Register
    result = runner.invoke(cli.app, [
        "register",
        "--username", "newuser",
        "--password", "newpass"
    ])
    assert result.exit_code == 0
    assert "✅ User 'newuser' registered successfully!" in result.output
    assert User.objects.filter(username="newuser").exists()

    # Login
    result = runner.invoke(cli.app, [
        "login",
        "--username", "newuser",
        "--password", "newpass"
    ])
    assert result.exit_code == 0
    assert "✅ Logged in as 'newuser'" in result.output

@pytest.mark.django_db
def test_logout(tmp_path):
    user = User.objects.create_user(username="logoutuser", password="logoutpass")
    session_file = tmp_path / ".cli_session"
    session_file.write_text(json.dumps({"user_id": user.id}))

    result = runner.invoke(cli.app, ["logout"])
    assert result.exit_code == 0
    assert "👋 Logged out successfully." in result.output
    assert not session_file.exists()

@pytest.mark.django_db
def test_add_book(test_user):
    user, session_file = test_user
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
    assert Book.objects.filter(title="Test Title", user=user).exists()

@pytest.mark.django_db
def test_list_books(test_user):
    user, session_file = test_user
    Book.objects.create(title="Dune", author="Frank Herbert", status="read", user=user)

    result = runner.invoke(cli.app, ["book", "list"])
    assert result.exit_code == 0
    assert "Dune" in result.output

@pytest.mark.django_db
def test_mark_read(test_user):
    user, session_file = test_user
    book = Book.objects.create(title="Test", author="A", status="reading", user=user)

    result = runner.invoke(cli.app, ["book", "mark-read", str(book.id)])
    assert result.exit_code == 0
    assert "marked as read" in result.output
    book.refresh_from_db()
    assert book.status == "read"

@pytest.mark.django_db
def test_log_reading(test_user):
    user, session_file = test_user
    book = Book.objects.create(title="LogMe", author="Log", status="read", user=user)

    result = runner.invoke(cli.app, [
        "book", "log-reading", str(book.id), "25", "--notes", "Focused session"
    ])
    assert result.exit_code == 0
    assert "Logged 25 min" in result.output
    assert ReadingSession.objects.filter(book=book, duration_minutes=25).exists()

@pytest.mark.django_db
def test_summary_output(test_user):
    user, session_file = test_user
    Book.objects.create(title="S", author="A", status="read", user=user)

    result = runner.invoke(cli.app, ["book", "summary"])
    assert result.exit_code == 0
    assert "📚 Reading Summary 📚" in result.output
