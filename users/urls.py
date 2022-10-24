from django.urls import path

from users.views import register_view, LogOutView, reset_password, user_login


app_name = 'users'


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('password_reset/', reset_password, name='reset_password'),
]
