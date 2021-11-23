<<<<<<< HEAD
# from django.conf.urls import url
from django.urls import path
=======
from django.urls import path
from rest_framework import urlpatterns
>>>>>>> main
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view())
=======
    path('users/', views.CustomUserList.as_view()), #users
    path('users/<int:pk>/', views.CustomUserDetail.as_view()), #/users/id

>>>>>>> main
]

urlpatterns = format_suffix_patterns(urlpatterns)