from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'published'
    raw_id_fields = ('author',)
    readonly_fields = ('view_image',)
    list_filter = ('status', 'created', 'published', 'author')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'created')
    search_fields = ('name',)
    date_hierarchy = 'published'
    list_filter = ('name', 'published')
