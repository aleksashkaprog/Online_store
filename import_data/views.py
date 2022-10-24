from django.shortcuts import render
from django.views import View

from . import forms


class ImportDataView(View):
    template_name = 'import_data/import_data.html'
    form = forms.LoadData

    def get(self, request):
        return render(request, self.template_name, context={
            'form': self.form()
        })

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.load()
        return render(request, self.template_name, context={
            'form': self.form(),
        })
