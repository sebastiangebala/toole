from django.shortcuts import render
from .models import Produkt
from django.shortcuts import render, get_object_or_404
from .forms import ProduktForm
from django.shortcuts import redirect

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
    return render(request, 'toole/kontakt.html', {})
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
    return redirect('toole.views.realizacje')
