from django.contrib import admin

from mainapp.models import ProductCategory, product

admin.site.register(ProductCategory)


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'category','short_description', ('price', 'quantity'), 'image', 'description' )
    readonly_fields = ('price',)
    ordering = ('name',)
    search_fields = ('name', 'category__name')
