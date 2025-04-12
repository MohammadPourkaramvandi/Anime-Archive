from django.contrib import admin
from . import models


@admin.register(models.AnimeItems)
class AnimeItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'seasone', 'episod']