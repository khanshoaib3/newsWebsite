from django.contrib import admin
from .models import Profile, Photos

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','emailVerified']

@admin.register(Photos)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo']