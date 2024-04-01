from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from apps.meows.forms import MeowsForm
from apps.meows.models import Meow
from apps.users.forms import UserLoginForm, UserRegistrationForm
from apps.users.models import User

# Obtener el perfil de un usuario
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    meow = Meow.objects.filter(user=user)
    form = MeowsForm()
    return render(request, 'users/user_profile.html', {'user': user, 'meows': meow, 'form': form, 'navigation': 'false'})

# Registrar un usuario
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            login(request, user)
            return redirect('meows_app:meows_list')
        else:
            print(form.errors)
            return HttpResponse({'errors': form.errors}, status=400)
    else:
        print('No es un POST')
        return redirect('meows_app:meows_list')

# Loguear un usuario
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['email'],  # O el campo que uses como 'username'
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('meows_app:meows_list')
            else:
                return HttpResponse({'errors': 'Usuario o contraseña incorrectos'}, status=400)
        else:
            return HttpResponse({'errors': form.errors}, status=400)
    else:
        return redirect('meows_app:meows_list')

# Cerrar sesion
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('meows_app:meows_list')