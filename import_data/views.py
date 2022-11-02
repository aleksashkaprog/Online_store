from django.shortcuts import render, redirect
from django.views import View

from . import forms
from . import decorators


class ImportDataView(View):
    """Вьюха страница импорта данных в БД"""
    template_name = 'import_data/import_data.html'
    form = forms.LoadData

    @decorators.check_status_import_data
    def get(self, request):
        return render(request, self.template_name, context={
            'form': self.form()
        })

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.load(request)
            return redirect('import_data')
        return render(request, self.template_name, context={
            'form': form,
        })
