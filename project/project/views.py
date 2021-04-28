from django.shortcuts import render
from django.http import HttpResponse
from newsBlog.models import Post
from taggit.models import Tag

def homeView(request):
    tags = Tag.objects.all()
    tagName = ""
    tagContents = []
    for tag in tags:
        tagName = tagName + tag.name+ "," 
        tagContents.append(Post.published.filter(tags__name__in=[tag.name+""]).distinct())
    return render(request,
                'home/files/homeContent.html',
                {'css':'home/files/homeCss.html',
                'nav':'common/nav.html',
                'tagnames':tagName,
                'tags':tagContents,
                'latest':Post.published.all()[:5]})