from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.





@login_required(login_url = "/")
def show_profile(request):
    #if request.user.is_authenticated:
    return render(request, 'profile.html')
    #return redirect('/')

@login_required(login_url = "/")
def show_random(request):
    return render(request, 'random.html')
