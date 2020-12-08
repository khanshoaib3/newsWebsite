from django.urls import path
from account.views import signin,signup,signout,profile,re_authenticate,editProfile,imageUpload, deleteImage

app_name = 'account'

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('reAuthenticate/', re_authenticate, name='reAuthenticate'),
    path('editProfile/', editProfile, name='editProfile'),
    path('imageUpload/', imageUpload, name='imageUpload'),
    path('deleteImage/', deleteImage, name='deleteImage'),
    path('', profile, name='profile'),
]
