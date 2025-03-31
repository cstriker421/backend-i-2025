import pytest
from django.urls import reverse, resolve
from books.views import (
    BookListView, 
    BookCreateView, 
    BookDetailView, 
    BookUpdateView, 
    BookDeleteView
)

@pytest.mark.parametrize(
    "name,kwargs,view_class",
    [
        ("book-list", {}, BookListView),
        ("book-add", {}, BookCreateView),
        ("book-detail", {"pk": 1}, BookDetailView),
        ("book-edit", {"pk": 1}, BookUpdateView),
        ("book-delete", {"pk": 1}, BookDeleteView),
    ]
)
def test_url_resolves_to_correct_view(name, kwargs, view_class):
    url = reverse(name, kwargs=kwargs)
    resolved = resolve(url)
    assert resolved.func.view_class == view_class
