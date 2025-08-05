from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transport', 'seat_number', 'is_canceled', 'created_at')
    list_filter = ('is_canceled', 'created_at')
    search_fields = ('user__username', 'transport__origin', 'transport__destination')
    ordering = ('-created_at',)
