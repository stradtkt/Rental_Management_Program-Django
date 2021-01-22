from django.contrib import admin

from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stars')
    list_display_links = ('id', 'title')
    # list_filter = ('',)
    # list_editable = ('',)
    search_fields = ('title', 'stars', 'description')
    list_per_page = 25

admin.site.register(Review, ReviewAdmin)