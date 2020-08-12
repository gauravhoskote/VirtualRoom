from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import time

# Create your views here.

from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage.html')


def getmilliseconds():
    milliseconds = int(round(time.time() * 1000))
    print(milliseconds)
    return milliseconds


def register(request):
    user = User()
    user.firstname = request.POST['firstname']
    user.lastname = request.POST['lastname']
    user.email = request.POST['mail']
    user.password = request.POST['password']
    user.uniqueid = "VR" +str(getmilliseconds())
    confirmPassword = request.POST['confirmpassword']
    if confirmPassword != user.password:
        messages.info(request, 'Passwords not the same')
        print("Password not the same")
        return redirect('/')
    else:
        if User.objects.filter(email = user.email).exists():
            messages.info(request, 'Mail already exists')
            print("Mail already exists")
            return redirect('/')
        else:
            print("User created!!!")
            print("mail = " + user.email)
            print("user = " + user.uniqueid)
            print(user)
            user.save()
            return userprofile(request,user.uniqueid)


def userprofile(request,uniqueid):
    users = User.objects.all()
    for user in users:
        if user.uniqueid == uniqueid:
            break
    print(user)
    return render(request, 'user.html', {"user":user})


