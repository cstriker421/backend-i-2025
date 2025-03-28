import pytest
from django.urls import reverse
from books.models import Book

@pytest.mark.django_db
def test_list_books(client):
    Book.objects.create( # Creates a sample book
        title="1984",
        author="George Orwell",
        genre="Dystopian",
        status="read",
        rating=5
    )
    url = reverse("book-list")
    response = client.get(url)
    assert response.status_code == 200
    assert b"1984" in response.content

@pytest.mark.django_db
def test_detail_view(client):
    book = Book.objects.create(
        title="Brave New World",
        author="Aldous Huxley",
        genre="Sci-Fi",
        status="to_read",
        rating=4
    )
    url = reverse("book-detail", args=[book.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Brave New World" in response.content

@pytest.mark.django_db
def test_add_book(client):
    url = reverse("book-add")
    data = {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Sci-Fi",
        "status": "reading",
        "rating": 4
    }
    response = client.post(url, data)
    
    assert response.status_code == 302 # Should redirect after success
    assert Book.objects.filter(title="Fahrenheit 451").exists()

@pytest.mark.django_db
def test_update_book(client):
    book = Book.objects.create(
        title="Test Book",
        author="Author",
        genre="Genre",
        status="to_read",
        rating=3
    )
    url = reverse("book-edit", args=[book.id])
    data = {
        "title": "Updated Book",
        "author": "Author Updated",
        "genre": "Genre",
        "status": "reading",
        "rating": 5
    }
    response = client.post(url, data)
    assert response.status_code == 302
    book.refresh_from_db()
    assert book.title == "Updated Book"
    assert book.status == "reading"

@pytest.mark.django_db
def test_delete_book(client):
    book = Book.objects.create(
        title="Delete Me",
        author="Author",
        genre="Genre",
        status="to_read",
        rating=2
    )
    url = reverse("book-delete", args=[book.id])
    get_response = client.post(url)
    assert get_response.status_code == 200

    post_response = client.post(url, follow=True)
    assert post_response.status.code == 200
    assert not Book.objects.filter(id=book.id).exists()
