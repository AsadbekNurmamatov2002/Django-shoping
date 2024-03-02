from django.contrib import admin
from .models import Product, ProductCollor, Size, Rasimlar

class ProductRasimlar(admin.TabularInline):
    model = Rasimlar
    raw_id_fields = ['product']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductRasimlar]

@admin.register(ProductCollor)
class ProductColloradmin(admin.ModelAdmin):
    list_display = ['color']


@admin.register(Size)
class ProductAdminSize(admin.ModelAdmin):
    list_display = ['size']