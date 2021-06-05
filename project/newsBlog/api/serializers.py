from rest_framework import serializers
from newsBlog.models import Post,Comment
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class GetPostSerializer(serializers.Serializer):
    typeOf = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        if validated_data['typeOf']=='all': # Return All Posts
            posts = Post.objects.all().values()
            return posts
        elif validated_data['typeOf'].find('Token')!=-1: # Return All Posts Uploaded by User of given Token
            spaceInWord = validated_data['typeOf'].find(' ')
            token = validated_data['typeOf'][spaceInWord+1:]
            try:
                user = Token.objects.get(key=token).user
                posts = Post.objects.filter(author=user).values()
                return posts
            except:
                return {'Error':'wrong token'}

        else: # Return Specific Post
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
        tags = validated_data['tag']
        try:
            user = Token.objects.get(key=validated_data['authorToken']).user
            post.author = user
            post.save()
            post.tags.add(tags)
            return {'Status':'ok','pk':post.pk}
        except:
            return {'Error':'Wrong Token!!'}

class EditPostSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    title = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    slug = serializers.SlugField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    body = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    thumbnail = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    authorToken = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    status = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    tag = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        try:
            post = Post.objects.filter(pk=validated_data['pk'])
            title = validated_data['title']
            slug = validated_data['slug']
            body = validated_data['body']
            thumbnail = validated_data['thumbnail']
            status = validated_data['status']
            tags = validated_data['tag']
            try:
                user = Token.objects.get(key=validated_data['authorToken']).user
            except:
                return {'Error':'Wrong Token!!'}
            post.update(title=title, slug=slug, body=body, thumbnail=thumbnail, status=status, author=user)
            post2 = Post.objects.filter(pk=validated_data['pk'])[0]
            for t in tags.split(','):
                post2.tags.add(t)
            return {'Status':'ok'}
        except:
            return {'Error':'Wrong pk!!'}

class DeletePostSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        post = Post.objects.filter(pk=validated_data['pk'])
        post.delete()
        return {'status':'ok'}


#=========================Comments===============================
class GetCommentSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)

    def create(self, validated_data):
        post = get_object_or_404(Post,pk=validated_data['pk'])
        comments = post.comments.filter(active=True).values()
        return comments
        return {'Error':'Wrong pk!!'}

class CreateCommentSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    body = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    active = serializers.BooleanField()
    def create(self,validated_data,user):
        post = get_object_or_404(Post,pk=validated_data['pk'])
        comment = Comment()
        comment.name = user.first_name
        comment.username = user.username
        comment.body = validated_data['body']
        comment.active = validated_data['active']
        comment.post = post
        comment.save()
        return {'Status':'ok','pk':comment.pk}

class EditCommentSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    body = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    active = serializers.BooleanField()
    
    def create(self,validated_data):
        try:
            comment = Comment.objects.filter(pk=validated_data['pk'])
            body = validated_data['body']
            active = validated_data['active']
            comment.update(body=body, active=active)
            return {'Status':'ok'}
        except:
            return {'Error':'Wrong pk!!'}

class DeleteCommentSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        comment = Comment.objects.filter(pk=validated_data['pk'])
        comment.delete()
        return {'status':'ok'}
