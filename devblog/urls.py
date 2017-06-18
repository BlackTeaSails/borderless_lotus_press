from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addpost/$', views.newpost_view, name='addpost'),
    url(r'^(?:page-(?P<page_number>\d+)/)?$', views.allpostsview , name='blog'),
    url(r'^(?:post-(?P<post_id>\d+)/)?$', views.post_view , name='post'),
    url(r'^(?:author-(?P<author_id>\d+)/)(?:page-(?P<page_number>\d+)/)?$', views.postsbyauthor , name='blog'),
]
