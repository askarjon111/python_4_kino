from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')
