from django.contrib import admin

from django.contrib import admin

from .models import Renter

class RenterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'kids', 'martial_status', 'income')
    list_display_links = ('id', 'first_name', 'last_name')
    # list_filter = ('',)
    # list_editable = ('',)
    search_fields = ('first_name', 'last_name', 'email', 'martial_status', 'kids', 'income', 'description')
    list_per_page = 25

admin.site.register(Renter, RenterAdmin)