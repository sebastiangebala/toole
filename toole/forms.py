from django import forms
from .models import Produkt
from django.forms import ModelForm, CharField, TextInput, extras

class ProduktForm(forms.ModelForm):


	class Meta:
		model = Produkt
		fields = ('title', 'text', 'image')

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Tytuł'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Twoja wiadomość'}))
	from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Twój e-mail'}))
