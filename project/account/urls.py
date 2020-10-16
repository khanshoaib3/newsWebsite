from django.urls import path
from account.views import signin,signup,signout,profile,re_authenticate

app_name = 'account'

urlpatterns = [
    path('signin/',signin),
    path('signup/',signup),
    path('logout/',signout),
    path('reAuthenticate/', re_authenticate, name='reAuthenticate'),
    path('',profile),
]
