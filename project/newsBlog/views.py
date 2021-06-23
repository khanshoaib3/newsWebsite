from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

#======================LIST VIEW========================
def list(request):
    searchorfiltered = False
    filters = request.GET.get("filters")
    if filters is not None:
        allPosts = Post.published.filter(tags__name__in=[filters])
        searchorfiltered = True
    else:
        allPosts = Post.published.all()

    search = request.GET.get("search")
    if search is not None:
        search = search.replace("+"," ")
        allPosts = allPosts.filter(title__icontains=""+search)
        searchorfiltered = True

    paginator = Paginator(allPosts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request,'newsBlog/files/listBlog.html',{'nav':'common/nav.html','posts':posts,'css':'newsBlog/files/listBlogCss.html','js':'newsBlog/files/listBlogJs.html','searchorfiltered':searchorfiltered})
#====================END LIST VIEW=======================




#======================DETAIL VIEW========================
def detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year,publish__month=month, publish__day=day,)

	comments = post.comments.filter(active=True)
	

	return render(request,'newsBlog/files/detailBlog.html',{'nav':'common/nav.html','css':'newsBlog/files/detailBlogCss.html','post':post,'comments':comments,'js':'newsBlog/files/detailBlogJs.html',})
#====================END DETAIL VIEW=======================




@login_required
@require_POST
def comment(request):
	post = get_object_or_404(Post, slug=request.POST.get('slug'), status='published', publish__year=request.POST.get('year'),publish__month=request.POST.get('month'), publish__day=request.POST.get('day'))
	newComment = request.POST.get('newComment')
	newCommentModel = Comment()
	newCommentModel.post = post
	newCommentModel.name = request.user.first_name
	newCommentModel.username = request.user.username
	newCommentModel.body = newComment
	newCommentModel.save()
	return JsonResponse({'status':'ok'})


@login_required
@require_POST
def deletePost(request):
    post = Post.objects.filter(author=request.user,id=request.POST.get("id"))
    post.delete()
    return JsonResponse({'status':'ok'})
