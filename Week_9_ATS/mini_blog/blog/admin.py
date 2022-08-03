from django.contrib import admin
from .models import Blog, Comment, Profile
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    list_filter = ("author", "post_date")
    list_display = ("title", "post_date", "author")
    inlines = [CommentInline]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_owner", "blog", "text")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)
