from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'login/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'login/index.html', {'message':username})
            # return HttpResponse("You have signed in.")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
        
    return render(request, 'login/signin.html')

def signout(request):
    logout(request)
    return redirect('home')
    
