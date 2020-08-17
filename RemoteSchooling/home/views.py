from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            return redirect('/profile')
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user
            login(request, user)
            return redirect("/profile")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')




