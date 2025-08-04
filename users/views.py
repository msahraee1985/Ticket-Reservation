# users/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied, ValidationError
from users.models import User
from .serializers import RegisterSerializer, StaffUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

class CreateStaffUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = StaffUserSerializer
  permission_classes = [permissions.IsAdminUser]

  def perform_create(self, serializer):
    if not self.request.user.is_superuser:
      raise PermissionDenied("Only superusers can create staff users.")
    serializer.save()

