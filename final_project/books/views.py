import logging
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

logger = logging.getLogger(__name__)

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        logger.info("Fetching book list")
        return super().get_queryset()

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        logger.info(f"Creating book: {form.cleaned_data.get('title')}")
        return super().form_valid(form)

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_object(self, queryset=None):
        book = super().get_object(queryset)
        logger.info(f"Viewing book: {book}")
        return book

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        logger.info(f"Updating book: {form.cleaned_data.get('title')}")
        return super().form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        logger.warning(f"Deleting book: {book}")
        return super().delete(request, *args, **kwargs)