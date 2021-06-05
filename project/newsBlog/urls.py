from django.urls import path
from .views import list,detail,comment,deletePost
from newsBlog.api.views import getPostView,editPostView,getComment,editComment

app_name = 'newsBlog'

urlpatterns = [
	path('' ,list ,name = 'list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', detail, name = 'detail'),
	path('getComment/' ,getComment ,name = 'getComment'),
	path('editComment/' ,editComment ,name = 'editComment'),
	path('comment/' ,comment ,name = 'comment'),
	path('deletePost/' ,deletePost ,name = 'deletePost'),
	path('api/getPost/' ,getPostView ,name = 'getPost'),
	path('api/editPost/' ,editPostView ,name = 'editPost'),
]