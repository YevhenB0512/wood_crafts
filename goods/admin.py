from django.contrib import admin
from goods.models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name',
                    'quantity',
                    'price',
                    'discount'
                    )
    list_editable = ('discount', 'price')
    search_fields = ('name', )
    list_filter = ('category', )
    fields = ('name',
              'category',
              'slug',
              'description',
              'image',
              'quantity',
              ('price', 'discount'),
              )
