from django.contrib import admin
from .models import Post, Tag, NewsTags


class MembershipInline(admin.TabularInline):
    model = Post.tags.through


class PostAdmin(admin.ModelAdmin):
    exclude = ('tags',)
    inlines = [MembershipInline, ]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(NewsTags)
