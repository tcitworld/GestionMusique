from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='url_home'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.song),
    url(r'^author/(?P<artist_id>[0-9]+)/$', views.artist),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group),
    url(r'^login/$',views.loginUser,name='url_login'),
    url(r'^register/$',views.register,name='url_register'),
    url(r'^logout/$',views.logoutUser),
]
