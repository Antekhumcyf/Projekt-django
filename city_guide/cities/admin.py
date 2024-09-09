from django.contrib import admin
from .models import City

@admin.action(description='Mark selected cities as active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'active')
    actions = [make_active]

admin.site.register(City, CityAdmin)
