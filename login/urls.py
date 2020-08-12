from django.urls import path
from login  import views



urlpatterns = [
    path('', views.loginpage),
    path('login', views.login),
]
