from django.contrib import admin
from .models import Record
from . import models


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'deezer_id', 'price', 'available_units']
    list_editable = ['deezer_id', 'price', 'available_units']
    list_per_page = 10
    ordering = ['artist', 'title']
    search_fields = ['artist', 'title']
