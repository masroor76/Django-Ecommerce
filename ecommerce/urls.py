from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('products/', views.Products.as_view()),
    path('about/', views.About.as_view())
]