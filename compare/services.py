from django.shortcuts import redirect
from django.urls import reverse


class CompareServices:
    def delete_from_compare(self, pk):
        """Удаление товара из списка сравнения"""
        products_pk: list = self.session.get('compare')
        products_pk.remove(pk)
        self.session['compare'] = products_pk
        return redirect(reverse('compare'))
