from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("add/", BookCreateView.as_view(), name="book-add"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/<int:pk>/edit", BookUpdateView.as_view(), name="book-edit"),
    path("book/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
]
