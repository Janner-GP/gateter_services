from django.shortcuts import redirect, render

from apps.meows.forms import MeowsForm
from apps.meows.models import Meow
from apps.users.forms import UserLoginForm, UserRegistrationForm

def get_meows(request):
    meows = Meow.objects.all()

    context = {
        'welcome_text': 'true',
        'login_form': UserLoginForm(),
        'register_form': UserRegistrationForm(),
        'meows': meows,
        'navigation': 'true'
    }

    return render(request, 'meows/meows_list.html', context)

def create_meows(request):
    if request.method == 'POST':
        form_meow = MeowsForm(request.POST)
        if form_meow.is_valid():
            # Asignar el mismo usuario que esta logueado
            form_meow.instance.user = request.user
            form_meow.save()
            return redirect('users_app:user_profile', request.user.id)
    return render(request, 'meows/create_meow.html')