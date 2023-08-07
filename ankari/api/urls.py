from django.urls import path
from rest_framework import routers
from services.views import SubscriptionView
from . import views

router = routers.DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('v1/userslist/', views.UsersAPIVIew.as_view()),
]

router.register(r'v1/subscription', SubscriptionView)

urlpatterns += router.urls