from django import forms
from .models import Appeal
from django.forms import widgets


class AppealForm(forms.ModelForm):
    text = forms.TextInput()
    class Meta:
        model = Appeal
        fields="__all__"