from django.contrib import admin

from products.models import Product

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'package_size_in_milliliters', 'price')
