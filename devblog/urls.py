from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?:page-(?P<page_number>\d+)/)?$', views.allpostsview , name='blog'),
    url(r'^(?:author-(?P<author_id>\d+)/)(?:page-(?P<page_number>\d+)/)?$', views.postsbyauthor , name='blog'),
]
