from django import forms

from .models import *


class TeacherForm(forms.Form):
    model = Teacher

    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}),
                                max_length=32)
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 max_length=32)
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
