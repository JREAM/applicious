from datetime import datetime
from django.conf.urls import patterns, url
from listing import views

urlpatterns = [
    url(r'^$', views.listings, name='listings'),
    url(r'^create/$', views.create, name='listing_create'),
    url(r'^edit/(?P<slug>)/$', views.edit, name='listing_edit'),
    url(r'^delete/(?P<slug>)/$', views.delete, name='listing_delete'),
    url(r'^pay/(?P<slug>)/$', views.pay, name='listing_pay'),
    url(r'^(?P<slug>)/$', views.view, name='listing_view'),
]
