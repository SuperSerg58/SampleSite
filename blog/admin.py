from django.contrib import admin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'create_date', 'published_date')
    list_display_links = ('title',)
    search_fields = ('title', 'text')


admin.site.register(Post, PostAdmin)
