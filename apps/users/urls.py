from django.urls import path

from apps.users.views import get_user, register_user, login_user, logout_user

app_name = 'users_app'

urlpatterns = [
    path('user/id/<str:user_id>', get_user, name='user_profile'),
    path('user/register', register_user, name='user_register'),
    path('user/login', login_user, name='user_login'),
    path('user/logout', logout_user, name='user_logout')
]