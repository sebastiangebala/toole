from django import forms
from .models import Produkt
from django.forms import ModelForm, CharField, TextInput, extras

class ProduktForm(forms.ModelForm):


	class Meta:
		model = Produkt
		fields = ('title', 'text', 'image')
