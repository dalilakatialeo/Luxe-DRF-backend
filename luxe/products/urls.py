from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('recommendations/', views.RecommendationList.as_view()),
    path('recommendations/<int:pk>/', views.RecommendationDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)