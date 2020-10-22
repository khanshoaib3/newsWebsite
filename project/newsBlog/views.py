from django.shortcuts import render
from .models import Post

# Create your views here.
def list(request):
	return render(request,'newsBlog/files/listBlog.html',{'nav':'common/nav.html','commonCss':'newsBlog/files/commonCss.html','posts':Post.published.all(),'css':'newsBlog/files/listBlogCss.html'})