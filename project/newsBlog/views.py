from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

#======================LIST VIEW========================
def list(request):
	return render(request,'newsBlog/files/listBlog.html',{'nav':'common/nav.html','posts':Post.published.all(),'css':'newsBlog/files/listBlogCss.html','js':'newsBlog/files/listBlogJs.html'})
#====================END LIST VIEW=======================




#======================DETAIL VIEW========================
def detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year,publish__month=month, publish__day=day,)

	comments = post.comments.filter(active=True)
	newComment = None

	if request.method == 'POST':
		commentForm = CommentForm(data=request.POST)
		if commentForm.is_valid():
			newComment = commentForm.save(commit=False)
			newComment.post = post
			newComment.save()
	else:
		commentForm = CommentForm()

	return render(request,'newsBlog/files/detailBlog.html',{'nav':'common/nav.html','css':'newsBlog/files/detailBlogCss.html','post':post,'commentForm':commentForm,'comments':comments})
#====================END DETAIL VIEW=======================
