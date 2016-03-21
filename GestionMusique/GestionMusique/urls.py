from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accueil$', views.home),
    url(r'^player/', include('player.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
]
