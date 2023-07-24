from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def main_page(request):
    return render(request, 'users/main.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('main_page') # urls name
    else:
        form = SignUpForm()
        
    return render(request, 'users/signup.html', {'form': form})