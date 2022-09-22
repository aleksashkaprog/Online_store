from django.contrib.auth import authenticate, login

from users.models import CustomUser


def register_user(request, user_form) -> None:
    """
    Функция, создает пользователя и авторизует его
    """
    user_form.save()
    email = user_form.cleaned_data.get('email')
    raw_password = user_form.cleaned_data.get('password1')
    user = authenticate(email=email, password=raw_password)
    login(request, user)


def password_change(request, user_form) -> None:
    """
    Функция заглушка для представления восстановления пароля
    """
    email = user_form.cleaned_data.get('email')
    user = CustomUser.objects.get(email=email)
    user.set_password('qwerty1234')
    user.save()
