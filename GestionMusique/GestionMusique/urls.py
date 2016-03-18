from django.conf.urls import include, url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accueil$', views.home),
    url(r'^player/', include('player.urls')),
]
