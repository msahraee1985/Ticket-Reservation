from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from transport.models import Transport
from transport.serializers import TransportSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser





class TransportViewSet(viewsets.ModelViewSet):
        queryset = Transport.objects.all().order_by('departure_date_time')
        serializer_class = TransportSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
        filterset_fields = ['origin', 'destination', 'transport_type']
        ordering_fields = ['price', 'departure_date_time']

        def get_permissions(self): # To do لطفا تنظیمات مربوط به کاربر ادمین رو در اپ یوزر برای درست عمل کردن این کد انجام دهید 
            if self.action in ['create', 'update', 'partial_update', 'destroy']:
                return [IsAdminUser()]
            return []


