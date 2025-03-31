import logging
from django import forms
from .models import Book, ReadingSession
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "genre", "status", "rating")
        widgets = {
            "status": forms.Select(choices=Book.STATUS_CHOICES),
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.debug("BookForm initialised")

class ReadingSessionForm(forms.ModelForm):
    class Meta:
        model = ReadingSession
        fields = ("duration_minutes", "notes")
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.debug("ReadingSessionForm initialised")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get("password") != cd.get("password2"):
            raise forms.ValidationError("Passwords do not match.")
        return cd.get("password2")