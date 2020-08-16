from django.urls import path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.login_view, name= 'login_view'),
    path('signup', views.signup_view, name= 'signup_view'),

]