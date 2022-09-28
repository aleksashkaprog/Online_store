from django.urls import path

from users.views import register_view, LogInView, LogOutView, reset_password

app_name = 'users'


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('password_reset/', reset_password, name='reset_password'),
]
