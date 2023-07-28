from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    user = request.user
    
    template_name = 'main/home.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)