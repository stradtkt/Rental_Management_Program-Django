from django.contrib import admin

from django.contrib import admin

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'address', 'city', 'state', 'zipcode', 'price')
    list_display_links = ('id', 'address')
    list_filter = ('owner',)
    # list_editable = ('',)
    search_fields = ('title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)