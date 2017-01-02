from datetime import datetime
from django.conf.urls import patterns, url
from deployment import views

urlpatterns = [
    url(r'^$', views.deployment, name='deployment'),
    url(r'^category/$', views.category_list, name='deployment_category_list'),
    url(r'^category/(<?P<slug>)/$', views.category, name='deployment_category'),
    url(r'^repository/$', views.repository, name='deployment_repository'),
    url(r'^repository/(<?P<slug>)/$', views.repository_list, name='deployment_repository_list'),
    url(r'^repository/(<?P<slug>)/run$', views.run, name='deployment_run'),
]
