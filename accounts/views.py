from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('loginview')
    return render(request, 'register.html', {'form': form})


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('adminview')
            else:
                messages.info(request, 'your not allowed to access this page!!')
        else:
            messages.info(request, 'username OR password incorrect')
    return render(request, 'login.html')


def loginstudent(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'username OR password incorrect')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('loginview')
