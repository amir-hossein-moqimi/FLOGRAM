from django import forms
from . import models

class CreationForm(forms.ModelForm):
    class Meta:
        model = models.CreateUser
        fields = ['username','Instagram','password','email','type']