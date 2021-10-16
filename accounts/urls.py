from django.contrib.auth import logout
from django.urls import path, include

from accounts.views import register, loginview, logoutUser, loginstudent

urlpatterns = [
    path('register/', register, name='register'),
    path('loginview/', loginview, name='loginview'),
    path('loginstudent/', loginstudent, name='loginstudent'),
    path('logoutUser/', logoutUser, name='logoutUser'),
]
