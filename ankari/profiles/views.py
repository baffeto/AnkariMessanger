from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm


def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm()
    
    context = {
        'profile': profile,
        'form': form,
    }
    
    return render(request, 'profiles/profile.html', context)
