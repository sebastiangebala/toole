from django.shortcuts import render

def base(request):
    return render(request, 'toole/base.html', {})
def o_firmie(request):
    return render(request, 'toole/o_firmie.html', {})
def oferta(request):
    return render(request, 'toole/oferta.html', {})
def realizacje(request):
    return render(request, 'toole/realizacje.html', {})
def kontakt(request):
    return render(request, 'toole/kontakt.html', {})
