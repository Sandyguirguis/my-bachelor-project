from django.contrib import admin
from .models import (Supplier, Product)


class ExcludeSlugAdmin(admin.ModelAdmin):
    exclude = ('slug', )


admin.site.register(Supplier)
admin.site.register(Product)
