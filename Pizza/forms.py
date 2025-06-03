from django import forms
from .models import Kontakt, Porosi

class KontaktForm(forms.ModelForm):
    class Meta:
        model = Kontakt
        fields = ['emri', 'email', 'mesazhi']

class PorosiForm(forms.ModelForm):
    class Meta:
        model = Porosi
        fields = ['emri', 'numri', 'adresa', 'pijet', 'pizzat']




