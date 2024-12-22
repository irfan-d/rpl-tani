from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

#-------------------------  Login-------
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})    

    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('plants')
        else:
            return render(request, 'user/register.html', {'form': form})


def sign_in(request):
  if request.method == 'GET':
      if request.user.is_authenticated:
          return redirect('plants')
      form = LoginForm()
      return render(request,'user/login.html', {'form': form})
  
  elif request.method == 'POST':
      form = LoginForm(request.POST)
  
      if form.is_valid():
          username = form.cleaned_data['username']
          password=form.cleaned_data['password']
          user = authenticate(request,username=username,password=password)
          if user:
              login(request, user)
              messages.success(request,f'Hi {username.title()}, welcome back!')
              return redirect('plants')
  
      # either form not valid or user is not authenticated
      messages.error(request,f'Invalid username or password')
      return render(request,'user/login.html',{'form': form})



#---------------------------- Logout ------------
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        

