from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView,DeleteView,DetailView

from django.core.mail import send_mail
from .models import Tasks#,Login,Register
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout ,login,update_session_auth_hash
from todo_app import settings
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.views import View


# Create your views here.


def mail(request):
    subject="Greetings"
    msg="congratulations for ur success"
    to='farzseenamrasheed@gmail.com'
    res=send_mail()

class TaskList(ListView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'tasklist.html'

class Taskcreate(CreateView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'

class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')     #after updation redirecting page
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')  # after updation redirecting page
    template_name = 'taskdelete.html'

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'taskdetail.html'

def Home(request):
    return render(request,'home.html')

def register_fun(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('login')
        messages.error(request, "Unsuccessful registration.Invalid Information")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_fun(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/task-list/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


