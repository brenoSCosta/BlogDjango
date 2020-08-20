from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'published'
    list_filter = ('status', 'created', 'published', 'author')
    prepopulated_fields = {'slug': ('title',)}
