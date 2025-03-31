from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    RegisterView,
    CustomLoginView
)

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("add/", BookCreateView.as_view(), name="book-add"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/<int:pk>/edit", BookUpdateView.as_view(), name="book-edit"),
    path("book/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="book-list"), name="logout"),
]
