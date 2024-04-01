from django.urls import path

from apps.meows.views import create_meows, get_meows

app_name = 'meows_app'

urlpatterns = [
    path('', get_meows, name='meows_list'),
    path('create', create_meows, name='create_meows')
]
