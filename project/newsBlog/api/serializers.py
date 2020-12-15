from rest_framework import serializers
from django.core import serializers as djangoSerializers
from newsBlog.models import Post
from rest_framework.authtoken.models import Token
import json
from django.core.serializers.json import DjangoJSONEncoder



class GetPostSerializer(serializers.Serializer):
    typeOf = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        if validated_data['typeOf']=='all':
            posts = Post.objects.all().values()
            return posts
        else:
            post = Post.objects.filter(pk=validated_data['typeOf']).values()
            return post


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    slug = serializers.SlugField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    body = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    thumbnail = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    authorToken = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    status = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    tag = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        post = Post()
        post.title = validated_data['title']
        post.slug = validated_data['slug']
        post.body = validated_data['body']
        post.thumbnail = validated_data['thumbnail']
        post.status = validated_data['status']
        post.tag = validated_data['tag']
        try:
            user = Token.objects.get(key=validated_data['authorToken']).user
            post.author = user
        except:
            return {'Error':'Wrong Token!!'}
