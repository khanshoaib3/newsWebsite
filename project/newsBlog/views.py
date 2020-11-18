from django.shortcuts import render, get_object_or_404
from .models import Post

#======================LIST VIEW========================
def list(request):
	return render(request,'newsBlog/files/listBlog.html',{'nav':'common/nav.html','posts':Post.published.all(),'css':'newsBlog/files/listBlogCss.html','js':'newsBlog/files/listBlogJs.html'})
#====================END LIST VIEW=======================




#======================DETAIL VIEW========================
def detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year,publish__month=month, publish__day=day,)
	return render(request,'newsBlog/files/detailBlog.html',{'nav':'common/nav.html','css':'newsBlog/files/detailBlogCss.html','post':post})
#====================END DETAIL VIEW=======================
