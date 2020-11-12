from django.urls import path
from .views import list ,detail

app_name = 'newsBlog'

urlpatterns = [
	path('' ,list ,name = 'list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', detail, name = 'detail'),
]