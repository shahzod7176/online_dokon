from django.contrib import admin
from apps.models import Category, Shoes, Buy


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Shoes)
class ShoesModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Buy)
class BuyModelAdmin(admin.ModelAdmin):
    pass

