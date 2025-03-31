import logging

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.views import View

from .models import Book, ReadingSession
from .forms import BookForm, ReadingSessionForm, UserRegistrationForm

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["session_form"] = ReadingSessionForm()
        context["sessions"] = self.object.sessions.all().order_by("-date")
        context["total_minutes"] = self.object.sessions.aggregate(
            total=Sum("duration_minutes")
        )["total"] or 0
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReadingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.book = self.object
            session.save()
            logger.info(f"Added reading session for book: {self.object}")
            messages.success(request, f"Reading session logged: {session.duration_minutes} minutes.")
            return redirect("book-detail", pk=self.object.pk)
        else:
            logger.warning("Invalid ReadingSessionForm submission")
            context = self.get_context_data()
            context ["session_form"] = form
            return self.render_to_response(context)

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
    
class RegisterView(View):
    template_name = "registration/register.html"

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            logger.info(f"New user registered: {user.username}")
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")
        else:
            logger.warning(f"Registration attempt failed. Errors: {form.errors}")
        return render(request, self.template_name, {"form": form})
    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        logger.info(f"User logged in: {form.get_user().username}")
        return super().form_valid(form)