from django.shortcuts import render, redirect
from .models import Produkt
from django.shortcuts import render, get_object_or_404
from .forms import ProduktForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings



def base(request):
    return render(request, 'toole/base.html', {})
def o_firmie(request):
    return render(request, 'toole/o_firmie.html', {})
def oferta(request):
    return render(request, 'toole/oferta.html', {})
def realizacje(request):
	produkts = Produkt.objects.all()
	return render(request, 'toole/realizacje.html', {'produkts': produkts})
def produkt_detail(request, pk):
	produkt = get_object_or_404(Produkt, pk=pk)
	return render(request, 'toole/produkt_detail.html', {'produkt': produkt})
def kontakt(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			recipients = form.cleaned_data['from_email']
			name = form.cleaned_data['name']
			to_sender = ('Cześć {},'.format(name) + '\ndziękujemy za wiadomość! \nPozdrawiamy, \nZespół Toole')
			nowa = ('Masz nową wiadomość od: {}'.format(name))
			wiadomosc = ('Masz nową wiadomość od: {}'.format(name) + '\nE-mail: {}'.format(from_email) + '\nTytuł: {}'.format(subject) + '\nWiadomość: {}'.format(message))
			try:
				send_mail('Zespół Toole dziękuje za wiadomość', 
				to_sender, 
				from_email, 
				[recipients]
				)
				send_mail(nowa, wiadomosc, from_email, ['bastekforever@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('thanks')
	return render(request, "toole/kontakt.html", {'form': form})
	
def thanks(request):
    return render(request, "toole/thanks.html", {'thanks': thanks})
    
def produkt_new(request):
    if request.method == "POST":
        form = ProduktForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            produkt = form.save(commit=False)
            produkt.save()
            return redirect('produkt_detail', pk=produkt.pk)
    else:
        form = ProduktForm()
    return render(request, 'toole/produkt_new.html', {'form': form})
def produkt_edit(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    if request.method == "POST":
        form = ProduktForm(request.POST or None, request.FILES or None, instance=produkt)
        if form.is_valid():
            produkt = form.save(commit=False)
            produkt.save()
            return redirect('produkt_detail', pk=produkt.pk)
    else:
        form = ProduktForm(instance=produkt)
    return render(request, 'toole/produkt_new.html', {'form': form})
def produkt_remove(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    produkt.delete()
    return redirect('realizacje')

