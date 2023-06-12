from django.contrib import admin
from .models import Shortener
# Register your models here.
@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = ['id', 'long_url', 'short_url', 'times_followed', 'created', 'last_accessed']