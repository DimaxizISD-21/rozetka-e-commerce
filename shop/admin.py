from django.contrib import admin
from .models import Catalog, Characteristic, Product

# Register your models here.

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['catalog', 'product_name', 'price']
    list_filter = ['catalog', 'product_name', 'publish']
    filter_horizontal = ('characteristics',)
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['admin_panel_name', 'characteristic', 'value']
    list_filter = ['characteristic', 'value']