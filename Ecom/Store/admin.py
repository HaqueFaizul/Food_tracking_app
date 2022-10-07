from django.contrib import admin
from .models import Product
from .models import Variation

class AdminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug','description','price','stock','category','is_available','modified_date')
admin.site.register(Product, AdminProduct)

class AdminVariation(admin.ModelAdmin):
    list_display = ('product', 'variation_category','variation_value','is_available','created_date')
    list_editable = ('is_available',)
    list_filter = ('product', 'variation_category','variation_value')
admin.site.register(Variation,AdminVariation)

# Register your models h
