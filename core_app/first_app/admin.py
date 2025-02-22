from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","slug","selected_categories") # admin panelde neleri gormey isteyirk
    list_display_links = ("name","price",) # neleri link olaraq isteyirik
    prepopulated_fields = {"slug": ("name",)} # avtomatik slug yaranmagi
    list_filter = ("name","price",) # neye gore filtr elemek isteyirk
    list_editable =("isActive",) # admin panelde isActivi update elemek
    search_fields = ("name","description",)  # neye gore axtariw elemek

    def selected_categories(self, obj):
        catagory_name = ""
        for category in obj.categories.all():
            catagory_name += category.name + " "
        return catagory_name

admin.site.register(Product,ProductAdmin) # product madelinin admin sehifede nece gprunmesi ile bagli yazilib
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Adress)
