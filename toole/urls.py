from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^o_firmie/$', views.o_firmie, name='o_firmie'),
    url(r'^oferta/$', views.oferta, name='oferta'),
    url(r'^realizacje/$', views.realizacje, name='realizacje'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
]
