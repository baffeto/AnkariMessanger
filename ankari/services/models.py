from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Как объект услуга, проще говоря премиум аккаунт 
class Service(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, unique=True)
    full_price = models.PositiveIntegerField()    
    
    def __str__(self) -> str:
        return f'{self.name} - {self.full_price}'
    
# Как вариант выбрать на какой срок будет премиум аккаунт, следовательно будет меняться стоимость и скидка на продукт
class Plan(models.Model):
    PLAN_TYPES = (
        ('year', 'year'),
        ('month', 'month'),
        ('week', 'week')
    )
    
    plan_type = models.CharField(choices=PLAN_TYPES, max_length=7)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    
    
class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscription', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='subscription', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.CASCADE)
