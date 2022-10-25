from django import forms
from django.utils.translation import gettext_lazy as _

from . import tools

import json
import xmltodict
import importlib


class LoadData(forms.Form):

    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': '',
            }
        )
    )

    @classmethod
    def check_file(cls, file):
        file_type = file.name.split('.')[-1]
        return file_type

    @classmethod
    def methods(cls, key):
        methods_dict = {
            'json': json.loads,
            'xml': xmltodict.parse,
        }
        return methods_dict.get(key)

    def import_data(self):
        file = self.cleaned_data.get('file')
        file_type = self.check_file(file)
        method = self.methods(file_type)

        with file.open() as f:
            data = method(f.read())
        return data

    def load_data(self):
        data = self.import_data()
        return data

    def load(self):
        data = self.load_data()
        tools.import_data_to_db.delay(data)
        return None
