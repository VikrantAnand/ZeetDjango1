from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Product)
# admin.site.register(Signup)
# admin.site.register(Blog)
# admin.site.register(Author)
# admin.site.register(Entry)

class Proadmin(admin.ModelAdmin):
    list_display=['name','price','description','review']
    list_filter=['name','price','description','review']
# admin.site.register(Pro,Proadmin)

admin.site.register(CompanyDetail)
admin.site.register(CompanyCustomer)
admin.site.register(CompanyProduct)
