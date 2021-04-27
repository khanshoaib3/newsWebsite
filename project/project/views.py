from django.shortcuts import render
from django.http import HttpResponse
from newsBlog.models import Post

def homeView(request):
    return render(request,
                'home/files/homeContent.html',
                {'css':'home/files/homeCss.html',
                'nav':'common/nav.html',
                'discord':Post.published.filter(tags__name__in=["discord"]).distinct(),
                'minecraft':Post.published.filter(tags__name__in=["minecraft"]).distinct(),
                'latest':Post.published.all()[:5]})