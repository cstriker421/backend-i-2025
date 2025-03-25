from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('to_read', 'To Read'),
        ('reading', 'Reading'),
        ('read', 'Read')
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_read')
    rating = models.IntegerField(null=True, blank=True)  # Optional, out of 5

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class ReadingSessions(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField(auto_now_add=True)
    duration_minutes = models.PositiveBigIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.duration_minutes} min on {self.date}"