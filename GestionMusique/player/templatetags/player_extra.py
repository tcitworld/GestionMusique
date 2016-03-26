from django import template
from django.core.files.storage import FileSystemStorage
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def exist(filename):
	""" Verifie si le fichier existe """
	fileStorage = FileSystemStorage(location="/")
	return fileStorage.exists(filename)

@register.filter
def escape(chaine):
	return mark_safe(escape(chaine))