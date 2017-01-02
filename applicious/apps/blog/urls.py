
from datetime import datetime
from django.conf.urls import patterns, url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='blog_post_list'),
    url(r'^(?P<slug>)/$', views.post,  name='blog_post'),
    url(r'^category/$', views.categories, name='blog_category_list'),
    url(r'^category/(<?P<slug>)/$', views.category, name='blog_category'),
    url(r'^tag/$', views.tag, name='blog_tag_list'),
    url(r'^tag/(<?P<slug>)/$', views.tag_list, name='blog_tag'),
]
