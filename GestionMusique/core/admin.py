from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.register(Author)
admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Classification)