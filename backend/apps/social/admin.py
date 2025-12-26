from django.contrib import admin
from .models import SocialPost

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('platform', 'sentiment', 'likes', 'comments', 'created_at')
