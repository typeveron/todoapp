from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'todo/home.html')

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        #Create User
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken'})           
        else:
            #Tell the user the passwords didn't match
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'passwords did not match'})

def loginuser(request):
        if request.method == 'GET':
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match'})
            else:
               login(request, user)
               return redirect('currenttodos') 



      


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




def currenttodos(request):
    return render(request, 'todo/currenttodos.html')