import os
from django.shortcuts import render, redirect
from .models import Produkt, Partner, Kariera
from django.shortcuts import render, get_object_or_404
from .forms import ProduktForm, PartnerForm, ContactForm, KarieraForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def base(request):
    return render(request, 'toole/base.html', {})
def o_firmie(request):
    return render(request, 'toole/o_firmie.html', {})
def oferta(request):
    return render(request, 'toole/oferta.html', {})
def kariera(request):
	karieras = Kariera.objects.all()
	return render(request, 'toole/kariera.html', {'karieras': karieras})
def partner(request):
	partners = Partner.objects.all()
	return render(request, 'toole/partner.html', {'partners': partners})
def realizacje(request):
	produkts = Produkt.objects.all()
	return render(request, 'toole/realizacje.html', {'produkts': produkts})
def produkt_detail(request, pk):
	produkt = get_object_or_404(Produkt, pk=pk)
	return render(request, 'toole/produkt_detail.html', {'produkt': produkt})
def partner_detail(request, pk):
	partner = get_object_or_404(Partner, pk=pk)
	return render(request, 'toole/partner_detail.html', {'partner': partner})
def kariera_detail(request, pk):
	kariera = get_object_or_404(Kariera, pk=pk)
	return render(request, 'toole/kariera_detail.html', {'kariera': kariera})
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
			to_sender = ('Cześć {},'.format(name) + '\n\ndziękujemy za wiadomość! \n\nPozdrawiamy, \n\nZespół Toole \n\nTa wiadomość została wygenerowana automatycznie. Prosimy nie odpowiadaj na nią')
			nowa = ('Masz nową wiadomość od: {}'.format(name))
			wiadomosc = ('Masz nową wiadomość od: {}'.format(name) + '\n\nE-mail: {}'.format(from_email) + '\n\nTytuł: {}'.format(subject) + '\n\nWiadomość: {}'.format(message))
			try:
				send_mail('Zespół Toole dziękuje za wiadomość', 
				to_sender, 
				from_email, 
				[recipients]
				)
				send_mail(nowa, wiadomosc, from_email, ['kontakt@toole.pl'])
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



def partner_new(request):
	if request.method == "POST":
		form = PartnerForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			partner = form.save(commit=False)
			partner.save()
			return redirect('partner_detail', pk=partner.pk)
	else:
		form = PartnerForm()
	return render(request, 'toole/partner_new.html', {'form': form})
def partner_edit(request, pk):
	partner = get_object_or_404(Partner, pk=pk)
	if request.method == "POST":
		form = PartnerForm(request.POST or None, request.FILES or None, instance=partner)
		if form.is_valid():
			partner = form.save(commit=False)
			partner.save()
			return redirect('partner_detail', pk=partner.pk)
	else:
		form = PartnerForm(instance=partner)
	return render(request, 'toole/partner_new.html', {'form': form})
def partner_remove(request, pk):
	partner = get_object_or_404(Partner, pk=pk)
	partner.delete()
	return redirect('partner')



def kariera_new(request):
	if request.method == "POST":
		form = KarieraForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			kariera = form.save(commit=False)
			kariera.save()
			return redirect('kariera')
	else:
		form = KarieraForm()
	return render(request, 'toole/kariera_new.html', {'form': form})
def kariera_edit(request, pk):
	kariera = get_object_or_404(Kariera, pk=pk)
	if request.method == "POST":
		form = KarieraForm(request.POST or None, request.FILES or None, instance=kariera)
		if form.is_valid():
			kariera = form.save(commit=False)
			kariera.save()
			return redirect('kariera')
	else:
		form = KarieraForm(instance=kariera)
	return render(request, 'toole/kariera_new.html', {'form': form})
def kariera_remove(request, pk):
	kariera = get_object_or_404(Kariera, pk=pk)
	kariera.delete()
	return redirect('kariera')

	    







