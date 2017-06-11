from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', views.reglog_view, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.reglog_view, name='signup'),
    url(r'^recover/$', views.recover_view, name='recover'),
    url(r'^profile/$', views.profile_view, name='profile'),
]
