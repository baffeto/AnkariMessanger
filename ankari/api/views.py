from rest_framework import generics
from .serializers import UsersSerializer
from django.contrib.auth.models import User

class UsersAPIVIew(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer