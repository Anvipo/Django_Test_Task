from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 max_length=32)
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             max_length=64,
                             error_messages={'required': 'Введите корректный email адрес',
                                             'invalid': 'Введёный email адрес некорректен'})

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('groups',)
