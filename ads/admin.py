from django.contrib import admin
from .models import City, Category, Ad
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    search_fields = ['name', 'city__name']
    list_filter = ['city']
    ordering = ['name']

admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)

class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'city', 'price', 'created_at']
    search_fields = ['title', 'category__name', 'city__name']
    list_filter = ['category', 'city']
    ordering = ['created_at']

admin.site.register(Ad, AdAdmin)
