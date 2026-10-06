from django.contrib import admin
# 这里改为 accounts
from accounts.models import User 
from .models import Article,  Attachment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'views', 'created_at')
    list_filter = ('status', 'author')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'article', 'created_at')