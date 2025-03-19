from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns=[
    path('registration', views.Registration.as_view()),
    path('login', views.Login.as_view()),
    path('dashboard', views.Dashboard.as_view())
]