from rest_framework import serializers
from .models import Subscription, Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    
    user_name = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    price = serializers.SerializerMethodField()
    
    def get_price(self, instance):
        return instance.price
        
    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'user_name', 'email', 'plan', 'price')
        