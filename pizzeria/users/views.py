from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserForm

from django.contrib.auth.models import User

# Create your views here.

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return render(request, "users/user.html", {"message": None})
        else:
            return HttpResponse('failed.')

    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    user_data = User.objects.get(pk=request.user.id)

    context = {
        "user": request.user,
        "form": UserForm(instance=user_data)
    }
    return render(request, "users/user.html", context)

def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # authenticate(request)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('failed.')

    else:
        form = UserForm()

    return render(request, "users/register.html", {'form': form})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("users:user"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def profile(request):
    form = ProfileForm()
    return render(request, "users/user.html", {'form': form})
