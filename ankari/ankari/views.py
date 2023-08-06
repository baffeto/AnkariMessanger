from django.http import HttpResponse
from django.shortcuts import render
import logging

# Тестим логирование нашего проекта 
logger = logging.getLogger('main')


def home_view(request):
    logger.info('Test!')
    user = request.user
    
    template_name = 'main/home.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)