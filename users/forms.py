

from django.forms.widgets import HiddenInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields =['username','picture']