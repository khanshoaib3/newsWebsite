from django.contrib import admin
from .models import Post, Comment


@admin.action(description='Mark selected stories as published')
def makePublished(Post, request, queryset):
    queryset.update(status='published')

@admin.action(description='Mark selected stories as draft')
def makeDraft(Post, request, queryset):
    queryset.update(status='draft')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','author','pk','thumbnail','created','publish','status','tags')
	list_filter=('author','publish','status','created')
	search_fields=('title','body')
	prepopulated_fields={'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')
	actions = [makePublished,makeDraft,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post','active','name','username','body','created',)
	list_filter = ('username','post','created','active',)
	search_fields = ('post','username','name')
	ordering = ('active',)