from django import forms
from .models import Produkt, Partner
from django.forms import ModelForm, CharField, TextInput, extras

class ProduktForm(forms.ModelForm):


	class Meta:
		model = Produkt
		fields = ('title', 'text', 'image')

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Tytuł', 'class': 'top_width'}))
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Imię', 'class': 'top_width'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Twoja wiadomość', 'class': 'message_width'}))
	from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Twój e-mail', 'class': 'top_width'}))

class PartnerForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = ('title', 'link', 'image')
