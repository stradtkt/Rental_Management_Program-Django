from django.contrib import admin

from django.contrib import admin

from .models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'name', 'email', 'phone', 'created')
    list_display_links = ('id', 'photo', 'name')
    # list_filter = ('',)
    # list_editable = ('',)
    search_fields = ('name', 'email', 'description', 'phone')
    list_per_page = 25

admin.site.register(Owner, OwnerAdmin)