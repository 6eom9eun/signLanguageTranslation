from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'published_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)