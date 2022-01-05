from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . form import RegisterUserForm 
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatroom')
        
        else:
            messages.success(request , ("Login Failed: username or password is incorrect"))
            return redirect('login')
       
    elif request.user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request , 'authenticate/login.html', {})
        
def logout_user(request):
    logout(request)
    messages.success(request , ("You've been logged out"))
    return redirect('homepage')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            authenticate(username=username , password=password)
            messages.success(request , ("Registration successful, please login to continue"))
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request , 'authenticate/register_user.html', {
    'form': form,
    })