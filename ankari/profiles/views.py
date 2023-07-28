from django.shortcuts import render
from .models import Profile


def profile_view(request):
    obj = Profile.objects.get(user=request.user)
    
    context = {
        'obj': obj
    }
    
    return render(request, 'profiles/profile.html', context)
