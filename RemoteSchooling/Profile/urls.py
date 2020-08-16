from django.urls import path
from Profile import views


app_name = 'Profile'

urlpatterns = [
    path('', views.show_profile, name= 'showprofile'),

]