from django.contrib import admin
from .models import DecksModel



class DeckModelAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'desc', 'id')

admin.site.register(DecksModel, DeckModelAdmin)