from django.shortcuts import render
from django.http import HttpResponse

def homeView(request):
    return render(request,
                'home/files/homeContent.html',
                {'css':'home/files/homeCss.html',
                'nav':'common/nav.html'})