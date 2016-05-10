from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home,name='url_home'),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.album, name='album'),
    url(r'^author/(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    url(r'^group/(?P<group_id>[0-9]+)/$', views.group, name='group'),
    url(r'^genre/(?P<genre_id>[0-9]+)/$', views.genre, name='genre'),
    url(r'^playlists/$', views.playlists, name='playlists'),
    url(r'^playlist/(?P<playlist_id>[0-9]+)/$', views.playlist, name='playlist'),
    url(r'^add-playlist/$', views.addplaylist, name='album'),
    url(r'^add-song-to-playlist/$', views.addsongtoplaylist, name='addsongtoplaylist'),
    url(r'^delete-song-from-playlist/(?P<playlist_id>[0-9]+)/(?P<song_id>.+)/$', views.deletefromplaylist, name='deletefromplaylist'),
    url(r'^delete-playlist/(?P<playlist_id>[0-9]+)/$', views.deleteplaylist, name='deleteplaylist'),
    url(r'^login/$',views.loginUser,name='url_login'),
    url(r'^register/$',views.register,name='url_register'),
    url(r'^logout/$',views.logoutUser, name='logout'),
    url(r'^search/$', views.search, name='search'),
]
