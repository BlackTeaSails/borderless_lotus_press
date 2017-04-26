from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages



def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login/')
    else:
        return redirect('login/')


def reglog_view(request):
    logout(request)
    form = SignUpForm()
    if request.method == 'POST':
        if 'register-submit' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        elif 'login-submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                messages.error(request, 'Fallo al entrar.')
    return render(request, 'registration/login.html', {'form': form})

# Create your views here.
def index(request):
     return render(request, 'main/index.html')
