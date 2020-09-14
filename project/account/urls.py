from django.urls import path
from account.views import signin,signup,signout,profile

app_name = 'account'

urlpatterns = [
    path('signin/',signin),
    path('signup/',signup),
    path('logout/',signout),
    path('',profile),
]
