from .models import ViewsHistory


class PersonalAccount:

    def add_viewed_product(self, user, product):
        """ Добавление продукта в список просмотренных """
        try:
            history_object = ViewsHistory.objects.get(user=user, product=product)
            history_object.delete()
            history_object = ViewsHistory.objects.create(user=user, product=product)
            history_object.save()
        except ViewsHistory.DoesNotExist:
            history_object = ViewsHistory.objects.create(user=user, product=product)
            history_object.save()

    def delete_viewed_product(self, user, product):
        """ Удаление продукта из списка просмотренных """
        history_object = ViewsHistory.objects.get(user=user, product=product)
        history_object.delete()

    def get_last_viewed(self, user):
        """ Получение списка просмотренных продуктов """
        history_objects = ViewsHistory.objects.filter(user=user).all()
        return history_objects

    def is_viewed(self, user, product):
        """ Узнать, есть ли товар в списке просмотренных """
        try:
            ViewsHistory.objects.get(user=user, product=product)
            return True
        except ViewsHistory.DoesNotExist:
            return False

    def get_count_viewed(self, user):
        """ Получение количества просмотренных продуктов """
        history_objects = ViewsHistory.objects.filter(user=user).count()
        return history_objects

    def get_profile_data(self):
        """ Получение данных профиля """
        pass

    def set_profile_data(self):
        """ Внесение изменений в профиль """
        pass

    def get_order_history(self):
        """ Получение истории заказов """
        pass

    def get_order_data(self):
        """ Получение данных конкретного заказа """
        pass

    def registration(self):
        """ Регистрация """
        pass

    def authorization(self):
        """ Авторизация """
        pass

    def logout(self):
        """ Логаут """
        pass

    def restore_password(self):
        """ Восстановление пароля """
        pass
