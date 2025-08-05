from rest_framework import serializers
from .models import Booking
from transport.models import Transport
from django.utils import timezone



class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'transport', 'seat_number', 'booking_date', 'status', 'total_price']
        read_only_fields = ['booking_date', 'status', 'created_at']  # وضعیت در API دستی تغییر نمی‌کنه

    def validate(self, attrs):
        transport = attrs.get('transport')
        seat_number = attrs.get('seat_number')
        user = self.context['request'].user

         # 1. زمان حرکت گذشته نباشد
        if transport.departure_date_time <= timezone.now():
            raise serializers.ValidationError("زمان حرکت این وسیله نقلیه گذشته است.")

         # 2. ظرفیت پر نشده باشد
        booked_count = Booking.objects.filter(transport=transport, status='active').count()
        if booked_count >= transport.capacity:
            raise serializers.ValidationError("ظرفیت این وسیله نقلیه پر شده است.")
        


        if Booking.objects.filter(transport=transport, seat_number=seat_number).exists():
            raise serializers.ValidationError("این صندلی قبلاً رزرو شده است.")
        

        # 4. یک کاربر دو بار برای یک transport رزرو نکند
        if Booking.objects.filter(transport=transport, user=user, status='active').exists():
            raise serializers.ValidationError("شما قبلاً برای این سفر رزرو ثبت کرده‌اید.")

        return attrs

    def create(self, validated_data):
        transport = validated_data['transport']
        validated_data['total_price'] = transport.price
        return super().create(validated_data)