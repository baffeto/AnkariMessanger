from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer
from django.db.models import Prefetch, F
from django.contrib.auth.models import User

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related('plan',
               Prefetch('user', queryset=User.objects.all())).annotate(
    price=F('service__full_price') - F('service__full_price') * F('plan__discount_percent') / 100.00)
    
    serializer_class = SubscriptionSerializer