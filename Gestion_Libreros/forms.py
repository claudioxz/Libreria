from django.forms import ModelForm
from Gestion_Libreros.models import Edicion, Sello, default_error_messages, Editorial


class EdicionForm(ModelForm):
    class Meta:
        model = Edicion
        error_messages = default_error_messages
        fields = ['tipo_isbn', 'isbn', 'n_paginas', 'anno', 'idioma', 'tapa', 'encuadernado', 'sello', 'imagen']


class SelloForm(ModelForm):
    class Meta:
        model = Sello
        fields = ['nombre', 'editorial']



