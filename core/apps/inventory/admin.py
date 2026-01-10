from django.contrib import admin
from apps.inventory.models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','quantity','created_at','updated_at']