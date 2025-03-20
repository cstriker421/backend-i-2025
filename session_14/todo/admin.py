from django.contrib import admin
from todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "due_date", "is_done")
    list_editable = ("due_date", "is_done")
    sortable_by = ("title", "due_date", "is_done" )

admin.site.register(Task,TaskAdmin)