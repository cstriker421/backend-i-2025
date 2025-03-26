from django.contrib import admin
from .models import Book, ReadingSession

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "rating")
    list_filter = ("status", "genre")

@admin.register(ReadingSession)
class ReadingSessionAdmin(admin.ModelAdmin):
    list_display = ("book", "date", "duration_minutes")
    list_filter = ("date",)