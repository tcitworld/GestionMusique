from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='url_home'),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.album),
    url(r'^author/(?P<artist_id>[0-9]+)/$', views.artist),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group),
    url(r'^genre/(?P<genre_id>[0-9]+)/$', views.genre),
    url(r'^playlists/$', views.playlists),
    url(r'^playlist/(?P<playlist_id>[0-9]+)/$', views.playlist),
    url(r'^add-playlist/$', views.addplaylist),
    url(r'^add-song-to-playlist/$', views.addsongtoplaylist),
    url(r'^delete-playlist/(?P<playlist_id>[0-9]+)/$', views.deleteplaylist),
    url(r'^login/$',views.loginUser,name='url_login'),
    url(r'^register/$',views.register,name='url_register'),
    url(r'^logout/$',views.logoutUser),
    url(r'^search/$', views.search),
]
