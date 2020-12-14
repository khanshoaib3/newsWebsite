from django.urls import path
from account import views
from account.api import views as apiViews

app_name = 'account'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('reAuthenticate/', views.re_authenticate, name='reAuthenticate'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('imageUpload/', views.imageUpload, name='imageUpload'),
    path('deleteImage/', views.deleteImage, name='deleteImage'),
    path('', views.profile, name='profile'),
    path('api/hw', apiViews.hello_world, name='hello_world'),
    path('api/signup/', apiViews.createUserView, name='signupAPI'),
    path('api/signin/', apiViews.loginUserView, name='signinAPI'),
    path('api/editProfile/', apiViews.editUserProfileView, name='editProfileAPI'),
    path('api/editPass/', apiViews.editUserPassView, name='editPassAPI'),
]
