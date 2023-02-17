from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'currency']
    list_display = ['name', 'currency', 'get_price']
