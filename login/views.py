from django.shortcuts import render, redirect
from homepage.models import User
from homepage.views import userprofile
from django.contrib import messages
# Create your views here.

from django.http import HttpResponse

def loginpage(request):
    print (request)
    return render(request, 'login.html')




def login(request):
    print ("I am here")
    email = request.POST['email']
    password = request.POST['password']
    print("EMAIL : " + email)
    print("EMAIL : " + password)
    users = User.objects.all()
    print(users)
    flag = False
    for user in users:
        print ("user email => " + user.email)
        print("and email => " + email)
        if user.email == email:
            flag = True
            print("Found mail")
            break
    if flag:
        if user.password == password:
            print("Passwwords are same")
            return userprofile(request, user.uniqueid)
        else:
            messages.info(request, 'Wrong password')
            print("Passwords not same")
            return loginpage(request)
    else:
        messages.info(request, 'Email does not exist')
        print("Cud not find mail")
        return loginpage(request)
