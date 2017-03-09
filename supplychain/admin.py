from django.contrib import admin
from .models import (Supplier, Product, Part)


class ExcludeSlugAdmin(admin.ModelAdmin):
    exclude = ('slug', )


admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Part)
