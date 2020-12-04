from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','author','thumbnail','updated','publish','status')
	list_filter=('author','publish','status','created')
	search_fields=('title','body')
	prepopulated_fields={'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post','active','name','username','body','created',)
	list_filter = ('username','post','created','active',)
	search_fields = ('post','username','name')
	ordering = ('active',)