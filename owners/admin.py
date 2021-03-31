from django.contrib import admin

from django.contrib import admin

from .models import Owner, Review

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'name', 'email', 'phone', 'created')
    list_display_links = ('id', 'photo', 'name')
    search_fields = ('name', 'email', 'description', 'phone')
    list_per_page = 25

admin.site.register(Owner, OwnerAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stars')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'stars', 'description')
    list_per_page = 25

admin.site.register(Review, ReviewAdmin)