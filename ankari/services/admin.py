from django.contrib import admin
from .models import Plan, Subscription, Service


admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Service)