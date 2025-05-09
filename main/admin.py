from django.contrib import admin
from .models import Bottle

@admin.register(Bottle)
class BottleAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_weight', 'empty_weight', 'full_volume')  # Колонки, которые будут отображаться в списке
    search_fields = ('name',)  # Поля для поиска