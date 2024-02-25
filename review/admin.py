from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'rating')

admin.site.register(Review, ReviewAdmin)