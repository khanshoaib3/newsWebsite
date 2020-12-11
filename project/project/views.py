from django.shortcuts import render
from django.http import HttpResponse
from newsBlog.models import Post

def homeView(request):
    return render(request,
                'home/files/homeContent.html',
                {'css':'home/files/homeCss.html',
                'nav':'common/nav.html',
                'globals':Post.published.filter(tag__name__in=["global","globals"]).distinct(),
                'techs':Post.published.filter(tag__name__in=["tech","technical","technology"]).distinct(),
                'gamings':Post.published.filter(tag__name__in=["game","gaming","games"]).distinct(),
                'entertainments':Post.published.filter(tag__name__in=["entertainment"]).distinct()})