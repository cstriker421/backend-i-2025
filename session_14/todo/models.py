from turtle import title
from django.db import models

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateField(null=False)
    is_done = models.BooleanField(null=False,blank=False,default=False)

    class Meta:
        db_table = "todo_tasks"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
