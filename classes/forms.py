from django import forms


class ClassForm(forms.Form):
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}),
                            max_length=32)
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  max_length=32)
