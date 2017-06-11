from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages # error and success messages
from django.forms.models import model_to_dict
from django.contrib.auth.models import User # password recovery
from django.core.exceptions import ObjectDoesNotExist # password recovery - getting user by email


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
            else:
                return render(request, 'registration/login.html', {'form': form, 'registro': "True"})
        elif 'login-submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                messages.error(request, 'Fallo al entrar.', extra_tags='warning')
    return render(request, 'registration/login.html', {'form': form, 'registro': "False"})

def profile_view(request):
    form = SignUpForm(instance=request.user)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Sus datos han sido actualizados.')

        else:
            messages.error(request, 'Fallo al modificar.', extra_tags='danger')
    return render(request, 'principal/profile.html', {'form': form})

def recover_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User()
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user = None

        if user is not None:
            # aqui se genera una contraseña nueva y se envia esta por email a través del gestor de mensajeria correspondiente.
            messages.success(request, 'Se ha generado una contraseña nueva que ha sido enviada a su email.')
        else:
            messages.error(request, 'No se lo quien me dices.', extra_tags='warning')
    return render(request, 'registration/recover.html', {})
