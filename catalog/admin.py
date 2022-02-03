from django.contrib import admin
from .models import RoastProfile,coffee_stock

# Register your models here.
admin.site.register(RoastProfile)
admin.site.register(coffee_stock)

class RoastProfileAdmin(admin.ModelAdmin):
    pass
