from django.urls import path
from .views import list

app_name = 'newsBlog'

urlpatterns = [
	path('' ,list ,name = 'list'),
]