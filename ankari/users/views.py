from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from .forms import SignUpForm


class SignUp(View):
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect()
        
        return render('users/main.html', {
            'form': form,
        })
            


