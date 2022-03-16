from django.contrib import admin
from .models import Comments, Posts, Likes


class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'published')
    list_display_links = ('author', 'content')
    prepopulated_fields = {'slug': ('content',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments)
admin.site.register(Likes)
