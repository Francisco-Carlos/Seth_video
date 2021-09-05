from Core.models import Usuarios,Videos
from django import forms
from django.contrib.auth.models import User

class Criar_UsuariosForms(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['Nikename','Foto',]
        widgets = {
            'nikename' : forms.TextInput(),
            'foto de perfil' : forms.FileInput(),

        }

