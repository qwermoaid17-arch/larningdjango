from django import forms
from .models import login

class login_form(forms.ModelForm):

    class Meta:
        model= login
        fields='__all__'
        widgets = {'password': forms.PasswordInput()}