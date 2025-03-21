from django.views.generic import ListView, TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm
from todo.models import Task
from django.contrib.auth import get_user

#def index(request):
#    tasks = Task.objects.all()
#    return render(request,"todo/index.html", {"foo":"BAR", "tasks":tasks})

class TaskListView(ListView):
    login_url = "/signin"
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user).all()

class IndexView(TemplateView):
    http_method_name = ['get']
    template_name = "todo/index.html"

class SignUpView(FormView):
    template_name =  "registration/signup.html"
    success_url = "/"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)