from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Post, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    list_filter = ('Name',)
    search_fields = ('Name',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'Created_date'
    list_display = ('Title', 'Author', 'Status', 'Created_date')
    list_filter = ('Title', 'Status', 'Author')
    search_fields = ('Title', 'Content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'Created_Date'
    list_display = ('Post', 'Name', 'Email', 'Subject')
    list_filter = ('Approved',)
    search_fields = ('Subject', 'Message')
