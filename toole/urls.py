from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.base, name='base'),
	url(r'^o_firmie/$', views.o_firmie, name='o_firmie'),
	url(r'^oferta/$', views.oferta, name='oferta'),
	url(r'^realizacje/$', views.realizacje, name='realizacje'),
	url(r'^kontakt/$', views.kontakt, name='kontakt'),
	url(r'^produkt/(?P<pk>[0-9]+)/$', views.produkt_detail, name='produkt_detail'),
	url(r'^produkt/new/$', views.produkt_new, name='produkt_new'),
	url(r'^produkt/(?P<pk>[0-9]+)/edit/$', views.produkt_edit, name='produkt_edit'),
	url(r'^produkt/(?P<pk>\d+)/remove/$', views.produkt_remove, name='produkt_remove'),
	url(r'^thanks/$', views.thanks, name='thanks'),
]
