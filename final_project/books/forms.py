import logging

logger = logging.getLogger(__name__)

from django import forms
from .models import Book

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
