from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import CustomUserCreationForm, ResetPasswordForm
from users.services import register_user, password_change


def register_view(request):
    """
    Представление с регистрацией пользователя
    """
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            register_user(request, user_form=form)
            # Здесь будет редирект на главную
            return HttpResponse('Заглушка редиректа на главную/в лк')

    return render(request, template_name='users/register.html', context={'form': form})


class LogInView(LoginView):
    template_name = 'users/login.html'


class LogOutView(LogoutView):
    template_name = 'users/logout.html'


def reset_password(request):
    """
    Представление с регистрацией пользователя
    """
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            password_change(request, user_form=form)
            # Здесь будет редирект на главную
            return HttpResponse('Заглушка.'
                                'Ваш новый пароль qwerty1234.')

    form = ResetPasswordForm()

    return render(request, template_name='users/reset_password.html', context={'form': form})
