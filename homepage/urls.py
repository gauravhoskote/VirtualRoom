from django.urls import path
from homepage import views



urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('register', views.register)
]
