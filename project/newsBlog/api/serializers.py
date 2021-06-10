from rest_framework import serializers
from newsBlog.models import Post
from rest_framework.authtoken.models import Token



class GetPostSerializer(serializers.Serializer):
    typeOf = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        if validated_data['typeOf']=='all':
            posts = Post.objects.all().values_list('id','title','body','status')
            return posts
        elif validated_data['typeOf'].find('Token')!=-1:
            spaceInWord = validated_data['typeOf'].find(' ')
            token = validated_data['typeOf'][spaceInWord+1:]
            try:
                user = Token.objects.get(key=token).user
                posts = Post.objects.filter(author=user).values_list('id','title','body','status')
                return posts
            except:
                return {'Error':'wrong token'}

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
        tags = validated_data['tag']
        try:
            user = Token.objects.get(key=validated_data['authorToken']).user
            post.author = user
            post.save()
            post.tags.add(tags)
            return {'Status':'ok'}
        except:
            return {'Error':'Wrong Token!!'}


class EditPostSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    title = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    slug = serializers.SlugField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    body = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    thumbnail = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    status = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    tag = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        post = Post.objects.filter(pk=validated_data['pk'])
        title = validated_data['title']
        slug = validated_data['slug']
        body = validated_data['body']
        thumbnail = validated_data['thumbnail']
        status = validated_data['status']
        tags = validated_data['tag']
        post.update(title=title, slug=slug, body=body, thumbnail=thumbnail, status=status)
        post2 = Post.objects.filter(pk=validated_data['pk'])[0]
        for t in tags.split(','):
            post2.tags.add(t)
        return {'Status':'ok'}

class DeletePostSerializer(serializers.Serializer):
    pk = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    def create(self,validated_data):
        post = Post.objects.filter(pk=validated_data['pk'])
        post.delete()
        return {'status':'ok'}