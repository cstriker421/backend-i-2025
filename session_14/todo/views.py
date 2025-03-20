from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo":"BAR", "tasks":tasks})

class IndexView(ListView):
    model = Task