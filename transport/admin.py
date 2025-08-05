from django.contrib import admin
from .models import Transport

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'transport_type', 'departure_date_time', 'price', 'capacity')
    list_filter = ('transport_type', 'origin', 'destination')
    search_fields = ('origin', 'destination')
    ordering = ('-departure_date_time',)
