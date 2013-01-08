from django import forms
from apps.database.models import Perfil
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil