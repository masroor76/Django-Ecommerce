from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns=[
    path('accounts/registration/', views.Registration.as_view()),
    path('accounts/login/', views.Login.as_view()),
    path('accounts/logout/', views.Logout.as_view()),
    path('dashboard/', views.Dashboard.as_view()) 
]